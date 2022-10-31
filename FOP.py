#!/usr/bin/env python3
""" FOP
    Filter Orderer and Preener
    Copyright (C) 2011 Michael

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>."""
# FOP version number [12.02.2017]
VERSION = 3.8

# Import the key modules
import collections, filecmp, os, re, subprocess, sys

# Check the version of Python for language compatibility and subprocess.check_output()
MAJORREQUIRED = 3
MINORREQUIRED = 1
if sys.version_info < (MAJORREQUIRED, MINORREQUIRED):
    raise RuntimeError(
        "FOP requires Python {reqmajor}.{reqminor} or greater, but Python {ismajor}.{isminor} is being used to run this program.".format(
            reqmajor=MAJORREQUIRED, reqminor=MINORREQUIRED, ismajor=sys.version_info.major,
            isminor=sys.version_info.minor))

# Import a module only available in Python 3
from urllib.parse import urlparse

# Compile regular expressions to match important filter parts (derived from Wladimir Palant's Adblock Plus source code)
ELEMENTDOMAINPATTERN = re.compile(r"^([^\/\*\|\@\"\!]*?)#\@?#")
FILTERDOMAINPATTERN = re.compile(r"(?:\$|\,)domain\=([^\,\s]+)$")
ELEMENTPATTERN = re.compile(r"^([^\/\*\|\@\"\!]*?)(#\@?#)([^{}]+)$")
OPTIONPATTERN = re.compile(r"^(.*)\$(~?[\w\-]+(?:=[^,\s]+)?(?:,~?[\w\-]+(?:=[^,\s]+)?)*)$")

# Compile regular expressions that match element tags and pseudo classes and strings and tree selectors; "@" indicates either the beginning or the end of a selector
SELECTORPATTERN = re.compile(
    r"(?<=[\s\[@])([a-zA-Z]*[A-Z][a-zA-Z0-9]*)((?=([\[\]\^\*\$=:@#\.]))|(?=(\s(?:[+>~]|\*|[a-zA-Z][a-zA-Z0-9]*[\[:@\s#\.]|[#\.][a-zA-Z][a-zA-Z0-9]*))))")
PSEUDOPATTERN = re.compile(r"(\:[a-zA-Z\-]*[A-Z][a-zA-Z\-]*)(?=([\(\:\@\s]))")
REMOVALPATTERN = re.compile(r"((?<=([>+~,]\s))|(?<=(@|\s|,)))(\*)(?=([#\.\[\:]))")
ATTRIBUTEVALUEPATTERN = re.compile(r"^([^\'\"\\]|\\.)*(\"(?:[^\"\\]|\\.)*\"|\'(?:[^\'\\]|\\.)*\')")
TREESELECTOR = re.compile(r"(\\.|[^\+\>\~\\\ \t])\s*([\+\>\~\ \t])\s*(\D)")
UNICODESELECTOR = re.compile(r"\\[0-9a-fA-F]{1,6}\s[a-zA-Z]*[A-Z]")

# Compile a regular expression that describes a completely blank line
BLANKPATTERN = re.compile(r"^\s*$")

# Compile a regular expression that validates commit comments
COMMITPATTERN = re.compile(r"^(A|M|P)\:\s(\((.+)\)\s)?(.*)$")

# List the files that should not be sorted, either because they have a special sorting system or because they are not filter files
IGNORE = (
    "CC-BY-SA.txt", "easytest.txt", "GPL.txt", "MPL.txt", "filter.txt", "exclusions.txt", "general_extensions.txt",
    "antiadblock.txt", "foreign.txt", "allowlist.txt", "general_js_api.txt", "allowlist_stealth.txt",
    "enhancedstats-addon.txt", "fanboy-tracking", "firefox-regional", "other")

# List all Adblock Plus options (excepting domain, which is handled separately), as of version 1.3.9
KNOWNOPTIONS = ("document", "elemhide", "generichide", "genericblock",
                "font", "image", "match-case", "object", "media", "protobuf", 
                "popup", "script", "websocket", "other",
                "stylesheet", "subdocument", "third-party", "xmlhttprequest",
                "mp4", "urlblock", "empty", "jsinject", "content", "important")

# List the supported revision control system commands
REPODEF = collections.namedtuple("repodef",
                                 "name, directory, locationoption, repodirectoryoption, checkchanges, difference, commit, pull, push")
GIT = REPODEF(["git"], "./.git/", "--work-tree=", "--git-dir=", ["status", "-s", "--untracked-files=no"], ["diff"],
              ["commit", "-m"], ["pull"], ["push"])
HG = REPODEF(["hg"], "./.hg/", "-R", None, ["stat", "-q"], ["diff"], ["commit", "-m"], ["pull"], ["push"])
REPOTYPES = (GIT, HG)

wait = input("PRESS ENTER TO START SORTING.")


def start():
    """ Print a greeting message and run FOP in the directories
    specified via the command line, or the current working directory if
    no arguments have been passed."""
    greeting = "FOP (Filter Orderer and Preener) version {version}".format(version=VERSION)
    characters = len(str(greeting))
    print("=" * characters)
    print(greeting)
    print("=" * characters)

    # Convert the directory names to absolute references and visit each unique location
    places = sys.argv[1:]
    if places:
        places = [os.path.abspath(place) for place in places]
        for place in sorted(set(places)):
            main(place)
            print()
    else:
        main(os.getcwd())


def main(location):
    """ Find and sort all the files in a given directory, committing
    changes to a repository if one exists."""
    # Check that the directory exists, otherwise return
    if not os.path.isdir(location):
        print("{location} does not exist or is not a folder.".format(location=location))
        return

    # Set the repository type based on hidden directories
    repository = None
    for repotype in REPOTYPES:
        if os.path.isdir(os.path.join(location, repotype.directory)):
            repository = repotype
            break
    # If this is a repository, record the initial changes; if this fails, give up trying to use the repository
    if repository:
        try:
            basecommand = repository.name
            if repository.locationoption.endswith("="):
                basecommand.append(
                    "{locationoption}{location}".format(locationoption=repository.locationoption, location=location))
            else:
                basecommand.extend([repository.locationoption, location])
            if repository.repodirectoryoption:
                if repository.repodirectoryoption.endswith("="):
                    basecommand.append(
                        "{repodirectoryoption}{location}".format(repodirectoryoption=repository.repodirectoryoption,
                                                                 location=os.path.normpath(
                                                                     os.path.join(location, repository.directory))))
                else:
                    basecommand.extend([repository.repodirectoryoption, location])
            command = basecommand + repository.checkchanges
            originaldifference = True if subprocess.check_output(command) else False
        except(subprocess.CalledProcessError, OSError):
            print(
                "The command \"{command}\" was unable to run; FOP will therefore not attempt to use the repository tools. On Windows, this may be an indication that you do not have sufficient privileges to run FOP - the exact reason why is unknown. Please also ensure that your revision control system is installed correctly and understood by FOP.".format(
                    command=" ".join(command)))
            repository = None

    # Work through the directory and any subdirectories, ignoring hidden directories
    print("\nPrimary location: {folder}".format(folder=os.path.join(os.path.abspath(location), "")))
    for path, directories, files in os.walk(location):
        for direct in directories[:]:
            if direct.startswith(".") or direct in IGNORE:
                directories.remove(direct)
        print("Current directory: {folder}".format(folder=os.path.join(os.path.abspath(path), "")))
        directories.sort()
        for filename in sorted(files):
            address = os.path.join(path, filename)
            extension = os.path.splitext(filename)[1]
            # Sort all text files that are not blacklisted
            if extension == ".txt" and filename not in IGNORE:
                fopsort(address)
            # Delete unnecessary backups and temporary files
            if extension == ".orig" or extension == ".temp":
                try:
                    os.remove(address)
                except(IOError, OSError):
                    # Ignore errors resulting from deleting files, as they likely indicate that the file has already been deleted
                    pass

    # If in a repository, offer to commit any changes
    if repository:
        commit(repository, basecommand, originaldifference)


def fopsort(filename):
    """ Sort the sections of the file and save any modifications."""
    temporaryfile = "{filename}.temp".format(filename=filename)
    CHECKLINES = 10
    section = []
    lineschecked = 1
    filterlines = elementlines = 0

    # Read in the input and output files concurrently to allow filters to be saved as soon as they are finished with
    with open(filename, "r", encoding="utf-8", newline="\n") as inputfile, open(temporaryfile, "w", encoding="utf-8",
                                                                                newline="\n") as outputfile:

        # Combines domains for (further) identical rules
        def combinefilters(uncombinedFilters, DOMAINPATTERN, domainseparator):
            combinedFilters = []
            for i in range(len(uncombinedFilters)):
                domains1 = re.search(DOMAINPATTERN, uncombinedFilters[i])
                if i + 1 < len(uncombinedFilters) and domains1:
                    domains2 = re.search(DOMAINPATTERN, uncombinedFilters[i + 1])
                if not domains1 or i + 1 == len(uncombinedFilters) or not domains2 or len(
                        domains1.group(1)) == 0 or len(domains2.group(1)) == 0:
                    # last filter or filter didn't match regex or no domains
                    combinedFilters.append(uncombinedFilters[i])
                elif domains1.group(0).replace(domains1.group(1), domains2.group(1), 1) != domains2.group(0):
                    # non-identical filters shouldn't be combined
                    combinedFilters.append(uncombinedFilters[i])
                elif re.sub(DOMAINPATTERN, "", uncombinedFilters[i]) == re.sub(DOMAINPATTERN, "",
                                                                               uncombinedFilters[i + 1]):
                    # identical filters. Try to combine them...
                    newDomains = "{d1}{sep}{d2}".format(d1=domains1.group(1), sep=domainseparator, d2=domains2.group(1))
                    newDomains = domainseparator.join(
                        sorted(set(newDomains.split(domainseparator)), key=lambda domain: domain.strip("~")))
                    if newDomains.count("~") > 0 and newDomains.count("~") != newDomains.count(domainseparator) + 1:
                        # skip combining rules with both included and excluded domains. It can go wrong in many ways and is not worth the code needed to do it correctly
                        combinedFilters.append(uncombinedFilters[i])
                    else:
                        domainssubstitute = domains1.group(0).replace(domains1.group(1), newDomains, 1)
                        uncombinedFilters[i + 1] = re.sub(DOMAINPATTERN, domainssubstitute, uncombinedFilters[i])
                else:
                    # non-identical filters shouldn't be combined
                    combinedFilters.append(uncombinedFilters[i])
            return combinedFilters

        # Writes the filter lines to the file
        def writefilters():
            if elementlines > filterlines:
                uncombinedFilters = sorted(set(section), key=lambda rule: re.sub(ELEMENTDOMAINPATTERN, "", rule))
                outputfile.write("{filters}\n".format(
                    filters="\n".join(combinefilters(uncombinedFilters, ELEMENTDOMAINPATTERN, ","))))
            else:
                uncombinedFilters = sorted(set(section), key=str.lower)
                outputfile.write("{filters}\n".format(
                    filters="\n".join(combinefilters(uncombinedFilters, FILTERDOMAINPATTERN, "|"))))

        for line in inputfile:
            minlength = 5
            curentline = line[:-1]
            linelength = len(curentline)
            if linelength == 0:
                continue
            if (linelength < minlength and curentline[0] != "!"):
                minlinetext = re.sub("^\s+|\n|\r|\s+$", '', curentline)
                print("***Warning***: The line length \"{minlinetext}\" is less than {minlength} ".format(
                    minlinetext=minlinetext, minlength=minlength))
            line = line.strip()
            if not re.match(BLANKPATTERN, line):
                # Include comments verbatim and, if applicable, sort the preceding section of filters and save them in the new version of the file
                if line[0] == "!" or line[:8] == "%include" or line[0] == "[" and line[-1] == "]":
                    if section:
                        writefilters()
                        section = []
                        lineschecked = 1
                        filterlines = elementlines = 0
                    outputfile.write("{line}\n".format(line=line))
                else:
                    # Neaten up filters and, if necessary, check their type for the sorting algorithm
                    elementparts = re.match(ELEMENTPATTERN, line)
                    if elementparts:
                        domains = elementparts.group(1).lower()
                        if lineschecked <= CHECKLINES:
                            elementlines += 1
                            lineschecked += 1
                        line = elementtidy(domains, elementparts.group(2), elementparts.group(3))
                    else:
                        if lineschecked <= CHECKLINES:
                            filterlines += 1
                            lineschecked += 1
                        line = filtertidy(line)
                    # Add the filter to the section
                    section.append(line)
        # At the end of the file, sort and save any remaining filters
        if section:
            writefilters()

    # Replace the existing file with the new one only if alterations have been made
    if not filecmp.cmp(temporaryfile, filename):
        # Check the operating system and, if it is Windows, delete the old file to avoid an exception (it is not possible to rename files to names already in use on this operating system)
        if os.name == "nt":
            os.remove(filename)
        os.rename(temporaryfile, filename)
        print("Sorted: {filename}".format(filename=os.path.abspath(filename)))
    else:
        os.remove(temporaryfile)


def filtertidy(filterin):
    """ Sort the options of blocking filters and make the filter text
    lower case if applicable."""
    optionsplit = re.match(OPTIONPATTERN, filterin)

    if not optionsplit:
        # Remove unnecessary asterisks from filters without any options and return them
        return removeunnecessarywildcards(filterin)
    else:
        # If applicable, separate and sort the filter options in addition to the filter text
        filtertext = removeunnecessarywildcards(optionsplit.group(1))
        optionlist = optionsplit.group(2).lower().replace("_", "-").split(",")

        domainlist = []
        removeentries = []
        for option in optionlist:
            # Detect and separate domain options
            if option[0:7] == "domain=":
                domainlist.extend(option[7:].split("|"))
                removeentries.append(option)
            elif option.strip("~") not in KNOWNOPTIONS:
                isReplace = len([i for i in optionlist if "replace=" in i]) > 0
                isProtoBuf =len([i for i in optionlist if "protobuf=" in i]) > 0
                isApp =len([i for i in optionlist if "app=" in i]) > 0
                if (isReplace or isProtoBuf or isApp):
                    if (isReplace):
                        optionlist = optionsplit.group(2).replace("_", "-").split(",")
                    if (isApp):
                        optionlist = optionsplit.group(2).split(",")
                else:
                    print(
                        "Warning: The option \"{option}\" used on the filter \"{problemfilter}\" is not recognised by FOP".format(
                            option=option, problemfilter=filterin))
        # Sort all options other than domain alphabetically
        # For identical options, the inverse always follows the non-inverse option ($image,~image instead of $~image,image)
        optionlist = sorted(set(filter(lambda option: option not in removeentries, optionlist)),
                            key=lambda option: (option[1:] + "~") if option[0] == "~" else option)
        # If applicable, sort domain restrictions and append them to the list of options
        if domainlist:
            optionlist.append("domain={domainlist}".format(
                domainlist="|".join(sorted(set(domainlist), key=lambda domain: domain.strip("~")))))

        # Return the full filter
        return "{filtertext}${options}".format(filtertext=filtertext, options=",".join(optionlist))


def elementtidy(domains, separator, selector):
    """ Sort the domains of element hiding rules, remove unnecessary
    tags and make the relevant sections of the rule lower case."""
    # Order domain names alphabetically, ignoring exceptions
    if "," in domains:
        domains = ",".join(sorted(set(domains.split(",")), key=lambda domain: domain.strip("~")))
    # Mark the beginning and end of the selector with "@"
    selector = "@{selector}@".format(selector=selector)
    each = re.finditer
    # Make sure we don't match items in strings (e.g., don't touch Width in ##[style="height:1px; Width: 123px;"])
    selectorwithoutstrings = selector
    selectoronlystrings = ""
    while True:
        stringmatch = re.match(ATTRIBUTEVALUEPATTERN, selectorwithoutstrings)
        if stringmatch == None: break
        selectorwithoutstrings = selectorwithoutstrings.replace(
            "{before}{stringpart}".format(before=stringmatch.group(1), stringpart=stringmatch.group(2)),
            "{before}".format(before=stringmatch.group(1)), 1)
        selectoronlystrings = "{old}{new}".format(old=selectoronlystrings, new=stringmatch.group(2))
    # Clean up tree selectors
    for tree in each(TREESELECTOR, selector):
        if tree.group(0) in selectoronlystrings or not tree.group(0) in selectorwithoutstrings: continue
        replaceby = " {g2} ".format(g2=tree.group(2))
        if replaceby == "   ": replaceby = " "
        selector = selector.replace(tree.group(0), "{g1}{replaceby}{g3}".format(g1=tree.group(1), replaceby=replaceby,
                                                                                g3=tree.group(3)), 1)
    # Remove unnecessary tags
    for untag in each(REMOVALPATTERN, selector):
        untagname = untag.group(4)
        if untagname in selectoronlystrings or not untagname in selectorwithoutstrings: continue
        bc = untag.group(2)
        if bc == None:
            bc = untag.group(3)
        ac = untag.group(5)
        selector = selector.replace("{before}{untag}{after}".format(before=bc, untag=untagname, after=ac),
                                    "{before}{after}".format(before=bc, after=ac), 1)
    # Make the remaining tags lower case wherever possible
    for tag in each(SELECTORPATTERN, selector):
        tagname = tag.group(1)
        if tagname in selectoronlystrings or not tagname in selectorwithoutstrings: continue
        if re.search(UNICODESELECTOR, selectorwithoutstrings) != None: break
        ac = tag.group(3)
        if ac == None:
            ac = tag.group(4)
        selector = selector.replace("{tag}{after}".format(tag=tagname, after=ac),
                                    "{tag}{after}".format(tag=tagname.lower(), after=ac), 1)
    # Make pseudo classes lower case where possible
    for pseudo in each(PSEUDOPATTERN, selector):
        pseudoclass = pseudo.group(1)
        if pseudoclass in selectoronlystrings or not pseudoclass in selectorwithoutstrings: continue
        ac = pseudo.group(3)
        selector = selector.replace("{pclass}{after}".format(pclass=pseudoclass, after=ac),
                                    "{pclass}{after}".format(pclass=pseudoclass.lower(), after=ac), 1)
    # Remove the markers from the beginning and end of the selector and return the complete rule
    return "{domain}{separator}{selector}".format(domain=domains, separator=separator, selector=selector[1:-1])


def commit(repository, basecommand, userchanges):
    """ Commit changes to a repository using the commands provided."""
    difference = subprocess.check_output(basecommand + repository.difference)
    if not difference:
        print("\nNo changes have been recorded by the repository.")
        return
    print("\nThe following changes have been recorded by the repository:")
    try:
        print(difference.decode("utf-8"))
    except UnicodeEncodeError:
        print("\nERROR: DIFF CONTAINED UNKNOWN CHARACTER(S). Showing unformatted diff instead:\n");
        print(difference)

    try:
        # Persistently request a suitable comment
        while True:
            comment = input("Please enter a valid commit comment or quit:\n")
            if checkcomment(comment, userchanges):
                break
    # Allow users to abort the commit process if they do not approve of the changes
    except (KeyboardInterrupt, SystemExit):
        print("\nCommit aborted.")
        return

    print("Comment \"{comment}\" accepted.".format(comment=comment))
    try:
        # Commit the changes
        command = basecommand + repository.commit + [comment]
        subprocess.Popen(command).communicate()
        print("\nConnecting to server. Please enter your password if required.")
        # Update the server repository as required by the revision control system
        for command in repository[7:]:
            command = basecommand + command
            subprocess.Popen(command).communicate()
            print()
    except(subprocess.CalledProcessError):
        print("Unexpected error with the command \"{command}\".".format(command=command))
        raise subprocess.CalledProcessError("Aborting FOP.")
    except(OSError):
        print("Unexpected error with the command \"{command}\".".format(command=command))
        raise OSError("Aborting FOP.")
    print("Completed commit process successfully.")


def isglobalelement(domains):
    """ Check whether all domains are negations."""
    for domain in domains.split(","):
        if domain and not domain.startswith("~"):
            return False
    return True


def removeunnecessarywildcards(filtertext):
    """ Where possible, remove unnecessary wildcards from the beginnings
    and ends of blocking filters."""
    whitelist = False
    hadStar = False
    if filtertext[0:2] == "@@":
        whitelist = True
        filtertext = filtertext[2:]
    while len(filtertext) > 1 and filtertext[0] == "*" and not filtertext[1] == "|" and not filtertext[1] == "!":
        filtertext = filtertext[1:]
        hadStar = True
    while len(filtertext) > 1 and filtertext[-1] == "*" and not filtertext[-2] == "|":
        filtertext = filtertext[:-1]
        hadStar = True
    if hadStar and filtertext[0] == "/" and filtertext[-1] == "/":
        filtertext = "{filtertext}*".format(filtertext=filtertext)
    if filtertext == "*":
        filtertext = ""
    if whitelist:
        filtertext = "@@{filtertext}".format(filtertext=filtertext)
    return filtertext


def checkcomment(comment, changed):
    """ Check the commit comment and return True if the comment is
    acceptable and False if it is not."""
    sections = re.match(COMMITPATTERN, comment)
    if sections == None:
        print("The comment \"{comment}\" is not in the recognised format.".format(comment=comment))
    else:
        indicator = sections.group(1)
        if indicator == "M":
            # Allow modification comments to have practically any format
            return True
        elif indicator == "A" or indicator == "P":
            if not changed:
                print(
                    "You have indicated that you have added or removed a rule, but no changes were initially noted by the repository.")
            else:
                address = sections.group(4)
                if not validurl(address):
                    print("Unrecognised address \"{address}\".".format(address=address))
                else:
                    # The user has changed the subscription and has written a suitable comment message with a valid address
                    return True
    print()
    return False


def validurl(url):
    """ Check that an address has a scheme (e.g. http), a domain name
    (e.g. example.com) and a path (e.g. /), or relates to the internal
    about system."""
    addresspart = urlparse(url)
    if addresspart.scheme and addresspart.netloc and addresspart.path:
        return True
    elif addresspart.scheme == "about":
        return True
    else:
        return False


if __name__ == '__main__':
    start()
print("DONE")
wait = input("PRESS ENTER TO EXIT.")

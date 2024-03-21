# Contributing to AdGuard filters

If you want to make AdGuard better by creating new rules, follow the
instructions below to make your ideas come to life faster!

## How to work with the repo

### Prepare

Here's what you need to do before you start working on the repo.

**Steps for contributors:**

1. If you don't have a GitHub account, [create one][createaccount].
2. Install [Git][git], [Node.js][nodejs] and [Yarn][yarn]. These are essential
   tools for working with the repo.
3. Install [Visual Studio Code][vscode] with the
   ["Adblock" syntax plugin][vscodeplugin]. We recommend using this editor to
   write filter rules.
4. Fork the original repo and clone *your fork* (since you don't have write
   access to the original repo). If you don't know how to do it, please read
   [this guide][clonerepo].
5. Install dependencies by running `yarn` in the root of the repo. This will
   install [AGLint][aglint] and [Husky][husky]. After the installation is
   complete, it will also call `postinstall` script that will install Husky
   pre-commit hook which will run AGLint on your changes before you commit
   them and will prevent you from committing if there are any errors.
6. Create a new branch for your changes. Please use the following naming
   convention: `fix/123` where `123` is the issue number you're working on.
7. Make your changes, test them and put them in the proper file or section
   of the file. Please read the [Repository structure](#repository-structure)
   section below to learn more about the structure of the repo.
8. If everything is fine, commit your changes. Please always make separate
   branches and commits for different issues and don't mix them in one. It
   is easier to manage and review them that way.
9. Push your new branch to your fork. This will create a new branch in your
    fork with the same name as the one you created locally and doesn't affect
    the original repo at this point.
10. Create a pull request from your fork to this repo and wait for the review.
    AGLint will run automatically on your PR and will report any errors.
    If there are any errors, fix them and push your changes to your fork.
    If AGLint passes, your PR will be reviewed by a maintainer.
11. If the review is successful, your changes will be merged into the `master`
    branch.

**Steps for maintainers:**

1. Installation and initial setup are the same as for contributors, but you
   don't need to fork the repo.
2. If you want to skip Husky pre-commit hook locally, use
   `git commit --no-verify -m "commit message"`
   but it is not recommended.
3. If you want to skip check on GitHub Actions, add `[skip ci]` to the commit
   message.

[aglint]: https://github.com/AdguardTeam/AGLint
[clonerepo]: https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository
[createaccount]: https://github.com/signup
[git]: https://git-scm.com/downloads
[husky]: https://typicode.github.io/husky
[nodejs]: https://nodejs.org/en/download
[vscode]: https://code.visualstudio.com/download
[vscodeplugin]: https://marketplace.visualstudio.com/items?itemName=adguard.adblock
[yarn]: https://classic.yarnpkg.com/en/docs/install

### Workflow

1. Make your changes and commit them.
2. Each commit should be linked to an issue. The commit message should look
   like the examples below. That way, the issue will be closed automatically
   once the commit is merged into the `master` branch.
   - `Fix #123 example.org` where `123` is the issue number and `example.org`
     is the website from the issue.
   - `Fix #123 comment` where `comment` is your comment for additional fixes in
     the pull request.

## How to write filter rules

Before you begin, please read and understand the current
[filters policy][policy] we adhere to. One of its most important points is the
[quality requirements][qualityrequirements].

The next step is creating rules.

- There is an [official documentation][documentation] that can help you.
- When you're done with creating rules, please take a look at the similar ones
  in the filters. This may help you to make a better version of the rule.

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/
[qualityrequirements]: https://adguard.com/kb/general/ad-filtering/filter-policy/#quality-requirements-for-filtering-rules
[documentation]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

## Repository structure

AdGuard filters are compiled from files in this repository. This is an automated
process that is periodically run by scripts in the [FiltersRegistry][registry]
repo. In this repository, each filter list is divided into several files, and
each file has its own purpose. If you're adding a new rule, make sure it is
added to the proper file or section of the file.

General requirements for submitting rules: don't add rules to the beginning of
the file, start entering them from line 4, for example. If you add rules with
a task comment or hints, put them next to the same structure in the file.

[registry]: https://github.com/AdguardTeam/FiltersRegistry

### AdGuard Base filter

- Purpose: this filter blocks various kinds of ads mostly on English-language
  and multilingual sites.
- [Base folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/BaseFilter/sections)
- Notes: The AdGuard Base filter includes [Easylist][easylist],
  so there's no need to add rules which are already in `Easylist`.

[easylist]: https://github.com/easylist/easylist

### AdGuard Mobile filter

- Purpose: this filter blocks various kinds of ads on mobile version of sites
  and in mobile apps.
- [Mobile folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/MobileFilter/sections)

### AdGuard Tracking Protection filter

- Purpose: this filter hides your actions online and helps avoid tracking.
- [Tracking Protection folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpywareFilter/sections)

### AdGuard URL Tracking filter

- Purpose: this filter removes various kinds of tracking parameters from sites.
- [URL Tracking folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TrackParamFilter/sections)

### AdGuard Social filter

- Purpose: this filter blocks various kinds of social widgets from sites.
- [Social folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SocialFilter/sections)

### AdGuard Annoyances filters

- Purpose: this filter blocks irritating elements on web pages including cookie
  notices, third-party widgets and in-page pop-ups.
- [Annoyances folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter)

  Contains the following AdGuard filters: Cookie Notices, Popups, Mobile
  App Banners, Other Annoyances and Widgets:

  - **Cookie Notices**

     Purpose: this filter blocks cookie notices on web pages.
    - [Cookies folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Cookies/sections)

  - **Mobile App Banners**

    - Purpose: this filter blocks irritating banners that promote mobile apps
      of websites.
    - [MobileApp folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/MobileApp/sections)

  - **Popups**

    - Purpose: this filter blocks all kinds of pop-ups that are not necessary
      for websites' operation.
    - [Popups folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Popups/sections)

  - **Widgets**

    - Purpose: this filter blocks annoying third-party widgets: online
      assistants, live support chats, etc.
    - [Widgets folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Widgets/sections)

  - **Other Annoyances**
    - Purpose: this filter blocks irritating elements on web pages that do not
      fall under the popular categories of annoyances.
    - [Other folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Other/sections)

### AdGuard Experimental filter

- Purpose: this filter serves to test some new filtering rules that can
  potentially cause conflicts and mess with websites' work. In case these rules
  perform without any issues, they get added to main filters.
- [Experimental folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ExperimentalFilter/sections)

### AdGuard Filter unblocking search ads and self-promotions

- Purpose: this filter unblocks search engine result that may be useful to
  users.
- [UsefulAdsFilter folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/UsefulAdsFilter/sections)

### AdGuard Russian filter

- Purpose: this filter blocks various kinds of ads on Russian-language sites.
- [Russian folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/CyrillicFilters/RussianFilter/sections)

### AdGuard Ukrainian filter

- Purpose: this filter blocks various kinds of ads on Ukrainian-language sites.
- [Ukrainian folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/CyrillicFilters/UkrainianFilter/sections)

### AdGuard Chinese filter

- Purpose: this filter blocks various kinds of ads on Chinese-language sites.
- [Chinese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ChineseFilter/sections)
- Notes: The AdGuard Chinese filter includes [Easylist China][easylistchina],
  so there's no need to add rules which are already in `Easylist China`.

[easylistchina]: https://github.com/easylist/easylistchina

### AdGuard Dutch filter

- Purpose: this filter blocks various kinds of ads on Dutch-language sites.
- [Dutch folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/DutchFilter/sections)

### AdGuard French filter

- Purpose: this filter blocks various kinds of ads on French-language sites.
- [French folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/FrenchFilter/sections)
- Notes: The AdGuard French filter includes [Liste FR][listefr],
  so there's no need to add rules which are already in `Liste FR`.

[listefr]: https://github.com/easylist/listefr

### AdGuard German filter

- Purpose: this filter blocks various kinds of ads on German-language sites.
- [German folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/GermanFilter/sections)
- Notes: The AdGuard German filter includes [Easylist Germany][easylistgermany],
  so there's no need to add rules which are already in `Easylist Germany`.

[easylistgermany]: https://github.com/easylist/easylistgermany

### AdGuard Japanese filter

- Purpose: this filter blocks various kinds of ads on Japanese-language sites.
- [Japanese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/JapaneseFilter/sections)

### AdGuard Spanish filter

- Purpose: this filter blocks various kinds of ads on Spanish-language and
  Portuguese-language sites.
- [Spanish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpanishFilter/sections)

### AdGuard Turkish filter

- Purpose: this filter blocks various kinds of ads on Turkish-language sites.
- [Turkish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TurkishFilter/sections)

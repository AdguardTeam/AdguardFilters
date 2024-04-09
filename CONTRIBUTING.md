# Contributing to AdGuard filters

If you want to make AdGuard better by creating new rules, follow the
instructions below to make your ideas come to life faster!

## Pre-requisites

- You need to have a [GitHub account][createaccount] to make contributions.
- You need to have the following tools installed on your machine:
  - [Git][git]
  - [Node.js][nodejs] (we recommend using the latest LTS version)
  - [Yarn][yarn] (you can install it using npm: `npm install -g yarn`)
  - [Visual Studio Code][vscode] (we recommend using this editor)
    - Install the recommended extensions for VSCode (listed in `.vscode/extensions.json`).
      - At first launch, you will be prompted to install them. If not, press `CTRL+SHIFT+P` and type
      `Show Recommended Extensions` and install them.
      - Please note that, by default Comment Anchors does not know adblock-style comments (like `! this is a comment`),
        so you'll need to add `!` as a match prefix in the `commentAnchors.tags.matchPrefix` setting
        (File -> Preferences -> Settings -> Extensions -> Comment Anchors Configuration).

[createaccount]: https://github.com/signup
[git]: https://git-scm.com/downloads
[nodejs]: https://nodejs.org/en/download
[vscode]: https://code.visualstudio.com/download
[yarn]: https://classic.yarnpkg.com/en/docs/install

## Setting up the repository

After you have installed the necessary tools, you need to set up the repository.

1. Fork the original repository on GitHub. This will create a copy of the repository in your account.
1. Clone remote repository from GitHub to your local machine.
1. Install the dependencies by running the following command in the terminal:
   ```bash
   yarn install
   ```
   This will install necessary tools like [AGLint][aglint] and initialize [Husky][husky] hooks.

[aglint]: https://github.com/AdguardTeam/AGLint
[husky]: https://typicode.github.io/husky

## Workflow for submitting changes

1. Create a new branch for your changes. Please use the following naming convention:
   `fix/123` where `123` is the issue number you're working on.
1. Make your changes, test them and put them in the proper file or section of the file.
   - You can learn how to write filtering rules in the [How to write filter rules][how-to-write-filters] section.
   - Please read and understand the current [filters policy][policy] we adhere to.
   - One of its most important points is the [quality requirements][qualityrequirements].
   - When you're done with creating rules, please take a look at the similar ones in the filters.
     This may help you to make a better version of the rule.
   - Please read the [Repository structure](#repository-structure) section below
     to learn more about the structure of the repo and where to put your rules.
1. If everything is fine, commit your changes. Please try to separate branches and commits
   for different issues and don't mix them in one. It is easier to manage and review them that way.
   - Note: By default, Husky pre-commit hook will run AGLint on your changes and will prevent you from committing
     if there are any errors in your changes.
1. Push your new branch to your remote repository.
1. Create a pull request from your branch to the `master` branch of the original repository.
   AGLint will run automatically on your PR and will report any errors.
   If there are any errors, fix them and push your changes to your fork.
   If AGLint passes, your PR will be reviewed by a maintainer.
1. If the review is successful, your changes will be merged into the `master` branch.

### Skipping checks

If you need to skip running checks, you can do it in the following ways.
Please note that it is only allowed in special cases and should not be used as a regular practice.

- Skip running Husky pre-commit hook: `git commit --no-verify -m "commit message"`.
- Skip running checks on GitHub: add `[skip ci]` to the commit message as a prefix.

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/
[qualityrequirements]: https://adguard.com/kb/general/ad-filtering/filter-policy/#quality-requirements-for-filtering-rules
[how-to-write-filters]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

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

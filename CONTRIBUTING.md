# Contributing to AdGuard filters

Short introduction, explain what the ways to contribute are.

## How to work with this repo

1. Install [Visual Studio Code](https://code.visualstudio.com/download) with the ["Adblock" syntax plugin](https://marketplace.visualstudio.com/items?itemName=adguard.adblock).
2. [Clone](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) (or fork and clone) this repo.
3. Make your changes and commit them.
4. Every commit needs to be linked to an issue. The commit message should look like the example below. This way the issue will be closed automatically once this commit lands in the `master` branch.
   * `Fix #123 site` where `123` is the issue number and `site` - website from the issue.
   * `Fix #123 comment` where `comment` is your comment for additional fixes in the pull request.

## How to write filter rules

Before you start, please also note we follow to the current [filters policy](https://kb.adguard.com/general/adguard-filter-policy). You should read and understand it - one of the most important things is the [quality requirements](https://kb.adguard.com/general/adguard-filter-policy#quality-requirements-for-filtering-rules).

Next step is creating rules.
* There is an official [documentation](https://kb.adguard.com/general/how-to-create-your-own-ad-filters) that can help you.
* When you're done with creating rules, please take a look at the similar ones in the filters. This may help you to make a better version of the rule.

## Repository structure

AdGuard filters are combined from the files in this repository. This is an automated process that is done periodically by the scripts in the [FiltersRegistry](https://github.com/AdguardTeam/FiltersRegistry) repo. In this repository, every filter list is split into a number of files and every file has its own purpose. If you're adding a new rule, make sure it is added to the proper file.

#### AdGuard Base filter

* Purpose: blocking different type of ads mostly on English, multilingual sites.
* [Base folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/EnglishFilter/sections)
* Requirements for rule submissions: don't add the rules at the beginning (make some step near the beginning); if you add rules with task comment or hints, put them next to the same structure in the file.
* Notes: AdGuard Base filter is supposed to be used alongside [Easylist](https://github.com/easylist/easylist) (as `AdGuard French` and `AdGuard Chinese`) so there's no need to add rules which are already in the `Easylist`.
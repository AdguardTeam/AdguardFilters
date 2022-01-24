# Contributing to AdGuard filters

If you want to make AdGuard better by implementing new rules, follow the instructions below to make your ideas come to life faster!

## How to work with the repo

1. Install [Visual Studio Code](https://code.visualstudio.com/download) with the ["Adblock" syntax plugin](https://marketplace.visualstudio.com/items?itemName=adguard.adblock).
2. [Clone](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) (or fork and clone) this repo.
3. Make your changes and commit them.
4. Each commit should be linked to an issue. The commit message should look like the examples below. That way, the issue will be closed automatically once the commit is merged into the `master` branch.
   * `Fix #123 site` where `123` is the issue number and `site` - website from the issue.
   * `Fix #123 comment` where `comment` is your comment for additional fixes in the pull request.

## How to write filter rules

Before you begin, please read and understand the current [filters policy](https://kb.adguard.com/general/adguard-filter-policy) we adhere to. One of its most important points is the [quality requirements](https://kb.adguard.com/general/adguard-filter-policy#quality-requirements-for-filtering-rules).

The next step is creating rules.
   * There is an official [documentation](https://kb.adguard.com/general/how-to-create-your-own-ad-filters) that can help you.
   * When you're done with creating rules, please take a look at the similar ones in the filters. This may help you to make a better version of the rule.

## Repository structure

AdGuard filters are compiled from files in this repository. This is an automated process that is periodically run by scripts in the [FiltersRegistry](https://github.com/AdguardTeam/FiltersRegistry) repo.  In this repository, each filter list is divided into several files, and each file has its own purpose. If you're adding a new rule, make sure it is added to the proper file.

#### AdGuard Base filter

* Purpose: this filter blocks various kinds of ads mostly on English-language and multilingual sites.
* [Base folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/EnglishFilter/sections)
* Requirements for submitting rules: don't add rules to the beginning of the file, start entering them from line 4, for example. If you add rules with a task comment or hints, put them next to the same structure in the file.
* Notes: The AdGuard Base filter is supposed to be used with [Easylist](https://github.com/easylist/easylist) (like `AdGuard French` and `AdGuard Chinese`) so there's no need to add rules that are already in `Easylist`.
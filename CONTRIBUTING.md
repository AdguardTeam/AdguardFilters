# Contributing to AdGuard filters

If you want to make AdGuard better by creating new rules, follow the instructions below to make your ideas come to life faster!

## How to work with the repo

1. Install [Visual Studio Code](https://code.visualstudio.com/download) with the ["Adblock" syntax plugin](https://marketplace.visualstudio.com/items?itemName=adguard.adblock).
2. [Clone](https://docs.github.com/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) (or fork and clone) this repo.
3. Make your changes and commit them.
4. Each commit should be linked to an issue. The commit message should look like the examples below. That way, the issue will be closed automatically once the commit is merged into the `master` branch.
   * `Fix #123 example.org` where `123` is the issue number and `example.org` - website from the issue.
   * `Fix #123 comment` where `comment` is your comment for additional fixes in the pull request.

## How to write filter rules

Before you begin, please read and understand the current [filters policy](https://kb.adguard.com/general/adguard-filter-policy) we adhere to. One of its most important points is the [quality requirements](https://kb.adguard.com/general/adguard-filter-policy#quality-requirements-for-filtering-rules).

The next step is creating rules.
   * There is an [official documentation](https://kb.adguard.com/general/how-to-create-your-own-ad-filters) that can help you.
   * When you're done with creating rules, please take a look at the similar ones in the filters. This may help you to make a better version of the rule.

## Repository structure

AdGuard filters are compiled from files in this repository. This is an automated process that is periodically run by scripts in the [FiltersRegistry](https://github.com/AdguardTeam/FiltersRegistry) repo.  In this repository, each filter list is divided into several files, and each file has its own purpose. If you're adding a new rule, make sure it is added to the proper file or section of the file.

General requirements for submitting rules: don't add rules to the beginning of the file, start entering them from line 4, for example. If you add rules with a task comment or hints, put them next to the same structure in the file.

### AdGuard Base filter

* Purpose: this filter blocks various kinds of ads mostly on English-language and multilingual sites.
* [Base folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/BaseFilter/sections)
* Notes: The AdGuard Base filter includes [Easylist](https://github.com/easylist/easylist) if you use AdGuard products, so there's no need to add rules which are already in `Easylist`.

### AdGuard Russian filter

* Purpose: this filter blocks various kinds of ads on Russian-language sites.
* [Russian folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/RussianFilter/sections)

### AdGuard Chinese filter

* Purpose: this filter blocks various kinds of ads on Chinese-language sites.
* [Chinese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ChineseFilter/sections)
* Notes: The AdGuard Chinese filter includes [Easylist China](https://github.com/easylist/easylistchina) if you use AdGuard products, so there's no need to add rules which are already in `Easylist China`.

### AdGuard Dutch filter

* Purpose: this filter blocks various kinds of ads on Dutch-language sites.
* [Dutch folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/DutchFilter/sections)

### AdGuard French filter

* Purpose: this filter blocks various kinds of ads on French-language sites.
* [French folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/FrenchFilter/sections)
* Notes: The AdGuard French filter includes [Liste FR](https://github.com/easylist/listefr) if you use AdGuard products, so there's no need to add rules which are already in `Liste FR`.

### AdGuard German filter

* Purpose: this filter blocks various kinds of ads on German-language sites.
* [German folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/GermanFilter/sections)
* Notes: The AdGuard German filter includes [Easylist Germany](https://github.com/easylist/easylistgermany) if you use AdGuard products, so there's no need to add rules which are already in `Easylist Germany`.

### AdGuard Japanese filter

* Purpose: this filter blocks various kinds of ads on Japanese-language sites.
* [Japanese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/JapaneseFilter/sections)

### AdGuard Spanish filter

* Purpose: this filter blocks various kinds of ads on Spanish-language and Portuguese-language sites.
* [Spanish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpanishFilter/sections)

### AdGuard Turkish filter

* Purpose: this filter blocks various kinds of ads on Turkish-language sites.
* [Turkish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TurkishFilter/sections)

### AdGuard Mobile filter

* Purpose: this filter blocks various kinds of ads on mobile version of sites.
* [Mobile folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/MobileFilter/sections)

### AdGuard Social filter

* Purpose: this filter blocks various kinds of social widgets from sites.
* [Social folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SocialFilter/sections)

### AdGuard Filter unblocking search ads and self-promotions

* Purpose: this filter unblocks search engine result that may be useful to users.
* [UsefulAdsFilter folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/UsefulAdsFilter/sections)

### AdGuard Annoyances filter

* Purpose: this filter blocks irritating elements on web pages including cookie notices, third-party widgets and in-page pop-ups.
* [Annoyances folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter)

   Contains the following AdGuard filters: Cookie Notices, Popups, Mobile App Banners, Other Annoyances and Widgets:

   - ### Cookie Notices
      * Purpose: this filter blocks cookie notices on web pages.
      * [Cookies folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Cookies/sections)

   - ### Mobile App Banners
      * Purpose: this filter blocks irritating banners that promote mobile apps of websites.
      * [MobileApp folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/MobileApp/sections)

   - ### Popups
      * Purpose: this filter blocks all kinds of pop-ups that are not necessary for websites' operation.
      * [Popups folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Popups/sections)

   - ### Widgets
      * Purpose: this filter blocks annoying third-party widgets - online assistants, live support chats, etc.
      * [Widgets folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Widgets/sections)

   - ### Other Annoyances
      * Purpose: this filter blocks irritating elements on web pages that do not fall under the popular categories of annoyances.
      * [Other folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Other/sections)

### AdGuard Experimental filter

* Purpose: this filter serves to test some new filtering rules that can potentially cause conflicts and mess with websites' work. In case these rules perform without any issues, they get added to main filters.
* [Experimental folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ExperimentalFilter/sections)

### AdGuard Tracking Protection filter

* Purpose: this filter hides your actions online and helps avoid tracking.
* [Tracking Protection folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpywareFilter/sections)

### AdGuard URL Tracking filter

* Purpose: this filter removes various kinds of tracking parameters from sites.
* [URL Tracking folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TrackParamFilter/sections)

# Adguard Ad Blocking Filters

### Introduction

This is a place where we create filters for Adguard. Every filter represents a set of rules in text format which are used by Adguard to filter advertising content (such as banners, pop-ups etc.). Rules specific for a particular Internet segment (English filter, Russian filter etc.) or serving a specific purpose (Social media filter, Spyware filter etc.) are collected into one list - filter - and can be enabled/disabled all at once. 

Filters are constantly updated. This repository lets anyone draw our attention to anything from a missed ad to a false positive, thus helping us to modify our filters, make them better and keep up-to-date.

Here you can find links to active Adguard forum threads devoted to [missed ads](https://forum.adguard.com/index.php?forums/missed-ads.67/) and [false positives](https://forum.adguard.com/index.php?forums/false-positives.68/).

### Syntax

Filters are designed for use in all Adguard products, but can also be used in Adblock Plus. However, note that the syntax of Adguard filtering rules is more advanced than in ABP. Therefore, part of the rules will not work in ABP.

You can find a manual for filtering rules creation syntax at [this link](https://adguard.com/filterrules.html).

### How to report a missed ad/false positive

1. Please, create a new issue for each new website.
2. Title of the issue should contain website’s address where a problem was detected, and preferably a short description - OS(Win, MacOS, iOS, Android) and type of problem.
For example: 
  - **site.com** - popup upon clicking anywhere [Windows] or
  - [Android] **The App** - banner in the main menu
3. The message should contain:
  - a screenshot of an unblocked ad or detailed description of where this ad is placed;
  - a direct link to the website; 
  - list of enabled filters.

### Adguard filter policy

Our filter policy is available [here](https://blog.adguard.com/en/adguard-news/adguard-filter-policy.html).

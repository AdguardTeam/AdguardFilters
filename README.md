# AdGuard Filters

### Introduction

This is the place where we create filters for AdGuard. Every filter represents a set of rules in text format which are used by AdGuard apps and programs to filter advertising and privacy-threatening content (such as banners, pop-ups, trackers etc.). Rules specific for a particular Internet segment (German filter, Russian filter etc.), or serving a specific purpose (Social media filter, Spyware filter etc.) are combined into one list - filter - and can be enabled/disabled all at once.

Our filters are being constantly updated. This repository lets anyone draw our attention to anything from a missed ad to a false positive, thus helping us to modify our filters, make them better and keep up-to-date.

To submit a report, proceed [here](https://github.com/AdguardTeam/AdguardFilters/issues) (please, read the [submission rules](https://github.com/AdguardTeam/AdguardFilters#how-to-report-a-missed-adfalse-positive) below first).

### Syntax

These filters are designed for use in all AdGuard products, but can also be used in Adblock Plus and other ad blockers. However, note that the syntax of AdGuard filtering rules is more advanced than in ABP. Therefore, part of the rules will not work there.

If you are interested in creating your own rules, you can find a syntax manual at [this link](https://kb.adguard.com/general/how-to-create-your-own-ad-filters).

### How to report a missed ad/false positive

We have launched a special web tool to report any filter-related problems with AdGuard: missed ads, false positives, anti-adblock scripts etc. Using it is much easier than manually filling out the form on GitHub with plain text, and in the end a bot will create a new issue in this repository anyway (you will get a link to it, of course). Please try it out: [AdGuard web reporting tool](https://reports.adguard.com/new_issue.html)

Alternatively, you can create a new issue the old-fashioned way. To do so, follow this step-by-step instruction:

1. Do a quick search to see if this issue has already been reported: https://github.com/AdguardTeam/AdguardFilters/issues/
2. Please, create a new issue for each new website.
3. The title should contain the address of the website where the problem was detected, and preferably a short description - OS prefix ([Win], [MacOS], [iOS], [Android]) and the type of the problem.
Examples of a good issue title: 
  - [Windows] **example.com** - popup upon clicking anywhere *or*
  - [Android] **The App** - banner in the main menu
4. There will be a template in the message body, asking you to provide the following information:
  - a screenshot of an unblocked ad or detailed description of where this ad is placed;
  - a direct link to the page; 
  - list of enabled filters;
  - some of your AdGuard settings;
  - your system details.

The more information you provide, the better are chances that we'll be able to pinpoint and fix the problem.  
  
### AdGuard filter policy

Our filter policy is available [here](https://kb.adguard.com/en/general/adguard-filter-policy).

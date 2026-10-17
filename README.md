<!-- markdownlint-disable -->
&nbsp;

<p align="center">
    <img width="275" alt="AdGuard Filters logo" src="https://cdn.adtidy.org/website/github.com/AdguardFilters/viking.svg" />
</p>
<h1 align="center">AdGuard Filters</h1>
<p align="center">
    The place where ad trackers are actually blocked.
</p>

<p align="center">
    <a href="https://adguard.com/">Website</a> |
    <a href="https://reddit.com/r/Adguard">Reddit</a> |
    <a href="https://x.com/AdGuard">X</a> |
    <a href="https://t.me/adguard_en">Telegram</a>
    <br /><br />
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml/badge.svg?branch=master" alt="AGLint status"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master" alt="GitHub Pages deployment"></a>
</p>

<p align="center">
    <a href="https://github.com/AdguardTeam/AdguardFilters/blob/master/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/AdguardTeam/AdguardFilters" alt="License"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AdguardTeam/AdguardFilters" alt="GitHub contributors"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/commit-activity" target="_blank"><img src="https://img.shields.io/github/commit-activity/m/AdguardTeam/AdguardFilters" alt="GitHub commit activity"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues" target="_blank"><img src="https://img.shields.io/github/issues/AdguardTeam/AdguardFilters" alt="GitHub issues"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues?q=is%3Aissue+is%3Aclosed" target="_blank"><img src="https://img.shields.io/github/issues-closed/AdguardTeam/AdguardFilters" alt="GitHub closed issues"></a>
</p><br />
<!-- markdownlint-restore -->

This is the place where we create filters for [AdGuard][adguard] and other
ad-blocking software, such as uBlock Origin. Each filter consists of a set of
text-based rules that AdGuard apps and programs use to filter out advertisements
and privacy-invasive content like banners, pop-ups, and trackers. Rules specific
to a certain region (e.g., German filter, Russian filter) or serving a specific
purpose (e.g., Social Media filter, Tracking Protection filter) are combined
into a single list, or filter, that can be enabled or disabled all at once.

Our filters are constantly updated. This repository allows anyone to bring our
attention to anything from overlooked ads to false positives, helping us refine
our filters, improve them, and keep them current.

We are proud of the fact that AdGuard filters are among the most actively
developed content-blocking filter lists available, if not the most.

[adguard]: https://adguard.com/

<!-- markdownlint-disable -->
<br />

* [AdGuard Filters Policy](#filterspolicy)
* [Contribution](#contribution)
  * [How to report an issue](#issue)
  * [Suggest filtering rules](#suggest)
  * [Translating AdGuard](#contribution-translating)
  * [Other options](#contribution-other)

<br />
<!-- markdownlint-restore -->

<a id="filterspolicy"></a>

## AdGuard Filters Policy

Our filter policy is available [here][policy].

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/

<a id="contribution"></a>

## Contribution

We are blessed to have a community that does not only love AdGuard, but also
gives back. A lot of people volunteer in various ways to make other users'
experience with AdGuard better, and you can join them! We, on our part, can
only be happy to reward the most active members of the community.
So, what can you do?

<a id="issue"></a>

### How to report an issue

GitHub can be used to report a bug or to submit a feature request. To do so,
go to [this page][issues] and click the *New issue* button.

>**Note:** for the filter-related issues (missed ads, false positives etc.)
>use our [reporting tool][tool].

[issues]: https://github.com/AdguardTeam/AdguardFilters/issues
[tool]: https://link.adtidy.org/forward.html?action=report&app=home&from=github

<a id="suggest"></a>

### Suggest filtering rules

You will find a lot of open issues, each one referencing a problem with some
website — a missed ad, a false positive etc. — choose any one and suggest your
own rules in comments. AdGuard filter engineers will review your suggestions,
and if they find them correct, your rules will be added to AdGuard filters.

Here is the [official documentation][documentation] on AdGuard filtering rules
syntax. You'll need to read it before you'll be able to create your own
filtering rules.

[documentation]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

<a id="contribution-translating"></a>

### Translating AdGuard

If you want to help with AdGuard translations, please learn more about
translating our products [here][translate].

[translate]: https://adguard.com/kb/miscellaneous/contribute/translate/program/

<a id="contribution-other"></a>

### Other options

Here is a [dedicated page][other] for those who are willing to contribute.

[other]: https://adguard.com/contribute.html

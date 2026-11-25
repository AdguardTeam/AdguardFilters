# Run instruction: AdguardFilters

The run verifies a rule in one of two blockers, chosen per report by the routing guidance: the
built-in AdGuard Browser Extension in Chromium, or AdGuard CLI as a filtering proxy for reports
from AdGuard apps that filter at the network level. The host prepares, launches and reads both back
itself. This file adds nothing to those routes but the guidance documents this repository writes
its rules against.

application: adguard-extension

The run loads its filter guidance at start from these role documents:

- [AdGuard filter syntax](https://github.com/AdguardTeam/KnowledgeBase/blob/master/docs/general/ad-filtering/create-own-filters.md)
- [AdGuard filter policy](https://github.com/AdguardTeam/KnowledgeBase/blob/master/docs/general/ad-filtering/filter-policy.md)
- [AdguardFilters contributing guide](https://github.com/AdguardTeam/AdguardFilters/blob/master/CONTRIBUTING.md)

Rule placement is deliberately not declared: this repository files rules per language and per
rule kind across `<Filter>/sections/*.txt`, and one declaration would force every rule into a
single file. Choose the file from where the repository already keeps rules like the new one: the
file that holds the reported site's rules, otherwise the one that holds rules of the same kind.

## Filter policy

The agent never closes an issue. "Recommend closing" below means the report says no rule is
needed; a maintainer checks it and decides.

- The site's own advertising (first-party ads): no rule; recommend closing.
- Paywalls: no rule; recommend closing.
- German anti-adblock walls: no rule; recommend closing. This covers only a German site's wall
  or popup that detects the ad blocker and asks to disable it or to allowlist the site. A page in
  German is not enough, and the reporter's choice of "anti-adblock" as the problem type is not
  evidence: check what the page itself shows.
- Any other anti-adblock wall: write a rule only once the page's requests the agent captured show
  the detector script; without it, hand the report to a maintainer.
- Not anti-adblock at all: scam, phishing, fake virus or tech-support pages, malware downloads.
  None of the rules above applies; handle the report like any other, for example with a rule
  that blocks the dangerous page.

## Maintainer rules

How this repository's maintainers write rules. These rules come on top of the documents above and
take precedence over the agent's own judgement of which rule is best. Maintainers add a rule here
whenever they keep fixing the agent's proposals the same way.

### Anti-adblock popups: hide the popup when that is enough

A cosmetic rule that hides the popup is fine when the page then works: the content is unlocked,
scrolling works and the popup does not come back. Neutralize the detector with a scriptlet
(usually `set-constant` or `abort-on-property-read`) only when hiding is not enough.

### Shared rules: extend them, but not the ones grouped by project

Many rules in every filter are shared by several sites: one rule listing every domain, often under
a comment naming the script or service it targets. When the fix fits an existing shared rule, add
the reported domain to that rule instead of writing a new one. Do not add a domain to a group of
rules kept for one project: those belong to that project's sites only.

Example, AdguardTeam/AdguardFilters#243463 (wzielonej.pl, anti-adblock popup): the site runs a
detector that `BaseFilter/sections/antiadblock.txt` already handles, so the fix is `wzielonej.pl`
added to the shared rule under `! 'tie.ad_blocker_detector' (tie-popup-adblock)`, which is
`#%#//scriptlet("set-constant", "tie.ad_blocker_detector", "")`.

### Cookie banners of a consent platform: use the platform's shared rule

Many cookie banners come from a consent platform, such as iubenda, Real Cookie Banner or the
Shopware cookie notice, that `AnnoyancesFilter/Cookies/sections/cookies_specific.txt` already
handles for other sites. Larger platforms have a group in the `Cookies - Popular rules` section at
the top of the file, under a comment that names the platform, its attribute or its script; others
have a rule or a few rules listing their sites further down. Find the platform's rules with
`search_rules`: search its script host as a URL pattern, written as the rules write it
(`||cs.iubenda.com^`), and the banner's selector. A cookie or storage key cannot be searched. Then
read the lines around a rule you found (`search_rules` with `filePath` and `line`): the platform's
other rules are next to it, with the comments that say which rule fits which banner.

When the platform has a shared rule, add the reported domain to it, even if it works differently
from the rule you would write: it may set the consent cookie or storage item, click a button on the
banner, block the platform's script or hide the banner. When the group has both a rule that hides
the banner and one that blocks the platform's script, and both work, use the blocking one. Use a
rule that clicks a button or sets the consent when the comments point to it, or when hiding and
blocking leave the page unusable. Banners without such a platform rule are still usually hidden.

Example, AdguardTeam/AdguardFilters#245366 (antispyshop.de, iubenda): the group under
`! START: iubenda CMP` hides the banner with `##body #iubenda-cs-banner` and blocks the platform's
script with `||cs.iubenda.com^$domain=<sites>`. The fix is `antispyshop.de` added to the blocking
rule, not to the hiding one.

### Google "preferred source" buttons: hide what is left around the link

Many news sites show a button that asks the reader to add the site as a preferred source on Google.
It links to `https://www.google.com/preferences/source?q=<site>` or
`https://google.com/preferences/source?q=<site>`. Generic rules in
`AnnoyancesFilter/Popups/sections/subscriptions_general.txt` hide both links on every site, so the
link needs no rule for the reported site. When text, an icon or an empty box stays around the
hidden link, hide the smallest block that holds only the button, for example with `:has()` on the
link, in `AnnoyancesFilter/Popups/sections/subscriptions_specific.txt`. When the link itself is
still visible, because generic hiding is off for the site or the link has another form, write a
rule for that link with the site's domain in the same file. Other Google buttons, such as
"Follow on Google" (`https://profile.google.com/cp/`) and Google News
(`https://news.google.com/publications/`), have shared rules that list their sites in that file:
add the reported domain to the rule for the button's link.

Example, AdguardTeam/AdguardFilters#246399 (prothomalo.com): the fix for the button is
`prothomalo.com##.story-content > div:has(> span + a[href^="https://www.google.com/preferences/source?q="])`
in `AnnoyancesFilter/Popups/sections/subscriptions_specific.txt`.

### Ads opened in a new tab on click: stop what opens them

When a click on the page opens an ad in a new tab or window, find what opens it and stop that:
block the ad script or the request that loads the ad's settings, or remove the click handler, for
example with `remove-attr` on an `onclick` attribute. `prevent-window-open` stops only the new tab,
while the ad code keeps running. Propose `prevent-window-open` only when you cannot find what opens
the tab.

Example, AdguardTeam/AdguardFilters#245402 (startseite.to): an `onclick` attribute on `body` opens
ddownload.com on every click, so the fix is
`startseite.to#%#//scriptlet('remove-attr', 'onclick', 'body[onclick]')`, not
`startseite.to#%#//scriptlet('prevent-window-open', 'ddownload.com')`.

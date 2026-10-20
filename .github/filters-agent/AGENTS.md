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

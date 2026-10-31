# FiltersAgent in AdguardFilters

[FiltersAgent](https://github.com/AdguardTeam/FiltersAgent) looks at every new issue in this
repository. It opens the reported page in a real browser with AdGuard Browser Extension or AdGuard
CLI, tries to write a rule that fixes the problem, and posts what it found as one comment on the
issue. It never commits a rule and never closes an issue: a maintainer reads the report and decides.

This guide is for filter maintainers. It explains how to read a report and how to change what the
agent does. What the agent proposes depends on what maintainers write for it.

## When a report appears

The agent runs on every new issue and usually reports within 20 minutes. It posts no report when:

- the issue has the `NSFW` label;
- a maintainer is already on the issue: the `A: In progress` label, an assignee or a maintainer's
  comment;
- the issue is closed, or a commit or pull request of this repository mentions it;
- the issue is not a filter report or names no page;
- the agent could not investigate the issue, for example when the page does not open from GitHub's
  servers.

The reason is in the log of the run. Find the run by the issue's title in the
[list of runs](https://github.com/AdguardTeam/AdguardFilters/actions/workflows/filters-agent.yml).
Runs marked as skipped come from label changes, so ignore them.

To ask for a report yourself, see [Run the agent again](#run-the-agent-again).

## Read a report

The first line of a report is the result. The sections under it are the evidence. A section with
nothing to say is left out.

### The result

- **Candidate rule proposed.** The agent tried the rule on the page and the problem went away. The
  check shows that the rule works on this page, not that it is the rule you would write: a shared
  rule or a more stable selector may fit better. Review the rule, then commit it or write your own.
- **Analysis-only findings, no verified change.** The agent has no rule it could prove. If it found
  a rule it could not confirm, the rule is under *Candidate for review*, with the reason. Check
  such a rule yourself, it can still be right. In
  [#245529](https://github.com/AdguardTeam/AdguardFilters/issues/245529#issuecomment-6439059952)
  a maintainer used the rule as it was and put it in another list.
- **The reported defect was not reproduced.** The agent did not see the problem. Its product,
  browser or region can differ from the reporter's, so compare them before you close the issue.
- **Already fixed in the current build.** The agent saw the problem without filters, and the
  current filters fix it. Compare the setups here too: the reporter may still see the problem.
- **The filter policy recommends closing without a rule.** A line of the filter policy says that no
  rule is needed, and *Policy rationale* quotes it. Check that the line fits the report, then
  decide. If the line is wrong, [change it](#edit-agentsmd).
- **The filter policy leaves this report to a maintainer.** The policy does not let the agent
  decide, or has no line for this case. *Policy rationale* says why.

Rarer results explain themselves, for example *Fixed in the filter source, pending publication*.

### The sections

- **Reproduced symptom.** Whether the agent saw the problem, and what it saw. *Indeterminate* means
  that it could not tell.
- **Rule.** The rule the agent checked.
- **Candidate for review.** A rule the agent could not confirm, the list it suggests, and why it
  could not confirm the rule.
- **Still visible after the rule.** What the agent's review still saw on the page with that rule.
- **Policy rationale.** The lines of the filter policy that allowed a rule or ruled it out.
- **Place in the list.** The file for the rule and the place in it. The links go to the filters
  commit in the last line of the report, so the lines may have moved since then. *By adding the
  domain to the existing rule on line N* means that a shared rule fits, as in
  [#245285](https://github.com/AdguardTeam/AdguardFilters/issues/245285#issuecomment-6385390775).
  *At the end of the file* means that the agent found no better place. The place is a suggestion:
  [Rule placement](../../CONTRIBUTING.md#rule-placement) has the final say.
- **Missing information.** What the agent lacked. It can be a detail from the reporter, or a case
  that its instructions do not cover, as in
  [#245307](https://github.com/AdguardTeam/AdguardFilters/issues/245307#issuecomment-6391155248).
  The second kind is a reason to [change the agent](#change-the-agent).
- **Screenshots.** The page without and with the rule. They are stored in the
  `filters-agent-screenshots` branch, so keep that branch.
- **Executor and version.** The AdGuard Browser Extension build the run used. The section is missing
  when the run did not use the extension, for example when it used AdGuard CLI.
- **Artifacts.** A link to the run. The Summary page of the run has the full evidence as a download:
  the agent's steps, screenshots, the page's DOM and its network log.

## Change the agent

The agent improves mostly through you. It does not learn from how you fix its proposals: every run
starts from the filter lists and from what is written in this folder. When you keep fixing its
proposals the same way, write that down, and later runs will follow it. You do not need to touch
its code: two things in this folder steer it.

- [AGENTS.md](AGENTS.md) goes into every run. Use it for rules that apply to many issues.
- A skill is read only when an issue needs it. Use it for a narrow procedure, such as how to handle
  one anti-adblock vendor. In AGENTS.md such a text would use space in every run.

### Edit AGENTS.md

The file has three parts:

- The top describes the run and links the documents the agent follows: the filter syntax, the
  filter policy and [CONTRIBUTING.md](../../CONTRIBUTING.md). Changes to these documents reach the
  agent too. Leave the `application: adguard-extension` line and the link titles as they are: the
  agent finds each document by the word `syntax`, `policy` or `contributing` in its title.
- `## Filter policy` says which reports get no rule and which go to a maintainer.
- `## Maintainer rules` says how this repository writes rules. These rules win over the agent's own
  judgement.

To add a maintainer rule, follow the rules already in that section: a `###` heading that states the
rule, a short paragraph and a real issue as an example. Say when the rule applies, what to write,
what not to write and why.

Two limits:

- The file can hold 16,000 characters. A longer file fails every run.
- A `##` heading that contains `preparation`, `application`, `verification`, `selection`,
  `which issues` or `report template` has a special meaning. Name your heading differently.

More in [Your own rules for the agent][own-rules].

### Add a skill

Create `.github/filters-agent/.agents/skills/<name>/SKILL.md`, where `<name>` uses lowercase
letters, digits and hyphens:

```markdown
---
name: <name>
description: <When this skill applies, in one sentence.>
---

<How to recognize the case, what to write, what not to write, a real issue as an example.>
```

- In every run the agent sees only `name` and `description`, and it decides from them whether to
  read the rest. Name what it can see on the page or in the issue, such as a script host or the
  text of a wall. Keep the description short, and put it in quotes if it contains a colon.
- Put longer material into text files next to `SKILL.md` and point to them by a relative path.
  Scripts in a skill do not run.
- Keep `README.md` and other `.md` files out of the top of `.agents/skills/`: each of them is read
  as a skill.
- A skill with a broken header is skipped, and the log of the run has a warning.

More in [Skills][skills].

### Send the change

Send a pull request, as for any other change in this repository. The agent reads these files from
`master`, so a change works from the first run after the merge. It cannot be tried on a branch, and
reports that are already posted stay as they are.

To see the effect on an open issue, [run the agent again](#run-the-agent-again) after the merge.
Keep that issue's number out of the pull request and its commits: a mention counts as a fix, and
the agent then skips the issue.

## Run the agent again

Add the `filters-agent` label to the issue. The agent then reports even when a maintainer is already
on the issue.

- If the title, the text and the comments of the issue have not changed since the agent's last
  report, the run posts nothing. Add a comment first. The agent reads the comments of the reporter
  and of maintainers, so you can also tell it what to look at. A comment with a rule or a link to a
  fix does not count, because the agent does not see it.
- The label stays on the issue. To run the agent once more, remove the label and add it again.
- The label has no effect on a closed issue, on an `NSFW` issue and on an issue that a commit or
  pull request mentions.
- If the run cannot open the page or fails, it posts a one-line notice with a link to the run.

## Ask for other changes

- **What the agent can do, and how its report looks.** Open an issue in
  [FiltersAgent](https://github.com/AdguardTeam/FiltersAgent/issues) with a link to the report.
- **When the agent runs, and which model it uses.** These are set in
  [filters-agent.yml](../workflows/filters-agent.yml). A change there is a pull request that the
  workflow's code owners review.

[own-rules]: https://github.com/AdguardTeam/FiltersAgent/blob/v1/docs/guides/github-action.md#your-own-rules-for-the-agent
[skills]: https://github.com/AdguardTeam/FiltersAgent/blob/v1/docs/guides/github-action.md#skills

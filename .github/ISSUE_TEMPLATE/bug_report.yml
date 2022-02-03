name: Pull request
description: Please include a summary of the change and which issue is fixed. If the related issue does not exist in our repository, please create it before making pool request.
body:
  - type: checkboxes
    attributes:
      label: Prerequisites
      description: |
        To avoid invalid pull requests, please check and confirm following checkboxes.
        It is highly recommended to use our [Web Reporting Tool](https://kb.adguard.com/en/technical-support/reporting-tool) instead of creating an issue on GitHub.
      options:
        - label: This is not an ad/bug report;
          required: true
        - label: Filters were updated before reproducing an issue;
          required: true
        - label: AdGuard product version is up-to-date;
          required: false
        - label: Browser version is up-to-date;
          required: true
        - label: If the site or app is broken, disabling AdGuard protection resolves an issue;
          required: true
        - label: My code follows the style guidelines of this project;
          required: true          
        - label: I have performed a self-review of my own code;
          required: true
        - label: My changes do not break web sites, apps and files structure.
          required: true  

- type: dropdown
    id: what-fixed
    attributes:
      label: What what problem does pull request fix?
      description: If the problem does not fall under any category that is listed here, please contact our tech support - support@adguard.com
      multiple: true
      options:
        - Missed ads or ad leftovers
        - Website or app doesn't work properly
        - AdGuard gets detected on a website
        - Social media buttons — share, like, tweet, etc.
        - Annoyances — pop-ups, cookie warnings, etc.
        - Missed analytics or tracker
    validations:
      required: true

- type: input
    id: issue
    attributes:
      label: Which issue is fixed?
      description: Enter an issue number or address.
      placeholder: ex. #100000 or https://github.com/AdguardTeam/AdguardFilters/issues/100000
    validations:
      required: true

- type: textarea
    id: comments
    attributes:
      label: Add your comment and screenshots
      description: |
        0. DO NOT upload screenshots with sexually explicit material on GitHub directly. Instead, upload it to third-party image hosting and post URL here;
        1. Add screenshots of the problem. You can drag and drop images or paste them from clipboard;
           Use `<details> </details>` tag to hide screenshots under the spoiler; 
        2. Describe the issue extensively unless it is absolutely clear from the screenshot what the problem is;
        You can also indicate any other information that you think the developers should know.

        Warning: Please remove personal information before uploading screenshots!
      value: |
          1. <comment>

          2. Screenshots
          <details><summary>Screenshot 1:</summary>

          <!-- paste screenshot here -->

          </details>

          <details><summary>Screenshot N:</summary>

          <!-- paste screenshot here -->

          </details>
    validations:
      required: true

  - type: checkboxes
    id: terms
    attributes:
      label: Privacy
      description: By submitting this issue, you agree that pull request does not contain private info
      options:
        - label: I agree to follow this condition
          required: true

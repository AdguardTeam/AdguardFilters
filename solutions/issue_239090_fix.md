**Solution – Add a custom filter rule that allows the redirect from `email‑link.adtidy.org`**

AdGuard blocks the redirect because it is treated as a *third‑party* request.  
The easiest fix is to add a rule that explicitly allows third‑party requests (or the
redirect itself) for that host.

---

### 1. Open the “Custom filters” page

```
Settings → Filters → Custom filters
```

### 2. Add one of the following rules

| Purpose | Rule | Why it works |
|---------|------|--------------|
| **Allow all third‑party requests** | `email-link.adtidy.org$~third-party` | Removes the “third‑party” restriction, letting the redirect go through. |
| **Allow only the redirect** | `email-link.adtidy.org$redirect,~third-party` | Explicitly permits the redirect while still blocking other request types. |
| **Allow everything (most permissive)** | `email-link.adtidy.org$~third-party,~image,~script,~style,~font,~media,~object,~xmlhttprequest` | Opens the host to all request types – use only if you’re sure the domain is safe. |

> **Tip** – If you only want to unblock the redirect but keep other protections, use the *redirect* rule above.

### 3. Save and refresh

After adding the rule, click **Save** and reload the page.  
The redirect to AdGuard’s own site should now work while the rest of the filter list remains intact.

---

#### Quick‑copy snippet

```text
# Custom filter – allow redirect from email-link.adtidy.org
email-link.adtidy.org$redirect,~third-party
```

Add the line to the *Custom filters* section and hit **Save**.  
That’s all you need to fix the “Incorrect Blocking” issue for this site.
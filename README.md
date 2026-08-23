# Check In On Me — checkinonme.app

Static marketing, support and legal site for **SafePulse** (shipped as **PulseGuard** on the
Amazon Appstore).

---

## Hosting and deploy — read this first

The site is served by a **Cloudflare Worker named `checkinonme-pages`**.

> ⚠️ **That name is misleading.** It is a **Worker**, not a Cloudflare Pages project. Look under
> **Workers & Pages → Workers**, not under Pages. The account has exactly one Pages project and
> it is `paulgeise-author`, which is a different site.

**To deploy: push to `master`.**

```
git push origin master
```

That is the whole process. There is no build step and no manual `wrangler` command. Confirmed
against the Worker's deployment log — every commit produces a `version_upload` roughly 45
seconds after the push:

| Commit | Pushed (EDT) | Deployed (UTC) |
|---|---|---|
| `6991e11` | Aug 10, 17:07 | Aug 10, 21:08 |
| `8bcbc16` | Aug 19, 18:37 | Aug 19, 22:38 |
| `4fdbfd1` | Aug 23, 17:22 | Aug 23, 21:23 |

The branch is **`master`**, not `main`.

### Verifying a deploy

Do **not** trust the browser alone — it caches this site's HTML hard, and a live change can
look missing for minutes. Hard-refresh with Ctrl+F5 before concluding anything is wrong.

Two verification routes do not work here:

- **WebFetch and plain `curl` get HTTP 403** — Cloudflare bot filtering.
- **Local `curl` is unreliable in general on this machine** — Norton HTTPS scanning breaks
  Python SSL and fakes failures.

What does work is `curl` with a browser User-Agent:

```
curl -s -o out.html -w "HTTP %{http_code}\n" \
 -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" \
 -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
 "https://checkinonme.app/"
```

Then grep `out.html` for the string you changed.

---

## Pages

Clean, extension-less URLs are served for every `*.html` file.

| File | Live URL | Purpose | Search |
|------|----------|---------|--------|
| `index.html` | `/` | Landing page | indexed |
| `compare.html` | `/compare` | SafePulse vs. competitors | indexed |
| `setup.html` | `/setup` | Setup guide | indexed |
| `privacy.html` | `/privacy` | **Privacy policy — use this URL in Android store listings** | indexed |
| `privacy-ios.html` | `/privacy-ios` | **Privacy policy for the App Store submission** | indexed |
| `terms.html` | `/terms` | Terms of Service | indexed |
| `sms-consent.html` | `/sms-consent` | SMS program and opt-in consent | indexed |
| `approve.html` | `/approve` | Contact consent landing page — the link in every invite text | noindex |
| `resume.html` + `resume-*.html` | `/resume`, `/resume-rhel`, … | Recruiter-facing résumé variants | noindex |
| `video-brief.html` | `/video-brief` | Unlisted brief for a viral-video creator | noindex |

Also served: `safepulse-alerts.vcf` (the "add SafePulse to my contacts" card linked from
`approve.html`), the résumé PDFs, `robots.txt`, `sitemap.xml`, and `_headers`.

`_headers` applies `X-Robots-Tag: noindex, nofollow` to `/*.pdf`, because a PDF cannot carry a
`<meta robots>` tag. The HTML pages use `<meta name="robots">` directly.

---

## Things that will bite

- **`/privacy` is referenced by live store listings and by shipped app binaries.** The Amazon
  build links it. It must keep resolving; do not rename or remove it.
- **Store forms and this site must agree.** A store declaration that contradicts the published
  policy is what got the Play v2.1.16 listing rejected. `AreYouDead/DATA_DISCLOSURE_CANONICAL.md`
  is the single source of truth for those facts — edit it first, then propagate here.
- **Never claim "no servers" or "your data never leaves your phone."** False since the gateway
  switch, on every platform. That claim has been removed from this site; do not reintroduce it.
- **Cross-promo bars** at the top of `index.html` link to `paulgeise.com`. The reverse link
  lives on that site, which is a **manual** Cloudflare Pages upload — a commit there deploys
  nothing.

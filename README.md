# Check In On Me — checkinonme.app

Static marketing + legal site for **SafePulse** (aka **PulseGuard** on Apple/Amazon),
hosted on **Cloudflare Pages** with the domain `checkinonme.app`.

## Pages
| File | Live URL | Purpose |
|------|----------|---------|
| `index.html` | https://checkinonme.app/ | Landing page |
| `privacy.html` | https://checkinonme.app/privacy | **Privacy policy** — use this URL in store listings |
| `terms.html` | https://checkinonme.app/terms | Terms of Service |

Cloudflare Pages serves `*.html` at clean extension-less URLs (`/privacy`, `/terms`).

## Deploy (Git-connected, auto-deploy)

1. **Create a GitHub repo** named `CheckInOnMe-Pages` (private is fine) and push this folder:
   ```
   git remote add origin https://github.com/slufoot80/CheckInOnMe-Pages.git
   git branch -M main
   git push -u origin main
   ```
2. **Cloudflare dashboard** → Workers & Pages → Create → Pages → **Connect to Git**.
   - Pick the `CheckInOnMe-Pages` repo, branch `main`.
   - Framework preset: **None**. Build command: *(leave blank)*. Build output directory: `/` (root).
   - Save and Deploy. You get a `*.pages.dev` URL.
3. **Attach the custom domain**: in the new Pages project → **Custom domains** → Set up a domain →
   enter `checkinonme.app` (and optionally `www.checkinonme.app`). Because the domain's DNS is
   already on Cloudflare, the CNAME/record is added automatically. SSL provisions in a few minutes.
4. After that, **every `git push` to `main` auto-deploys**.

## Status
- Governing law (Terms §14): **Michigan, United States** — filled in.
- Privacy policy: ready, no edits needed. Use `https://checkinonme.app/privacy` in store listings.

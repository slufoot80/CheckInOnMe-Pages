#!/usr/bin/env node
// Monthly source check for the statistics cited on /home-health-safety.
//
// What this does NOT do: rewrite a statistic. The BLS injury survey publishes
// once a year, and a number scraped wrong and pushed live in front of clinicians
// is worse than a number that is a year stale. So this script only ever:
//
//   1. re-fetches each cited source and confirms the figures we quote are still
//      present on the page we attribute them to,
//   2. stamps "Statistics last verified <Month Year>" — but only if (1) passed,
//   3. reports when BLS has published a newer data year, so a human goes and
//      updates the figures deliberately.
//
// Exit codes: 0 = verified (page may have been re-stamped), 1 = a cited figure
// could not be confirmed, 2 = a source could not be fetched at all.

import { readFile, writeFile } from "node:fs/promises";

const PAGE = new URL("../home-health-safety.html", import.meta.url);

// Each claim is pinned to the source we credit on the page. `needles` are the
// figures as published; if any goes missing, the citation is no longer safe.
const CLAIMS = [
  {
    id: "bls-rate",
    url: "https://www.bls.gov/iif/factsheets/workplace-violence-healthcare-2018.htm",
    needles: ["10.4", "2.1"],
    note: "healthcare 10.4 vs all-industry 2.1 per 10,000 FTE",
  },
  {
    id: "bls-share",
    url: "https://www.bls.gov/iif/factsheets/workplace-violence-healthcare-2018.htm",
    needles: ["73"],
    note: "73% of nonfatal workplace violence injuries",
  },
];

// A newer edition of the fact sheet we cite would appear on the fact sheet
// index as workplace-violence-healthcare-<year>. Matching that slug rather than
// any four-digit year on the page keeps this from firing on stray dates.
const RELEASE_INDEX = "https://www.bls.gov/iif/factsheets/";
const FACTSHEET_SLUG = /workplace-violence-healthcare-(\d{4})/g;
const PINNED_DATA_YEAR = 2018;

// BLS rejects browser-impersonating user agents with a 403 and serves an
// honest, identifying one just fine. Verified against both: a Chrome UA gets
// 403, this gets 200. Do not "fix" this by pretending to be a browser.
const UA = "CheckInOnMe stats verifier (checkinonme@checkinonme.app)";

async function fetchText(url) {
  const res = await fetch(url, {
    headers: { "User-Agent": UA, Accept: "text/html,application/xhtml+xml" },
    redirect: "follow",
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.text();
}

const problems = [];
const notices = [];

// --- 1. confirm every cited figure is still on the page we credit -----------
const cache = new Map();
for (const claim of CLAIMS) {
  let html = cache.get(claim.url);
  if (html === undefined) {
    try {
      html = await fetchText(claim.url);
      cache.set(claim.url, html);
    } catch (err) {
      problems.push(`FETCH  ${claim.id}: ${claim.url} — ${err.message}`);
      cache.set(claim.url, null);
      continue;
    }
  }
  if (html === null) continue;

  const text = html.replace(/<[^>]*>/g, " ");
  const missing = claim.needles.filter((n) => !text.includes(n));
  if (missing.length) {
    problems.push(
      `FIGURE ${claim.id}: ${missing.join(", ")} no longer found at ${claim.url} (${claim.note})`
    );
  } else {
    console.log(`ok  ${claim.id} — ${claim.note}`);
  }
}

// --- 2. has BLS published a newer data year? --------------------------------
try {
  const idx = await fetchText(RELEASE_INDEX);
  const years = [...idx.matchAll(FACTSHEET_SLUG)].map((m) => Number(m[1]));
  const newest = years.length ? Math.max(...years) : null;
  if (newest && newest > PINNED_DATA_YEAR) {
    notices.push(
      `BLS has published a "Workplace Violence in Healthcare, ${newest}" fact sheet; ` +
        `this page still cites ${PINNED_DATA_YEAR}. Read the new fact sheet, then update ` +
        `the figures, the source links and PINNED_DATA_YEAR by hand.`
    );
  } else if (!years.length) {
    notices.push(
      `No workplace-violence-healthcare fact sheet found on ${RELEASE_INDEX} — the index ` +
        `layout may have changed. Worth a look.`
    );
  }
} catch (err) {
  notices.push(`Could not read ${RELEASE_INDEX} to check for a newer data year — ${err.message}`);
}

// --- 3. stamp the page, but only if every figure verified -------------------
const hardFail = problems.some((p) => p.startsWith("FIGURE"));
const fetchFail = problems.some((p) => p.startsWith("FETCH"));

if (problems.length === 0) {
  const now = new Date();
  const iso = now.toISOString().slice(0, 10);
  const label = now.toLocaleString("en-US", {
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });

  const html = await readFile(PAGE, "utf8");
  const STAMP = /(<span id="stats-verified" data-verified=")[^"]*("\s*>)[^<]*(<\/span>)/;

  if (!STAMP.test(html)) {
    console.error(
      "\ncould not find the stats-verified stamp in home-health-safety.html — " +
        "the markup changed and this script needs updating"
    );
    process.exitCode = 1;
  } else {
    const stamped = html.replace(STAMP, `$1${iso}$2${label}$3`);
    if (stamped === html) {
      console.log(`\nverified — already stamped ${label} (${iso}), nothing to write`);
    } else {
      await writeFile(PAGE, stamped);
      console.log(`\nverified — stamped ${label} (${iso})`);
    }
  }
} else {
  console.error("\nNOT stamping the page. Problems:");
  for (const p of problems) console.error("  " + p);
}

for (const n of notices) console.log("\nnotice: " + n);

if (hardFail) process.exitCode = 1;
else if (fetchFail) process.exitCode = 2;

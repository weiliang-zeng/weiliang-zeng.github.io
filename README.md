# weiliang-zeng.github.io (Hugo)

Personal homepage of Weiliang Will Zeng, rebuilt in [Hugo](https://gohugo.io/) with the
[hugo-profile](https://github.com/gurusabarish/hugo-profile) theme, replacing the previous
jemdoc-based setup. Content is authored in plain Markdown / YAML config -- no build step
beyond running Hugo itself (no npm/Node involved).

## Layout

- `hugo.yaml` -- all site config: bio, experience, education, software/projects, contact.
  This is the closest equivalent to what used to be `index.jemdoc`/`software.jemdoc`.
- `content/publications.md` -- the publications list (was `publication.jemdoc`). Plain
  Markdown; add new entries as list items under the relevant `##` heading.
- `static/` -- images, favicon, and the downloadable `.zip` code archives.
- `themes/hugo-profile/` -- the theme, vendored as a plain copied directory (not a git
  submodule) at commit `ecc48c8` (2026-02-08), so this site never breaks if the upstream
  theme repo is renamed or restructured. To update the theme deliberately later: re-clone
  it to a temp dir, diff, and copy over by hand.
- `.github/workflows/deploy.yml` -- builds with a pinned Hugo Extended version and deploys
  to GitHub Pages via GitHub Actions (Pages source = "GitHub Actions", not a branch).

## Local development

```
hugo server -D    # live preview at http://localhost:1313
hugo --gc --minify   # production build -> public/
```

Hugo Extended is required (the theme uses Hugo's asset pipeline). It's installed in this
environment at `~/.local/bin/hugo` (pinned to v0.166.0, matching `.github/workflows/deploy.yml`).

## Content not carried over from jemdoc

These `UploadServer/img/` files aren't referenced by any current page, so they were left
behind rather than migrated: `matlab.png`, `Network.png`/`.svg`, `pdf.gif`, `z.png`/`.svg`,
`P16.jpg`. If any of these turn out to still be wanted somewhere, they're still sitting in
the old `myWebsite2/UploadServer/img/` folder.

The old Google Analytics (Universal Analytics) snippet was dropped -- that property has
been dead since GA sunset UA in July 2023. Uncomment `services.googleAnalytics` in
`hugo.yaml` and put in a GA4 measurement ID if you want analytics back.

Math: no real equations exist in the current content, but the theme supports MathJax
per-page -- add `mathjax: true` to a page's front matter if a future page needs it (see
`themes/hugo-profile/exampleSite/content/blogs/math.md` for an example).

## Python tooling (uv)

`scripts/check_links.py` walks all Markdown content and checks every external link (the
publications page accumulates DOI/PDF links that rot over the years). Run it with:

```
uv sync              # first time / after editing pyproject.toml
uv run scripts/check_links.py
```

`.venv/` is created inside this folder (self-contained -- everything for this project lives
here), but is tagged with Dropbox's ignore extended attribute so it never syncs or eats into
Dropbox storage:

```
attr -s user.com.dropbox.ignored -V 1 .venv   # already applied; re-run if .venv is recreated
```

(On macOS the equivalent is `xattr -w com.dropbox.ignored 1 .venv`.)

## Deploying

Push to `main` -- GitHub Actions builds and deploys automatically. See the migration plan
for the scratch-repo verification step and the cutover procedure before this replaces the
live site.

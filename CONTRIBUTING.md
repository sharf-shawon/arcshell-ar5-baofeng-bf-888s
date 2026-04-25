# Contributing to the BaoFeng BF-888S / Arcshell AR-5 Guide

Thank you for helping make this the best beginner radio guide on the internet! 🎉

This repository is a community-maintained documentation site. Everyone from complete beginners to licensed hams is welcome to contribute.

---

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Submitting Content Changes](#submitting-content-changes)
- [Style Guide](#style-guide)
- [Local Development Setup](#local-development-setup)
- [Pull Request Process](#pull-request-process)
- [Recognition](#recognition)

---

## Ways to Contribute

| Type | How |
|------|-----|
| 🐛 Fix a broken link | Open an issue or PR |
| ✏️ Correct inaccurate information | Open a Content Correction issue or PR |
| 📝 Add new content | Open a Feature Request issue first, then PR |
| 🌍 Add regional frequency info | PR with a new section or page |
| 📻 Share CHIRP config templates | PR adding `.img` or `.csv` to `chirp-configs/` |
| 🖼️ Add helpful images/diagrams | PR with image in `assets/images/` |
| 🔤 Improve translations | Open an issue to discuss |

---

## Reporting Issues

Use the appropriate [issue template](.github/ISSUE_TEMPLATE/):

- **Content Correction** — factual error, outdated information, bad source
- **Bug Report** — broken link, page not loading, formatting problem
- **Feature Request** — new section, new page, new resource

Please **search existing issues** before opening a new one.

---

## Submitting Content Changes

### For Small Fixes (typos, broken links)

1. Click the **"Edit this page"** link at the bottom of any documentation page
2. Make your edit directly on GitHub
3. Propose the change via the GitHub UI

### For Larger Changes (new sections, new pages)

1. **Fork** the repository
2. Create a descriptive branch:
   ```bash
   git checkout -b fix/broken-chirp-download-link
   git checkout -b content/add-repeater-etiquette
   git checkout -b feat/regional-frequencies-uk
   ```
3. Make your changes following the [Style Guide](#style-guide)
4. Test that the site builds locally (see [Local Development Setup](#local-development-setup))
5. Push and open a **Pull Request** against `main`

---

## Style Guide

### Markdown Formatting

- Use **ATX-style headings** (`##`, `###`) — not underline style
- Use **fenced code blocks** with a language tag (e.g., ` ```yaml `)
- Use **relative links** for internal pages (e.g., `[CHIRP Setup](../programming/chirp-setup)`)
- Wrap tables in a `<div class="table-wrapper">` for mobile scroll
- End every file with a newline

### Content Standards

- ✅ **Accuracy first** — verify every technical claim independently
- ✅ **Cite sources** — add a reference link when making specific claims
- ✅ **Beginner-friendly** — explain jargon the first time it appears
- ✅ **Neutral tone** — avoid brand preference; focus on technical facts
- ❌ No affiliate links
- ❌ No content promoting illegal radio use
- ❌ No personal opinions stated as facts without sourcing

### Images

- Place images in `assets/images/`
- Use descriptive filenames: `chirp-download-radio-menu.png` ✅, `screenshot1.png` ❌
- Always include an `alt` attribute: `![CHIRP Download from Radio dialog box](...)` 
- Max width: 800px (resize before adding)
- Preferred formats: `.jpg`, `.webp`, `.png`

### Front Matter (for new pages)

Every new page must include:

```yaml
---
layout: default
title: "Your Page Title | BaoFeng BF-888S Guide"
description: "150-160 character SEO description targeting your primary keyword."
keywords: "primary keyword, secondary keyword, tertiary keyword"
nav_order: 10
parent: "Parent Section Name"  # omit if top-level
has_children: false
---
```

---

## Local Development Setup

### Requirements

- Ruby 3.0+
- Bundler (`gem install bundler`)

### Setup

```bash
git clone https://github.com/sharf-shawon/arcshell-ar5-baofeng-bf-888s.git
cd arcshell-ar5-baofeng-bf-888s
bundle install
```

### Run locally

```bash
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000/arcshell-ar5-baofeng-bf-888s/` in your browser.

### Run Markdown lint

```bash
npm install -g markdownlint-cli
markdownlint "docs/**/*.md" --config .markdownlint.yml
```

---

## Pull Request Process

1. Ensure the site **builds without errors** (`bundle exec jekyll build`)
2. Ensure **Markdown linting passes** (or note known exceptions)
3. Fill out the [PR template](.github/pull_request_template.md) completely
4. PRs are reviewed within ~7 days
5. One approving review from a maintainer is required to merge

---

## Recognition

All contributors are welcome! Your GitHub username will appear in the commit history and you may be acknowledged in the site's [Resources page](docs/resources.md).

Thank you for helping the ham radio community! 📡

---

## Questions?

Open a [Discussion](https://github.com/sharf-shawon/arcshell-ar5-baofeng-bf-888s/discussions) or [Issue](https://github.com/sharf-shawon/arcshell-ar5-baofeng-bf-888s/issues) — we're happy to help!

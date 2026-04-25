# 📡 Project Evolution Plan: Arcshell AR-5 & BaoFeng BF-888S Guide

> **Vision:** To build the definitive, SEO-optimized beginner's resource for the world's most popular budget UHF radios, hosted on GitHub Pages.

---

## 🏗️ Core Strategy & Tech Stack

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| **Framework** | [Jekyll](https://jekyllrb.com/) | Native GitHub Pages support, no JS overhead, high performance. |
| **Theme** | [Just the Docs](https://just-the-docs.github.io/just-the-docs/) | Purpose-built for documentation, mobile-first, built-in search. |
| **Primary CTA** | ⭐ Star on GitHub | Builds social proof and drives organic discovery loops. |
| **License** | Apache 2.0 | Existing permissive license to encourage community contributions. |

---

## 📈 SEO & Audience Targeting

### Audience Segments

- **The New Owner:** Looking for "how to use" and "out-of-the-box" setup.
- **The Programmer:** Searching for CHIRP tutorials and cable driver fixes.
- **The Reset Seeker:** specifically looking for factory default `.img` files.
- **The Ham Aspirant:** Interested in licensing (FCC Technician class).

### High-Value Keyword Map

| Page | Primary Keyword | Secondary Keywords |
| :--- | :--- | :--- |
| **Home** | BaoFeng BF-888S guide | Arcshell AR-5, ham radio beginner, BF-888S clone |
| **Programming** | CHIRP programming tutorial | BF-888S CHIRP guide, radio programming cable |
| **Defaults** | BF-888S factory image | AR-5 factory reset, CHIRP default frequency |
| **Legal** | Ham radio license USA | FCC technician exam, license-free walkie talkie |

---

## 🗂️ Proposed Repository Structure

```text
/
├── .github/
│   ├── workflows/          # CI/CD: deploy.yml (Pages) & ci.yml (Linting)
│   └── ISSUE_TEMPLATE/     # Structured feedback for content & bugs
├── docs/                   # Content Hub
│   ├── programming/        # CHIRP walkthroughs & advanced tips
│   ├── frequencies/        # FRS/GMRS & factory channel charts
│   ├── troubleshooting/    # Logic-based fix guides
│   └── resources/          # Community links & study materials
├── assets/
│   ├── images/             # Radio photos and diagrams (Existing)
│   └── css/                # Minor 'Just the Docs' theme overrides
├── factory-default-images/ # Original radio backups (Existing)
├── _config.yml             # Jekyll & SEO configuration
├── Gemfile                 # Ruby dependency management
└── README.md               # Transformed into a "Portal" to the site
```

---

## 📝 Implementation Roadmap

### Phase 1: Foundation & Infrastructure 🏗️

- [ ] Initialize `Gemfile` with `jekyll` and `just-the-docs`.
- [ ] Configure `_config.yml` (SEO tags, navigation, social links).
- [ ] Set up `.github/workflows/deploy.yml` for automated Pages deployment.
- [ ] Implement `.github/workflows/ci.yml` (Markdown linting & broken link checking).

### Phase 2: Core Content Development ✍️

- [ ] **Home (index.md):** High-impact hero section with "Start Here" and "Star Repo" CTAs.
- [ ] **Getting Started:** Expand current README into a multi-step beginner guide.
- [ ] **Programming Suite:**
    - [ ] CHIRP setup guide (Drivers, Installation).
    - [ ] Step-by-step radio backup and frequency upload.
- [ ] **Factory Defaults:** Direct download links for existing `.img` files with MD5 hashes.

### Phase 3: Reference & Legal ⚖️

- [ ] **Legal Guide:** Clear distinction between Ham (Part 90) and FRS/GMRS (Part 95).
- [ ] **Frequency Charts:** Table of factory channels vs. legal frequencies.
- [ ] **Troubleshooting:** Q&A style guide for "Cable not recognized" and "No TX" issues.

### Phase 4: Community & Polish ✨

- [ ] Create `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`.
- [ ] Optimize SEO: Add JSON-LD Structured Data for "HowTo" and "FAQ" rich snippets.
- [ ] Final visual polish: Custom callout boxes for "Pro-Tips" and "Warnings".

---

## 🛠️ Engineering Standards

### Quality Control

- **Markdown Linting:** Strict adherence to `.markdownlint.yml` to ensure clean source code.
- **Link Integrity:** Automated `lychee` checks to prevent 404s on external resource links.
- **Verification:** All technical procedures (CHIRP steps, etc.) must be verified against physical hardware.

### SEO Technicals

- **Canonical URLs:** Enabled via `jekyll-seo-tag`.
- **Sitemaps:** Auto-generated via `jekyll-sitemap`.
- **Speed:** 100/100 Lighthouse score target (Static site advantage).

---

## 📅 Project Status Tracker

- [x] Initial Strategy & Research
- [x] Resource Gathering (Images, Factory Files)
- [x] Jekyll Environment Setup
- [x] Site Content Drafting
- [x] Production Deployment

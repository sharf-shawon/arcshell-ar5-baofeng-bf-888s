# Local Development Guide

To preview the documentation site on your local machine before pushing to GitHub:

## Prerequisites

1.  **Ruby:** [Download and install Ruby](https://rubyinstaller.org/) (use the Recommended version with Devkit).
2.  **Bundler:** Run `gem install bundler` in your terminal.

## Setup & Preview

1.  **Open in VS Code:** Open this project folder.
2.  **Install Dependencies:**
    - Press `Ctrl+Shift+P`
    - Type `Tasks: Run Task`
    - Select `Bundle: Install`
3.  **Start Preview Server:**
    - Press `Ctrl+Shift+P`
    - Type `Tasks: Run Task`
    - Select `Jekyll: Serve`
4.  **View Site:**
    - Open your browser to: `http://localhost:4000`
    - The site will automatically refresh when you save changes to your Markdown files.

## Troubleshooting

- **'bundle' is not recognized:** This means Bundler is not in your PATH.
    1. Run `gem install bundler` in your terminal.
    2. **Restart VS Code** (this is required to refresh your system PATH).
- **'gem' is not recognized:** You need to install Ruby from [rubyinstaller.org](https://rubyinstaller.org/). Ensure "Add Ruby to PATH" is checked during setup.

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
HEPHAION_ROOT = PACKAGE_ROOT.parent

REQUIRED_PACKAGE_FILES = (
    "AGENTS.md",
    "README.md",
    "design.md",
    "case-studies.md",
    "skills/gildrb-portfolio/SKILL.md",
    "skills/gildrb-spacing/SKILL.md",
    "skills/gildrb-typography/SKILL.md",
    "skills/gildrb-color-audit/SKILL.md",
    "skills/gildrb-shell-layout/SKILL.md",
    "skills/gildrb-media/SKILL.md",
    "skills/gildrb-interaction/SKILL.md",
    "skills/gildrb-accessibility/SKILL.md",
    "skills/gildrb-visual-verification/SKILL.md",
    "skills/gildrb-publishing/SKILL.md",
)

REQUIRED_DESIGN_PHRASES = (
    "Independent designer and engineer building brand systems, interfaces, and digital products.",
    "Gil Rodrigues\n→ Filen",
    "Gil Rodrigues\n→ mL7",
    "Case-specific letter spacing is always `0`.",
    "Do not use middle-dot separators.",
    "Do not crop process images.",
    "Page title desktop: `28px`, weight `500`, line height `36px`.",
    "Page title mobile: `24px`, weight `500`, line height `32px`.",
    "the top edge of the page title must align with the top edge of `Gil Rodrigues`",
    "Actionable text links use `--text-tertiary` at rest.",
    "Text-link hover uses `--text-primary`",
    "The same sidebar content persists on the homepage and every case-study route",
    "Do not show a `Portfolio` heading on the homepage",
    "Order homepage projects newest to oldest",
    "Place one `Date` / `Title` / `Field` / `Link` header row",
    "Make every project row a full-width link target.",
    "© <current year> Gil Rodrigues",
    "Case-study prose is user-owned.",
    "do not imply permission to alter wording",
    "Treat that desktop boundary as a maximum endpoint, not a target baseline.",
    "Own the live Heph terminal once in `src/partials/heph-demo.html` and include it only on `/heph`.",
    "No broad design skill exists.",
)

REQUIRED_OPERATIONAL_CONTRACTS = {
    "AGENTS.md": (
        "A live-only fix is incomplete.",
        "maximum endpoint for long posts, never a target",
    ),
    "skills/gildrb-spacing/SKILL.md": (
        "Never use article `min-height`, flex distribution, `margin-top: auto`, or last-child top padding",
        "applied once per boundary",
        "declared once in shared `src/styles/10-base.css`",
    ),
    "skills/gildrb-shell-layout/SKILL.md": (
        "Heph demo markup has one canonical owner: `src/partials/heph-demo.html`",
        "Project location uses two lines",
        "The homepage row stays in document flow; case-study rows remain sticky.",
    ),
    "skills/gildrb-interaction/SKILL.md": (
        "A touch drag on the mobile homepage moves the name, theme control, and content as one page",
        "Pull-to-refresh remains available",
    ),
    "skills/gildrb-typography/SKILL.md": (
        "Case-study Markdown uses compact `###` headings",
        "explicit `.case-code-arrow` span",
    ),
    "skills/gildrb-visual-verification/SKILL.md": (
        "Short case natural flow and long case ending at or above the desktop theme control",
        "returns a cited answer",
        "both top edges resolve to `48px`",
    ),
}

REQUIRED_CASE_ROUTES = ("/site", "/heph", "/filen", "/n0thing", "/ml7")
REQUIRED_SKILL_REFERENCES = {
    "skills/gildrb-portfolio/SKILL.md": (
        "references/homepage.md",
        "references/case-study.md",
        "references/routing.md",
        "references/verification.md",
    ),
    "skills/gildrb-publishing/SKILL.md": (
        "references/preview.md",
        "references/release.md",
    ),
}

REQUIRED_ATOMIC_SKILLS = {
    "gildrb-spacing": "Change or audit spatial distance",
    "gildrb-typography": "Change or audit text metrics",
    "gildrb-color-audit": "Prove that every visible color",
    "gildrb-shell-layout": "Preserve one shared responsive shell",
    "gildrb-media": "Publish complete, uncropped, optimized evidence",
    "gildrb-interaction": "Make one interaction behave predictably",
    "gildrb-accessibility": "Ensure the existing interface is operable",
    "gildrb-visual-verification": "Produce measured, reproducible acceptance evidence",
}

ATOMIC_SKILL_SECTIONS = (
    "## Mission",
    "## Owns",
    "## Excludes",
    "## Procedure",
    "## Reject",
    "## Verify",
    "## Done",
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontmatter_valid(text: str) -> bool:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return False
    block = match.group(1)
    return bool(
        re.search(r"^name: [a-z0-9-]+$", block, re.MULTILINE)
        and re.search(r"^description: .+$", block, re.MULTILINE)
    )


def _filled_lines(path: Path) -> int:
    return sum(bool(line.strip()) for line in _read(path).splitlines())


def _package_errors() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PACKAGE_FILES:
        if not (PACKAGE_ROOT / relative).is_file():
            errors.append(f"missing package file: gildrb/{relative}")

    design_path = PACKAGE_ROOT / "design.md"
    case_path = PACKAGE_ROOT / "case-studies.md"
    if design_path.is_file():
        design = _read(design_path)
        for phrase in REQUIRED_DESIGN_PHRASES:
            if phrase not in design:
                errors.append(f"design.md missing contract: {phrase}")
    if case_path.is_file():
        case_studies = _read(case_path)
        for route in REQUIRED_CASE_ROUTES:
            if f"`{route}`" not in case_studies:
                errors.append(f"case-studies.md missing route: {route}")

    agent_path = PACKAGE_ROOT / "AGENTS.md"
    if agent_path.is_file() and _filled_lines(agent_path) > 80:
        errors.append("gildrb/AGENTS.md exceeds 80 filled lines")

    readme_path = PACKAGE_ROOT / "README.md"
    if readme_path.is_file():
        readme = _read(readme_path)
        if "Each skill has one mission and one owned failure class." not in readme:
            errors.append("gildrb/README.md does not define atomic skill ownership")
        if "skills/gildrb-design/" in readme:
            errors.append("gildrb/README.md still routes the retired broad design skill")

    root_agent = _read(HEPHAION_ROOT / "AGENTS.md")
    root_readme = _read(HEPHAION_ROOT / "README.md")
    if "gildrb/AGENTS.md" not in root_agent:
        errors.append("root AGENTS.md does not route gildrb work")
    if "`gildrb/`" not in root_readme:
        errors.append("root README.md does not list gildrb")

    for skill_relative, references in REQUIRED_SKILL_REFERENCES.items():
        skill_path = PACKAGE_ROOT / skill_relative
        if not skill_path.is_file():
            continue
        skill = _read(skill_path)
        if not _frontmatter_valid(skill):
            errors.append(f"invalid skill frontmatter: gildrb/{skill_relative}")
        for reference in references:
            if reference not in skill:
                errors.append(f"{skill_relative} does not route {reference}")
            if not (skill_path.parent / reference).is_file():
                errors.append(f"missing skill reference: {skill_relative}/{reference}")
    retired_design_skill = PACKAGE_ROOT / "skills/gildrb-design/SKILL.md"
    if retired_design_skill.exists():
        errors.append("retired broad skill still exists: skills/gildrb-design/SKILL.md")
    registered_skills = set(REQUIRED_ATOMIC_SKILLS) | {"gildrb-portfolio", "gildrb-publishing"}
    for skill_directory in (PACKAGE_ROOT / "skills").iterdir():
        if skill_directory.is_dir() and (skill_directory / "SKILL.md").is_file() and skill_directory.name not in registered_skills:
            errors.append(f"unregistered or broad skill exists: {skill_directory.name}")
    for skill_name, mission in REQUIRED_ATOMIC_SKILLS.items():
        skill_path = PACKAGE_ROOT / f"skills/{skill_name}/SKILL.md"
        if not skill_path.is_file():
            continue
        skill = _read(skill_path)
        if not _frontmatter_valid(skill):
            errors.append(f"invalid atomic skill frontmatter: {skill_name}")
        frontmatter_name = re.search(r"^name: ([a-z0-9-]+)$", skill, re.MULTILINE)
        if not frontmatter_name or frontmatter_name.group(1) != skill_name:
            errors.append(f"atomic skill frontmatter name does not match its directory: {skill_name}")
        description = re.search(r"^description: (.+)$", skill, re.MULTILINE)
        if not description or "Do not use" not in description.group(1):
            errors.append(f"atomic skill description lacks an explicit trigger boundary: {skill_name}")
        if mission not in skill:
            errors.append(f"atomic skill has an ambiguous mission: {skill_name}")
        if skill.count("## Mission") != 1 or skill.count("## Owns") != 1 or skill.count("## Excludes") != 1:
            errors.append(f"atomic skill ownership sections are not singular: {skill_name}")
        for section in ATOMIC_SKILL_SECTIONS:
            if section not in skill:
                errors.append(f"atomic skill missing section {section}: {skill_name}")
        section_positions = [skill.find(section) for section in ATOMIC_SKILL_SECTIONS]
        if section_positions != sorted(section_positions):
            errors.append(f"atomic skill sections are out of required order: {skill_name}")
        if "## Fixed Contract" not in skill and "## Required Matrix" not in skill:
            errors.append(f"atomic skill missing deterministic contract: {skill_name}")
        if "[TODO" in skill or "gildrb-design" in skill:
            errors.append(f"atomic skill contains stale or unfinished guidance: {skill_name}")
        agent_metadata = skill_path.parent / "agents/openai.yaml"
        if not agent_metadata.is_file():
            errors.append(f"atomic skill missing agents/openai.yaml: {skill_name}")
        else:
            metadata = _read(agent_metadata)
            if f"${skill_name}" not in metadata:
                errors.append(f"atomic skill metadata does not invoke ${skill_name}")
    two_line_location = "two lines: `Gil Rodrigues` then `→ <Project>`"
    for relative in ("AGENTS.md", "case-studies.md", "skills/gildrb-portfolio/SKILL.md", "skills/gildrb-shell-layout/SKILL.md"):
        path = PACKAGE_ROOT / relative
        if path.is_file() and two_line_location not in _read(path):
            errors.append(f"{relative} does not preserve the two-line case location")
    authorship_contracts = {
        "AGENTS.md": "Treat case-study copy as user-owned.",
        "case-studies.md": "Case-study prose is author-owned.",
        "skills/gildrb-portfolio/SKILL.md": "Preserve case-study copy unless the user explicitly requests copy work.",
        "skills/gildrb-portfolio/references/case-study.md": "The user owns every title, deck, caption, metadata description, and body paragraph.",
    }
    for relative, contract in authorship_contracts.items():
        path = PACKAGE_ROOT / relative
        if path.is_file() and contract not in _read(path):
            errors.append(f"{relative} does not preserve user-owned case-study copy")
    for relative, contracts in REQUIRED_OPERATIONAL_CONTRACTS.items():
        path = PACKAGE_ROOT / relative
        if not path.is_file():
            continue
        text = _read(path)
        for contract in contracts:
            if contract not in text:
                errors.append(f"{relative} missing operational contract: {contract}")
    return errors


def _portfolio_errors(portfolio_repo: Path) -> list[str]:
    errors: list[str] = []
    required = (
        "src/styles/10-base.css",
        "src/styles/20-portfolio-media.css",
        "src/styles/30-heph-demo.css",
        "src/styles/40-preview-content.css",
        "src/styles/50-case-study.css",
        "src/styles/90-responsive.css",
        "src/sections/profile-summary.html",
        "src/sections/portfolio-open.html",
        "src/sections/portfolio-engineering.html",
        "src/sections/portfolio-design.html",
        "src/partials/references.html",
        "src/partials/heph-demo.html",
        "src/partials/sidebar-links.html",
        "src/partials/sidebar.html",
        "src/partials/theme-toggle.html",
        "src/filen.template.html",
        "src/heph.template.html",
        "src/site.template.html",
        "src/page.template.html",
        "src/ml7.template.html",
        "src/n0thing.template.html",
        "src/scripts/30-email.js",
        "src/scripts/15-portfolio-sort.js",
        "scripts/build-page.mjs",
        "scripts/site-config.mjs",
        "scripts/render-case-markdown.mjs",
        "scripts/verify-page.mjs",
        "content/README.md",
        "content/filen.md",
        "content/heph.md",
        "content/ml7.md",
        "content/n0thing.md",
        "content/site.md",
        "src/data/profile.json",
        "llms.txt",
        "index.html.md",
        ".well-known/llms.txt",
        "humans.txt",
        "sitemap.xml",
        "feed.xml",
        "scripts/check-public.mjs",
        "vercel.json",
    )
    for relative in required:
        if not (portfolio_repo / relative).is_file():
            errors.append(f"portfolio source missing: {relative}")
    if errors:
        return errors

    base_css = _read(portfolio_repo / "src/styles/10-base.css")
    portfolio_css = _read(portfolio_repo / "src/styles/20-portfolio-media.css")
    case_css = _read(portfolio_repo / "src/styles/50-case-study.css")
    responsive_css = _read(portfolio_repo / "src/styles/90-responsive.css")
    profile = _read(portfolio_repo / "src/sections/profile-summary.html")
    portfolio_open = _read(portfolio_repo / "src/sections/portfolio-open.html")
    portfolio_engineering = _read(portfolio_repo / "src/sections/portfolio-engineering.html")
    portfolio_design = _read(portfolio_repo / "src/sections/portfolio-design.html")
    builder = _read(portfolio_repo / "scripts/build-page.mjs")
    site_config = _read(portfolio_repo / "scripts/site-config.mjs")
    renderer = _read(portfolio_repo / "scripts/render-case-markdown.mjs")
    homepage_template = _read(portfolio_repo / "src/page.template.html")
    homepage_references = _read(portfolio_repo / "src/partials/references.html")
    sidebar_links = _read(portfolio_repo / "src/partials/sidebar-links.html")
    homepage_sidebar = _read(portfolio_repo / "src/partials/sidebar.html")
    filen_template = _read(portfolio_repo / "src/filen.template.html")
    heph_template = _read(portfolio_repo / "src/heph.template.html")
    site_template = _read(portfolio_repo / "src/site.template.html")
    ml7_template = _read(portfolio_repo / "src/ml7.template.html")
    n0thing_template = _read(portfolio_repo / "src/n0thing.template.html")
    core_script = _read(portfolio_repo / "src/scripts/10-core.js")
    portfolio_sort_script = _read(portfolio_repo / "src/scripts/15-portfolio-sort.js")
    email_script = _read(portfolio_repo / "src/scripts/30-email.js")
    content_guide = _read(portfolio_repo / "content/README.md")
    structured_profile = json.loads(_read(portfolio_repo / "src/data/profile.json"))
    public_portfolio_docs = tuple(
        _read(portfolio_repo / relative)
        for relative in ("llms.txt", ".well-known/llms.txt", "humans.txt", "index.html.md")
    )
    sitemap = _read(portfolio_repo / "sitemap.xml")
    feed = _read(portfolio_repo / "feed.xml")
    vercel = json.loads(_read(portfolio_repo / "vercel.json"))

    if 'from "./render-case-markdown.mjs"' not in builder:
        errors.append("portfolio builder must render case studies from Markdown")
    case_templates = {
        "filen": filen_template,
        "heph": heph_template,
        "ml7": ml7_template,
        "n0thing": n0thing_template,
        "site": site_template,
    }
    route_titles = {
        "filen": "Filen",
        "heph": "Heph",
        "ml7": "mL7",
        "n0thing": "n0thing",
        "site": "gildrb.com",
    }
    if "<title>Gil Rodrigues</title>" not in homepage_template:
        errors.append("homepage browser title must be only Gil Rodrigues")
    for slug, template in case_templates.items():
        markdown = _read(portfolio_repo / f"content/{slug}.md")
        if f"<!-- @case-markdown:{slug} -->" not in template:
            errors.append(f"{slug} template must use its Markdown insertion token")
        if 'class="case-title"' in template or 'class="case-copy"' in template:
            errors.append(f"{slug} template must not duplicate author-owned Markdown prose")
        if f"<title>{route_titles[slug]}</title>" not in template:
            errors.append(f"{slug} browser title must contain only its project name")
        metadata_count = len(re.findall(r"^- \*\*[^*]+:\*\* .+$", markdown, re.MULTILINE))
        if not markdown.startswith("# ") or metadata_count not in (0, 3):
            errors.append(f"content/{slug}.md must preserve the documented case-study header")
        body_lines = markdown.splitlines()[1:]
        authored_body = any(
            line.strip()
            and not line.strip().startswith(("!", "#", "- **"))
            for line in body_lines
        )
        if re.search(r"^##\s", markdown, re.MULTILINE):
            errors.append(f"content/{slug}.md must use compact ### headings only")
        if metadata_count == 0 and not authored_body and not markdown.rstrip().endswith("## MORE SOON"):
            errors.append(f"content/{slug}.md must contain authored prose or end with ## MORE SOON")

    expected_tokens = {
        "--bg": "#000000",
        "--text-primary": "#ffffff",
        "--text-secondary": "#b3b3b3",
        "--text-tertiary": "#767676",
        "--highlight-bg": "#b3b3b3",
        "--highlight-text": "#ffffff",
        "--sidebar-column": "240px",
        "--content-column": "760px",
        "--layout-gap": "48px",
        "--media-radius": "22px",
    }
    for name, value in expected_tokens.items():
        if not re.search(rf"{re.escape(name)}:\s*{re.escape(value)}\s*;", base_css):
            errors.append(f"portfolio token drift: {name} must be {value}")
    if not re.search(r"::selection\s*\{[^}]*color:\s*var\(--highlight-text\)[^}]*background:\s*var\(--highlight-bg\)", base_css, re.DOTALL):
        errors.append("text selection must use white over the approved bright-gray highlight")
    scroll_contract = (
        'window.history.scrollRestoration = "manual";',
        'window.addEventListener("pagehide", saveScrollPosition);',
        'window.addEventListener("pageshow", restoreScrollPosition);',
        'navigationType !== "back_forward"',
        "window.sessionStorage.setItem(",
    )
    if not all(token in core_script for token in scroll_contract):
        errors.append("shared navigation must preserve per-tab scroll position only across back/forward traversal")

    semantic_color_rules = (
        (r"\.links-label\s*\{[^}]*color:\s*var\(--text-secondary\)", "labels must use --text-secondary"),
        (r"\.external-link,\s*\n\.reference-link\s*\{[^}]*color:\s*var\(--text-tertiary\)", "text links must use --text-tertiary at rest"),
        (r"\.external-link:hover,\s*\n\s*\.reference-link:hover\s*\{[^}]*color:\s*var\(--text-primary\)", "text-link hover must use --text-primary"),
        (r"\.email\s*\{[^}]*color:\s*var\(--text-tertiary\)", "email must use --text-tertiary at rest"),
        (r"\.theme-toggle\s*\{[^}]*color:\s*var\(--text-tertiary\)", "icon controls must use --text-tertiary at rest"),
    )
    for pattern, message in semantic_color_rules:
        if not re.search(pattern, base_css, re.DOTALL):
            errors.append(f"portfolio semantic color drift: {message}")

    case_color_rules = (
        (r"\.case-location \.case-home-link,\s*\n\.case-arrow\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case home link and location arrow must use --text-tertiary at rest"),
        (r"\.case-arrow\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case location arrow must use --text-tertiary"),
        (r"\.case-location \.case-current-link\s*\{[^}]*color:\s*var\(--text-primary\)", "current case project must use --text-primary"),
        (r"\.case-location \.case-home-link:hover\s*\{[^}]*color:\s*var\(--text-primary\)", "case home-link hover must use --text-primary"),
        (r"\.case-location\s*\{[^}]*flex-wrap:\s*wrap", "case location must wrap onto two lines"),
        (r"\.case-home-link\s*\{[^}]*flex-basis:\s*100%", "case home link must occupy the first location line"),
        (r"\.case-location\s*\{[^}]*row-gap:\s*0", "case location lines must not add an extra vertical gap"),
        (r"\.case-article article\s*\{[^}]*width:\s*min\(100%,\s*760px\)\s*;[^}]*margin-right:\s*auto\s*;[^}]*margin-left:\s*auto\s*;", "case article must use the centered 760px blog-width boundary"),
        (r"\.case-intro,\s*\n\.case-copy\s*\{[^}]*margin-right:\s*auto\s*;[^}]*margin-left:\s*auto\s*;", "case prose columns must be centered inside the media container"),
    )
    for pattern, message in case_color_rules:
        if not re.search(pattern, case_css, re.DOTALL):
            errors.append(f"portfolio semantic color drift: {message}")
    if 'font: 14px/20px "Geist Mono", monospace;' not in case_css:
        errors.append("case code pre must use the pure Geist Mono monospace stack")
    if "case-code-arrow" not in renderer:
        errors.append("case code renderer must wrap arrows in the explicit arrow span")
    if not re.search(
        r"\.case-code \.case-code-arrow\s*\{[^}]*font-family:\s*\"Inter\",\s*sans-serif",
        case_css,
        re.DOTALL,
    ):
        errors.append("case code arrow spans must use the Inter sans-serif family")

    if not re.search(r"\.layout\s*\{[^}]*max-width:\s*calc\(\s*var\(--sidebar-column\) \+ var\(--layout-gap\) \+ var\(--content-column\)\s*\)[^}]*margin:\s*0 auto", base_css, re.DOTALL):
        errors.append("desktop layout must center the sidebar and 760px content column as one unit")
    if not re.search(r"\.content\s*\{[^}]*max-width:\s*var\(--content-column\)", base_css, re.DOTALL):
        errors.append("shared content must use the 760px boundary from the base bundle")
    if not re.search(r"\.content\s*\{[^}]*padding:\s*48px 0", base_css, re.DOTALL):
        errors.append("shared desktop content must use 48px vertical padding from the base bundle")
    if re.search(r"\.content\s*\{", portfolio_css):
        errors.append("homepage-only CSS must not own or duplicate the shared content shell")
    if not re.search(r"\.portfolio-section\s*\{[^}]*display:\s*grid[^}]*grid-template-columns:\s*auto max-content max-content minmax\(0,\s*1fr\) auto", portfolio_css, re.DOTALL):
        errors.append("homepage project rows must share date, title, field, spacer, and affordance columns")
    if not re.search(r"\.portfolio-card-link\s*\{[^}]*grid-column:\s*1 / -1[^}]*grid-template-columns:\s*subgrid[^}]*width:\s*100%[^}]*color:\s*var\(--text-tertiary\)", portfolio_css, re.DOTALL):
        errors.append("homepage project rows must be full-width subgrid links using --text-tertiary at rest")
    if not re.search(r'\.portfolio-card-arrow\s*\{[^}]*grid-column:\s*5[^}]*font-family:\s*"Inter",\s*sans-serif[^}]*font-size:\s*16px', portfolio_css, re.DOTALL):
        errors.append("homepage project rows must show a right-aligned 16px Inter arrow")
    if not re.search(r"\.portfolio-card-link:hover \.portfolio-card-view\s*\{[^}]*visibility:\s*visible", portfolio_css, re.DOTALL):
        errors.append("homepage project row hover must expose the View label")
    if not re.search(r"\.portfolio-card-link:focus-visible\s*\{[^}]*outline:\s*1px solid var\(--text-primary\)[^}]*outline-offset:\s*6px", portfolio_css, re.DOTALL):
        errors.append("homepage project row focus must use the full-width focus ring")
    if 'class="portfolio-table-header"' not in portfolio_open or not all(
        token in portfolio_open
        for token in ('data-sort-key="date"', 'data-sort-key="title"', 'data-sort-key="field"', ">Link</span>", 'class="portfolio-list"')
    ):
        errors.append("homepage must place the Date, Title, Field, and Link header before its global project list")
    if not re.search(r'\.portfolio-table-header\s*\{[^}]*display:\s*grid[^}]*grid-template-columns:\s*subgrid[^}]*color:\s*var\(--text-primary\)[^}]*font-family:\s*"Inter",\s*sans-serif[^}]*font-size:\s*16px[^}]*line-height:\s*24px', portfolio_css, re.DOTALL):
        errors.append("homepage column headings must use the project subgrid and primary Inter at 16px/24px")
    if not re.search(r"@media \(min-width:\s*768px\)[\s\S]*?\.portfolio-table-header\s*\{[^}]*padding-top:\s*0", portfolio_css):
        errors.append("desktop column headings must share the sidebar Links text axis")
    if re.search(r"\.portfolio-sort-button:hover\s*\{[^}]*text-decoration:\s*underline", portfolio_css, re.DOTALL):
        errors.append("homepage sort controls must not introduce a bespoke underline hover state")
    if not all(
        token in portfolio_sort_script
        for token in (
            '".portfolio-sort-button"',
            'document.querySelector(".portfolio-list")',
            "titleCollator.compare(leftValue, rightValue)",
            'querySelector(`.portfolio-card-${key}`)',
            'getAttribute("datetime")',
            "leftValue.localeCompare(rightValue)",
            "rows.forEach((row) => portfolioList.append(row));",
            "announce(`Projects sorted by ${key}, ${description}.`)",
            "if (event.detail !== 0) button.blur();",
            'key === "field"',
            '"A to Z"',
            '"Z to A"',
        )
    ):
        errors.append("homepage Date, Title, and Field controls must globally reorder all projects and announce the active direction")
    if not re.search(r"\.portfolio-list\s*\{[^}]*display:\s*grid[^}]*grid-template-columns:\s*subgrid[^}]*margin-top:\s*0", portfolio_css, re.DOTALL) or ".portfolio-group" in portfolio_css:
        errors.append("homepage projects must use one sortable subgrid list without category wrappers")
    if not re.search(r"\.portfolio-section\s*\{[^}]*grid-template-columns:\s*auto max-content max-content minmax\(0,\s*1fr\) auto[^}]*column-gap:\s*16px", portfolio_css, re.DOTALL):
        errors.append("homepage Field track must begin four Inter spaces after the longest Title track")
    if not re.search(r"\.portfolio-card-field\s*\{[^}]*grid-column:\s*3[^}]*color:\s*var\(--text-tertiary\)[^}]*font-size:\s*16px[^}]*line-height:\s*24px", portfolio_css, re.DOTALL):
        errors.append("homepage field tags must use tertiary 16px/24px text in column three")
    field_markup = portfolio_engineering + portfolio_design
    expected_fields = {
        "Design engineering": 1,
        "Product design and engineering": 1,
        "Brand identity": 1,
        "Wordmark": 2,
    }
    for field, count in expected_fields.items():
        if field_markup.count(f'class="portfolio-card-field">{field}') != count:
            errors.append(f"homepage field tags must preserve {count} {field} row(s)")
    if not re.search(
        r"@media \(max-width:\s*767px\)[\s\S]*?\.portfolio-section\s*\{[^}]*grid-template-columns:\s*max-content max-content minmax\(0,\s*1fr\) auto[^}]*column-gap:\s*clamp\(8px,\s*3vw,\s*16px\)[\s\S]*?\.portfolio-card-field\s*\{[^}]*min-width:\s*0[^}]*overflow:\s*hidden[^}]*text-overflow:\s*ellipsis",
        portfolio_css,
    ):
        errors.append("homepage project table must keep 16px type and truncate long fields inside the flexible mobile track")
    if not re.search(
        r"@media \(max-width:\s*767px\)[\s\S]*?\.portfolio-card-view\s*\{[^}]*display:\s*none",
        portfolio_css,
    ):
        errors.append("mobile homepage rows must hide View while preserving the Inter arrow")
    if not re.search(r"\.case-copy p,\s*\n\.case-copy li\s*\{[^}]*color:\s*var\(--text-secondary\)", case_css, re.DOTALL):
        errors.append("case prose must use --text-secondary")
    if not re.search(r"\.case-caption[^}]*color:\s*var\(--text-tertiary\)", case_css, re.DOTALL):
        errors.append("case captions must use --text-tertiary")
    if not re.search(r"\.case-meta div\s*\{[^}]*grid-template-columns:\s*104px minmax\(0,\s*1fr\)[^}]*column-gap:\s*24px", case_css, re.DOTALL):
        errors.append("case metadata must use the shared desktop label/value grid")
    if not re.search(r"@media \(max-width:\s*768px\)[\s\S]*?\.case-meta div\s*\{[^}]*grid-template-columns:\s*88px minmax\(0,\s*1fr\)[^}]*column-gap:\s*16px", case_css):
        errors.append("case metadata must use the compact mobile label/value grid")
    for markdown_path in (portfolio_repo / "content").glob("*.md"):
        if markdown_path.name == "README.md":
            continue
        captions = re.findall(r"^!\[(.*)\]\(media:[a-z0-9-]+\)$", _read(markdown_path), re.MULTILINE)
        if any(not caption.strip() or len(caption.split()) > 5 for caption in captions):
            errors.append(f"case media captions must contain one to five words: {markdown_path.name}")
    if not re.search(r"\.case-section\s*\{[^}]*margin-top:\s*80px", case_css, re.DOTALL):
        errors.append("case sections must use the compact 80px rhythm")
    if not re.search(r"\.name\s*\{[^}]*line-height:\s*var\(--link-line-height\)[^}]*min-height:\s*calc\(var\(--link-line-height\) \* 2\)", base_css, re.DOTALL):
        errors.append("desktop location must reserve two lines so shared links never move")
    preview_css = _read(portfolio_repo / "src/styles/40-preview-content.css")
    if "portfolio-label" in portfolio_open or 'aria-label="Portfolio"' not in portfolio_open:
        errors.append("homepage must omit the visible Portfolio label while preserving its accessible section name")
    homepage_projects = (
        "<!-- @include:sections/portfolio-engineering.html -->",
        "<!-- @include:sections/portfolio-design.html -->",
    )
    project_positions = [homepage_template.find(project) for project in homepage_projects]
    if any(position < 0 for position in project_positions) or project_positions != sorted(project_positions):
        errors.append("homepage must place Engineering rows before Design rows in its authored default order")
    default_project_ids = (
        "portfolio-site-title",
        "portfolio-heph-title",
        "portfolio-filen-title",
        "portfolio-n0thing-title",
        "portfolio-ml7-title",
    )
    portfolio_markup = portfolio_engineering + portfolio_design
    default_positions = [portfolio_markup.find(f'id="{project_id}"') for project_id in default_project_ids]
    if any(position < 0 for position in default_positions) or default_positions != sorted(default_positions):
        errors.append("homepage projects must default newest-first: gildrb.com, Heph, Filen, n0thing, mL7")
    if not re.search(r"--text-media-gap:\s*32px", base_css):
        errors.append("homepage must define the 32px optical text-to-media gap")
    if not re.search(r"\.profile-summary\s*\{[^}]*margin-bottom:\s*var\(--text-media-gap\)", preview_css, re.DOTALL):
        errors.append("homepage description must use the optical 32px transition into the project table")
    if not re.search(r"\.portfolio-card-link\s*\{[^}]*width:\s*100%", portfolio_css, re.DOTALL):
        errors.append("standalone project metadata links must expose a full-width hit target")
    if not re.search(r"\.profile-copy\s*\{[^}]*color:\s*var\(--text-primary\)", preview_css, re.DOTALL):
        errors.append("homepage biography must use --text-primary")
    if '<footer class="site-footer">' not in homepage_references:
        errors.append("homepage Metadata and copyright must share one semantic footer")
    if '© <span id="copyright-year">2026</span> Gil Rodrigues' not in homepage_references:
        errors.append("homepage copyright must preserve the 2026 no-JavaScript fallback")
    if not re.search(r"\.site-footer\s*\{[^}]*display:\s*grid[^}]*grid-template-columns:\s*minmax\(0,\s*1fr\) auto[^}]*align-items:\s*end", preview_css, re.DOTALL):
        errors.append("homepage footer must align profile.json left and copyright right")
    if not re.search(r'\.copyright\s*\{[^}]*color:\s*var\(--text-tertiary\)[^}]*font-family:\s*"Inter",\s*sans-serif[^}]*font-size:\s*16px[^}]*line-height:\s*var\(--link-line-height\)[^}]*margin-bottom:\s*var\(--footer-stack-bottom-gap\)', preview_css, re.DOTALL):
        errors.append("homepage copyright must use dark-gray Inter at 16px/24px and share profile.json's optical bottom margin")
    if not re.search(r"@media \(max-width:\s*767px\)[\s\S]*?\.site-footer\s*\{[^}]*display:\s*none", responsive_css):
        errors.append("homepage metadata and copyright footer must stay desktop-only")
    if 'document.querySelector("#copyright-year")' not in core_script or "copyrightYear.textContent = year;" not in core_script:
        errors.append("homepage copyright year must update from the visitor's current local year")
    if any('<!-- @include:partials/references.html -->' in template for template in case_templates.values()):
        errors.append("case-study routes must not include the homepage copyright footer")
    if not re.search(r"\.references-links\s*\{[^}]*margin-top:\s*0\s*;", preview_css, re.DOTALL):
        errors.append("Metadata must not use a negative desktop offset")
    if re.search(r"\.references-links\s*\{[^}]*margin-top:\s*-", responsive_css, re.DOTALL):
        errors.append("Metadata must not use a negative mobile offset")
    heph_demo = _read(portfolio_repo / "src/partials/heph-demo.html")
    heph_css = _read(portfolio_repo / "src/styles/30-heph-demo.css")
    if not re.search(r"\.heph-demo\s*\{[^}]*overflow:\s*visible", heph_css, re.DOTALL):
        errors.append("Heph project section must not clip its metadata focus outline")
    if 'class="heph-demo-frame"' not in heph_demo:
        errors.append("mobile Heph terminal must use a dedicated decorative frame")
    if "<!-- @include:partials/heph-demo.html -->" in homepage_template:
        errors.append("the Heph terminal must stay off the text-only homepage")
    if _read(portfolio_repo / "content/heph.md").count("![Heph demo](media:heph-demo)") != 1:
        errors.append("the Heph case study must include the canonical terminal media exactly once")
    if not re.search(r"@media\s*\(max-width:\s*700px\)[\s\S]*?\.heph-demo-frame\s*\{[^}]*padding:\s*34px 14px[^}]*background:\s*var\(--heph-demo-mobile-bg\)", heph_css, re.DOTALL):
        errors.append("mobile Heph panel must use its distinct outer frame surface")
    heph_hex_colors = {color.lower() for color in re.findall(r"#[0-9a-f]{6}", heph_css, re.IGNORECASE)}
    if not re.search(r"--heph-demo-terminal-bg:\s*color-mix\(\s*in srgb,\s*var\(--bg\) 96%,\s*var\(--text-primary\)", heph_css, re.DOTALL):
        errors.append("Heph terminal surface must derive from the active page theme")
    if not re.search(r"--heph-demo-row-bg:\s*color-mix\(\s*in srgb,\s*var\(--bg\) 94%,\s*var\(--text-primary\)", heph_css, re.DOTALL):
        errors.append("Heph prompt and composer rows must use the second derived surface")
    if not re.search(r"--heph-demo-mobile-bg:\s*color-mix\(\s*in srgb,\s*var\(--bg\) 92%,\s*var\(--text-primary\)", heph_css, re.DOTALL):
        errors.append("Heph mobile outer frame must use the stronger theme-derived surface")
    for row_selector in (".heph-demo-prompt", ".heph-demo-composer"):
        if not re.search(rf"{re.escape(row_selector)}[^{{]*\{{[^}}]*background:\s*var\(--heph-demo-row-bg\)", heph_css, re.DOTALL):
            errors.append(f"Heph terminal row does not use the derived row surface: {row_selector}")
    if not all(token in heph_css for token in ("color: var(--text-primary);", "color: var(--text-secondary);", "color: var(--text-tertiary);")):
        errors.append("Heph terminal must use shared primary, value, and label tokens")
    if not heph_hex_colors.issubset({"#f96664", "#face2e", "#3bc55d"}):
        errors.append("Heph terminal contains a private flat color outside the macOS lights")
    for mixed_value in ("EVIDENCE <b>ctrl+g</b>", "SCOPE <b>4/4</b>", "EXCERPTS <b>4</b>"):
        if mixed_value not in heph_demo:
            errors.append(f"Heph terminal does not separate label and value: {mixed_value}")

    required_case_rules = (
        "margin: 0 0 24px;",
        "font-size: 28px;",
        "font-size: 24px;",
        "font-size: 19px;",
        "font-weight: 500;",
        "line-height: 36px;",
        "line-height: 32px;",
        "line-height: 28px;",
        "letter-spacing: 0;",
    )
    for rule in required_case_rules:
        if rule not in case_css:
            errors.append(f"case CSS missing rule: {rule}")
    if not re.search(
        r"@media\s*\(min-width:\s*769px\)[\s\S]*?\.case-article article > :last-child\s*\{[^}]*padding-bottom:\s*calc\([^}]*var\(--footer-title-center-offset\)[^}]*var\(--theme-toggle-size\)",
        case_css,
        re.DOTALL,
    ):
        errors.append("desktop case ending must derive its vertical alignment from the theme toggle footer tokens")
    if re.search(
        r"\.case-article article > :last-child\s*\{[^}]*(?:margin-top:\s*auto|padding-top:)",
        case_css,
        re.DOTALL,
    ):
        errors.append("desktop case endings must not stretch or add artificial space before short content")
    if not re.search(
        r"\.case-section:last-child \.case-copy:last-child h2:last-child\s*\{[^}]*margin-bottom:\s*0",
        case_css,
        re.DOTALL,
    ):
        errors.append("desktop case ending must remove the final heading's independent bottom margin")
    if not re.search(
        r"\.case-media\s*\{[^}]*margin-top:\s*var\(--text-media-gap\)",
        case_css,
        re.DOTALL,
    ):
        errors.append("case media must use the shared optical transition after preceding prose")
    if not re.search(
        r"\.case-media \+ \.case-copy,\s*\.case-media-grid \+ \.case-copy\s*\{[^}]*margin-top:\s*var\(--text-media-gap\)",
        case_css,
        re.DOTALL,
    ):
        errors.append("prose after case media must use the same shared optical transition")
    for banned in ("object-fit: cover", "border-top:", "border-bottom:"):
        if banned in case_css:
            errors.append(f"case CSS contains banned rule: {banned}")

    biography = "Independent designer and engineer building brand systems, interfaces, and digital products."
    if biography not in " ".join(profile.split()):
        errors.append("homepage biography does not match the gildrb contract")
    if not all(f'href="/{slug}"' in portfolio_design for slug in ("filen", "n0thing", "ml7")):
        errors.append("homepage project list must route to Filen, n0thing, and mL7")
    if 'href="/heph"' not in portfolio_engineering or 'href="https://github.com/gildrb/heph"' in portfolio_engineering:
        errors.append("Heph homepage row must route to /heph instead of GitHub")
    if "[GitHub repository](https://github.com/gildrb/heph)" not in _read(portfolio_repo / "content/heph.md"):
        errors.append("Heph case study must link to its GitHub repository inside the article")
    if 'href="/site"' not in portfolio_engineering:
        errors.append("homepage project list must route to the website case study")
    if "siteConfig.caseStudies.map" not in builder or 'path.join(root, slug, "index.html")' not in builder:
        errors.append("builder must generate every configured top-level case-study route")
    profile_graph = structured_profile.get("@graph", [])
    website_profile = next(
        (entry for entry in profile_graph if entry.get("@id") == "https://gildrb.com/#website"),
        {},
    )
    website_parts = {
        entry.get("@id") for entry in website_profile.get("hasPart", [])
    }
    for slug in case_templates:
        route = f"https://gildrb.com/{slug}"
        case_id = f"{route}#case-study"
        if f'- `{slug}.md`' not in content_guide:
            errors.append(f"content guide does not enumerate content/{slug}.md")
        if not all(route in document for document in public_portfolio_docs):
            errors.append(f"public agent documentation does not enumerate /{slug}")
        if f"<loc>{route}</loc>" not in sitemap:
            errors.append(f"sitemap does not enumerate /{slug}")
        if f"<link>{route}</link>" not in feed:
            errors.append(f"feed does not enumerate /{slug}")
        if not any(entry.get("@id") == case_id for entry in profile_graph):
            errors.append(f"structured profile does not define /{slug}#case-study")
        if case_id not in website_parts:
            errors.append(f"structured profile website does not include /{slug}#case-study")
    required_sidebar_links = (
        "https://behance.net/gildrb",
        "https://github.com/gildrb",
        "https://www.goodreads.com/gildrb",
        "https://letterboxd.com/gildrb/",
        "https://www.linkedin.com/in/gildrb/",
        "hi@gildrb.com",
        "https://signal.me/",
    )
    for link in required_sidebar_links:
        if link not in sidebar_links:
            errors.append(f"shared sidebar missing profile or contact target: {link}")
    if "<!-- @include:partials/sidebar-links.html -->" not in homepage_sidebar:
        errors.append("homepage does not include the shared sidebar links")
    if "<!-- @include:partials/theme-toggle.html -->" not in homepage_sidebar:
        errors.append("homepage does not include the shared theme control")
    for template_name, template in (
        ("Filen", filen_template),
        ("Heph", heph_template),
        ("mL7", ml7_template),
        ("n0thing", n0thing_template),
        ("gildrb.com", site_template),
    ):
        if "<!-- @include:partials/sidebar-links.html -->" not in template:
            errors.append(f"{template_name} does not include the shared sidebar links")
        if template.count("<!-- @include:partials/sidebar-links.html -->") != 2:
            errors.append(f"{template_name} must reuse the shared links partial in desktop and mobile placements")
        if not (
            'class="case-desktop-links"' in template
            and 'class="case-mobile-links"' in template
            and template.find("</main>") >= 0
            and template.find('class="case-mobile-links"') > template.find("</main>")
        ):
            errors.append(f"{template_name} mobile links do not follow the article in DOM order")
        if "<!-- @include:partials/theme-toggle.html -->" not in template:
            errors.append(f"{template_name} does not include the shared theme control")
        if 'class="case-footer"' in template:
            errors.append(f"{template_name} repeats the sidebar email as a footer call to action")
    # Both wrappers use display: contents on mobile, so explicit grid order must
    # preserve the already-correct DOM and focus order instead of reversing it.
    if not re.search(
        r"\.case-page \.links\s*\{[^}]*order:\s*6\s*;",
        responsive_css,
        re.DOTALL,
    ):
        errors.append("shared Links and Contact wrapper does not follow the article in the mobile layout")
    if not re.search(
        r"\.content > \*\s*\{[^}]*order:\s*5\s*;",
        responsive_css,
        re.DOTALL,
    ):
        errors.append("mobile article content does not precede the shared Links and Contact wrapper")
    responsive_visibility_rules = (
        (case_css, r"\.case-mobile-links\s*\{[^}]*display:\s*none\s*;", "mobile case links must be hidden on desktop"),
        (responsive_css, r"\.case-desktop-links\s*\{[^}]*display:\s*none\s*;", "desktop case links must be hidden on mobile"),
        (responsive_css, r"\.case-mobile-links\s*\{[^}]*display:\s*contents\s*;", "mobile case links must be present after the article"),
    )
    for stylesheet, pattern, message in responsive_visibility_rules:
        if not re.search(pattern, stylesheet, re.DOTALL):
            errors.append(message)
    if not re.search(r"const sharedCaseScripts = Object\.freeze\(\[\s*\"10-core\.js\",\s*\"20-theme\.js\",\s*\"30-email\.js\",?\s*\]\)", site_config):
        errors.append("case-page script bundle does not include shared email behavior")
    if 'querySelectorAll(".email")' not in email_script:
        errors.append("shared email behavior does not bind every responsive email control")
    redirect_pairs = {
        (item.get("source"), item.get("destination"), item.get("permanent"))
        for item in vercel.get("redirects", [])
    }
    if ("/index/filen", "/filen", True) not in redirect_pairs:
        errors.append("missing permanent /index/filen to /filen redirect")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the gildrb product package and optional portfolio checkout.",
    )
    parser.add_argument(
        "--portfolio-repo",
        type=Path,
        help="Path to a local gildrb portfolio checkout.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = _package_errors()
    if args.portfolio_repo:
        errors.extend(_portfolio_errors(args.portfolio_repo.expanduser().resolve()))
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    scope = "package and portfolio" if args.portfolio_repo else "package"
    print(f"ok: gildrb {scope} contracts verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

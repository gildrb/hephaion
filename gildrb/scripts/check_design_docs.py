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
    "skills/gildrb-design/SKILL.md",
    "skills/gildrb-publishing/SKILL.md",
)

REQUIRED_DESIGN_PHRASES = (
    "Designing brands, interfaces, and the systems that connect them.",
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
    "The homepage is a text-only index",
    "A shared subgrid aligns the date column, title column, and right-hand arrows across both groups",
    "The label-to-first-entry gap is `--section-content-gap` plus the row's intrinsic `8px` top padding",
    "Case-study prose is user-owned.",
    "do not imply permission to alter wording",
    "Treat that desktop boundary as a maximum endpoint, not a target baseline.",
    "Own the live Heph terminal once in `src/partials/heph-demo.html`",
)

REQUIRED_OPERATIONAL_CONTRACTS = {
    "AGENTS.md": (
        "A live-only fix is incomplete.",
        "maximum endpoint for long posts, never a target",
    ),
    "skills/gildrb-design/SKILL.md": (
        "update `../../design.md`, the matching reference, and `../../scripts/check_design_docs.py`",
        "Reused interfaces have one canonical partial",
    ),
    "skills/gildrb-design/references/typography-and-spacing.md": (
        "Do not use article `min-height`, flex distribution, `margin-top: auto`, or last-child `padding-top`",
        "This is a maximum endpoint for a long post",
        "Use `--text-media-gap: 32px` exactly once",
    ),
    "skills/gildrb-design/references/media-and-interaction.md": (
        "Own the Heph terminal markup once in `src/partials/heph-demo.html`",
        "immediately before the GitHub repository link",
    ),
    "skills/gildrb-design/references/verification.md": (
        "a short case page keeps its final content directly after the preceding content",
        "a long desktop case page ends at or above the theme toggle",
        "submitting a question in either Heph demo produces a cited response",
    ),
}

REQUIRED_CASE_ROUTES = ("/heph", "/filen", "/n0thing", "/ml7")
REQUIRED_SKILL_REFERENCES = {
    "skills/gildrb-portfolio/SKILL.md": (
        "references/homepage.md",
        "references/case-study.md",
        "references/routing.md",
        "references/verification.md",
    ),
    "skills/gildrb-design/SKILL.md": (
        "references/typography-and-spacing.md",
        "references/shell-and-navigation.md",
        "references/media-and-interaction.md",
        "references/verification.md",
    ),
    "skills/gildrb-publishing/SKILL.md": (
        "references/preview.md",
        "references/release.md",
    ),
}


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
    two_line_location = "two lines: `Gil Rodrigues` then `→ <Project>`"
    for relative in ("AGENTS.md", "case-studies.md", "skills/gildrb-portfolio/SKILL.md", "skills/gildrb-design/references/shell-and-navigation.md"):
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
        "src/styles/40-preview-content.css",
        "src/styles/50-case-study.css",
        "src/styles/90-responsive.css",
        "src/sections/profile-summary.html",
        "src/sections/portfolio-open.html",
        "src/sections/portfolio-engineering.html",
        "src/sections/portfolio-design.html",
        "src/partials/sidebar-links.html",
        "src/partials/sidebar.html",
        "src/partials/theme-toggle.html",
        "src/filen.template.html",
        "src/heph.template.html",
        "src/page.template.html",
        "src/ml7.template.html",
        "src/n0thing.template.html",
        "src/scripts/30-email.js",
        "scripts/build-page.mjs",
        "scripts/render-case-markdown.mjs",
        "scripts/verify-page.mjs",
        "content/README.md",
        "content/filen.md",
        "content/heph.md",
        "content/ml7.md",
        "content/n0thing.md",
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
    engineering = _read(portfolio_repo / "src/sections/portfolio-engineering.html")
    design = _read(portfolio_repo / "src/sections/portfolio-design.html")
    builder = _read(portfolio_repo / "scripts/build-page.mjs")
    site_config = _read(portfolio_repo / "scripts/site-config.mjs")
    renderer = _read(portfolio_repo / "scripts/render-case-markdown.mjs")
    homepage_template = _read(portfolio_repo / "src/page.template.html")
    sidebar_links = _read(portfolio_repo / "src/partials/sidebar-links.html")
    homepage_sidebar = _read(portfolio_repo / "src/partials/sidebar.html")
    filen_template = _read(portfolio_repo / "src/filen.template.html")
    heph_template = _read(portfolio_repo / "src/heph.template.html")
    ml7_template = _read(portfolio_repo / "src/ml7.template.html")
    n0thing_template = _read(portfolio_repo / "src/n0thing.template.html")
    core_script = _read(portfolio_repo / "src/scripts/10-core.js")
    email_script = _read(portfolio_repo / "src/scripts/30-email.js")
    vercel = json.loads(_read(portfolio_repo / "vercel.json"))

    if 'from "./render-case-markdown.mjs"' not in builder:
        errors.append("portfolio builder must render case studies from Markdown")
    case_templates = {
        "filen": filen_template,
        "heph": heph_template,
        "ml7": ml7_template,
        "n0thing": n0thing_template,
    }
    route_titles = {
        "filen": "Filen",
        "heph": "Heph",
        "ml7": "mL7",
        "n0thing": "n0thing",
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
        (r"\.case-location \.case-home-link,\s*\n\.case-arrow\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case home link must use --text-tertiary at rest"),
        (r"\.case-arrow\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case location arrow must use --text-tertiary"),
        (r"\.case-location \.case-current-link\s*\{[^}]*color:\s*var\(--text-primary\)", "current case project must use --text-primary"),
        (r"\.case-home-link:hover\s*\{[^}]*color:\s*var\(--text-primary\)", "case home-link hover must use --text-primary"),
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
    if not re.search(r"\.content\s*\{[^}]*max-width:\s*var\(--content-column\)", portfolio_css, re.DOTALL):
        errors.append("homepage content must use the shared 760px content boundary")
    if not re.search(r"\.content\s*\{[^}]*padding:\s*48px 0", portfolio_css, re.DOTALL):
        errors.append("desktop content must use the compact 48px vertical padding")
    if ".portfolio-card-image::after" in portfolio_css or "opacity: 0.55" in portfolio_css:
        errors.append("clickable project media must remain free of hover overlays and tint layers")
    if re.search(r"\.portfolio-card-image::before\s*\{", portfolio_css):
        errors.append("project interaction labels must stay outside the image")
    if "mix-blend-mode:" in portfolio_css:
        errors.append("project media hover must use normal blending")
    if ".case-study-entry:hover img" in case_css:
        errors.append("case-study entries must not use opacity-only image hover")
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
        errors.append("homepage projects must stay ordered: Engineering before Design")
    if not re.search(r"--text-media-gap:\s*32px", base_css):
        errors.append("homepage must define the 32px optical text-to-media gap")
    if not re.search(r"\.profile-summary\s*\{[^}]*margin-bottom:\s*var\(--text-media-gap\)", preview_css, re.DOTALL):
        errors.append("homepage biography must use the optical 32px transition into the first project group")
    if not re.search(
        r"\.portfolio-section\s*\{[^}]*display:\s*grid;[^}]*grid-template-columns:\s*auto minmax\(0,\s*1fr\) auto;[^}]*column-gap:\s*16px",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage must define one shared three-column grid")
    if not re.search(
        r"\.portfolio-group\s*\{[^}]*display:\s*grid;[^}]*grid-column:\s*1 / -1;[^}]*grid-template-columns:\s*subgrid",
        portfolio_css,
        re.DOTALL,
    ) or not re.search(
        r"\.portfolio-card-link\s*\{[^}]*grid-column:\s*1 / -1;[^}]*grid-template-columns:\s*subgrid",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage groups and rows must share the portfolio subgrid")
    if not re.search(
        r"\.portfolio-card-link\s*\{[^}]*color:\s*var\(--text-tertiary\)",
        portfolio_css,
        re.DOTALL,
    ) or not re.search(
        r"\.portfolio-card-link time\s*\{[^}]*color:\s*inherit",
        portfolio_css,
        re.DOTALL,
    ) or not re.search(
        r"\.portfolio-card-arrow\s*\{[^}]*grid-column:\s*3[^}]*color:\s*inherit[^}]*font-size:\s*16px",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage date and arrow must inherit the tertiary row color")
    if not re.search(
        r"\.portfolio-group \.section-title\s*\{[^}]*margin-bottom:\s*var\(--section-content-gap\)[^}]*color:\s*var\(--text-secondary\)",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage group labels must use the shared secondary label gap and color")
    if "first-of-type" in portfolio_css or not re.search(
        r"\.portfolio-card-link\s*\{[^}]*padding:\s*8px 0",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage rows must keep symmetric padding without a first-row override")
    if not re.search(
        r"\.portfolio-card-link \+ \.portfolio-card-link\s*\{[^}]*border-top:\s*1px solid\s*color-mix\(in srgb, var\(--text-primary\) 12%, transparent\)",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage adjacent rows must retain faint structural separators")
    if ".portfolio-card-link::after" in portfolio_css or "font-variant-numeric: tabular-nums" in portfolio_css:
        errors.append("homepage must not use pseudo-element arrows or tabular numerals")
    if not re.search(
        r"@media\s*\(hover:\s*hover\)[\s\S]*?\.portfolio-card-link:hover\s*\{[^}]*color:\s*var\(--text-primary\)",
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage row hover must set the link currentColor to primary")
    if not re.search(r"\.portfolio-card-link\s*\{[^}]*width:\s*100%", portfolio_css, re.DOTALL):
        errors.append("homepage project rows must expose a full-width hit target")
    if not re.search(r"\.portfolio-card-link:focus-visible\s*\{[^}]*color:\s*var\(--text-primary\)[^}]*outline:\s*1px solid var\(--text-primary\);[^}]*outline-offset:\s*6px", portfolio_css, re.DOTALL):
        errors.append("homepage project focus must set link currentColor and use the 6px ring")
    if re.search(r"\.portfolio-card-link:focus-visible\s+\.portfolio-card-(?:title|arrow)", portfolio_css):
        errors.append("homepage focus must not use redundant descendant color rules")
    if not re.search(
        r"\.name\s*\{[^}]*min-height:\s*calc\(var\(--link-line-height\) \* 2\);[^}]*margin-bottom:\s*calc\(\s*var\(--section-gap\) \+ var\(--section-content-gap\) \+\s*var\(--text-media-gap\) - var\(--link-line-height\)\s*\)",
        base_css,
        re.DOTALL,
    ):
        errors.append("sidebar name spacing must align Links with the first homepage project group")
    if not re.search(r"\.profile-copy\s*\{[^}]*color:\s*var\(--text-primary\)", preview_css, re.DOTALL):
        errors.append("homepage biography must use --text-primary")
    if not re.search(r"\.references-links\s*\{[^}]*margin-top:\s*0\s*;", preview_css, re.DOTALL):
        errors.append("Metadata must not use a negative desktop offset")
    if re.search(r"\.references-links\s*\{[^}]*margin-top:\s*-", responsive_css, re.DOTALL):
        errors.append("Metadata must not use a negative mobile offset")
    if not re.search(r"\.showcase\s*\{[^}]*margin-bottom:\s*32px", portfolio_css, re.DOTALL):
        errors.append("case showcase entries must retain the optical 32px gap")
    if not re.search(r"\.gallery\s*\{[^}]*margin-bottom:\s*32px", portfolio_css, re.DOTALL):
        errors.append("case gallery entries must retain the optical 32px gap")
    if "margin-bottom: 80px;" in responsive_css:
        errors.append("mobile homepage must not restore 80px project-entry gaps")
    heph_demo = _read(portfolio_repo / "src/partials/heph-demo.html")
    heph_css = _read(portfolio_repo / "src/styles/30-heph-demo.css")
    if not re.search(r"\.heph-demo\s*\{[^}]*overflow:\s*visible", heph_css, re.DOTALL):
        errors.append("Heph project section must not clip its metadata focus outline")
    if 'class="heph-demo-frame"' not in heph_demo:
        errors.append("mobile Heph terminal must use a dedicated decorative frame")
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

    biography = "Designing brands, interfaces, and the systems that connect them."
    if biography not in " ".join(profile.split()):
        errors.append("homepage biography does not match the gildrb contract")
    if 'href="/site"' not in engineering or 'href="/heph"' not in engineering:
        errors.append("Engineering homepage rows must route to /site and /heph")
    if not all(route in design for route in ('href="/filen"', 'href="/n0thing"', 'href="/ml7"')):
        errors.append("Design homepage rows must route to /filen, /n0thing, and /ml7")
    if "[GitHub repository](https://github.com/gildrb/heph)" not in _read(portfolio_repo / "content/heph.md"):
        errors.append("Heph case study must link to its GitHub repository inside the article")
    if 'class="portfolio-card-arrow" aria-hidden="true">→</span>' not in engineering + design:
        errors.append("every homepage project row must expose a real accessible-hidden arrow")
    for project in ("filen", "ml7"):
        if 'path.join(root, slug, "index.html")' not in builder:
            errors.append(f"builder does not generate /{project}")
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
        ("mL7", ml7_template),
        ("n0thing", n0thing_template),
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
    if not all(token in site_config for token in ('"10-core.js"', '"20-theme.js"', '"30-email.js"')):
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

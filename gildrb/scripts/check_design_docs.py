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
    "Page title desktop: `40px`, weight `600`, line height `48px`.",
    "Page title mobile: `32px`, weight `600`, line height `40px`.",
    "Actionable text links use `--text-tertiary` at rest.",
    "using Inter's tabular numerals",
    "Text-link hover uses `--text-primary`",
    "The same sidebar content persists on the homepage and every case-study route",
)

REQUIRED_CASE_ROUTES = ("/filen", "/ml7")
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
        "src/sections/portfolio-filen.html",
        "src/sections/portfolio-ml7.html",
        "src/partials/sidebar-links.html",
        "src/partials/sidebar.html",
        "src/partials/theme-toggle.html",
        "src/filen.template.html",
        "src/page.template.html",
        "src/ml7.template.html",
        "src/n0thing.template.html",
        "src/scripts/30-email.js",
        "scripts/build-page.mjs",
        "scripts/verify-page.mjs",
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
    filen = _read(portfolio_repo / "src/sections/portfolio-filen.html")
    ml7 = _read(portfolio_repo / "src/sections/portfolio-ml7.html")
    builder = _read(portfolio_repo / "scripts/build-page.mjs")
    sidebar_links = _read(portfolio_repo / "src/partials/sidebar-links.html")
    homepage_sidebar = _read(portfolio_repo / "src/partials/sidebar.html")
    filen_template = _read(portfolio_repo / "src/filen.template.html")
    ml7_template = _read(portfolio_repo / "src/ml7.template.html")
    n0thing_template = _read(portfolio_repo / "src/n0thing.template.html")
    email_script = _read(portfolio_repo / "src/scripts/30-email.js")
    vercel = json.loads(_read(portfolio_repo / "vercel.json"))

    expected_tokens = {
        "--bg": "#000000",
        "--text-primary": "#ffffff",
        "--text-secondary": "#b3b3b3",
        "--text-tertiary": "#767676",
        "--sidebar-column": "240px",
        "--content-column": "760px",
        "--layout-gap": "48px",
        "--media-radius": "22px",
    }
    for name, value in expected_tokens.items():
        if not re.search(rf"{re.escape(name)}:\s*{re.escape(value)}\s*;", base_css):
            errors.append(f"portfolio token drift: {name} must be {value}")
    if not re.search(r"::selection\s*\{[^}]*color:\s*var\(--text-primary\)[^}]*background:\s*var\(--text-tertiary\)", base_css, re.DOTALL):
        errors.append("text selection must preserve primary-on-tertiary contrast")

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

    if not re.search(
        r'\.portfolio-card-meta time\s*\{[^}]*font-variant-numeric:\s*tabular-nums\s*;[^}]*font-feature-settings:\s*"tnum"\s+1\s*;',
        portfolio_css,
        re.DOTALL,
    ):
        errors.append("homepage project dates must use Inter tabular numerals")

    case_color_rules = (
        (r"\.case-home-link\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case home link must use --text-tertiary at rest"),
        (r"\.case-arrow\s*\{[^}]*color:\s*var\(--text-tertiary\)", "case location arrow must use --text-tertiary"),
        (r"\.case-location span:last-child\s*\{[^}]*color:\s*var\(--text-primary\)", "current case project must use --text-primary"),
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

    if not re.search(r"\.layout\s*\{[^}]*max-width:\s*calc\(\s*var\(--sidebar-column\) \+ var\(--layout-gap\) \+ var\(--content-column\)\s*\)[^}]*margin:\s*0 auto", base_css, re.DOTALL):
        errors.append("desktop layout must center the sidebar and 760px content column as one unit")
    if not re.search(r"\.content\s*\{[^}]*max-width:\s*var\(--content-column\)", portfolio_css, re.DOTALL):
        errors.append("homepage content must use the shared 760px content boundary")
    if not re.search(r"\.content\s*\{[^}]*padding:\s*48px 0", portfolio_css, re.DOTALL):
        errors.append("desktop content must use the compact 48px vertical padding")
    if not re.search(r"\.case-copy p,\s*\n\.case-copy li\s*\{[^}]*color:\s*var\(--text-secondary\)", case_css, re.DOTALL):
        errors.append("case prose must use --text-secondary")
    if not re.search(r"\.case-caption[^}]*color:\s*var\(--text-tertiary\)", case_css, re.DOTALL):
        errors.append("case captions must use --text-tertiary")
    if not re.search(r"\.case-section\s*\{[^}]*margin-top:\s*80px", case_css, re.DOTALL):
        errors.append("case sections must use the compact 80px rhythm")
    if not re.search(r"\.name\s*\{[^}]*line-height:\s*var\(--link-line-height\)[^}]*min-height:\s*calc\(var\(--link-line-height\) \* 2\)", base_css, re.DOTALL):
        errors.append("desktop location must reserve two lines so shared links never move")
    preview_css = _read(portfolio_repo / "src/styles/40-preview-content.css")
    if not re.search(r"\.profile-copy\s*\{[^}]*color:\s*var\(--text-primary\)", preview_css, re.DOTALL):
        errors.append("homepage biography must use --text-primary")
    if not re.search(r"\.references-links\s*\{[^}]*margin-top:\s*0\s*;", preview_css, re.DOTALL):
        errors.append("Metadata must not use a negative desktop offset")
    if re.search(r"\.references-links\s*\{[^}]*margin-top:\s*-", responsive_css, re.DOTALL):
        errors.append("Metadata must not use a negative mobile offset")
    if not re.search(r"\.showcase\s*\{[^}]*margin-bottom:\s*32px", portfolio_css, re.DOTALL):
        errors.append("homepage showcase entries must use the optical 32px gap")
    if not re.search(r"\.gallery\s*\{[^}]*margin-bottom:\s*32px", portfolio_css, re.DOTALL):
        errors.append("homepage gallery entries must use the optical 32px gap")
    if "margin-bottom: 80px;" in responsive_css:
        errors.append("mobile homepage must not restore 80px project-entry gaps")
    heph_section = _read(portfolio_repo / "src/sections/portfolio-heph.html")
    heph_css = _read(portfolio_repo / "src/styles/30-heph-demo.css")
    if 'class="heph-demo-frame" aria-hidden="true"' not in heph_section:
        errors.append("mobile Heph terminal must use a dedicated decorative frame")
    if not re.search(r"\.heph-demo-frame\s*\{[^}]*padding:\s*34px 14px[^}]*background:\s*var\(--heph-demo-mobile-bg\)", heph_css, re.DOTALL):
        errors.append("mobile Heph panel styling must stay on the terminal-only frame")

    required_case_rules = (
        "font-size: 40px;",
        "line-height: 48px;",
        "font-size: 32px;",
        "line-height: 40px;",
        "letter-spacing: 0;",
    )
    for rule in required_case_rules:
        if rule not in case_css:
            errors.append(f"case CSS missing rule: {rule}")
    for banned in ("object-fit: cover", "border-top:", "border-bottom:"):
        if banned in case_css:
            errors.append(f"case CSS contains banned rule: {banned}")

    biography = "Designing brands, interfaces, and the systems that connect them."
    if biography not in " ".join(profile.split()):
        errors.append("homepage biography does not match the gildrb contract")
    if 'href="/filen"' not in filen:
        errors.append("Filen homepage image does not route to /filen")
    if 'href="/ml7"' not in ml7:
        errors.append("mL7 homepage image does not route to /ml7")
    responsive_full_size = "(max-width: 768px) calc(100vw - 24px), (max-width: 1100px) calc(100vw - 336px), 760px"
    for source_name, source in (("homepage preload", _read(portfolio_repo / "src/page.template.html")), ("Filen homepage media", filen), ("mL7 homepage media", ml7)):
        if responsive_full_size not in source:
            errors.append(f"{source_name} must use the responsive 760px media boundary")
    for project in ("filen", "ml7"):
        if f'path.join(root, "{project}/index.html")' not in builder:
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
    if '["10-core.js", "20-theme.js", "30-email.js"]' not in builder:
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

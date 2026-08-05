"""Generate static SVG stat cards for the profile README from real GitHub data.

Runs `gh api graphql` (works locally and in GitHub Actions where GH_TOKEN is set)
and writes generated/stats.svg and generated/top-langs.svg in a tokyonight theme.
"""

import json
import subprocess
from pathlib import Path

USERNAME = "hariharan-brucewayne220"

# Repos whose language bytes are dominated by vendored third-party code.
EXCLUDE_REPOS_FROM_LANGS = {"sentinel-blockchain-agent"}

# Markup / config noise hidden from the language card.
HIDDEN_LANGS = {
    "HTML", "CSS", "Jupyter Notebook", "Batchfile", "Shell", "Dockerfile",
    "Roff", "Makefile", "JSON5", "PLpgSQL",
}

# tokyonight palette (matches the old github-readme-stats theme)
BG = "#1a1b27"
TITLE = "#70a5fd"
TEXT = "#38bdae"
ACCENT = "#bf91f3"
MUTED = "#a9b1d6"

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes {
        name
        stargazerCount
        languages(first: 8, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar { totalContributions }
    }
    pullRequests { totalCount }
  }
}
"""


def fetch():
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"login={USERNAME}"],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)["data"]["user"]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def stats_card(user):
    contrib = user["contributionsCollection"]
    rows = [
        ("Contributions (last year)", contrib["contributionCalendar"]["totalContributions"]),
        ("Public commits (last year)", contrib["totalCommitContributions"]),
        ("Private contributions (last year)", contrib["restrictedContributionsCount"]),
        ("Total pull requests", user["pullRequests"]["totalCount"]),
        ("Repositories", user["repositories"]["totalCount"]),
    ]
    line_h = 26
    height = 70 + line_h * len(rows)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="495" height="{height}" viewBox="0 0 495 {height}" role="img" aria-label="GitHub stats">',
        f'<rect width="495" height="{height}" rx="8" fill="{BG}" stroke="#2a2c3f"/>',
        f'<text x="25" y="35" font-family="Segoe UI, Ubuntu, sans-serif" font-size="18" font-weight="600" fill="{TITLE}">Hariharan\'s GitHub Stats</text>',
    ]
    y = 68
    for label, value in rows:
        parts.append(f'<circle cx="30" cy="{y - 5}" r="3.5" fill="{ACCENT}"/>')
        parts.append(f'<text x="44" y="{y}" font-family="Segoe UI, Ubuntu, sans-serif" font-size="14" fill="{MUTED}">{esc(label)}</text>')
        parts.append(f'<text x="470" y="{y}" text-anchor="end" font-family="Segoe UI, Ubuntu, sans-serif" font-size="14" font-weight="600" fill="{TEXT}">{value:,}</text>')
        y += line_h
    parts.append("</svg>")
    return "\n".join(parts)


def langs_card(user):
    totals, colors = {}, {}
    for repo in user["repositories"]["nodes"]:
        if repo["name"] in EXCLUDE_REPOS_FROM_LANGS:
            continue
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in HIDDEN_LANGS:
                continue
            totals[name] = totals.get(name, 0) + edge["size"]
            colors[name] = edge["node"]["color"] or ACCENT
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
    grand = sum(v for _, v in top) or 1

    line_h = 40
    height = 70 + line_h * len(top)
    bar_x, bar_w = 25, 445
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="495" height="{height}" viewBox="0 0 495 {height}" role="img" aria-label="Top languages">',
        f'<rect width="495" height="{height}" rx="8" fill="{BG}" stroke="#2a2c3f"/>',
        f'<text x="25" y="35" font-family="Segoe UI, Ubuntu, sans-serif" font-size="18" font-weight="600" fill="{TITLE}">Most Used Languages</text>',
    ]
    y = 66
    for name, size in top:
        pct = 100.0 * size / grand
        w = max(4, bar_w * size / grand)
        parts.append(f'<text x="{bar_x}" y="{y}" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="{MUTED}">{esc(name)}</text>')
        parts.append(f'<text x="470" y="{y}" text-anchor="end" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" font-weight="600" fill="{TEXT}">{pct:.1f}%</text>')
        parts.append(f'<rect x="{bar_x}" y="{y + 7}" width="{bar_w}" height="8" rx="4" fill="#2a2c3f"/>')
        parts.append(f'<rect x="{bar_x}" y="{y + 7}" width="{w:.1f}" height="8" rx="4" fill="{colors[name]}"/>')
        y += line_h
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    user = fetch()
    out = Path(__file__).resolve().parent.parent / "generated"
    out.mkdir(exist_ok=True)
    (out / "stats.svg").write_text(stats_card(user), encoding="utf-8")
    (out / "top-langs.svg").write_text(langs_card(user), encoding="utf-8")
    print("wrote", out / "stats.svg", "and", out / "top-langs.svg")


if __name__ == "__main__":
    main()

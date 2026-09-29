#!/bin/sh
# Renders docs/banner.html to docs/assets/banner-light.png and banner-dark.png
# with headless Chrome (960x288 at 2x device scale). Needs a Chrome/Chromium
# binary on PATH (google-chrome, chromium, chromium-browser) and network access
# for Google Fonts. Playwright is not required for this one.
set -eu

here=$(cd "$(dirname "$0")" && pwd)
docs=$(cd "$here/../../docs" && pwd)

for c in "${CHROME:-}" google-chrome google-chrome-stable chromium chromium-browser; do
  [ -n "$c" ] && command -v "$c" >/dev/null 2>&1 && chrome=$c && break
done
[ -n "${chrome:-}" ] || { echo "banner.sh: no Chrome binary found (set CHROME=/path/to/chrome)" >&2; exit 1; }

shoot() { # $1 = query string, $2 = output file
  "$chrome" --headless=new --disable-gpu --hide-scrollbars --no-sandbox \
    --force-device-scale-factor=2 --window-size=960,288 \
    --virtual-time-budget=8000 \
    --screenshot="$docs/assets/$2" "file://$docs/banner.html$1" >/dev/null 2>&1
  echo "wrote $2"
}

shoot ""      banner-light.png
shoot "?dark" banner-dark.png

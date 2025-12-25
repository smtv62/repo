import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.xyzsports-1f2df0dd8c.xyz/"
}

def find_baseurl():
    url = "https://main.uxsyplayer03b8129d46.click/index.php?id=s-sport"

    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code != 200:
        return None

    match = re.search(r"baseStreamUrl\s*=\s*'([^']+)'", r.text)
    if match:
        return match.group(1)

    return None

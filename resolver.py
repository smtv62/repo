import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def find_xyzsports_site():
    url = "https://www.selcuksportshd.is/"
    r = requests.get(url, headers=HEADERS, timeout=10)

    match = re.search(r'https://www\.xyzsports-[a-z0-9]+\.xyz', r.text)
    if match:
        site = match.group(0)
        print(f"[OK] Xyzsports bulundu: {site}")
        return site

    return None


def find_baseurl(site):
    r = requests.get(site, headers=HEADERS, timeout=10)

    # baseurl = data.baseurl;
    match = re.search(r'baseurl\s*=\s*data\.baseurl', r.text)
    if not match:
        return None

    m3u8 = re.search(r'https?://[^"\']+\.m3u8', r.text)
    if m3u8:
        return m3u8.group(0).rsplit("/", 1)[0]

    return None

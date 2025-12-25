import requests
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

def find_active_site(start=3, end=50):
    for i in range(start, end + 1):
        site = f"https://tvdahibet{i}.com"
        try:
            r = requests.get(site, timeout=5)
            if r.status_code == 200:
                print(f"[OK] Aktif site: {site}")
                return site
        except:
            continue
    return None

def find_baseurl(site, channel_id):
    url = f"{site}/channel.html?id={channel_id}"
    headers = HEADERS.copy()
    headers["Referer"] = site + "/"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
    except:
        return None

    match = re.search(r'baseurl\s*[:=]\s*["\']([^"\']+)', r.text)
    if match:
        return match.group(1)

    m3u8 = re.search(r'https?://[^"\']+\.m3u8', r.text)
    if m3u8:
        return m3u8.group(0).rsplit('/', 1)[0] + '/'

    return None
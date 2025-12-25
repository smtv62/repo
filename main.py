import requests
import re

MAIN_SITE = "https://www.xyzsports-1f2df0dd8c.xyz/"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": MAIN_SITE
}

def get_channels():
    r = requests.get(MAIN_SITE, headers=HEADERS, timeout=10)
    r.raise_for_status()

    channels = []
    matches = re.findall(r'data-url="([^"]+)"', r.text)

    for url in matches:
        name = url.split("id=")[-1].replace("-", " ").title()
        channels.append({
            "name": name,
            "url": url
        })

    return channels

def get_baseurl(channel_url):
    r = requests.get(channel_url, headers=HEADERS, timeout=10)
    r.raise_for_status()

    m = re.search(
        r"baseStreamUrl\s*=\s*['\"]([^'\"]+)",
        r.text
    )

    if m:
        return m.group(1)

    return None

def main():
    channels = get_channels()

    if not channels:
        print("[HATA] Kanal bulunamadı")
        return

    baseurl = get_baseurl(channels[0]["url"])
    if not baseurl:
        print("[HATA] BaseURL bulunamadı")
        return

    lines = ["#EXTM3U"]

    for ch in channels:
        stream = baseurl.rstrip("/") + "/playlist.m3u8"

        lines.append(f'#EXTINF:-1,{ch["name"]}')
        lines.append(f'#EXTVLCOPT:http-referrer={MAIN_SITE}')
        lines.append(stream)

        print(f"[OK] Eklendi: {ch['name']}")

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] playlist.m3u oluşturuldu")

if __name__ == "__main__":
    main()

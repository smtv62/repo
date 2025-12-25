import requests
import re

SITE = "https://www.xyzsports-1f2df0dd8c.xyz/"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": SITE
}

def get_channels():
    r = requests.get(SITE, headers=HEADERS, timeout=10)
    r.raise_for_status()

    # data-url="https://main.xxx.click/index.php?id=bein-sports-1"
    urls = re.findall(r'data-url="([^"]+)"', r.text)

    channels = []
    for u in urls:
        cid = u.split("id=")[-1]
        name = cid.replace("-", " ").upper()
        channels.append({
            "id": cid,
            "name": name,
            "url": u
        })

    return channels

def resolve_stream(channel_url):
    r = requests.get(channel_url, headers=HEADERS, timeout=10)
    r.raise_for_status()

    # this.baseStreamUrl = 'https://xxxx.click/live/'
    m = re.search(r"baseStreamUrl\s*=\s*'([^']+)'", r.text)
    if not m:
        return None

    return m.group(1) + "playlist.m3u8"

def main():
    channels = get_channels()

    if not channels:
        print("[HATA] Kanal bulunamadı")
        return

    lines = ["#EXTM3U"]

    for ch in channels:
        stream = resolve_stream(ch["url"])
        if not stream:
            print(f"[!] Çözülemedi: {ch['name']}")
            continue

        lines.append(f'#EXTINF:-1,{ch["name"]}')
        lines.append(f'#EXTVLCOPT:http-referrer={SITE}')
        lines.append(stream)

        print(f"[OK] Eklendi: {ch['name']}")

    if len(lines) == 1:
        print("[HATA] Playlist boş")
        return

    with open("playlist.m3u8", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] playlist.m3u8 oluşturuldu")

if __name__ == "__main__":
    main()

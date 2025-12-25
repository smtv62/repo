import requests
from resolver import extract_channels, extract_base_stream

SITE = "https://www.xyzsports-1f2df0dd8c.xyz/"

r = requests.get(SITE, timeout=10)
channels = extract_channels(r.text)

if not channels:
    print("[HATA] Kanal bulunamadı")
    exit(1)

lines = ["#EXTM3U"]

for url in channels:
    player = requests.get(url, timeout=10)
    base = extract_base_stream(player.text)

    if not base:
        continue

    name = url.split("id=")[-1].replace("-", " ").title()
    stream = base + "playlist.m3u8"

    lines.append(f"#EXTINF:-1,{name}")
    lines.append(f"#EXTVLCOPT:http-referrer={SITE}")
    lines.append(stream)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("[OK] playlist.m3u oluşturuldu")

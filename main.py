from channels import CHANNELS

BASEURL = "https://dga1op10s1u3leo.38f3bb9511487c.click/live"
SITE = "https://www.xyzsports-1f2df0dd8c.xyz"

def main():
    lines = ["#EXTM3U"]

    for ch in CHANNELS:
        stream = BASEURL.rstrip("/") + "/" + ch["file"]

        lines.append(f'#EXTINF:-1,{ch["name"]}')
        lines.append(f'#EXTVLCOPT:http-referrer={SITE}/')
        lines.append(stream)

        print(f"[OK] Eklendi: {ch['name']}")

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] playlist.m3u oluşturuldu")

if __name__ == "__main__":
    main()

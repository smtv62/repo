from resolver import find_xyzsports_site, find_baseurl
from channels import CHANNELS

def main():
    site = find_xyzsports_site()
    if not site:
        print("[HATA] Xyzsports linki bulunamadı")
        return

    baseurl = find_baseurl(site)
    if not baseurl:
        print("[HATA] BaseURL bulunamadı")
        return

    lines = ["#EXTM3U"]

    for ch in CHANNELS:
        lines.append(f"#EXTINF:-1,{ch['name']}")
        lines.append(f"#EXTVLCOPT:http-referrer={site}")
        lines.append(f"{baseurl}/{ch['file']}")

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] playlist.m3u oluşturuldu")

if __name__ == "__main__":
    main()

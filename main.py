import requests
from channels import CHANNELS
from resolver import find_baseurl, find_active_site

def main():
    site = find_active_site(start=3, end=50)
    if not site:
        print("[HATA] Aktif site bulunamadı")
        return

    baseurl = find_baseurl(site, "yayinzirve")
    if not baseurl:
        print("[HATA] BaseURL bulunamadı")
        return

    lines = ["#EXTM3U"]

    for ch in CHANNELS:
        stream = baseurl.rstrip("/") + "/" + ch["file"]
        lines.append(f'#EXTINF:-1,{ch["name"]}')
        lines.append(f'#EXTVLCOPT:http-referrer={site}/')
        lines.append(stream)
        print(f"[OK] Eklendi: {ch['name']}")

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] playlist.m3u oluşturuldu")

if __name__ == "__main__":
    main()
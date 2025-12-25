from resolver import find_baseurl

def main():
    baseurl = find_baseurl()
    if not baseurl:
        print("[HATA] BaseURL bulunamadı")
        return

    playlist = [
        "#EXTM3U",
        "#EXTINF:-1,S Sport",
        "#EXTVLCOPT:http-referrer=https://www.xyzsports-1f2df0dd8c.xyz/",
        baseurl + "playlist.m3u8"
    ]

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(playlist))

    print("[OK] playlist.m3u oluşturuldu")

if __name__ == "__main__":
    main()

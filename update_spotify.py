# (c) 2026 ogata2104. All rights reserved.
# 無断転載・営利目的の利用を禁じます。

import os
import requests
import base64
import sys

# リアルタイムでログを出力させる設定
sys.stdout.reconfigure(line_buffering=True)

# 1. アクセストークンの更新
def get_access_token():
    print("Fetching access token...")
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{os.environ['SPOTIFY_CLIENT_ID']}:{os.environ['SPOTIFY_CLIENT_SECRET']}".encode()).decode()
    
    res = requests.post(auth_url, data={
        "grant_type": "refresh_token",
        "refresh_token": os.environ['SPOTIFY_REFRESH_TOKEN']
    }, headers={"Authorization": f"Basic {auth_header}"})
    return res.json().get("access_token")

# 2. 最近聴いた曲を取得
def get_recently_played():
    token = get_access_token()
    print("Fetching recently played tracks...")
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=50" # 重複除外を考慮して多めに取得
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    data = res.json()
    return data.get("items", [])
    
# 3. README.md を書き換える
def update_readme():
    raw_items = get_recently_played()
    
    # --- 【修正1】重複を除外するロジック ---
    seen_ids = set()
    unique_tracks = []
    for item in raw_items:
        track_id = item['track']['id']
        if track_id not in seen_ids:
            unique_tracks.append(item['track'])
            seen_ids.add(track_id)
    
    # 表示したい件数（例：5件）に絞る
    unique_tracks = unique_tracks[:5] 

    spotify_content = "### 🎧 Recently Played\n\n"
    
    if not unique_tracks:
        spotify_content += "No recent tracks found."
    else:
        # テーブル形式で綺麗に並べる（お好みでリスト形式にも戻せます）
        spotify_content += "| Cover | Track | Artist |\n"
        spotify_content += "| :--- | :--- | :--- |\n"
        
        for track in unique_tracks:
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            # --- 【修正2】ジャケット写真のURLを取得 ---
            # images[0]が最大サイズ、[1]が中サイズ、[2]が最小サイズ（64x64）
            img_url = track['album']['images'][2]['url'] 
            
            # Markdownの中にHTMLのimgタグを埋め込む（サイズ調整がしやすいため）
            cover_img = f'<img src="{img_url}" width="50" height="50" alt="cover">'
            
            spotify_content += f"| {cover_img} | [{name}]({url}) | {artist} |\n"

    filename = "README.md"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""
    
    if start_marker in content and end_marker in content:
        print("Markers found! Updating content...")
        parts_start = content.split(start_marker)
        parts_end = parts_start[1].split(end_marker)
        
        new_content = parts_start[0] + start_marker + "\n" + spotify_content + "\n" + end_marker + parts_end[1]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.md")
    else:
        print(f"Error: Markers not found in {filename}!")

if __name__ == "__main__":
    print("--- Script Starting ---")
    update_readme()
    print("--- Script Finished ---")

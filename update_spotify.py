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
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=20"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    return res.json().get("items", [])
    
# 3. README.md を書き換える
def update_readme():
    raw_items = get_recently_played()
    
    # 重複を除外
    seen_ids = set()
    unique_tracks = []
    for item in raw_items:
        track = item['track']
        if track['id'] not in seen_ids:
            unique_tracks.append(track)
            seen_ids.add(track['id'])
            
    unique_tracks = unique_tracks[:9] # 表示曲数はここで指定

    spotify_content = "### 🎧 Recently Played\n\n"
    
    if not unique_tracks:
        spotify_content += "No recent tracks found."
    else:
        # タイル状（3列のグリッド）にするための設定
        spotify_content += "| | | |\n"
        spotify_content += "| :---: | :---: | :---: |\n"
        
        count = 0
        for track in unique_tracks:
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            # 大きめの画像URLを取得（[1]は300x300サイズ）
            img_url = track['album']['images'][1]['url'] 
            
            # 【ここを修正】カード1つ分のHTML/Markdown
            # style属性で「正方形を維持」「枠に合わせてトリミング」「角丸」を指定します
            card = (
                f'<a href="{url}">'
                f'<img src="{img_url}" '
                f'style="width: 100px; height: 100px; aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;">'
                f'<br><b>{name}</b></a><br>'
                f'<font size="2">{artist}</font>'
            )
            
            spotify_content += f"| {card} "
            count += 1
            
            # 3つ並んだら改行して次の行へ
            if count % 3 == 0:
                spotify_content += "|\n"
        
        # 最後に閉じタグがなければ追加
        if count % 3 != 0:
            spotify_content += "|\n"

    filename = "README.md"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # マーカーの指定（ここが空になっていないか確認してください）
    start_marker = "<!-- SPOTIFY_START -->"
    end_marker = "<!-- SPOTIFY_END -->"
    
    if start_marker in content and end_marker in content:
        parts_start = content.split(start_marker)
        parts_end = parts_start[1].split(end_marker)
        new_content = parts_start[0] + start_marker + "\n" + spotify_content + "\n" + end_marker + parts_end[1]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.md (Privacy-focused version)")
    else:
        print("Error: Markers not found!")

if __name__ == "__main__":
    update_readme()

# (c) 2026 ogata2104. All rights reserved.
# 無断転載・営利目的の利用を禁じます。

import os
import requests
import base64
import sys
from datetime import datetime, timedelta, timezone

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
    
    # 重複を除外しつつ、再生時間も保持
    seen_ids = set()
    unique_tracks = []
    for item in raw_items:
        track = item['track']
        if track['id'] not in seen_ids:
            # 日本時間に変換
            utc_dt = datetime.strptime(item['played_at'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
            jst_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
            played_at_str = jst_dt.strftime('%m/%d %H:%M')
            
            unique_tracks.append({
                'track': track,
                'played_at': played_at_str
            })
            seen_ids.add(track['id'])
    
    # 最新の5曲に絞る
    unique_tracks = unique_tracks[:5] 

    spotify_content = "### 🎧 Recently Played\n\n"
    
    if not unique_tracks:
        spotify_content += "No recent tracks found."
    else:
        # テーブルヘッダー
        spotify_content += "| Cover | Track | Artist | Played At |\n"
        spotify_content += "| :---: | :--- | :--- | :--- |\n"
        
        for item in unique_tracks:
            track = item['track']
            url = track['external_urls']['spotify']
            img_url = track['album']['images'][2]['url'] 
            
            # 全てをリンクで囲む
            cover_link = f'<a href="{url}"><img src="{img_url}" width="50" height="50" alt="cover"></a>'
            track_link = f'<a href="{url}">{track["name"]}</a>'
            artist_link = f'<a href="{url}">{track["artists"][0]["name"]}</a>'
            time_link = f'<a href="{url}">{item["played_at"]}</a>'
            
            spotify_content += f"| {cover_link} | {track_link} | {artist_link} | {time_link} |\n"

    filename = "README.md"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 記号の間にスペースを入れず、正確に指定（全角に見えますが半角で打ち込んでください）
    start_marker = ""
    end_marker = ""
    
    if start_marker in content and end_marker in content:
        parts_start = content.split(start_marker)
        parts_end = parts_start[1].split(end_marker)
        new_content = parts_start[0] + start_marker + "\n" + spotify_content + "\n" + end_marker + parts_end[1]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.md with full features!")
    else:
        print("Error: Markers not found!")

if __name__ == "__main__":
    update_readme()

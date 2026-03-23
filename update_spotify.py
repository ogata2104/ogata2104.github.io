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
    url = "https://api.spotify.com/v1/me/player/recently-played"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    data = res.json()
    
    print(f"API Response: {data}") 
    return data.get("items", [])
    
# 3. README.md を書き換える
def update_readme():
    items = get_recently_played()
    items = items[:5]
    spotify_content = "### 🎧 Recently Played\n\n"
    
    if not items:
        spotify_content += "No recent tracks found."
    else:
        for item in items:
            track = item['track']
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            spotify_content += f"- [{name}]({url}) - {artist}\n"

    filename = "README.md"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 【修正箇所】マーカーをしっかり指定する
    start_marker = "<!-- SPOTIFY_START -->"
    end_marker = "<!-- SPOTIFY_END -->"
    
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
        print(f"Looking for: '{start_marker}' and '{end_marker}'")

# 【最重要】スクリプトを実行する「号令」を追加
if __name__ == "__main__":
    print("--- Script Starting ---")
    update_readme()
    print("--- Script Finished ---")

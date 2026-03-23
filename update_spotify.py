import os
import requests
import base64

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
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=5"
    res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    return res.json().get("items", [])

# 3. README.md を書き換える
def update_readme():
    items = get_recently_played()
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

    # README.md の特定のコメントの間を書き換える
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""
    
    if start_marker in content and end_marker in content:
        new_content = content.split(start_marker)[0] + start_marker + "\n" + spotify_content + "\n" + end_marker + content.split(end_marker)[1]
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)

if __name__ == "__main__":
    update_readme()

# <span style="display:none;">2104's Ordinary World</span>
<style>
  /* チラつき完全防止：最初のデフォルト背景をあらかじめ消しておきます */
  .page-header { background-image: none !important; }
</style>

<script>
const changeHeaderBg = () => {
  const header = document.querySelector('.page-header');
  if (!header) return;

  const images = [
    'header1.jpg',
    'header2.jpg',
    'header3.jpg'
  ];

  // ランダムに1つ選択
  const randomImage = images[Math.floor(Math.random() * images.length)];
  
  // 自分のサイトの画像フォルダへのパスを組み立てる
  const imageUrl = `url("https://ogata2104.github.io/header_img/${randomImage}")`;
  
  header.style.backgroundImage = imageUrl;
};

// 最速タイミングでの実行
changeHeaderBg();

const fastTimer = setInterval(() => {
  const header = document.querySelector('.page-header');
  if (header) {
    changeHeaderBg();
    clearInterval(fastTimer);
  }
}, 1);

window.addEventListener('DOMContentLoaded', changeHeaderBg);
</script>
### 🌐 Social Links

<div style="display: flex; gap: 15px; align-items: center;">

  <a href="https://www.threads.net/@ogata2104" target="_blank">
    <img src="https://cdn.simpleicons.org/threads/%23000000" alt="Threads" height="30" width="30">
  </a>

  <a href="https://www.instagram.com/ogata2104" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="30">
  </a>

  <a href="https://www.facebook.com/ogata2104" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="30">
  </a>

  <a href="https://www.linkedin.com/in/ogata2104/" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="30">
  </a>

</div>

---

<!-- SPOTIFY_START -->
### 🎧 Recently Played by Spotify

<div style="display: flex; flex-wrap: wrap; gap: 12px;">
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/3eLxgtsuBq2ReQGrxjlggH" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">眠れない夜に</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/22tjzKa8lk477bUyUtUEOz" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">雲のように</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/1ErH7Wbvmt3dd5zEVNBpBM" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">素敵なベイビー</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/23x7wg6yXVLb0q2c2yCIj5" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">双子の恋人</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/7irqoF7bdPhPeNav1P2H1v" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">そして甘いキッス -Then He Kissed Me-</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/74W7UnZnkvTOvbBqPoRqWm" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">レインボー・スキップ (joyholic mix)</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/6JGkFSN6YkukhOeXZE5SK4" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">さよならの秘密</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/33KPD5FRPmxAiRUBXOfK5c" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">タイムマシン・ブレイカー</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/5x5bXJiru3FEXT60umOAP0" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">サイダービーチは柑橘系</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/6IpOgTOFSpfG4bftlFPyzg" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">恋がしたかった</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/7HctHeoIzKHxh1dBNW6QgO" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2732df333127c9d7bcabe64d778" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">ピクニック・ラブ</div>
      <div style="font-size: 11px; color: #586069;">市井 由理</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/2ThS2c9kpTCMmH87BHN9Ph" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2734f3d95af56438156f9def595" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Caballero - live</div>
      <div style="font-size: 11px; color: #586069;">Arabesque</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/0sewBNaOINuZYTUPxYbXnF" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab6742d3000053b7b12ed2ac47900dbe9c4b8776" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Letter to N.Y.</div>
      <div style="font-size: 11px; color: #586069;">Senri Oe</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/30HKJAi50JJzWPt4sPHTB6" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2734f3d95af56438156f9def595" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Midnight Dancer - live</div>
      <div style="font-size: 11px; color: #586069;">Arabesque</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/6hqfJcRiOmeNUu4WKbOExj" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b2731bd66d51ff6dc6eb4b529d0d" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Friday Night</div>
      <div style="font-size: 11px; color: #586069;">Arabesque</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/5cIi629DHDNgYx5MmyntO0" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b273ce372b493d53ce044b28cf15" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">On The Day's</div>
      <div style="font-size: 11px; color: #586069;">Hamlet Minassian</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/1XPXwFLP4nVpWdlaR2w6bH" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b27386b363ec994f6e55729173d3" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Hazeny</div>
      <div style="font-size: 11px; color: #586069;">Hany Shnoda Ferqet Masr</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/3qaJBMgQkHYvg2kkJgzORN" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b27314ed239cedb7c6a85d39e50b" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">El Arwam</div>
      <div style="font-size: 11px; color: #586069;">Eman El Bahr Darwish</div>
    </a>
  </div>
  <div style="flex: 1; min-width: 160px; max-width: 200px; border: 1px solid #e1e4e8; border-radius: 12px; padding: 12px; background-color: #f6f8fa;">
    <a href="https://open.spotify.com/track/4YmNfxo3gehMgoBN0wbJ0b" style="text-decoration: none;">
      <img src="https://i.scdn.co/image/ab67616d0000b273621a8d6f350407499291eeaf" style="width: 100%; border-radius: 8px; aspect-ratio: 1/1; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 13px; font-weight: bold; color: #0366d6; line-height: 1.3; margin-bottom: 4px;">Liza... Liza</div>
      <div style="font-size: 11px; color: #586069;">Elias Rahbani and His Orchestra</div>
    </a>
  </div>
</div>

<!-- SPOTIFY_END -->
[more](https://ogata2104.notion.site/ogata2104-s-Spotify-Log-68427f72819c49ae8dbbbcfd7f1d8220)

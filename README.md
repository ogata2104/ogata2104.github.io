# <span style="display:none;">2104's Ordinary World</span>

<style>
.tagline-type {
  font-family: 'Special Elite', 'Courier New', Courier, monospace;
  letter-spacing: 0.02em;
}
.tagline-type-jp {
  font-family: 'DotGothic16', 'Special Elite', 'Courier New', Courier, monospace;
  letter-spacing: 0.02em;
}
</style>
<p class="tagline-type">
I just want to live a peaceful life.<br>
<span class="tagline-type-jp">ただただ平穏に暮らしていきたい</span>
</p>
<p class="tagline-type">
From TOKYO JAPAN
</p>

---

<!-- THREADS_START -->
<h3 class="tagline-type">🧵 Latest Threads Posts</h3>

<style>
.threads-stack-wrapper {
  position: relative;
}
.threads-stack {
  display: flex;
  align-items: center;
  height: 360px;
  margin: 24px 0 12px;
  overflow-x: auto;
  overflow-y: visible;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
  padding-inline: calc(50% - 90px);
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}
.threads-stack::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}
.threads-card {
  box-sizing: border-box;
  position: relative;
  flex: 0 0 auto;
  scroll-snap-align: center;
  width: 180px;
  height: 300px;
  overflow: hidden;
  border: 1px solid #ececec;
  border-radius: 10px;
  padding: 12px;
  background-color: #ffffff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s;
}
/* Cover Flow風に横のカードを深めに(=幅の約6割)重ねるよう、先頭以外は左に寄せる */
.threads-card:not(:first-child) {
  margin-left: -112px;
}
.threads-card:nth-child(1) { z-index: 20; }
.threads-card:nth-child(2) { z-index: 19; }
.threads-card:nth-child(3) { z-index: 18; }
.threads-card:nth-child(4) { z-index: 17; }
.threads-card:nth-child(5) { z-index: 16; }
.threads-card:nth-child(6) { z-index: 15; }
.threads-card:nth-child(7) { z-index: 14; }
.threads-card:nth-child(8) { z-index: 13; }
.threads-card:nth-child(9) { z-index: 12; }
.threads-card:nth-child(10) { z-index: 11; }
.threads-card:nth-child(11) { z-index: 10; }
.threads-card:nth-child(12) { z-index: 9; }
.threads-card:nth-child(13) { z-index: 8; }
.threads-card:nth-child(14) { z-index: 7; }
.threads-card:nth-child(15) { z-index: 6; }
.threads-card:nth-child(16) { z-index: 5; }
.threads-card:nth-child(17) { z-index: 4; }
.threads-card:nth-child(18) { z-index: 3; }
.threads-card:nth-child(19) { z-index: 2; }
.threads-card:nth-child(20) { z-index: 1; }
.threads-card:hover {
  transform: scale(1.08);
  box-shadow: 0 12px 28px rgba(0,0,0,0.22);
  z-index: 999;
}
/* Cover Flow風エフェクト(spotify_updaterと同じ考え方)。CSSのscroll-driven animationは
   transition/:hoverより優先度が高いため、対応ブラウザではこれがhoverの代わりとして効く。
   - threads-coverflow: 中央の前後1枚分(±68px)の範囲だけで正面⇔斜めを切り替え、それより外側は
     fill-mode bothで斜め向きのまま固定する(画面幅に依存せず、隣のカードは常に最大角度になる)
   - threads-coverflow-z: 画面全体(cover 0%〜100%)で中央に近いカードほどz-indexを高くし、
     左右どちらの側でも中央寄りのカードが手前に重なるようにする
   view(inline)の進行度は 0%=右端 → 50%=中央 → 100%=左端。
   なおscroll-padding-inline: 50%を付けるとview timelineのスクロールポート幅が0扱いになり
   z-indexの段階付けが中央付近でしか効かなくなるため付けない(中央スナップはpadding-inlineで足りる) */
@supports (animation-timeline: view()) {
  .threads-card {
    animation: threads-coverflow linear both, threads-coverflow-z linear both;
    animation-timeline: view(inline), view(inline);
    animation-range: cover calc(50% - 68px) cover calc(50% + 68px), cover 0% cover 100%;
  }
}
@keyframes threads-coverflow {
  0% { transform: perspective(600px) translateX(34px) translateZ(-100px) rotateY(-55deg); box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
  50% { transform: perspective(600px) translateX(0) translateZ(0) rotateY(0) scale(1.08); box-shadow: 0 12px 28px rgba(0,0,0,0.22); }
  100% { transform: perspective(600px) translateX(-34px) translateZ(-100px) rotateY(55deg); box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
}
@keyframes threads-coverflow-z {
  0%, 100% { z-index: 1; }
  50% { z-index: 999; }
}
.threads-card .t-content {
  position: absolute;
  top: 12px;
  left: 12px;
  right: 12px;
  bottom: 48px;
  overflow: hidden;
}
.threads-card .t-thumb {
  display: block;
  width: 100%;
  border-radius: 6px;
  aspect-ratio: 1/1;
  object-fit: cover;
  margin-bottom: 8px;
  pointer-events: none;
}
.threads-card .t-text {
  font-size: 12px;
  color: #2b2b2b;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
  text-overflow: ellipsis;
}
.threads-card .t-text-long {
  -webkit-line-clamp: 12;
}
.threads-card .t-date {
  position: absolute;
  left: 12px;
  bottom: 26px;
  font-size: 10px;
  color: #767676;
}
.threads-card .t-open {
  position: absolute;
  left: 12px;
  bottom: 10px;
  z-index: 2;
  font-size: 10px;
  font-weight: bold;
  color: #1db954;
  text-decoration: none;
}
.threads-card .t-open:hover {
  text-decoration: underline;
}
</style>
<div class="threads-stack-wrapper">
  <div class="threads-stack">
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
      <div class="t-text t-text-long">最近、よくThreadsで見かける「Happy Birthday！」の深尾巴恵選手。気になって調べてみたら『龍が如く』ファンのようで、私の中で高感度上がった。</div>
    </div>
    <div class="t-date">2026-11-17 08:26</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Df0iJIQH573" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Vr-1zZHrsHwQ7kNvwHRBAl-&amp;_nc_oc=Adq5p2OV0CwcjOY8Qfzz9_UnvfwHknqaRn5B0uM_jl2Drm1VmnbLrteysPokc8uk9yg&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQI5cBLcQXN8OtF7OnSVkdzGyag84RdUTvBYsTbvoTkb7zUXkVOlCLyBa49zQyRdea8SFPhpKMqL0A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTnQRgofhv1xYQmRf7-xuQh9zDVMxqDfnNyDOgJRnLDJw&amp;oe=6B0600E5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ieTbCsvd2fMQ7kNvwHL2jPc&amp;_nc_oc=Adp39CwLXp3QPiKq8p2M9s7-h8aknpLL3Z7Ijl3PfKzXUcpVnukb13V91WXiobO8jyg&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQLc7WxgqHjcQ9339VmPSc5R2NcU0Q3avkYKFelGlb_WuPu1hPlil_1EzQ32zVxGc4lL1OAnRDm_7w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT_Wdd-NcrJ7cxsJX8QXxiOBH8awZKwADOUOwhRxKsY_A&amp;oe=6B06111D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WtyzJYc2-bgQ7kNvwGVmQLk&amp;_nc_oc=Adq4iYCd-ZmqOIMsqUwGZwFdAOnFiE3CWpCQdsKAzoPv15dWfcspz3GDxkfmN8EhN7k&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQIsXGuXiAquQyfNyoQkQXTb7k-AVxNsJU3i4gCOtt0-QL2TZXQz34oae83evZvb-jOtnQFZW_UAMw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTN0kB9Ua_BIxhrWD7Bx4hWjzW8WHL2kuwQcYZkKacy1Q&amp;oe=6B05F39E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=T3mNwtpgZfUQ7kNvwFtUvVd&amp;_nc_oc=Adp6iD8mtBbCpdca4Ixwj7o1AZISmKs3RzRRfivP4a-KXY8ldI4EsTAXw2OCQ66mqfs&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQLsrRixIP37izgrVefS_BWvqAmrls__h1yT_KsUX-zp9FSm1oDJKQX173AhCOvaMFyjmSOTKJqSRg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRoezAUBvyQMpu_ttCPqWI5olQEKuBnjpUNHUUHOT7ROQ&amp;oe=6B05F225" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tLcfJQ91ZUgQ7kNvwGC2-l0&amp;_nc_oc=AdoxuTv_w7_Hk2hKhDbjHpfy0zr1wGwrQRYuW3aFUPD2Fqw7irLfbpTUYC48cDxEJ_w&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQJCtqDHg20tH9XajUZI7hwP4xK197_WUKrzzE8wmCDSBVSxKRx7xRWtxvbKtFOXNom1Ke7TuY3EMw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQThKHhSTfw61jfDuTBQCR7FaFxule0tafZdNh8EFQ1-KQ&amp;oe=6B05F399" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rNOKgHzkKs0Q7kNvwGX43Wi&amp;_nc_oc=AdqqD73XiMnyDHWkXTPu8z01X-c6bbHrJM8B1KrfvlDCk5oUe8ksLVV5SVUkz_IGVkM&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQJ8ZHmLgsQK34Oq9YuF0gk7J95cR51bYdFDnVZ0WsbNl-cEWaO_fp3SnrO79kjzkvKUwC-FwXMJbQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRMNT9wC6Z6osfEZ7Ebu8mUpeHheAz-5U26vHIjfZCnYg&amp;oe=6B05F0AE" alt="" class="t-thumb">
      <div class="t-text">#わたしの知らない子どもたち 観てきました！<br>そして、何故この3人のトークイベン…</div>
    </div>
    <div class="t-date">2026-10-27 00:23</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/De9mId1Cb85" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
      <div class="t-text t-text-long">KAN DAN SAにやられる</div>
    </div>
    <div class="t-date">2026-10-23 10:26</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/De0YBqIn_ae" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=R8nIGnx8dEQQ7kNvwF27eYo&amp;_nc_oc=Adr0t6DNOQYe7WpsLXtwZY7E8nQlpMyHWlxW4sDza-Db9qJPdsNCBnxbXjc8Z9m2yAY&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQLEXG9U77koDT-QylaILpVC13W19RJ4khKxHGb-eqGUwtnwY3C_urotu7zLkZ0-HVTTjO9dLMYegg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTK0yktG9_ngZd6VUokIQKqCQxOe9Kdgxg0eMxKQzaH1A&amp;oe=6B05F41E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4HOFkUSIwjUQ7kNvwHzGXxQ&amp;_nc_oc=AdrY2iY0B0d8ZvZOoaGeQacHXymyZqVy5p1bqKq_qZ8qf_4L8ZBK6tdVjcL8xYxfYyQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQI55XqjrnZhrNTakRR3vPAd6QrKgkjtZz17a58CgUD0r_4OJW5OcuVeMPVFKP4SFyA0kKlD9NW-HQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT0RwBG0lCC0O5B6UpjIh2zI6FAnys8z1dYTj5aU8__OQ&amp;oe=6B0604F5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-3Nc8se2CHcQ7kNvwGkLg8Y&amp;_nc_oc=Adpx5-nK4mgjRvT9hXScCqO1QJxAIMhr7LsqAsqI2IRJ1VtZYL-RDedLP67rMMiyZnE&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQJbW95Mvvivtw5VDgmpcEx5twySjd7QexhMbaZluEiBb3KcPTSEw4fxerB0fGDQs3JLR8Yi7J1o4g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ7Qk_cRcTnw2Lf8Tkqrr1Zq32rG5g5eDwguvINyUEg0w&amp;oe=6B05F076" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yCLLjF1eU3wQ7kNvwGx7NQl&amp;_nc_oc=Adr5IATuJ3Jq3uWSk2Ctk2eeCBpTKUAZTK67_FWzuhor3xtD9xj9t4pZX_LWOcUkAVg&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQIwdLjar7bqsu0TCtYqqJYxfzbRV8JPJu9Hw4rVnNppuQrSYJILe44EspqEAaidzsAYdhWq5HBfcw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRKlimupsbEneGSHRR-xKGEIOpBZtP7klwGkjUkwm6XNA&amp;oe=6B0600A6" alt="" class="t-thumb">
      <div class="t-text">噂に違わぬすごい映画でした。とにかく高密度で観終わった後、（いい意味で）どっと疲…</div>
    </div>
    <div class="t-date">2026-10-16 08:20</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeiH_O1gXbf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
      <div class="t-text t-text-long">昔、『バルダーダッシュ』っていうPCゲームがあって、似たようなゲームがやりたくなったので、Claude Codeで自作しようかなと思ったら、Switch版の『バルダーダッシュ』ってのがあった。作る手間が省けた。</div>
    </div>
    <div class="t-date">2026-10-10 23:25</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeUSvL4GsPS" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4-6g72QQ6fsQ7kNvwH38Xu3&amp;_nc_oc=AdpYO52ZRmntOyFdDPb6HQ1mBYct_FuCvW876-yeWYt3rdhk5iHmSRVi9hG8qOdIbzs&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQLBUdTv2gERcZM5i2sFYYNRxpgs6wyEHZeQwnHdWh_3AdeDrzv5rGLDXmHQ1uLKEoYXcTPuTCPP2Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTHIoTHMMlEHlMwCXRXDEp0scHFEMOzyLaa7ae2Jd91qQ&amp;oe=6B05F3C1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=fbRJmrSwkvsQ7kNvwGLWNmF&amp;_nc_oc=AdrrYVxoojBXp6boQTctlmKlfHnPD3ntKo9BNa3pIyokM86Wk1UJNovCoANh7vItiww&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQKs_qoIThL3fQdAITR2h9OaZup8p84vHeOP5nUtp-6X2cap5Dj0HrqHPsfnE7Q19OhYMbySa414Tg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTgyh6mYbhLOZxLNLuS_ulVN0h1sO2SWLhzznqd-OeV5w&amp;oe=6B05F41F" alt="" class="t-thumb">
      <div class="t-text">#ナイルレストランのムルギーランチ 頂いてきました。<br>チキンとポテトの甘みで程よ…</div>
    </div>
    <div class="t-date">2026-10-03 22:12</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeCI6xfAYVT" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
      <div class="t-text t-text-long">コロナ禍のステイホーム期間中にFODで『北の国から』イッキ観しました。<br>ドラマシリーズやSPをリアタイでずっと追っかけてましたが、その時とはまた違う味わいや発見がありましたね。<br>純と蛍がその後、どんな人生を歩むかわかっているだけに、子供時代…</div>
    </div>
    <div class="t-date">2026-10-01 08:26</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dd7gu2Xn_nk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WvhigryquigQ7kNvwE_PQkZ&amp;_nc_oc=Adqr_vBktWwYE4Id6B6CDwbjUiTiEFHtNG4vNJ9SDR0NOAZ6codiHFuBmzsDwuwY5BE&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQLxDalV13w-SekqBTyMYqQlkC6mmP6wH2BSe1FS-vD1r5qfuA72Ej89yvlv9vHyYkLfCNw0SmCSbQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQvCn2BBQh-2tBzCfW01VXZz3D0tzcHWkiM7ECfGpp-Ag&amp;oe=6B060AEA" alt="" class="t-thumb">
      <div class="t-text">iOSアプリがクラッシュしまくり</div>
    </div>
    <div class="t-date">2026-09-29 10:32</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dd2llzin-Xw" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
      <div class="t-text t-text-long">早稲田松竹で『鉄男』がかかるのね。<br>『ネルソンさん、あなたは人を殺しましたか？』で塚本晋也監督を知った人は是非観て欲しい。<br>CGが普及してなかった時代に一コマ一コマ丁寧に撮影された映像は、ある意味とても贅沢で豊かだし、今観ると手作りの温かみ…</div>
    </div>
    <div class="t-date">2026-09-23 00:59</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdmHNLQmo3G" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=VLIgWgptvXEQ7kNvwHsIqAq&amp;_nc_oc=AdqVIRt7FgA5uF-I8RyrzVcQIBFLWG7CCC5YjtWGbITQ8nCFEQxBCsxHkRBA-v2Vgec&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQJb3-evfCU8ai2BT86hf1vDqAJXjgWh2CKbzvq53XaKU_75-nongCdKs0qUNzfFRSRfGyj1YQWbXw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRXcUNNBsIygmHinKxjEgoo9nBVLHhW-frUHzIE4rtFVA&amp;oe=6B05FE5C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7dOZo3JmgeQQ7kNvwHtNN3s&amp;_nc_oc=Adpl4XedOXbr1nhmG979Xcyr6BM4YGqM9u1SgG4lzYkkUAR2bjcYR9xiYdjjp3gIewE&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=-Y7hmPdThm4c9Ae3D0UIKA&amp;_nc_tpa=Q5bMBQIPYwqdo109VAyk_7soY0LWnwtKUX3q5XKU3tfLEhOPS1xCgehJDaE5HSlgD9m59q2oB-m-TKhrfw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQr2Gr3Qi41IHi5qtLW_gaFgkaa2wavjQ-_OsOr6VadTQ&amp;oe=6B060E76" alt="" class="t-thumb">
      <div class="t-text">台風接近中の中、2年ぶりのTGS。<br>始発で行って雨の中2時間半並んだ甲斐あって、…</div>
    </div>
    <div class="t-date">2026-09-20 20:52</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Ddgha79ibTF" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  </div>
</div>

<!-- THREADS_END -->

---

<!-- SPOTIFY_START -->
<h3 class="tagline-type">🎧 Recently Played by Spotify</h3>

<style>
.spotify-stack-wrapper {
  position: relative;
}
.spotify-stack {
  display: flex;
  align-items: center;
  height: 325px;
  margin: 24px 0 12px;
  overflow-x: auto;
  overflow-y: visible;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
  padding-inline: calc(50% - 80px);
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}
.spotify-stack::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}
.spotify-card {
  box-sizing: border-box;
  position: relative;
  flex: 0 0 auto;
  scroll-snap-align: center;
  width: 160px;
  border: 1px solid #e1e4e8;
  border-radius: 10px;
  padding: 10px;
  background-color: #f6f8fa;
  box-shadow: 0 2px 6px rgba(27,31,35,0.12);
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.3s;
}
/* Cover Flow風に横のカードを深めに(=幅の約6割)重ねるよう、先頭以外は左に寄せる */
.spotify-card:not(:first-child) {
  margin-left: -100px;
}
.spotify-card:nth-child(1) { z-index: 19; }
.spotify-card:nth-child(2) { z-index: 18; }
.spotify-card:nth-child(3) { z-index: 17; }
.spotify-card:nth-child(4) { z-index: 16; }
.spotify-card:nth-child(5) { z-index: 15; }
.spotify-card:nth-child(6) { z-index: 14; }
.spotify-card:nth-child(7) { z-index: 13; }
.spotify-card:nth-child(8) { z-index: 12; }
.spotify-card:nth-child(9) { z-index: 11; }
.spotify-card:nth-child(10) { z-index: 10; }
.spotify-card:nth-child(11) { z-index: 9; }
.spotify-card:nth-child(12) { z-index: 8; }
.spotify-card:nth-child(13) { z-index: 7; }
.spotify-card:nth-child(14) { z-index: 6; }
.spotify-card:nth-child(15) { z-index: 5; }
.spotify-card:nth-child(16) { z-index: 4; }
.spotify-card:nth-child(17) { z-index: 3; }
.spotify-card:nth-child(18) { z-index: 2; }
.spotify-card:nth-child(19) { z-index: 1; }
.spotify-card:hover {
  transform: scale(1.08);
  box-shadow: 0 12px 28px rgba(27,31,35,0.35);
  z-index: 999;
}
/* Cover Flow風エフェクト。CSSのscroll-driven animationはtransition/:hoverより優先度が高いため、
   対応ブラウザではこれがhoverの代わりとして効く。
   - spotify-coverflow: 中央の前後1枚分(±60px)の範囲だけで正面⇔斜めを切り替え、それより外側は
     fill-mode bothで斜め向きのまま固定する(画面幅に依存せず、隣のカードは常に最大角度になる)
   - spotify-coverflow-z: 画面全体(cover 0%〜100%)で中央に近いカードほどz-indexを高くし、
     左右どちらの側でも中央寄りのカードが手前に重なるようにする
   view(inline)の進行度は 0%=右端 → 50%=中央 → 100%=左端 */
@supports (animation-timeline: view()) {
  .spotify-card {
    animation: spotify-coverflow linear both, spotify-coverflow-z linear both;
    animation-timeline: view(inline), view(inline);
    animation-range: cover calc(50% - 60px) cover calc(50% + 60px), cover 0% cover 100%;
  }
}
@keyframes spotify-coverflow {
  0% { transform: perspective(600px) translateX(30px) translateZ(-90px) rotateY(-55deg); box-shadow: 0 2px 6px rgba(27,31,35,0.12); }
  50% { transform: perspective(600px) translateX(0) translateZ(0) rotateY(0) scale(1.08); box-shadow: 0 12px 28px rgba(27,31,35,0.35); }
  100% { transform: perspective(600px) translateX(-30px) translateZ(-90px) rotateY(55deg); box-shadow: 0 2px 6px rgba(27,31,35,0.12); }
}
@keyframes spotify-coverflow-z {
  0%, 100% { z-index: 1; }
  50% { z-index: 999; }
}
.spotify-card img {
  position: relative;
  width: 100%;
  border-radius: 6px;
  aspect-ratio: 1/1;
  object-fit: cover;
  margin-bottom: 6px;
  pointer-events: none;
}
.spotify-card .t-name {
  position: relative;
  font-size: 12px;
  font-weight: bold;
  color: #24292e;
  line-height: 1.3;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.spotify-card .t-artist {
  position: relative;
  font-size: 10px;
  color: #586069;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 6px;
}
.spotify-card .t-open {
  position: relative;
  z-index: 2;
  display: inline-block;
  font-size: 10px;
  font-weight: bold;
  color: #1db954;
  text-decoration: none;
}
.spotify-card .t-open:hover {
  text-decoration: underline;
}
</style>
<div class="spotify-stack-wrapper">
  <div class="spotify-stack">
  <div class="spotify-card" title="Dream Weaver - Gary Wright">
    <img src="https://i.scdn.co/image/ab67616d0000b2730c51c850e900c074c093fce6" alt="Dream Weaver">
    <div class="t-name">Dream Weaver</div>
    <div class="t-artist">Gary Wright</div>
    <a class="t-open" href="https://open.spotify.com/track/74DrA5fFoGSy4xgkZarZtP" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All I Want for Christmas Is You - Mariah Carey">
    <img src="https://i.scdn.co/image/ab67616d0000b273c0862332847213b151ffab31" alt="All I Want for Christmas Is You">
    <div class="t-name">All I Want for Christmas Is You</div>
    <div class="t-artist">Mariah Carey</div>
    <a class="t-open" href="https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Last Christmas - Wham!">
    <img src="https://i.scdn.co/image/ab67616d0000b273f2d2adaa21ad616df6241e7d" alt="Last Christmas">
    <div class="t-name">Last Christmas</div>
    <div class="t-artist">Wham!</div>
    <a class="t-open" href="https://open.spotify.com/track/2FRnf9qhLbvw8fu4IBXx78" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケテナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b27378823b4e368a816a90378780" alt="イケテナイ太陽">
    <div class="t-name">イケテナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/7hA4kaAFiM3Vr61JaFGzvy" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="うさぎラップ (ソロver.) - うさぎ（CV.小澤亜李）">
    <img src="https://i.scdn.co/image/ab67616d0000b273f991d9ccecdbade375f6b0dd" alt="うさぎラップ (ソロver.)">
    <div class="t-name">うさぎラップ (ソロver.)</div>
    <div class="t-artist">うさぎ（CV.小澤亜李）</div>
    <a class="t-open" href="https://open.spotify.com/track/4EXp6T9ou0y6BCLiaoYg0R" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b27378823b4e368a816a90378780" alt="イケナイ太陽">
    <div class="t-name">イケナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/3rYx4H5RpE6tp4x1ZU01QS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="come again - m-flo">
    <img src="https://i.scdn.co/image/ab67616d0000b27340b9da3f4fc33ebdcae34c84" alt="come again">
    <div class="t-name">come again</div>
    <div class="t-artist">m-flo</div>
    <a class="t-open" href="https://open.spotify.com/track/477CB93mH986mrIheQD0RR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Jamboree Mickey! - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b2737d6027d98eeaa6d5e9af4847" alt="Jamboree Mickey!">
    <div class="t-name">Jamboree Mickey!</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/2O70g7QJJRskIbAF596CHm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary - Ken Ishii">
    <img src="https://i.scdn.co/image/ab67616d0000b27373918e960a1fd4f240df6686" alt="JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary">
    <div class="t-name">JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary</div>
    <div class="t-artist">Ken Ishii</div>
    <a class="t-open" href="https://open.spotify.com/track/7wr97Scn0CfH3b1AJBW8Zh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dancing Queen - ABBA">
    <img src="https://i.scdn.co/image/ab67616d0000b273ec5de82891e542d4877c6d98" alt="Dancing Queen">
    <div class="t-name">Dancing Queen</div>
    <div class="t-artist">ABBA</div>
    <a class="t-open" href="https://open.spotify.com/track/1rMfDvE2C8ne8UZj847rKM" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Shine - Original Mix - Chuck New">
    <img src="https://i.scdn.co/image/ab67616d0000b2732ff89e5c56347ccac1fae742" alt="Shine - Original Mix">
    <div class="t-name">Shine - Original Mix</div>
    <div class="t-artist">Chuck New</div>
    <a class="t-open" href="https://open.spotify.com/track/6uYCP6MK1oxgQZAxxXOTLH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Thinking - Louis Cole">
    <img src="https://i.scdn.co/image/ab67616d0000b27369f27ac28a49aadfd395b4ae" alt="Thinking">
    <div class="t-name">Thinking</div>
    <div class="t-artist">Louis Cole</div>
    <a class="t-open" href="https://open.spotify.com/track/1JDS6yAk0wCsfkFLN9Tr7i" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Hold Me Now - キャロル&amp;チューズデイ(Vo.Nai Br.XX&amp;Celeina Ann)">
    <img src="https://i.scdn.co/image/ab67616d0000b2734378d9eb85031d774e94d17f" alt="Hold Me Now">
    <div class="t-name">Hold Me Now</div>
    <div class="t-artist">キャロル&amp;チューズデイ(Vo.Nai Br.XX&amp;Celeina Ann)</div>
    <a class="t-open" href="https://open.spotify.com/track/7KYQfBt49UM0GYBHkD9TgF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="California Dreamin&#x27; - The Mamas &amp; The Papas">
    <img src="https://i.scdn.co/image/ab67616d0000b273cbd56c3a8faf8cf8c8bea0df" alt="California Dreamin&#x27;">
    <div class="t-name">California Dreamin&#x27;</div>
    <div class="t-artist">The Mamas &amp; The Papas</div>
    <a class="t-open" href="https://open.spotify.com/track/1ZEOIhSn6BKErV59bIgn76" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Marvel Studios Fanfare - Michael Giacchino">
    <img src="https://i.scdn.co/image/ab67616d0000b273df0b8480336e407d174bf040" alt="Marvel Studios Fanfare">
    <div class="t-name">Marvel Studios Fanfare</div>
    <div class="t-artist">Michael Giacchino</div>
    <a class="t-open" href="https://open.spotify.com/track/5xdTdPiQVFhI5iVEw2ctbk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score - Brian Tyler">
    <img src="https://i.scdn.co/image/ab67616d0000b273f7522b5f7b34e774cfba81f5" alt="Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score">
    <div class="t-name">Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score</div>
    <div class="t-artist">Brian Tyler</div>
    <a class="t-open" href="https://open.spotify.com/track/0y6nWKlwppOXeprZxMsHQ2" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="B-A-Y-M-A-X - Without Dialogue - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b273045ffc089890c9c7993ace19" alt="B-A-Y-M-A-X - Without Dialogue">
    <div class="t-name">B-A-Y-M-A-X - Without Dialogue</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/4l29cPGOSXh9TRcYp1t5d9" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Happy Song - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b273045ffc089890c9c7993ace19" alt="Happy Song">
    <div class="t-name">Happy Song</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/3CTvENkGrXC47vyQNti7J4" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="SHUT UP AND EXPLODE - BOOM BOOM SATELLITES">
    <img src="https://i.scdn.co/image/ab67616d0000b2736efc076b0f1f602a8c82e56e" alt="SHUT UP AND EXPLODE">
    <div class="t-name">SHUT UP AND EXPLODE</div>
    <div class="t-artist">BOOM BOOM SATELLITES</div>
    <a class="t-open" href="https://open.spotify.com/track/3fD5HVFpDIAQ0tsPTFPDPl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  </div>
</div>

<!-- SPOTIFY_END -->

---

<h3 class="tagline-type">🌐 Social Links</h3>

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

  <a href="https://open.spotify.com/user/21tuk3i5t4cipp67csfpuxqga" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/spotify.svg" alt="Spotify" height="30" width="30">
  </a>

</div>

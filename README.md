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
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ELCqIXYiPVAQ7kNvwHpAqLB&amp;_nc_oc=Adqf6Rn7rww0s9wiOX4vYgx2hlVD2lgta9U7nXk647F1Y_OgoxmVeVOokGwef1ZeRGg&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQKeid_WIlPFXgQH7psam2KQ6rb7jlJSuTR8EJvO4Hu0K6nZg7kD42PRFCUcVkP3XWC4POoIuMV30g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSSSvNKZxIawAB40RHRVF6Csc1iE_nPm0-n_BFMMJeMvQ&amp;oe=6AFF415D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-Pg6txvdhO0Q7kNvwEm13i0&amp;_nc_oc=Adr-MbtpcRjaDgyfHlDH2nYZ_kDt90ZV8EqX4neXfRrH9a6fLOXrlyOHB1HXGJPiNpg&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQILrH4xz4h4R7jjCMJYUfn0jTW_EmltXVu4N9MZ0tZyzCo1yTkrZlcx-XoqjLJUu5oyKxAgG6FziA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQLv7II0hD8oPKpaYfrCPzMVdVpiK7VuWmMCBEbVhBKoQ&amp;oe=6AFF5C1E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=jeV0wgwRwdsQ7kNvwEcSlHx&amp;_nc_oc=AdosRY3E74iiHs99kSPiUV0WTVGF0Wd-6MyqDTytgJe6DXS8X2kZoDIUTyTGGrzAo9A&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJypkX46nyKzp5POjw15TCQsJBVL_UWVUlByEHF57j1J-HHsBcgPaRGKrIJqyc2ZCAJIux1fzVJmw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR_z9ykLvAMn4wu_pO4LnQ-RxXmNsM2ub4HC8-IhqMX0Q&amp;oe=6AFF5AA5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=CiC_u11QyUIQ7kNvwFDQXFK&amp;_nc_oc=AdraoE1e-w1fQHNeosFym6zJ5YMx0VSZyHTokGZSQ5QAR0vX16jnidFJ17pu9RrMH00&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQIVHZErVm7DfY3RcBt8gO0HntE7PrpPZgW2CXw1wCYQv3MjvKFkOXGs3aPo4_cNwRrXyvDhDpPjbg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSYM_LEkTF1QQiCWsY_kK5PVe5XmIrPJL5CfLaUcsWcMA&amp;oe=6AFF5C19" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7YsI9zT8BR0Q7kNvwFqEqGS&amp;_nc_oc=Adq_GeSCcToSIN65A-cXKF6hoqU3JZb8HjNYDmdMSjxISaProki9mJ3oPJrCVcIB308&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQIpH6UT5cIZkdJggCQEiBabxRwYA5GynZNLarSXOGhrXM-m3ESz4IWl2iCPwTlCuxntjaAeZwvxkg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQXDDfRcGJooGnFuM9nAnRMe5IgI7tEQJCYRdEWsYl9Nw&amp;oe=6AFF592E" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=jbi5-m-7AGYQ7kNvwHBTh9b&amp;_nc_oc=AdpV9-IbNRbKmCD3K4Ksf0ru5m3ceMWAop9oI7ZPQ_F1ylsv1XkLBY4Tj32UTPSrt7A&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJqlPv_asrlE_R7Py9wC12zZMuzMPvBylztzfolTbxmJwRWWI-Cam4hx2aMSiBTiOvZfrh73RButw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS8zu-lP0kucNV8NQvjRJcVzMHYY7S5h0R4U5VPNMcq4w&amp;oe=6AFF5C9E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=nl8Bgo-KOYMQ7kNvwHwp6mP&amp;_nc_oc=AdoH0UOu9rsz831w5B2YHHUBTzXURNql7Cv8RNtdYBa4x0hCu5f_QiJeZAI-aMg_oo4&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQIpaf3LajXPThzsjgoMAjQFStkoUZX_3xyatWpQHh9vIfNuPqslrGGzafVoT64XRwpNQgCyiIcfTw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSZxPKojWQQKCtMjMr0uoS6WH6LxEgPhsAhS_wyEFrZcw&amp;oe=6AFF3535" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MZ_n9EAlP5AQ7kNvwH9L9VF&amp;_nc_oc=AdqxUR2vtcxUT7g3apqjdELCBFK5B55WOT7-5p1jx4EGtsH3WKlfupenysIkb6bLq3I&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQKuQpSWUmJvL13n9mz9UG-1JFqs5lsPMVuVIG-s3fJ-soMe6i-xrGei1801dfme6yAKHjODZnmogw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTMXydFu5aGfTqzEEaIbUnqikuf0zNWiFRP_ro204wLbA&amp;oe=6AFF58F6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=iO1cFkl3V3sQ7kNvwHGbIRG&amp;_nc_oc=AdoHOl4pREXCqmYKCsAOVk3KgFXWUVbuxcMYFnsZZ9nTHF_2-W3HZ9JmY8Lgy0u3npM&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQLnSOFg33yoTBhvOGsnsEVbHrb5Ezv4mc8W4jAe8rw1CCtoX1VK35IYaOODOuXREX_EceBDvG6SLA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSfKOhi5nRU5Kf-st_NCtQffkveho7EMU84wlnP4pUUdw&amp;oe=6AFF30E6" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=NNv2uQXsiEAQ7kNvwEI3dWA&amp;_nc_oc=AdrlRbNS1GkD7Wx8dE1vLUWigmSxQi_1as0Cbdyw7tI1To9hP_UdtWBJdxOUPrpQBRg&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJBBOqG7EdJ2-e7McurBfBw64UG2x-dBMFvIga4BM_sNqqJYwnVAGOBgGzakn2PpKSD5gRb1bIOxg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTmsHCAsKeyaBUbwdv4fyGWkqvQHeSqmE-0Lntbqi3kIQ&amp;oe=6AFF5C41" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Fn--GVOi_7wQ7kNvwEKEasY&amp;_nc_oc=AdpXwnnjLUGOGL4JqYbIuIWXOCb5J-5LHqGWr2cAVUfada1klQlgGROpKrxlKY-HEmY&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQIl7Y_9Qk7C_yIebD-Fc0kpUIzmcfloUkNTr6RM8Q8CHaPlOkX5x1j5e5lFixN5QfUME5yMgMCexg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSRYuhSdZMHAJWLw71N95HLY0wwEoYVN-0J8-YSC3140w&amp;oe=6AFF5C9F" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=b3UH0DqjbzAQ7kNvwFC-hmH&amp;_nc_oc=Adr7LQX6QZJPdDq3S90oOJwqwulApcSUZZPkVuvrNYtmnqcboow8Z6_hPdlJYGwG6nU&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJLJB-vJsOmgq2-rM0WDT7WXYNF7mpiJOc1wsqTd0PWDuleu_C0EyUmeEIYjpnzwnrRKZw73KqcqA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSDrEON--jSwFsTKqNmCIQBhd0Is0TbrJae6xs5Q3Cqiw&amp;oe=6AFF3B2A" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hGUrTmchzBAQ7kNvwF--Qe9&amp;_nc_oc=AdqW2GhbEwdh9F-gm4RH5L4RCc6SX3PIgQF0YWe5aZkDIxXJNw10_F8yKe1wC2nszs8&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJQ3GZYDrLStINYBqoUDFu4tA1GF1dc4dAlhWL36QNhAz9qJOE_tGZQNmbYR_-FMVAZ4MDEd2FQaA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQsap2Aemxc385b1-dEEFA3rICxvkNDICLh2p6n3axOCA&amp;oe=6AFF66DC" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw6-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=FCZEN9GI0W0Q7kNvwGEjgtE&amp;_nc_oc=AdphSfa59pTyZgSsfanKVeHXJucEavlcTHIyyDN8Yz89EUtJUjbwzxbho-MpAKWk0qc&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQLTKfybK1qS7mqIn2u48xI_CkY7fHUJ6B6-LWALsPXbceGXqjx6AgxbaxeuFUQkt-18GnVAECKG4Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQScPqrJe9IkfXdPiTNmW5dE9Wab2cLia6WUGGXsD3skGw&amp;oe=6AFF3EB6" alt="" class="t-thumb">
      <div class="t-text">台風接近中の中、2年ぶりのTGS。<br>始発で行って雨の中2時間半並んだ甲斐あって、…</div>
    </div>
    <div class="t-date">2026-09-20 20:52</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Ddgha79ibTF" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/814470857_17988626214105617_8431201690405807241_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S4ubk_1CmvAQ7kNvwEfEowT&amp;_nc_oc=AdrGkFnTGBRXtDvfOwqclpeXVXW7zUNah1b8oRMcc4r5cie4ZODYlzzGZkLrSWnT7BQ&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=MrGRZtCVdIc0CXWFc38E_w&amp;_nc_tpa=Q5bMBQJTqN9OIr1ol29Jmn91jWBlKnHGOOpk5cC9JEqC6Nk-jLWzhjEUSrjJ86vymNGwEu2Jkbd9KOrgrg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTOYOOJW85pWGz6UPoIVhrcAfKtxWFp3nFM-XP8Ii5g_w&amp;oe=6AFF58C0" alt="" class="t-thumb">
      <div class="t-text">TGS、月曜の最終日、開催中止になってしまった。</div>
    </div>
    <div class="t-date">2026-09-19 16:18</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdddPfhGhKv" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text t-text-long">とにかく各登場人物の「顔」に圧倒されます。今年の個人的顔映画オブザイヤーです。こんな凄い映画がなぜ都内で3館、全国でも9館でしか上映されないのか？この映画を広く公開されると何が不都合がある人でもいるのかな？などとメタな考察もしてみたり。音と…</div>
    </div>
    <div class="t-date">2026-09-17 12:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdX3D8Rmjnr" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
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
.spotify-card:nth-child(1) { z-index: 17; }
.spotify-card:nth-child(2) { z-index: 16; }
.spotify-card:nth-child(3) { z-index: 15; }
.spotify-card:nth-child(4) { z-index: 14; }
.spotify-card:nth-child(5) { z-index: 13; }
.spotify-card:nth-child(6) { z-index: 12; }
.spotify-card:nth-child(7) { z-index: 11; }
.spotify-card:nth-child(8) { z-index: 10; }
.spotify-card:nth-child(9) { z-index: 9; }
.spotify-card:nth-child(10) { z-index: 8; }
.spotify-card:nth-child(11) { z-index: 7; }
.spotify-card:nth-child(12) { z-index: 6; }
.spotify-card:nth-child(13) { z-index: 5; }
.spotify-card:nth-child(14) { z-index: 4; }
.spotify-card:nth-child(15) { z-index: 3; }
.spotify-card:nth-child(16) { z-index: 2; }
.spotify-card:nth-child(17) { z-index: 1; }
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
  <div class="spotify-card" title="Unbreakable - Michael Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b27376bfd700e0c47fae7f2c7b75" alt="Unbreakable">
    <div class="t-name">Unbreakable</div>
    <div class="t-artist">Michael Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/5L9anTQJGLyRObYDYvLWdh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Invisible Touch - 2007 Remaster - Genesis">
    <img src="https://i.scdn.co/image/ab67616d0000b273b917174eb6069392e8a3cc7f" alt="Invisible Touch - 2007 Remaster">
    <div class="t-name">Invisible Touch - 2007 Remaster</div>
    <div class="t-artist">Genesis</div>
    <a class="t-open" href="https://open.spotify.com/track/0xpBr84T3FTm9j4D1MdPtk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="BLOOM WORLD - ふぉ～ゆ～">
    <img src="https://i.scdn.co/image/ab67616d0000b2734eb269db0236878baadd33f1" alt="BLOOM WORLD">
    <div class="t-name">BLOOM WORLD</div>
    <div class="t-artist">ふぉ～ゆ～</div>
    <a class="t-open" href="https://open.spotify.com/track/3L0Z9ZFAz6bxsSDzGkED9t" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Walk - Mayer Hawthorne">
    <img src="https://i.scdn.co/image/ab67616d0000b27369069f0a19609de8db3e7152" alt="The Walk">
    <div class="t-name">The Walk</div>
    <div class="t-artist">Mayer Hawthorne</div>
    <a class="t-open" href="https://open.spotify.com/track/4nd8rHES5zOlFhwDxDdugW" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="ファンファーレがきこえる - Base Ball Bear">
    <img src="https://i.scdn.co/image/ab67616d0000b2736713542f83aa31b91a5ffb91" alt="ファンファーレがきこえる">
    <div class="t-name">ファンファーレがきこえる</div>
    <div class="t-artist">Base Ball Bear</div>
    <a class="t-open" href="https://open.spotify.com/track/7nHQr8zBVrZio8CgjVvSk3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Don&#x27;t Speak - Loaded Honey">
    <img src="https://i.scdn.co/image/ab67616d0000b2738e515a0c788f14697d9c6faa" alt="Don&#x27;t Speak">
    <div class="t-name">Don&#x27;t Speak</div>
    <div class="t-artist">Loaded Honey</div>
    <a class="t-open" href="https://open.spotify.com/track/2sKjOX72UX1HiCDhI2HdlR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Just The Way You Are - Milky">
    <img src="https://i.scdn.co/image/ab67616d0000b2735054a99f9ce5b356db8d5852" alt="Just The Way You Are">
    <div class="t-name">Just The Way You Are</div>
    <div class="t-artist">Milky</div>
    <a class="t-open" href="https://open.spotify.com/track/7K3Lc3TfSR14aTOjIH7TUj" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Man I Need - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b273e3d69e17dde129037a1f09e2" alt="Man I Need">
    <div class="t-name">Man I Need</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/1qbmS6ep2hbBRaEZFpn7BX" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Last Train to London - Rikas">
    <img src="https://i.scdn.co/image/ab67616d0000b2731a61a0637f0d90538a950303" alt="Last Train to London">
    <div class="t-name">Last Train to London</div>
    <div class="t-artist">Rikas</div>
    <a class="t-open" href="https://open.spotify.com/track/5fewYZz1bCsj72vjSwSxzq" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Set Adrift On Memory Bliss - P.M. Dawn">
    <img src="https://i.scdn.co/image/ab67616d0000b2735423456a99eaf4218893d20a" alt="Set Adrift On Memory Bliss">
    <div class="t-name">Set Adrift On Memory Bliss</div>
    <div class="t-artist">P.M. Dawn</div>
    <a class="t-open" href="https://open.spotify.com/track/7vo0ILIm1He4wo30ikYBHh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Moon So High - Remi Wolf">
    <img src="https://i.scdn.co/image/ab67616d0000b273fa3db827a24dd8dbaa1bf245" alt="Moon So High">
    <div class="t-name">Moon So High</div>
    <div class="t-artist">Remi Wolf</div>
    <a class="t-open" href="https://open.spotify.com/track/2aST6n3igBIOhdoCZQcmmX" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Cha Cha Cha - Bruno Mars">
    <img src="https://i.scdn.co/image/ab67616d0000b2733eb8dc748f7efb1470f74395" alt="Cha Cha Cha">
    <div class="t-name">Cha Cha Cha</div>
    <div class="t-artist">Bruno Mars</div>
    <a class="t-open" href="https://open.spotify.com/track/6QletrrmpkUpeJkipX9pgf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Verano! - Ivana June">
    <img src="https://i.scdn.co/image/ab67616d0000b27349f3bbad1cc5f0627ae87b4e" alt="Verano!">
    <div class="t-name">Verano!</div>
    <div class="t-artist">Ivana June</div>
    <a class="t-open" href="https://open.spotify.com/track/7cN5M5xQgljTIDX65h9EF3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Asleep Talking - Magnus Ferrell">
    <img src="https://i.scdn.co/image/ab67616d0000b2730a0f50681631065bd6c5024a" alt="Asleep Talking">
    <div class="t-name">Asleep Talking</div>
    <div class="t-artist">Magnus Ferrell</div>
    <a class="t-open" href="https://open.spotify.com/track/5dBXBY5CsYxEjC20ewA9EU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Worth It. - RAYE">
    <img src="https://i.scdn.co/image/ab67616d0000b27394e5237ce925531dbb38e75f" alt="Worth It.">
    <div class="t-name">Worth It.</div>
    <div class="t-artist">RAYE</div>
    <a class="t-open" href="https://open.spotify.com/track/7JgNAnCjJvL8hBR1kmCOFF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Don&#x27;t Walk Away - Jade">
    <img src="https://i.scdn.co/image/ab67616d0000b27329cf454757f957fb528cb18e" alt="Don&#x27;t Walk Away">
    <div class="t-name">Don&#x27;t Walk Away</div>
    <div class="t-artist">Jade</div>
    <a class="t-open" href="https://open.spotify.com/track/7tsRp7QKUBp6hc9bth0h7x" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Every Little Step - Bobby Brown">
    <img src="https://i.scdn.co/image/ab67616d0000b27353cf43170dc29787984cf6b4" alt="Every Little Step">
    <div class="t-name">Every Little Step</div>
    <div class="t-artist">Bobby Brown</div>
    <a class="t-open" href="https://open.spotify.com/track/0s6e7ZafqOAUBDoQYGmxrc" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

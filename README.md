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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ukxcv0m3Rj0Q7kNvwFeMDqL&amp;_nc_oc=Adr7bkZoOJWOkxn89OCx0PJ1753edKOaQwmsBqDebiijIhW7TLFFR5FWnTfuvYr-lRM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQKNdjcYYOuuNIJkwDXJ37NzWo4LiCyLamz7vTGyx5JCiggu6mZq_tr-SXWEKCP7WVHU05kRKeGV9A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRtmiYO4fRKgHNu8XcQo96qtnIaSXD_5nGuoTk2IWnG2g&amp;oe=6B019BE5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XE0KclzW5xUQ7kNvwFILIGU&amp;_nc_oc=AdrbSkc3f7U-UzYpG2iMIF1oeJ_mbvL0w751ZmKWyNGkyV-r7dDYEC1T-mHGJEjJoeM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQITeAAfB1W3z0WDa_FHx-CNU4IHNfKQH2W3OjWeD3wh6UuxORWKhttkTE0f5p7J4kOERVT8nN56wA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTnR_sV0U-UcWAx3l7BwEKK24x09E2hqgUfhEoHBCbDqQ&amp;oe=6B01AC1D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ok-cGax8GA4Q7kNvwGbc7Di&amp;_nc_oc=AdqIa2hX6eMP6CbxJIckgMv8GWgeAhafkmxdo749Ocqle_gFbjAWbP8g3so3wrCbPhc&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQKx1hcl4wqwdQYQjBdotR8N9dA--p8HMCHxBaF0Qh36vN2IXcThcxkeo2Ma_11jwc1wV8D_-KhVCw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ2HQukovTgy2dE3rtBZBdQDwAuEC_ozIkncgZC-gNfyA&amp;oe=6B018E9E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4P2NmKQR0ZoQ7kNvwH33zG0&amp;_nc_oc=AdrJhFIsTHVFjwA6eD8Wo-Cc_oqRZGUcWkerXkv9nTJ9c8ZSyikBsvWaEL15KOKIido&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQJQmqGvZ8PFi-2Z9rfu2oQaP5hgLEs4FdC8E3Ir4urU_8_J2l_7ZWt20XdGaJQHzGdEcC7EaFbxLA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSsRF-rWFRrLf9gO_gYwpVuhiD3siAJVDOEDAZSe45jfw&amp;oe=6B01C565" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=CiC_u11QyUIQ7kNvwFp_QIX&amp;_nc_oc=Adq6MhRLZjMtR27b2BJrVNDNLx-Tc_dkMuQ9g8YqooEfsc6jTkZtIYwq5ppmbDqn_Vg&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQIrByAWlWOxeq9N4m15kh1EzGysaGP6_YjLzEL8raTo51ufXUCsa_FeXCSUq2J3Zn5WYeBZqL8ceg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSZl8PzVRIX670MKjSJdXlV1xwVu2vlB842RSyM7EUDSA&amp;oe=6B018E99" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7YsI9zT8BR0Q7kNvwGLd6Iu&amp;_nc_oc=Adq9ZNW6_Ru17zfoiB5gFyykfYyMv9i3h2-xdOQEiKBy0WitZR5C5v0AhIdGOo3aNY4&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQJGZqAR7hAs0NDMaogoCUq7O1uCBiTkDK4ij9M0RuhM2wetYPcMZ383pH3DYfEvG4ViikUWeCicrA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRWp4AXVekKM6vZN1qdrAsUWvldcu09wOckwwvMj8112Q&amp;oe=6B01C3EE" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Rz4F_ge4AL8Q7kNvwHMcMSt&amp;_nc_oc=AdoPSP3BkC6Hm6b_wd20_WvRTJ9nt5U7aEG6ze30sBrtmbuU6H95Ugc7kUHPLUhlJkg&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQK-7JLBqqTGqkpfAbTk0pthR4H6cV2foNZQqgP5L9j_OFSIXkNz_11DULlPLe-r8QF2xvyycywH6Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTo8KTvP-De3ZfWltq957KqouPzRbtb_k3VrOPn0cjLKg&amp;oe=6B018F1E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=f3XgNVFnN7EQ7kNvwEnuIHv&amp;_nc_oc=Adp1yYxg9xC1HxCjyGwsSNBNySg-yTJ1-sNLwsVerRn3rVqRfh-mphXOxxzvXggeoy0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQK6AqSLZVQot3qV5EqAmfAO-8AYEUWufK50VsiFMIj0sF18jPssMrd-hS-liqC4mlwJk0ioTOMGow&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSkSpdaNlt92NSVFDvuxSNN6f0kOg4-eS0L7uCQfQZiaA&amp;oe=6B019FF5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MZ_n9EAlP5AQ7kNvwGeLKr7&amp;_nc_oc=AdrN-stXtiPN55ZUKv-EW258u-LAEYgYyAxI7G_qLNakKjif7LH_mMruLiZPCai_BEA&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQJlmUv0qXKJJipUQ0ngwIGCQnqznpkUblmbKc0bKy1t6H8OGI1XisWepXmiHXBkgMxS3zdyFg7aHA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR7uTFKV8A7KeaWHOwUmjUa7zgaNkRIrAY_yFxxzMH_MQ&amp;oe=6B01C3B6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=6J1dNTaPjzIQ7kNvwH9h9Pv&amp;_nc_oc=AdrCpzj1F7uYgFrnCIAtlHWyzPbB5Rc-hWZRwmz6l46OxVaYFc27tbBUPWELtv2xH44&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQJSRzjtOotEh0T9-MYC6hMRVZFOB9_hWYuc8V2cRJ_YUwCAZM1fcVGitsf_0P7jyYagNwa393xSsA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSUyag4Q1TJfuKxxsjToATdUEUZbc002BU69xIcvhF1Zw&amp;oe=6B019BA6" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=NNv2uQXsiEAQ7kNvwFa7TE3&amp;_nc_oc=AdoB0cpdIlkvZflLzspV8lYpgdb4GU_e5Tgf3joir8SlTaU882-CVPXygOvESBIgt_o&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQKgXUf8Q3Qrwaeg4MtDGl77qMd_DgtBfBg26taYEV8wP7cTzf9-O3lPhK_xMds4-niWkyX9DJ_amg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS2R-9qDwCHtNFe6SY3CES99re1zsCLzNV2RafvBaJKFQ&amp;oe=6B018EC1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Fn--GVOi_7wQ7kNvwFw-bqC&amp;_nc_oc=Adp2Qh8vVcaUn1Towod4qtFez_yLDB18dnrGmbyeA5foyZZtF1R1NlSijpfuISE9joI&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQI-K64mbpct__lQU6FLft3q6nF51KgjhMU4YdpkPBdvxkbr96Zx3-sFGqlx3hLCcbVEtD5KcURxWw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT66V23EnAmSQdv_ObHGGpcLyRFjTKoGKldRs6D6iRhoA&amp;oe=6B018F1F" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-306fbG4B-kQ7kNvwEWVAZ9&amp;_nc_oc=AdpXXLl5WNaHWKzPqgIsH-MW_K9maZObO4b5Txsumam31QXYh7Q9r_WujtxHyurF9IE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQK9FdqH01Zx8E0qiQw6_iUDqTAYS8P8gKcr2cJjyD8H6pndzLy1kg92uiOOGrr1LbpJuftfCJoU6A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR1__LlswgroF_dls41a4kv0qcMYRbaa0VIv42jehaOVw&amp;oe=6B01A5EA" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hGUrTmchzBAQ7kNvwF4fdBO&amp;_nc_oc=AdqoeU4_B9C5E4j3nKUxYQnv49NRE2qP5h-q2_5Zn1kqTZ_w178MyYcj0HNYH5wQQ4s&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQLKp6b6dQro7erKS_M7m0PCEZIvQPcSln1Ep9_1NhGZo2UXWLeSiltD_KGP9FdyV3jXx8uiKbOlGA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQMH9cOwttMzDspSs0PfzODKKuOlWYtf4jcI6R5p1cA9w&amp;oe=6B01995C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=FCZEN9GI0W0Q7kNvwHq5hNc&amp;_nc_oc=AdpyDYkvWMPB0CrDtjv1e-g3F4C6tZN6yuHYNKTL5zyZHW-7vUgTZySoOwca5zEx8lo&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ftxXQUd7G4ZuDpZ4t9LrNw&amp;_nc_tpa=Q5bMBQKDnIVFfs9X2k_JekCJBOkuA9LJaP5LDgBzbhllATZ3Tf6yV3IfP6oNPOmj_dVaVygYUMK5jupLMg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQvXXI6VK9WNKXGpEQnWQnURBqEyTHEiSSl92z4mcd87Q&amp;oe=6B01A976" alt="" class="t-thumb">
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
  <div class="spotify-card" title="Baby He&#x27;s Your Man - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b27384bb3ed07820b1b818abd2c9" alt="Baby He&#x27;s Your Man">
    <div class="t-name">Baby He&#x27;s Your Man</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/5w2PPpREIfphI1XayqcxqH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="サ上とロ吉 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273370f9c1c7fccc0b7d95d2b6b" alt="サ上とロ吉">
    <div class="t-name">サ上とロ吉</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/373WK4HGaoZ0n9n4oYGkKJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="PRINCE OF YOKOHAMA 2222 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273a0ae148c841c81f9abc95d0c" alt="PRINCE OF YOKOHAMA 2222">
    <div class="t-name">PRINCE OF YOKOHAMA 2222</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/1UKOYk4ZVxIqeQjw9ENSfY" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27303e728a9ad440c4a7cfe1f49" alt="RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL">
    <div class="t-name">RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/5HcQ7gGLdsxNxURUmJB1fm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Three Musketeers Mic Relay - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273825ca2f52579817a1828ece2" alt="The Three Musketeers Mic Relay">
    <div class="t-name">The Three Musketeers Mic Relay</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/3JFK10dXAHjv2zeJ0QTCYo" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="More &amp; More feat. ももいろクローバーZ - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27355f8c188a6300394b31f101c" alt="More &amp; More feat. ももいろクローバーZ">
    <div class="t-name">More &amp; More feat. ももいろクローバーZ</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/6tyDJit7oCemK3KXDXMCfh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="START LINE feat. RYUZO - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273370f9c1c7fccc0b7d95d2b6b" alt="START LINE feat. RYUZO">
    <div class="t-name">START LINE feat. RYUZO</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/4VSffG2zodK3hK0bR1RF2w" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="WONDER WHEEL - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273370f9c1c7fccc0b7d95d2b6b" alt="WONDER WHEEL">
    <div class="t-name">WONDER WHEEL</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/5PyLGT8Mf3PLmQ1R5fcLnQ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="ちゅうぶらりん feat. 後藤まりこ - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27392865e7a853ea3062216dc37" alt="ちゅうぶらりん feat. 後藤まりこ">
    <div class="t-name">ちゅうぶらりん feat. 後藤まりこ</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/5ZAkY5I700IU2ypCoVhBAu" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="PRINCE OF YOKOHAMA 2016 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273096012cf02f9fade40fd082e" alt="PRINCE OF YOKOHAMA 2016">
    <div class="t-name">PRINCE OF YOKOHAMA 2016</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/5nOFDbTGWymTWlQjqAJew4" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="ぶっかます - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b2731af4b10c82720d6c77192e42" alt="ぶっかます">
    <div class="t-name">ぶっかます</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/4YCdcog59Hu5UHzQbWG7ww" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="ヨコハマシカ feat. OZROSAURUS - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273bb748ebdde17c28fc5bf7fc9" alt="ヨコハマシカ feat. OZROSAURUS">
    <div class="t-name">ヨコハマシカ feat. OZROSAURUS</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/3hM4fl1yY0ZRCIFBJ0rt6y" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="空っぽの街角 REMIX feat. LUVRAW&amp;BTB - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27359953726ad30ff15609eb810" alt="空っぽの街角 REMIX feat. LUVRAW&amp;BTB">
    <div class="t-name">空っぽの街角 REMIX feat. LUVRAW&amp;BTB</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/0bufABO9ZrP34Gq7FK4C5E" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="RAW LIFE feat. 鎮座DOPENESS - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273c422172fdfa022a3c507771e" alt="RAW LIFE feat. 鎮座DOPENESS">
    <div class="t-name">RAW LIFE feat. 鎮座DOPENESS</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/4CkAoUK0CfJ2Z2bXvMKdYn" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="よっしゃっしゃっす〆 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27392865e7a853ea3062216dc37" alt="よっしゃっしゃっす〆">
    <div class="t-name">よっしゃっしゃっす〆</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/75fF6bjNbeuIubddsvO1JI" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Tokyo Swindlers Main Theme - Takkyu Ishino">
    <img src="https://i.scdn.co/image/ab67616d0000b273016e6dc65337b409f4553908" alt="Tokyo Swindlers Main Theme">
    <div class="t-name">Tokyo Swindlers Main Theme</div>
    <div class="t-artist">Takkyu Ishino</div>
    <a class="t-open" href="https://open.spotify.com/track/09qwKDU6TwQoQC84UiQGaf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Night Distance - I love you Orchestra Swing Style">
    <img src="https://i.scdn.co/image/ab67616d0000b273bc6d25c51e2f9b43720c370b" alt="Night Distance">
    <div class="t-name">Night Distance</div>
    <div class="t-artist">I love you Orchestra Swing Style</div>
    <a class="t-open" href="https://open.spotify.com/track/0G9OA0VqF6SKtyYraNE5xv" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Cruisin’ Cruisin’ - bonobos">
    <img src="https://i.scdn.co/image/ab67616d0000b273c12de844ac9bf4d4e40a87db" alt="Cruisin’ Cruisin’">
    <div class="t-name">Cruisin’ Cruisin’</div>
    <div class="t-artist">bonobos</div>
    <a class="t-open" href="https://open.spotify.com/track/1ZBiaJ7v6KHLoaytAVvCjA" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="サーカスナイト - Tavito Nanao">
    <img src="https://i.scdn.co/image/ab67616d0000b273f3eea33cdd0429a65d438a53" alt="サーカスナイト">
    <div class="t-name">サーカスナイト</div>
    <div class="t-artist">Tavito Nanao</div>
    <a class="t-open" href="https://open.spotify.com/track/1bhF1dbIKLXbVW2QupmvJl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

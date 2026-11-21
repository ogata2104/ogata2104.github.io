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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Vr-1zZHrsHwQ7kNvwFCNGHv&amp;_nc_oc=AdpC-p_sK3aeG1ATga5aO5zGaw5kzsOf330YoUAyWm8zJ_LbGaD9dYbsda56UiYbbsk&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQI4Vy4zqbp3LM4l_Vd7JXcO6DyU5TjwVMyVqieLP04MZxdbbUZnFmg_dxxoHw-w_zjLqaGxDDxZMw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSpNYVPlYgrkaHlW8F3Sdgo-Vwyhc9n_ErJxsSDBRKcag&amp;oe=6B06E1E5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ieTbCsvd2fMQ7kNvwHWxuvR&amp;_nc_oc=AdqpD-viaTkctYPQ86lLjN7URHH-wkUrSSHbphiti5-eKquTqT3PfMBIjQKamMCkRhs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQLpt7PXkgkoG8PYVufOjqxbvruk7NFvIUpBX29q-sL_34gACEpVwDGKpVD9Ln_d-zCqzSER9jyRiw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS6k45xcxKYM2tJj0KSvNd6h45ZH2jSjJVef4sAcF4OVw&amp;oe=6B06F21D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WtyzJYc2-bgQ7kNvwHA00tX&amp;_nc_oc=AdrqqpN9EI9orfz1iD3i5AVDOflQnPRyJiB3EKNYE9JqvUUmVw9-tTYqC6iVjb_w-9g&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQKBPCXYiXM-J6bJ_PrbWPQQPIahXFCgxvafqIVe0DY1pYx37RPu10N9HJfSw2Cl6m9CSp1p6BHtPg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSK7xWTbaVw2qotdchq3YK9wocH7rTDxa6tUkCRBHVTWw&amp;oe=6B06D49E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=T3mNwtpgZfUQ7kNvwFgQUPj&amp;_nc_oc=AdoDZ4233f7UYlYZXjLk_5e1ZHCRw-Ushvx6Gu4S1uhOf1D7z-o1P4w3_g-gjQZPsqE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQLLymi9bbYnogTp1AXZQeC1zGFTlWeAuylxTLrdK56oj7B_qDaZ2P2bIQQwVJJN92YVztnodU__ZQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRIgJ3iODGurhfiqmxyDkvso73OX6r90IRYp_l96h7cqg&amp;oe=6B06D325" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9YSLF_Ac-yQQ7kNvwH-q2TS&amp;_nc_oc=AdqwgPZL4kdeKybn_p40JNIUUaGqaUJU-yYvpO55r4xIb1UGbpcaJCrIdEk4YYZYCEA&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQLPOLAVdybdduM_9LWLQFGT-IEZHd_UK7SIxKO1abipeHiobrihGJZ9ZgdDJ_mqT29u2SJogGWhnQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQOxiiNfFUW3YlaswRI9BaaW0bAQ7CBJTpRPjwUVa6jxA&amp;oe=6B06D499" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=eIqcC5m-AWEQ7kNvwGfV4V3&amp;_nc_oc=AdrSqMbA9goatedmnM8cDTKgBduwSpIDVCcfz8C3OEsX5lPJZTUx6zFSl7QFOItjg98&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQI89xtcfJnuTMgEdL8ipsihY15z_79Wxpu4S8O4L2s2RwYs5G67ZEZRwdcHAfnFe7OQgOCQxvQiEQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTB6MTHCAS_5rVSP8kELld9_48g6WslBhPrHbNy6Mw-Zg&amp;oe=6B06D1AE" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=R8nIGnx8dEQQ7kNvwG5MKfn&amp;_nc_oc=AdpBdrqYduaSBqJ-gj2Wo3SYHZ39SZVb28uUxqRX-kepalGnxmh-TGV7anM2w4pzqlo&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQJbG7cyr8wqvwO1rDnV8s8z89T6646ctRGO8OAUVd3mloAXS03uR76ZvXkFOvIeEW0SPy1lLmDzwg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTEqgG5xUuoIPUmAZ54uo9hMLc1Ymzuckg2sGLa1f-a0Q&amp;oe=6B06D51E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4HOFkUSIwjUQ7kNvwEICYZ-&amp;_nc_oc=AdoRCcSRxhqXAICk6FEyhIS0h6WkzdO9jIXkXTjPKfDhSN2bLKsxHrhBuZ5cVeF1bfo&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQIdzpcxrcsCJMRphQXF3Vh0u_peuW-3H5cG55SPMiB4IC6Oy0KObJZmCMjRe9uIZh5zvpVpW9JhcQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ6VNllffUQxZx4zdpXGxOoZ1WVAvQHkSDXvhPXvPuizQ&amp;oe=6B06E5F5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kZrOmlk3180Q7kNvwEQfPWP&amp;_nc_oc=AdrtXTa1o492NytSZ53MSRYektUj7vVgZ-GuaEo2w7JCriiQ4SiB4zYPeMmDZLrsLF8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQJL_cRTJJ6l-6l-J6AtInXmyZfbLJrmdSkMAxzVaStTRQLCvx2na-veDtTFh4onIDGajIUAVv9YGw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSchZn185CR-AxUYz1qgswe_zEmU435-RztVDga-oWXkw&amp;oe=6B06D176" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yCLLjF1eU3wQ7kNvwE5Dww8&amp;_nc_oc=AdrZujVzgtm49ftVNSdIvJvI1PjEj6TAWA4PJbvJUrFE2v2acsr6YOxKrCJFzFtFRcw&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQIbB40wWEPAryqy2kEF0CFM1u8KdbZC6y-QZMsMp3akpwPfeFkWW4sSVVlXexd3USJ-8Vrm2W_S1A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQl6HSh2KQbNWL7ginzRTfYq5HeG8ABUKq8px6UF4aMNA&amp;oe=6B06E1A6" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=BMhmi_2p-LMQ7kNvwEI8Y1_&amp;_nc_oc=AdpasXm0-ynxqpEO0bmG7NIsE5gVVvQKOT-_zKlXYeEAFi14rUXimd1jsl5nqut441k&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQKlcT37ImQAeKQ4WOpCWbKMHaTT6eOiUdlQ33GOf7R9L9xvR2eUzlFCY1k0jDU0zw5oPc8TMswMmA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSyxyemE12-dQCw891GvM_C1djzD2uo4Y4Qxockx6iIhg&amp;oe=6B06D4C1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=fbRJmrSwkvsQ7kNvwGyzeHH&amp;_nc_oc=Adpdgh6XdocLNDGU-iKSwSKZeuenEFrwHsx8jRO7HS8lUga95AdpiGhxzSbSi-VXU0Y&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQKm_aXyaJ1WIekRSA-gSBq724dAhuo_KKAb8Ylabk2a23nYNuCQzr--PBuNnYVlQ8uAbI_ZPNxB7Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQNDrpPxHq2u2EfYaBzAsnf6V5SrRZN0kLQkZbpd_vhMQ&amp;oe=6B06D51F" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WvhigryquigQ7kNvwEN4Pt6&amp;_nc_oc=AdpjYPgWAbET3ox5N5Jz19SIHWHKTvadvlAUUpZ3GpgbezcKzohwGJcQED6rnqw6ubs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQKUiM-FiVgvFnU5bQfuG8asqVD7hbgBQRwJ5UmWo1Ofd7X7zaBgdTvZ9zi3L2I4maKpwPCZUD_isQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTqBqE0MWbDZ_m_1k9g0RX_wAWcLIzqpymlm8pnrnyJtA&amp;oe=6B06EBEA" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_EHfebc1SeIQ7kNvwETu6K3&amp;_nc_oc=Adqpc6WW2CJNvAXwnUf_VEXD-ImfH5uNWw52BkCweXfwSY-2mHrUc0Gb5A3urtguYsE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQJB0RQqYzCG5wQv1wdqOtG68l4PKrbBxt51FRdESCZ9DdoRIhcAqUIgV9gOaSHAO0_N_sHGrWyWug&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTeNTK1cQaZnHZLu97tzCTlxGLulILz4Va5xoJan6519g&amp;oe=6B06DF5C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7dOZo3JmgeQQ7kNvwHs07GZ&amp;_nc_oc=AdqQvcJVXFQGqogs6C0f8qwwy4JOApkGmlv12Cd0tRHC5IJUswfVTtvhIU-PqrtCzJs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=__MJYPH7jKYznX65q0UGmg&amp;_nc_tpa=Q5bMBQKj2t9HXYB2cWOiI3UfOJyiP1mhSn0wTGLDYDpaPQSM7tQWXJrLTGz82LNqGAfX4-QhrSuD5z5dDw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRbsJzNsZiFYS6luSt2skGQUgA_AzTB2vIWus3KgR19Mw&amp;oe=6B06EF76" alt="" class="t-thumb">
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

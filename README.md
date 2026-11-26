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
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/928332965_18659847517027991_6354731744409032337_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9-hepWeJn2sQ7kNvwF_oFgH&amp;_nc_oc=AdqQ5Ly0WHPZH1Z1qMp6uE5sRzKBtj7RwdgUodPZDgySrHVqw5u0Jywe_J2VOFtT1XA&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQJuwN0qw4TcW_GdDN0K-cIcx3SZp-snuDkyQ_Z6xs_8CjCXP3X4XdzxdIl7pLBysKffNxk6QwoTVQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTjKllIpt0w14JmsdlT8Sof97aQhxFt65XGGX7-nv0Sig&amp;oe=6B0D3565" alt="" class="t-thumb">
      <div class="t-text">蕎麦にラー油を入れて来た。<br>太麺蕎麦、美味でした。</div>
    </div>
    <div class="t-date">2026-11-25 23:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgKtar6iR7Y" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/930725029_18659712334027991_3881358735396705569_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=YMvXcTE8kQQQ7kNvwHI2EVs&amp;_nc_oc=Adq5v1lHpp36h8YGZYiiPDnk8MoslRrwVgdCNPaa586212UH57SgouJgqlGNUeRU8ro&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQKlvraId16KsgKaETyFc--FcERo2_YriJzwg41uA02E95pWnaHxjeyolRc9bw7EKs3LJl3kVaVQWw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQotPuMqoQ3burEN9FqXXw_Swff9ptpI-8OJ9sSSHfFtg&amp;oe=6B0D52F1" alt="" class="t-thumb">
      <div class="t-text">つなぐ練習してます。<br>#reloop <br>#reloopmixtourpro</div>
    </div>
    <div class="t-date">2026-11-25 08:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgJLU0_gVaJ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=v0DUHwZ1sa4Q7kNvwGdPMZC&amp;_nc_oc=AdrjAzuEuIRIUIlDnvIJaU6L-27XaIWSSmFEYhslnDOVMprAf68Cfuh3okUmhJDx95w&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQKr2uA8wFAGPl7KvHpLfs2olKvv4KMNdTbyCy0E0CjGR86S9Ugg93yisRUE72R1ElDqQV9AkSjrpQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ_7bV1U6XBcuerH5nCn5yDYTj2BHhEXGK6sAPWGCqnxQ&amp;oe=6B0D41E1" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=sxTVw5ABe7EQ7kNvwHu2wul&amp;_nc_oc=AdqUIAh_5w4GKnIgDvd4rPaVgvEWQRzGW3CkCHTjBuweBbGzV1kvTe24-3ZpwNwIt98&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQKUogmb8La9sVmvaCSJtihJYYGkffICQKkSSpi1WGl81JmCRE9CEBw-lybjX2ayUG13xplbnw089Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQZiuKlLVmUV1BTAHZEbVKqsMiTyBvgm4FJH5Y3AqcIfA&amp;oe=6B0D6805" alt="" class="t-thumb">
      <div class="t-text">幻影とクリスタルを巡る冒険が終わったので、今度はハイラルでトライフォースを巡る冒…</div>
    </div>
    <div class="t-date">2026-11-22 13:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgB5tx2AcXP" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
      <div class="t-text t-text-long">最近、よくThreadsで見かける「Happy Birthday！」の深尾巴恵選手。気になって調べてみたら『龍が如く』ファンのようで、私の中で高感度上がった。</div>
    </div>
    <div class="t-date">2026-11-17 08:26</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Df0iJIQH573" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=pYZ_67YSwmIQ7kNvwF0Dt8c&amp;_nc_oc=Adq_44j8xBaWIG7NquM5gEQ2yjryootNxMLGBNFuKlDJLN3H2_IvgOb9pWiEtay5Bm0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQJGuLZjThvBiS0CNF55XIlfvz_YZ05d0yKybqRtCRazypZjqGaXxoUgSH3cQbJlla30CJpq7gwGWw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQtWowJ3fX-1_D3mcbR0HdPiN6WQHbtJZWxCnuZ6hXzXQ&amp;oe=6B0D4125" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9Dr-Cb2GblwQ7kNvwHIIcPD&amp;_nc_oc=AdqkqSQ4cbv4KO4JUnIljbZk311kv8bM4kJaKz1nfXI-2Q31I21CAzP6WKh7yK5NQ6A&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQJCl491TjMwtgfABeRFojQYCz_eT_uDGUJh_k7D-WgxDuOdsxx-Clf0_yt-tUzhgJ2Xpbz7OeTqMA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRPb5i7iFp7sSJLXH4M4sNXaPKeumCNzEylkz2v01wl9g&amp;oe=6B0D515D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yC1D5gNSICgQ7kNvwEKtmeL&amp;_nc_oc=Ado_PAfwdxGHvHb38LXfjS9SGQgFqm1kS_gVMMTP6dCilStPxWfGL_CYQAd_haF-Ifk&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQJqPeaIDxD8N71niqT5tMn9arTIo2dlu5l5kkVnkxjFrtff-BK6rMPRDp4qvrZaKaNhKvp51dQO2g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQST9MxKGGkbYt-j2Wwf7qtuej7RQFhrdQfFN7OOkqdVuw&amp;oe=6B0D33DE" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S5XyIqwGJqgQ7kNvwHktOGi&amp;_nc_oc=AdogXEf1oYmsnmqlveD-M88tYEqkili124U3s7DR9DuBTbq4wQ7o07z-RzlGZ2xUpeA&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQL45imqGE0RkYb_j_TuD49KTX1p6wA1jU11Pvl6Qrd4w3o2RF0nkLPtOfWnIO4VzIO4jdjk7CNgQg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTzyCezOX2HpuQd_btyt7cdCJv6WSOxwCpEyEyRfRIJgw&amp;oe=6B0D3265" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_RPOb-PgzY0Q7kNvwHTaeLx&amp;_nc_oc=AdplcVFGcwwuBtsMfv-602s6Oni2QcQVi-6YfL-GZh1C7yMj9nzXrlaq2lTpwtO3BS4&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQK-xAtLp_hqwmr4qw_CZSRMIne0t176ZFm-ldPLJ8RURBKm8yG4IY_sd8mAeTkBUj5qvOpsgr9UQQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTisje1V_Pw0_nGuGI5iK5VTd88ZL5f37pGKsyl5zYAOA&amp;oe=6B0D33D9" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=GI5DN-TQ-0gQ7kNvwFSFEHu&amp;_nc_oc=Adp-Brkijr9cF4br6T8Dj55eojcDUIj2toufgCAiHM9jUnCJJMJgoK8meS3LhBPPZMs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQLwJmMj5FUao78y7IX025rzgJh4qldoTNFn1ka4VisQHVYlVz62TyA9YRQRihJ0A8WcL8m0LYRcCA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTh0VBAGau733UXIDHv_UNQzoT3y2Y2Y3O3MEidohKrwA&amp;oe=6B0D692E" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ohf87Nojt0EQ7kNvwEjPhwq&amp;_nc_oc=AdoWlJvnZ-YlPB-0iLrXcMZVMZdjmztkfSyyztFsBkUn4Pak1on6QXpweLIQMJcDoS4&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQKy__4k_10YvYMrSsOzajAYRIbdrqqRVRG8y3ZId9_u2Fjrj19cF9pvNtdxf5xmCug8FZijrMb3rw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQqfWPFoMdwfr6T7OBMEAiMVxyqPQc24N_UULjvrVnCiQ&amp;oe=6B0D345E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=n5OR5aIDs34Q7kNvwGFfd_6&amp;_nc_oc=Adq5oJ1pSdPPb3DrQFZpJb843CgCh9uxBIyHQAnNgaQAfCC4JnhJmzUIQC92mM8_Y8c&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQJyVohx1thjGMZ5gGZibzhKuLhHVwykGACeO85Vo1idUrZwnEWyd9l9DkZtW7FIJQO3DfoMLeYyhw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSl5W6lQdwY_eoA709UYArsfQ5vzLIWfmpNO8jAy-64kw&amp;oe=6B0D4535" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ih4UpxJVRusQ7kNvwEVoSBb&amp;_nc_oc=AdoY50eYzie0T0u35cwkUEBzQi6GIm01z43qoEL3XpmDbzJim6yEoag7Ha5UfqHn3wQ&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQIbS4HTPKQ-aDk_gwNi_as-OIUWSVLd64tB_fBYQR9MfV8hPdvLS14GQLNOCviXqAatQHysOoRQwA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRad7WWKF8emSFyil0aFaJWchXbCuy11pIQ0CMl6WE6SA&amp;oe=6B0D68F6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7UaQqSrN4NQQ7kNvwH3_30A&amp;_nc_oc=AdrBbkoaPofOHc3HXKqkrxOs1Ru-6elzS6U_ZM1I0f9Xjo7-QddlCrFxiZk2BMjcGLs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQIXKxwtcm_RVhPzb3_Tx1SEYRrFL8F9Ol7krjt4_BHvV1mcbeE06l8r8yLn-vc1duTN3sA9OkgR4A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTuzAOfv9xHmUsAuccKQNFtZhGd0Fj-vIj1wy8UG85rIg&amp;oe=6B0D40E6" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kTWGxyC9Wu8Q7kNvwGmyCDN&amp;_nc_oc=AdokwooOdldBHyz7D-ptD7qvjfa31dqdjjqF7ZAcLRfqKyjNZpO11MnF_vtzbGKn4hk&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQLA-7jiivtRmt42iHCIZuQLPgGu7h173f6h_Ro9gm_LQLQBRv2IoUbfqk77jd4yTd7EE3WewwqosA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTBFvneL69e__Lf9VWNyUMDQOuyU8YmbRZV-oAS-JdEEw&amp;oe=6B0D3401" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bjBrf8U-b4cQ7kNvwGrfPoT&amp;_nc_oc=AdrWU9ok74TL5_c36Fgac5ocQn4gTc9RCiekFP2Rbt1y9hUcLobYa9oML3vUOV4BR14&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=TO8MgToBTRI5K_Gl9MRC1w&amp;_nc_tpa=Q5bMBQL3OIN0pyd9dHF0WhZpbux-HzviGdw9Ofdi884vhiPka-aOcco6X-IdDkeM_U6TbyNuoWQjyKowHQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTc_c6oXVXtoc8sgf5wYP5h2I-vhp8nflDxRpZipb1TbA&amp;oe=6B0D345F" alt="" class="t-thumb">
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
.spotify-card:nth-child(1) { z-index: 15; }
.spotify-card:nth-child(2) { z-index: 14; }
.spotify-card:nth-child(3) { z-index: 13; }
.spotify-card:nth-child(4) { z-index: 12; }
.spotify-card:nth-child(5) { z-index: 11; }
.spotify-card:nth-child(6) { z-index: 10; }
.spotify-card:nth-child(7) { z-index: 9; }
.spotify-card:nth-child(8) { z-index: 8; }
.spotify-card:nth-child(9) { z-index: 7; }
.spotify-card:nth-child(10) { z-index: 6; }
.spotify-card:nth-child(11) { z-index: 5; }
.spotify-card:nth-child(12) { z-index: 4; }
.spotify-card:nth-child(13) { z-index: 3; }
.spotify-card:nth-child(14) { z-index: 2; }
.spotify-card:nth-child(15) { z-index: 1; }
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
  <div class="spotify-card" title="It&#x27;s My Life - Bon Jovi">
    <img src="https://i.scdn.co/image/ab67616d0000b2737a231174875d7930de9dad58" alt="It&#x27;s My Life">
    <div class="t-name">It&#x27;s My Life</div>
    <div class="t-artist">Bon Jovi</div>
    <a class="t-open" href="https://open.spotify.com/track/0v1XpBHnsbkCn7iJ9Ucr1l" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="flowers - Nujabes">
    <img src="https://i.scdn.co/image/ab67616d0000b27328e6909795cc2c798fc9e1da" alt="flowers">
    <div class="t-name">flowers</div>
    <div class="t-artist">Nujabes</div>
    <a class="t-open" href="https://open.spotify.com/track/00P7qBMdsxcgS4EnnAhf43" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="TUI - FKJ">
    <img src="https://i.scdn.co/image/ab67616d0000b2730324f3751e44962fff83e72a" alt="TUI">
    <div class="t-name">TUI</div>
    <div class="t-artist">FKJ</div>
    <a class="t-open" href="https://open.spotify.com/track/0syxBXqvW4MhO3yYGcxkuw" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Water Baby - Tom Misch">
    <img src="https://i.scdn.co/image/ab67616d0000b273abe203531eac29d17260966f" alt="Water Baby">
    <div class="t-name">Water Baby</div>
    <div class="t-artist">Tom Misch</div>
    <a class="t-open" href="https://open.spotify.com/track/2xOdFPQn17smnZrFCtFNSv" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Stay With Me - Sam Smith">
    <img src="https://i.scdn.co/image/ab67616d0000b273899983dd29114e8b29fb051b" alt="Stay With Me">
    <div class="t-name">Stay With Me</div>
    <div class="t-artist">Sam Smith</div>
    <a class="t-open" href="https://open.spotify.com/track/7876ppTxozBmoZ2EZZqV1i" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="RASEN in OKINAWA - Awich">
    <img src="https://i.scdn.co/image/ab67616d0000b2737eca0a952a35b51d100c081e" alt="RASEN in OKINAWA">
    <div class="t-name">RASEN in OKINAWA</div>
    <div class="t-artist">Awich</div>
    <a class="t-open" href="https://open.spotify.com/track/7d5uA21GZEzdlnyP251Ou0" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="APT. - ROSÉ">
    <img src="https://i.scdn.co/image/ab67616d0000b27346085aa1855bd888abc51a5a" alt="APT.">
    <div class="t-name">APT.</div>
    <div class="t-artist">ROSÉ</div>
    <a class="t-open" href="https://open.spotify.com/track/5vNRhkKd0yEAg8suGBpjeY" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b273dce91774924868ea69bd4b87" alt="イケナイ太陽">
    <div class="t-name">イケナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/7emibp3qHeqNNYqZ2Y09xb" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Self Control (方舟に曳かれて) - TM NETWORK">
    <img src="https://i.scdn.co/image/ab67616d0000b27378dda3216b558e7017b6a822" alt="Self Control (方舟に曳かれて)">
    <div class="t-name">Self Control (方舟に曳かれて)</div>
    <div class="t-artist">TM NETWORK</div>
    <a class="t-open" href="https://open.spotify.com/track/0XCbkMFU8U6dyhTAQvSm0s" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Twinkle Snow Powdery Snow - Perfume">
    <img src="https://i.scdn.co/image/ab67616d0000b27306ca33f0236a9b67e18e2a85" alt="Twinkle Snow Powdery Snow">
    <div class="t-name">Twinkle Snow Powdery Snow</div>
    <div class="t-artist">Perfume</div>
    <a class="t-open" href="https://open.spotify.com/track/0fqpebgPghAzMlJU09D6ZH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="NO WAY - DONGURIZU">
    <img src="https://i.scdn.co/image/ab67616d0000b27333428b64f27c48685c59de3b" alt="NO WAY">
    <div class="t-name">NO WAY</div>
    <div class="t-artist">DONGURIZU</div>
    <a class="t-open" href="https://open.spotify.com/track/2vjH6qrmEcwrvEQ5WGipUM" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="P.Y.T. (Pretty Young Thing) - Michael Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b27332a7d87248d1b75463483df5" alt="P.Y.T. (Pretty Young Thing)">
    <div class="t-name">P.Y.T. (Pretty Young Thing)</div>
    <div class="t-artist">Michael Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/1CgmY8fVN7kstVDZmsdM5k" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="September - Earth, Wind &amp; Fire">
    <img src="https://i.scdn.co/image/ab67616d0000b2730faf2fc17446651865ce2282" alt="September">
    <div class="t-name">September</div>
    <div class="t-artist">Earth, Wind &amp; Fire</div>
    <a class="t-open" href="https://open.spotify.com/track/3kXoKlD84c6OmIcOLfrfEs" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="One More Time - Daft Punk">
    <img src="https://i.scdn.co/image/ab67616d0000b2731e81bff9807a9e629fce5ade" alt="One More Time">
    <div class="t-name">One More Time</div>
    <div class="t-artist">Daft Punk</div>
    <a class="t-open" href="https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Man I Need - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b2739a336bfb6d40bbd90a507417" alt="Man I Need">
    <div class="t-name">Man I Need</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/0mYXRQpTGjaLJt1l9MY4ps" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

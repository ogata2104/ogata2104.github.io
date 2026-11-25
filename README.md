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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/928332965_18659847517027991_6354731744409032337_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9-hepWeJn2sQ7kNvwFGywVt&amp;_nc_oc=AdoMatHaxbmveQTVH47ZFqh3Ig8RwyDa8loL1humnWuOGv_i7Tpo4djEVmA9yp4k0wY&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQLxpfJTQwmHOTV22t_iJ6yLxl8TSa9qY50GyTe2WHg4yA2ti9TApnA-271SxSozZOx4PVOqbjs_bg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQXVjAWJN0csSdFSBeZnhGg-ouW-RfX6Xktv5dCKZSf3A&amp;oe=6B0CC4E5" alt="" class="t-thumb">
      <div class="t-text">蕎麦にラー油を入れて来た。<br>太麺蕎麦、美味でした。</div>
    </div>
    <div class="t-date">2026-11-25 23:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgKtar6iR7Y" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/930725029_18659712334027991_3881358735396705569_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=YMvXcTE8kQQQ7kNvwHnVQql&amp;_nc_oc=AdqwjSPKq6ZRxR67tNjBqcSVX_xTwrCNnwwMYgYpaxxD_X48Z1jamaS6c-4YLlLmPII&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQL0jFTayb5w7SSDdEDc2mKa1KxvC9dEJrV8pdFu1ReUwUWh4gxat5FuY4cXdjG642VXCJGowiVh1g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTuGdGWwXb483VNAXxZo7-bmr-Ve_pqq9tWk2p87JsBaw&amp;oe=6B0CE271" alt="" class="t-thumb">
      <div class="t-text">つなぐ練習してます。<br>#reloop <br>#reloopmixtourpro</div>
    </div>
    <div class="t-date">2026-11-25 08:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgJLU0_gVaJ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=v0DUHwZ1sa4Q7kNvwErvcD0&amp;_nc_oc=AdqX_cmwMQoloRXON8Vg0yAHgEzmkuyKw6t3PWI9TXlqiDDLOxBqmZKFM3FmHZ8gHgw&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQKZmPaV_li6Y4y6jHMyIEuY7KdJOIiQTNgLoeAv7HCYhgzGs8DbxMITgtwlPJ__mZHS_hG3uhzUgg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ1c4HNWLz_ZvqeePicRoC9yRAWJSI63WK5EVmqWTvGSw&amp;oe=6B0CD161" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=sxTVw5ABe7EQ7kNvwEPmvFV&amp;_nc_oc=AdpwvdzI0f_RVIqrlY-k-ulZLYPXofOw6oGhPySdhhcjR9xLhcPYvbZJugtPrKP_v_U&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQIu6-56BKYmNu7UJplu5KGhmP-YnmudaiXq9PIvkFSt1TXRPJvoGw4aV3aMAKnrlNKB-xE4QZznrw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSZnBWGFDbsEC2_DJACyuoOR3EW6qV6vJLGgYlhakGpPA&amp;oe=6B0CBF45" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=pYZ_67YSwmIQ7kNvwGVTHpE&amp;_nc_oc=AdqEoHUm6dBUfNM2Knal6Rh4HWaF1kOcr9bdsuEHhAKXFcWRH5uw86vOK31lDZqpHQs&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQI146oS6ZQY7eZSXJfSLIarTDeBA854Z1IPXNG1BSO4t2A7tHwo2Tccab430FrHS0pzHILAWapVcw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTtsGsvW6uIqW5td0LX5IjmLTI79GNEyXu8qBDV1P9nkA&amp;oe=6B0CD0A5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9Dr-Cb2GblwQ7kNvwF1MEoT&amp;_nc_oc=Adp4gnhfWb6JBd3L72k3yZ0xQjh1W5BTI7yl5raIDYowpKTZupkNinA-k8fMWuo3b1w&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQKTG_LanSENItQxtKnLrMgyiWwxZfdU-Tcfv9SUBDJOlDZurgiz7AWWFJx1wRCHXVCMIfHJfd0sMg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS4mnxFYQpBR4rG7Z1f9v20LEQBLyM3X23M3A_n-2_XiQ&amp;oe=6B0CE0DD" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yC1D5gNSICgQ7kNvwHa-daZ&amp;_nc_oc=AdpyBGhwOpf3d-85mKPdIxFa2tX_Gj4fpQ80UVEkaBr8tK89jDawi1ElyAhfdA4dbrE&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQJN2RA9Tf-SWTaaqkuBl9Iupd1OwaozhQAqUZnDmnGghARNT6pq1VJbwFm6VkIlD6V3Gtq05773yw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRaF_XSuYjlvq9Z6JkgrYv02W9aHMc1f90Piw6qcEbZIA&amp;oe=6B0CC35E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S5XyIqwGJqgQ7kNvwHe0MiV&amp;_nc_oc=AdpQIUiF53A7OW4keaG_nwBPU6Gr3p6MEcPV8eOWcMziMDWOx1-6Y9bjD1J7VgBv-js&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQKGoYFI8xXNR1mamC9schZd73tTfqNM1JdxgD3ElpZKwPnwXrZHXUvE0agXR98ctoc8RxnrkezKeQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRBdWfxcBaRp2iVrg1MPBvSyM8CeN3HYaSTDmPNj4L4Nw&amp;oe=6B0CC1E5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_RPOb-PgzY0Q7kNvwHM1VNa&amp;_nc_oc=AdqxtDYQuAOTeqV7fNFxyHqBofqg5E5X1cdKjkYQqRm4foIQcbry83QB7YXB2SXzxjs&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQKXU-msjU_ICGZQwQJ7a67kFnJuT7yijsdQnmbSKG-xK2zsRdijzUV3hk0VQ1LgO_jaq6ERvEj6Bg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTtX1d7F2kONlNoyOMOSW7z-0QsEQ8Y50N8HZgEQcNY-g&amp;oe=6B0CC359" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=GI5DN-TQ-0gQ7kNvwGc49E4&amp;_nc_oc=AdoipmZAhXG2qP8m-mcQKQjK4wwnG91Ot3vPoeIscDToYiUMfMa5_2DWBcMTm34emxg&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQLZFdsiY6HjIbTpLBLPo554VWcNa5VxEClrnBia2bJr6Msrub1-7Gcj5NH70db7R6v1BGbEFDfYgg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTFqlgGcVQpK6z43ptZGGoh9KXbfLdbB0ImgQLsBnGfiQ&amp;oe=6B0CC06E" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ohf87Nojt0EQ7kNvwEEkWBq&amp;_nc_oc=AdrOoVwKIR8LLZRR2JyfN4fyB-eepENwbLGyulImD55htcQX2CoUIxJnDVjTt2Ndyik&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQLB3rARRpaThZgUr0Q7bM0P0mIuo0UTRVwZPrwrTiE4yj3sdvw--qo572YTxZ_usAJDKNi62IXMQg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQTWOtiMifT86s7iPgdJ79alxJKG4ohr3cvBcKSFhwzyg&amp;oe=6B0CC3DE" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=n5OR5aIDs34Q7kNvwH7ZJ50&amp;_nc_oc=AdohQ9UB6vipE6o4MadcfJ_Jl7SoLKnC4qwmXXe_ANxxJ3c-wIRCWi5q9HKyPqzvMLY&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQJQZdhXIC-gY_0u06iamklvJETz4H9iWAqS9zKUdgBVPvLRRvFU4Fm6mnNvjWm1vqOwtZoMFeMSpQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTFOoOqjN_VrCScah_wOGed8a8fCz65ASOMmYfVUJN-lA&amp;oe=6B0CD4B5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ih4UpxJVRusQ7kNvwERLSRT&amp;_nc_oc=Adr-992ojF1oZeX05kI-DZQeCQC54KDk9V3Cgnq4C88h530Qy4AwLoJNjml5M7E7LXA&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQIbN53z6pzTegsRXLTwhvr--3qSji3fuhynexSIbnD7xwTSAYB2cwia4xDEeXx5DGJYFV3FwCt5MQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT3XhXUFryLUkV3PRZAHkRd7dtVI-k8pt_ZUjjTvFeR3A&amp;oe=6B0CC036" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7UaQqSrN4NQQ7kNvwHDBRqs&amp;_nc_oc=AdqO7sQ2XcXeDETtZDjGb2LPFcz9qp9ZrsUNIHPAGlgraIqmM9hJUHd1Ila7KLaDz_0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQI09Bqm2CTM5BtN2Ni2d0jJ81S3Z6K6jvxu0r8keK8mHy9oivUkJbXefE-hle0hUxtudCqiQ1Zz-Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRaaDZW_is8-aqhq8yoh-UHc73IzLsCrkfVl-ZpebiYvg&amp;oe=6B0CD066" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kTWGxyC9Wu8Q7kNvwFa5q_L&amp;_nc_oc=AdpVg6Ve5F2RTSoM8AweAah0lhw9xcTkYbPA_OJ0GbKl3e_tkxglX7hZx3htKvepHeI&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQIjEGBsd_GnQ2K3I1an2WGUCI0K3Fww9O3Jc1-oWmDYCFtHB63C81uqW6xJtVgqhnaYURe4YUvu5g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQtViYF2D9cInfR_O19tETQSFA9ctuDWF2kq3KzxnfQSg&amp;oe=6B0CC381" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bjBrf8U-b4cQ7kNvwEY48_j&amp;_nc_oc=Adot7cQBAtbIOH17MwwP2dgBGf5e6TwbgVtgqsR-44CPlYD0BCEmh0d2wQF2tXeM6Qw&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=El39azYas8xJouq24rFlyQ&amp;_nc_tpa=Q5bMBQJYbvNEmmkHnhKrIe_9NuPh1vVcyl9SKfkmGyZ1g273yC26XD89TcHgyliyiwaP_N-OMj_xmfs2UQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTnpexSTi7ok_lR9SHv_cxxkQE5e9hjXC9d09_Nm8Q-YA&amp;oe=6B0CC3DF" alt="" class="t-thumb">
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
.spotify-card:nth-child(1) { z-index: 16; }
.spotify-card:nth-child(2) { z-index: 15; }
.spotify-card:nth-child(3) { z-index: 14; }
.spotify-card:nth-child(4) { z-index: 13; }
.spotify-card:nth-child(5) { z-index: 12; }
.spotify-card:nth-child(6) { z-index: 11; }
.spotify-card:nth-child(7) { z-index: 10; }
.spotify-card:nth-child(8) { z-index: 9; }
.spotify-card:nth-child(9) { z-index: 8; }
.spotify-card:nth-child(10) { z-index: 7; }
.spotify-card:nth-child(11) { z-index: 6; }
.spotify-card:nth-child(12) { z-index: 5; }
.spotify-card:nth-child(13) { z-index: 4; }
.spotify-card:nth-child(14) { z-index: 3; }
.spotify-card:nth-child(15) { z-index: 2; }
.spotify-card:nth-child(16) { z-index: 1; }
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
  <div class="spotify-card" title="It&#x27;s My Life - Bon Jovi">
    <img src="https://i.scdn.co/image/ab67616d0000b2737a231174875d7930de9dad58" alt="It&#x27;s My Life">
    <div class="t-name">It&#x27;s My Life</div>
    <div class="t-artist">Bon Jovi</div>
    <a class="t-open" href="https://open.spotify.com/track/0v1XpBHnsbkCn7iJ9Ucr1l" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Man I Need - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b2739a336bfb6d40bbd90a507417" alt="Man I Need">
    <div class="t-name">Man I Need</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/0mYXRQpTGjaLJt1l9MY4ps" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Can&#x27;t Do Without (My Baby) - Cosmo&#x27;s Midnight">
    <img src="https://i.scdn.co/image/ab67616d0000b273e3439c31982a8c4801044924" alt="Can&#x27;t Do Without (My Baby)">
    <div class="t-name">Can&#x27;t Do Without (My Baby)</div>
    <div class="t-artist">Cosmo&#x27;s Midnight</div>
    <a class="t-open" href="https://open.spotify.com/track/4hG6H7xPvEleJD9QUEqaAS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Light the Way - Leon Bridges">
    <img src="https://i.scdn.co/image/ab67616d0000b273bb0c51f02a25bef0a34f3dd1" alt="Light the Way">
    <div class="t-name">Light the Way</div>
    <div class="t-artist">Leon Bridges</div>
    <a class="t-open" href="https://open.spotify.com/track/3G1hTUddM2diIyYA0yy9kS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="flowers - Nujabes">
    <img src="https://i.scdn.co/image/ab67616d0000b27328e6909795cc2c798fc9e1da" alt="flowers">
    <div class="t-name">flowers</div>
    <div class="t-artist">Nujabes</div>
    <a class="t-open" href="https://open.spotify.com/track/00P7qBMdsxcgS4EnnAhf43" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

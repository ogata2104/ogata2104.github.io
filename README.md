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
    <img src="https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/928332965_18659847517027991_6354731744409032337_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=vcwiPkp2L08Q7kNvwHlhgLx&amp;_nc_oc=AdogH4IwosH82UATvPupMlf0FneGT0X4BbrAhO_B65oKp3-ZdNUQIxndFlMdnotUzEI&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQJf-v2JxDKD-yzwQZ04oS59clFcNvoIO9fmKnyTlwj3jjKpTl9xeneTwsAF4a0kRgE513FdBAgwsg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQV-cya-nfSMkBXSIMnsdS_NPnPa97CzZpOBXMMhtz719Q&amp;oe=6B10B965" alt="" class="t-thumb">
      <div class="t-text">蕎麦にラー油を入れて来た。<br>太麺蕎麦、美味でした。</div>
    </div>
    <div class="t-date">2026-11-25 23:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgKtar6iR7Y" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/930725029_18659712334027991_3881358735396705569_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Hh5jEKgUktMQ7kNvwGHlgBX&amp;_nc_oc=AdpNi2NLaJmsi7Cvsh25bmh5tEvpBwCzbQSiUWCcMfFihrwY2gKRhcPmlfozlekxKyE&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQKujLU7gg_lRXa2sdYXNcreNu6n6DhABssLXKk-dYZyjCQJq9OtCwWDYhWGc_divKmGAiDuq1OuLQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUraCMuUHQIrNcef3EkHxLbDLg1Pcn6BV-r14SLGP2TdA&amp;oe=6B109EB1" alt="" class="t-thumb">
      <div class="t-text">つなぐ練習してます。<br>#reloop <br>#reloopmixtourpro</div>
    </div>
    <div class="t-date">2026-11-25 08:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgJLU0_gVaJ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=vAv6yoU3BVsQ7kNvwFAywz-&amp;_nc_oc=AdoRv3tiiuK1NYrpHa2Jfrdf81FwO52KVM7fZByFPPhL2a8ndKqJkmzVe7wjGeInUig&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQJLaWswI0lgZ2TAFwFbx03eBIuptvNQJQIcSQWT3ARi-2b3esDPkXWHNVURvI4XkUy1Kiog6ayxfw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQXLy9s_2sOI6nX94Qyd4428dZQHkv-ZHReO1vRpL8g32g&amp;oe=6B10C5E1" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ctyofseINYYQ7kNvwGSBQeU&amp;_nc_oc=AdrJPCuAJQx7zZtR5EtKIBybqpHnlsw2dfaNR56NREq0weenWQlSdbNaWQvWPJuzJDc&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQI97gISkkpGGHQiKJ0EavmHrrEn-etIwrqUxmRLAxk6LZAhZXQH84eCVy6PPgMSPBRkkfuZtvPFVg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUc0LNirdVlcDNZ76trXYatKKZ5Hx9I2Z2wWnNzxQJ4Yg&amp;oe=6B10B3C5" alt="" class="t-thumb">
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
    <img src="https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=nMpNUV_KJR8Q7kNvwFraOPg&amp;_nc_oc=Adr6Vweq0wNWAGzeAF7Qui-A7jlZE11xXZbCYIsP0WUhIjSGR5jefw1eklY3qocPjV0&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQL6V0sZmkKjkQ7bemaMMuj6Cugik4wh3h055Ewi7J9qpkLFm1fSeOFiUqeBSa8oz0eYZeA0iUDydQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQWR9XAal9V9sgT8qmWcSRGy3NLocNCcWWfQi3CIT91NSg&amp;oe=6B10C525" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_IMeaw_BXp8Q7kNvwGd0604&amp;_nc_oc=Adpos3mA9RyPL6m-hxs11M3ciirgXtcXcZrNWiMj6ZS9nibh0FpDfxSoEyjJHApj10g&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQICu7gHO6NqCZNsPatB8Y0dC34XdkVl3WRpMCPdkSaSPExKqzbIMGIWfLkQxU5xJlGxxJDCYfTHrw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQWEyIlZkOfhHaktMbwKSOE22gKWTHC1bmfvTmjNMUIcLA&amp;oe=6B109D1D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yC1D5gNSICgQ7kNvwEB8pew&amp;_nc_oc=Adq9KlIDwzcbqMWLZD0uPH3AOV0aVW1ts19p8awGXcLpVsK2HgNjkWRbsh75zLDQVoE&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQJF87lsJRAuWcvcdN_O8FbtA05Aaz6GbahQSmDvZnhudsqH58lbGz9L-vEeIbuhzc-zJRMq6A7ErA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQXD9olIN75BwmsdqWkiOqTxgeT-E18JdkmQZW9jEUMdXw&amp;oe=6B10B7DE" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yqkDjIr5IDwQ7kNvwE-xLE_&amp;_nc_oc=AdpY7DJAtfPdnm6nd4sGyMSMAnfEtI-T8DnKjesRH3ROEAkaIeZhNKk4gUHPFx2-_Lw&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQKnw7RHttBz6451SxzuS5ZDE7b8EmAEEmjtz21AxBOUu6iqj--5TB8YXy_UIBFx38L-c1Y6PQczgg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQWe3yAoP7GW3DG5or-ctAtZqhKv5_t1MmCx4tNRMtckpg&amp;oe=6B10B665" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=P1Hux9cnHNwQ7kNvwHG8XZq&amp;_nc_oc=AdonTjPkVTnP0w1nQEb8pE3krOrwvTF4vqRFatqOwcUCN3EdpufvYsHJoFqht2eEA-g&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQLLvhtsBP0lGTWGGpfB35G_ovcL1t5OscP128OMRdcdXJ0nlJoQoiy3N38NqcaLUJVvJpqIHgte6Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVc679L4Jqu8aS0dz5_V29fjkBEL9zpbCU5NN4JlIgdbQ&amp;oe=6B10B7D9" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XIbr6CcGCyIQ7kNvwFc6mCS&amp;_nc_oc=AdoSakLAiweELcCxP-gOX3fVzXDcAlTAnq0DZpOtOZ6r0Ez4-kVS7Rrq5aOKdwuOQqI&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQLL9bL0e5dn-LIMKTR8B9Fn2UyNbfwC8GYjvctBKZXr3Sc0OqyATe1d77wQpclBAwWCzpqZywjUrw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUsE5bS3veYOI_BzV1lUXgWf8Pk423DwGz_gpr6w44P6Q&amp;oe=6B10B4EE" alt="" class="t-thumb">
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
    <img src="https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=LYY3T0QmxawQ7kNvwH0X93R&amp;_nc_oc=AdqTdbuXpRRQZfY5BSTbeRJfOyMebrr4BT8_KsOMA2Ngul_52e9P4niAyqLCee5f4js&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQJKwVkK9YfRoKJqXpdA3y5jcCz4zfL1zTiG7pEtk6benHATNXJApnLzqz1uc4MF0v8kBOCEpBs1YA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQWrxBfC0QM3XrQ4Zb3WyG6BuGUnsL2KjS41dxtq-twF0w&amp;oe=6B10B85E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=a6HG3iccTyIQ7kNvwHj49r-&amp;_nc_oc=Adphq85rMr5KHnzo0FN4slSMcZAxmdMvlImeynSr1x0z-GHlO7HUtTLsBriK8GPD9wE&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQIm8hqbaigXgXpL9O3hVYi8KMeV3yqsgL4iDiAgpsX_697HJQor_GweYx7PhA3WnvE5NBi2BFVcPw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUXC9-F25U8kNs3Xb9rtMRU4gNT3Q0Mp5-LmOwkbfoIRw&amp;oe=6B10C935" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=VjcUF1OXEjkQ7kNvwHlOqaA&amp;_nc_oc=AdoWHOSD38tgqAZSuzKrcjt-j0qJxEmBcKqdNzB90Mh1p_QVvgn7hXBRNdtaWl96Rds&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQKpFuWE_lhhE3KRNlMBiyej_LMWSYKIiObS30LPQNmKZSAd0UK54UwMk-t9p9fcBLw1uXqdvfCOSg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUMFnRrL0-M1WRe12r-YVxibEJhLTHPovw-DHuMSR75Aw&amp;oe=6B10B4B6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-lgpdjGyb4oQ7kNvwELxIew&amp;_nc_oc=AdqxUq3AdyNzGAgcvnkYO2A6rG54fw5my4UR1_acZ8uWxz6xZybgXqbR0fVgfCyfZr8&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQLRgazplelqvlo0g6kAoXiPSGtB6xfd_VtYCj36k6s9UKZdBTR7d1FhxqWbEgEY09AedbV0QvNe6A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVZCCqF0Ss9ybVSgCXhfEWGzWsRVLsTdH_c7USYjtnaPg&amp;oe=6B10C4E6" alt="" class="t-thumb">
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
    <img src="https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rd6P4FzUPjUQ7kNvwH9R5lb&amp;_nc_oc=AdrxshZemp0-iDaF-q6efTjbswpmkIxTZ-VqiMP817C3UMqBrPokLEjLtvy2vknvuBA&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQKtyv_6X8PJpvsp0rkDOn6mf1N7J5rAoAaKRLg63LVU2fxuMABL8uIzlo1fmcFnvWBfYafP0bovGA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQU3pYsPPK78_9tTEukDWMI_pyX5v2mnAFczbT5OnO5q3A&amp;oe=6B10B801" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=DLL7cwjtz2cQ7kNvwE5tH2l&amp;_nc_oc=Adpewo5--rGEg-EtpleDn-F9jMnWqSgFwWuHNwOFqSa1etolTFJ-W06j33w-JR4GHkM&amp;_nc_zt=23&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=scrFICkFHk9hZo8LDPDhCw&amp;_nc_tpa=Q5bMBQLFkLwet9_Q5J1bI8OByqBoRvKK7CgCVKli-OQiXKdLN3EgU5zoI67l6lhc70SWfIaB8X3vjjpCIQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQV_aRZdJzBJZei7GhfrMNbLX1zPW5z__Lm7EpU1gMXETg&amp;oe=6B10B85F" alt="" class="t-thumb">
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
.spotify-card:nth-child(1) { z-index: 20; }
.spotify-card:nth-child(2) { z-index: 19; }
.spotify-card:nth-child(3) { z-index: 18; }
.spotify-card:nth-child(4) { z-index: 17; }
.spotify-card:nth-child(5) { z-index: 16; }
.spotify-card:nth-child(6) { z-index: 15; }
.spotify-card:nth-child(7) { z-index: 14; }
.spotify-card:nth-child(8) { z-index: 13; }
.spotify-card:nth-child(9) { z-index: 12; }
.spotify-card:nth-child(10) { z-index: 11; }
.spotify-card:nth-child(11) { z-index: 10; }
.spotify-card:nth-child(12) { z-index: 9; }
.spotify-card:nth-child(13) { z-index: 8; }
.spotify-card:nth-child(14) { z-index: 7; }
.spotify-card:nth-child(15) { z-index: 6; }
.spotify-card:nth-child(16) { z-index: 5; }
.spotify-card:nth-child(17) { z-index: 4; }
.spotify-card:nth-child(18) { z-index: 3; }
.spotify-card:nth-child(19) { z-index: 2; }
.spotify-card:nth-child(20) { z-index: 1; }
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
  <div class="spotify-card" title="Jingle Bells - Frank Sinatra">
    <img src="https://i.scdn.co/image/ab67616d0000b273292a3767391b5767f95e708f" alt="Jingle Bells">
    <div class="t-name">Jingle Bells</div>
    <div class="t-artist">Frank Sinatra</div>
    <a class="t-open" href="https://open.spotify.com/track/4KV9bM7a1KDc7b7OakFZic" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="おジャ魔女カーニバル!! - MAHO堂">
    <img src="https://i.scdn.co/image/ab67616d0000b273bcc732761535e35901be9bcc" alt="おジャ魔女カーニバル!!">
    <div class="t-name">おジャ魔女カーニバル!!</div>
    <div class="t-artist">MAHO堂</div>
    <a class="t-open" href="https://open.spotify.com/track/63CbmTcrmJlFYSehryyG48" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b273dce91774924868ea69bd4b87" alt="イケナイ太陽">
    <div class="t-name">イケナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/7emibp3qHeqNNYqZ2Y09xb" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="HOT LIMIT - T.M.Revolution">
    <img src="https://i.scdn.co/image/ab67616d0000b2734b3508f48e05ee385aabbb41" alt="HOT LIMIT">
    <div class="t-name">HOT LIMIT</div>
    <div class="t-artist">T.M.Revolution</div>
    <a class="t-open" href="https://open.spotify.com/track/6CyfYaQZe5ytEDdshdtEeC" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="come again - m-flo">
    <img src="https://i.scdn.co/image/ab67616d0000b27340b9da3f4fc33ebdcae34c84" alt="come again">
    <div class="t-name">come again</div>
    <div class="t-artist">m-flo</div>
    <a class="t-open" href="https://open.spotify.com/track/477CB93mH986mrIheQD0RR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="White Love - SPEED">
    <img src="https://i.scdn.co/image/ab67616d0000b273ba8ba4afd86f69b8e5f3719a" alt="White Love">
    <div class="t-name">White Love</div>
    <div class="t-artist">SPEED</div>
    <a class="t-open" href="https://open.spotify.com/track/5CFnoR8l9QaKoOplzqUL8Q" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Everybody (Backstreet&#x27;s Back) - Radio Edit - Backstreet Boys">
    <img src="https://i.scdn.co/image/ab67616d0000b273530cec85d4543693bd726167" alt="Everybody (Backstreet&#x27;s Back) - Radio Edit">
    <div class="t-name">Everybody (Backstreet&#x27;s Back) - Radio Edit</div>
    <div class="t-artist">Backstreet Boys</div>
    <a class="t-open" href="https://open.spotify.com/track/1di1BEgJYzPvXUuinsYJGP" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dancing Queen - ABBA">
    <img src="https://i.scdn.co/image/ab67616d0000b27370f7a1b35d5165c85b95a0e0" alt="Dancing Queen">
    <div class="t-name">Dancing Queen</div>
    <div class="t-artist">ABBA</div>
    <a class="t-open" href="https://open.spotify.com/track/0GjEhVFGZW8afUYGChu3Rr" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Feather - Nujabes">
    <img src="https://i.scdn.co/image/ab67616d0000b27328e6909795cc2c798fc9e1da" alt="Feather">
    <div class="t-name">Feather</div>
    <div class="t-artist">Nujabes</div>
    <a class="t-open" href="https://open.spotify.com/track/0s1nGaLTeCvTl3if7sllIG" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All Time Low - Jon Bellion">
    <img src="https://i.scdn.co/image/ab67616d0000b273a01c1fddc334c0bd15e4452d" alt="All Time Low">
    <div class="t-name">All Time Low</div>
    <div class="t-artist">Jon Bellion</div>
    <a class="t-open" href="https://open.spotify.com/track/1CnPYaKxTVb4LWOtiGOm0m" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Underdog - Alicia Keys">
    <img src="https://i.scdn.co/image/ab67616d0000b273ae04a4470c76dcc39ee1a932" alt="Underdog">
    <div class="t-name">Underdog</div>
    <div class="t-artist">Alicia Keys</div>
    <a class="t-open" href="https://open.spotify.com/track/68iyjZjS32nQU0k1ITyoXJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Her Favorite Song - Mayer Hawthorne">
    <img src="https://i.scdn.co/image/ab67616d0000b2733f8bb8f846f3eff23924768d" alt="Her Favorite Song">
    <div class="t-name">Her Favorite Song</div>
    <div class="t-artist">Mayer Hawthorne</div>
    <a class="t-open" href="https://open.spotify.com/track/5p50Y4YcBSjQYd481iVrzv" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Baby Don&#x27;t Cry - Lalah Hathaway">
    <img src="https://i.scdn.co/image/ab67616d0000b2737490d41e91de1c15a949680c" alt="Baby Don&#x27;t Cry">
    <div class="t-name">Baby Don&#x27;t Cry</div>
    <div class="t-artist">Lalah Hathaway</div>
    <a class="t-open" href="https://open.spotify.com/track/7bsdoELUKMk8A8S7Sf7Lij" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Stay With Me - Sam Smith">
    <img src="https://i.scdn.co/image/ab67616d0000b273899983dd29114e8b29fb051b" alt="Stay With Me">
    <div class="t-name">Stay With Me</div>
    <div class="t-artist">Sam Smith</div>
    <a class="t-open" href="https://open.spotify.com/track/7876ppTxozBmoZ2EZZqV1i" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="夜明けのスキャット - Saori Yuki">
    <img src="https://i.scdn.co/image/ab67616d0000b273b7076fccb9efbcf254b0e687" alt="夜明けのスキャット">
    <div class="t-name">夜明けのスキャット</div>
    <div class="t-artist">Saori Yuki</div>
    <a class="t-open" href="https://open.spotify.com/track/5EWqdfxKvQxnfE9DTh7mRU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Yeah! 年末 - Bakufu Slump">
    <img src="https://i.scdn.co/image/ab67616d0000b27393994f4f8b1b1bdcaa9e71dc" alt="Yeah! 年末">
    <div class="t-name">Yeah! 年末</div>
    <div class="t-artist">Bakufu Slump</div>
    <a class="t-open" href="https://open.spotify.com/track/5L8NAOTEDbunSVO9sMaNpz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="No Pasa Nada - RHYMESTER">
    <img src="https://i.scdn.co/image/ab67616d0000b273aac506fd6b6aa991ae4357c7" alt="No Pasa Nada">
    <div class="t-name">No Pasa Nada</div>
    <div class="t-artist">RHYMESTER</div>
    <a class="t-open" href="https://open.spotify.com/track/3VmuX2r1qZiPUhu9iDC217" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Reflex - 2010 Remaster - Duran Duran">
    <img src="https://i.scdn.co/image/ab67616d0000b273b66a8f4f3f57f2cc43c88775" alt="The Reflex - 2010 Remaster">
    <div class="t-name">The Reflex - 2010 Remaster</div>
    <div class="t-artist">Duran Duran</div>
    <a class="t-open" href="https://open.spotify.com/track/60StghTk9dzZHrtd470zcp" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Ken Ishii at Circus Nation 2026, playing &quot;Strange Attractor&quot; by Brainstorm - Ken Ishii">
    <img src="https://i.scdn.co/image/ab6742d3000053b73aec90a6cfab3e060d413ba1" alt="Ken Ishii at Circus Nation 2026, playing &quot;Strange Attractor&quot; by Brainstorm">
    <div class="t-name">Ken Ishii at Circus Nation 2026, playing &quot;Strange Attractor&quot; by Brainstorm</div>
    <div class="t-artist">Ken Ishii</div>
    <a class="t-open" href="https://open.spotify.com/track/2s1z92YuCgeXOj6EhaZzh3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="It&#x27;s My Life - Bon Jovi">
    <img src="https://i.scdn.co/image/ab67616d0000b2737a231174875d7930de9dad58" alt="It&#x27;s My Life">
    <div class="t-name">It&#x27;s My Life</div>
    <div class="t-artist">Bon Jovi</div>
    <a class="t-open" href="https://open.spotify.com/track/0v1XpBHnsbkCn7iJ9Ucr1l" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

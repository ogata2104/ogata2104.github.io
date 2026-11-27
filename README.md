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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/928332965_18659847517027991_6354731744409032337_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9-hepWeJn2sQ7kNvwFTcBNf&amp;_nc_oc=AdpYjmpHFMRzuOTSzuqsu1eZvXH1xlcMY_1MyBS4xsxmSUs9X0mi_-eWZmS7vTq-lig&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQI64gJSg7cFROP_Z2K4Hl_XjRnNih7xpYgBketv9SjYhZ6yEBxaUN9ytd6RYvEL9h0iNl_a3uSxyg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVEzfnUhLa4f-iQvSdgWLVciVLcGcqnNAOootmm5-H6SQ&amp;oe=6B0EBF25" alt="" class="t-thumb">
      <div class="t-text">蕎麦にラー油を入れて来た。<br>太麺蕎麦、美味でした。</div>
    </div>
    <div class="t-date">2026-11-25 23:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgKtar6iR7Y" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/930725029_18659712334027991_3881358735396705569_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=YMvXcTE8kQQQ7kNvwEQih-J&amp;_nc_oc=AdomXYgT_SjuV2BCI9rZgCxfiuZ2Jcy40tiQ6q6a-b-Vptr66rPXC7AZ6q70NJGOlAs&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQJ5E7kF6BQ-D7IVk_FAZz15rkNRe_BfpIfhHiK8F7yky8JpfVE4kyQGPejNX9Lvwi97RGLk7sl9PA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVFsuV8-Hr0fKeEe2GLZ6vgsKTfyjELl1qkEZjhDMp4eg&amp;oe=6B0EDCB1" alt="" class="t-thumb">
      <div class="t-text">つなぐ練習してます。<br>#reloop <br>#reloopmixtourpro</div>
    </div>
    <div class="t-date">2026-11-25 08:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgJLU0_gVaJ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=v0DUHwZ1sa4Q7kNvwEO09Pa&amp;_nc_oc=AdpZfFt-gpIfZy01aiXp5q5pIp-XjNiKRBh4aQ2XDrPd9pV4l7a45h_b4dsK-hTkcB0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQKBc3PQvPSWk0jWRJUw0k1phE5lLf1SA3BhZgmPsoUJwFRA-WLzZKR8SY3U50xS3RC-r0EgT5UEnA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQXbyQTUegHr7BnWq1arKjsWGR4OEu6IBwHHHflwvT8N-w&amp;oe=6B0ECBA1" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ctyofseINYYQ7kNvwE89hgP&amp;_nc_oc=AdoNtvcaW08f3JDh0jZOIYlqRAh5AIDiJlQpgWWi2JJQVQM6JJnFi6TBk9X0ZMe7tGI&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQI6deQ9PCQIMw1pOrCvD2NI4Q5nMA5soW6PrfUsE7jjsNh3gmhXyKU3gd9hoCk_H2vS75CbCE6ATA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUCdAD4TS6gjEKOT5oCqWsfMQTLRbp2kBFoC7RfgG6S9Q&amp;oe=6B0EF1C5" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=pYZ_67YSwmIQ7kNvwGskUmc&amp;_nc_oc=AdqGCAcH9s9xdD6FJ8D1-yDDrvwFsfO1AljZtx4pVmDHO8RwgU9YiLUYQvjnU1Rl07k&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQLaE_IgVjKlWOSUHmX4dnnaA5nTv9DsizRjqWN732ywUaR5J1FmsZ4SzqobBPh_m5VT68iFYBBWQw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVdUZtgCPlZiRdB1TPETgCFcFsND0ClBZqS_DmwgqpBzg&amp;oe=6B0ECAE5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9Dr-Cb2GblwQ7kNvwEVuTlP&amp;_nc_oc=AdpFJzKAHwdYkPW40F2Zdz-6hs0V2QIojykn4s42a4q1qx2a21MhufDAh9_D3T-nqu0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQLkyg8SIJ7f7cQmzg8tYO_UK69N7r5TozWH0nhRTLdLefvMyZZyBAnfljc7U8sxZGdpjQiOHOlH_g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQWMHAyeL4CQ4-1RwzcWBIZfoEjTTZtdFbT_4NFSC5BVPg&amp;oe=6B0EDB1D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yC1D5gNSICgQ7kNvwF9f4Wt&amp;_nc_oc=AdqrsaCnstBtiIILV2f4FwfYHgO0DlMdh0x23EaXNV48DkDGH9pf9Vh53eoqs-yK9lQ&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQIVRgOJ_-T9PQhyv3gD05dkz4IlHKb1jOFuVE7L4tZ6HZaUmx_gjgiXaooGHDUjmM2VLrGshzdcFw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQV0cuMgyRutfnbhOFTAJxd9LBjR96Cm9poGAd-HSCyu9Q&amp;oe=6B0EBD9E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S5XyIqwGJqgQ7kNvwHZxWcU&amp;_nc_oc=AdoTkIht32iSgXGXnm2CDj1LJfgrnToDL0vCNxRKIuV8_wTHrJ3-7Uo41QSwvPXPgw8&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQI54hVuarkzBVt3Oanf5Oe4LTTpIQHA_tsRNRf7IcXeQComa8c4R0eiiBze2qQ0rMS8vF-JAsl9RQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVHCyfsnmWEzSbuH9AOu4lvNLBwGPl09oR33iSLJgcwNQ&amp;oe=6B0EBC25" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=P1Hux9cnHNwQ7kNvwGpdz2k&amp;_nc_oc=AdqgxE_cwSiwjT4sAHlaTXVn3LTEmkzbhmOY0kEYgyqCCqTgETah-s2Z-oDLzhbPhj0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQKlI98sCnH-TSDOXD112P34VKBrPuCn8U1e1v75mKbStqb0dtMJteQkyrH1fCExKTqRuQAQSP6rhQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUV_GKQi8aY_sitgQl4Oh-8Lz-QEWM6ptDcFZ_6bOE9eg&amp;oe=6B0EBD99" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XIbr6CcGCyIQ7kNvwE4Mo06&amp;_nc_oc=Adr0oifxW2y2KCMdF7gu4KjvH8ISShnNY08VLgmsjFTI46TwvrDl8szGmlpnLF3QdJs&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQKVIXLFI-b_oduLTAuYvUh9O8qGocHBQWE84QqP0WolCk29LX_HK2jUwvkLiR8JyaI76pGb5koZcQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVSCkSOQR54WifRTksxiZUs4GpGUybWT2JHxhE-e-SV2Q&amp;oe=6B0EBAAE" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ohf87Nojt0EQ7kNvwE9oeKp&amp;_nc_oc=AdqLTFQmIlaa2wmKhRQrUQzRS-E1Dlw3AJxqt0dkIhtbK9Yv8xFmsFTQhKbNXoOkZRU&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQKGuUjd5Ph6o2PLoO_dyyQSVMTqVc5oxLD68nypul-KchjSbG2uJGJEi_DC5wW6C_CgES15LsJE9g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVoLbhpgzHDO4PwRBmkGFv1Vxzn4n2UL2Tw9SoG3EazaA&amp;oe=6B0EBE1E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=n5OR5aIDs34Q7kNvwGWnD7e&amp;_nc_oc=AdoAWu6_RGrD0ErbxFgVcrs8Pa2x-m7zYzoA8G0Ml3j08Q6EDlaUToc70q_6jrY3uBU&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQLxT7mCLCsvVn31W3i_mcUqzN5_BhIywX9kHnmDRGl1LJqyVKTBgb3iwr2vEIMHJi8FXzCeGz8luw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVJ5-8j96WRf2Lfz7TrvlYetJ5JfogWIiR4Puma8CFSQA&amp;oe=6B0ECEF5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=VjcUF1OXEjkQ7kNvwFXIFai&amp;_nc_oc=Adqt8-yr-PBmw7f893gjMFMTIFxXV2Ir6iv1tBNLHSI0TOApOwClu4WEJqSfUHPd2R0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQJTyQzBxgAniNK8KrDtuqHUtsV9S3cKVKt1f62XRZtOyhTibF6zYfAxgFVQtw8wE8bHZEPaSJ4pmQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQXmQNbhGMVfi37Lzpn4yIim93lR7Ogh-10-YKuGNckEKQ&amp;oe=6B0EBA76" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7UaQqSrN4NQQ7kNvwEBmy-I&amp;_nc_oc=Adqx1sK8KRMUs6ICV4dNr6B51eN8ieRJ8LK2yjk7xVtWMauaA5qFHK1Xg9biIrtLtC4&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQIkzrrhXMZmw5NN0Pg_shN8CO6UdVjzg9hfgrISoU5DQbiae49pcuHxW-IX053OyB_zv9AHpKBodQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQUujJruTA3pfyiKKOl_uEQurX3n44kmSxnGwzsxiY9YBw&amp;oe=6B0ECAA6" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rd6P4FzUPjUQ7kNvwH8tun8&amp;_nc_oc=AdprAZwp7A1lqyqhct6SCTteS7uKNsobk62mmFqHdoTqlYWieZ8MnERZZay_s8uwC8I&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQIXw-KPlhtRVY9QNTMg4YjX7r8mIZkhFh9ydj--aGAqRga7hNz_3ZjgxM-a6RZMJIENmE26UeTfyg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQVN0-71eUdfW1JtbmZ1Edo62kk59o__9nV29ObYK2kv5g&amp;oe=6B0EBDC1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=DLL7cwjtz2cQ7kNvwEiXzif&amp;_nc_oc=AdqwlnjQUv7_C9T_cVgIb1gp5tU5IfmAC9eqzSZ0IBSuKDX7VHGKQlOCd-d26vKry48&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=tj9LP4jU7g85Z0dSD5Q8Ug&amp;_nc_tpa=Q5bMBQJymQn1r76D-6ogCpYxlqJ50LSUelxGah_kly9PsdjjDoKg_NvtI0kf3wmh-wjX9k5Ix6UujmnC-g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQXWuDB2rFCSZ1C3qVW-5KeI9de_LtvSDrTPxZMgKqinhg&amp;oe=6B0EBE1F" alt="" class="t-thumb">
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

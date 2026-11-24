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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=v0DUHwZ1sa4Q7kNvwG1BXKj&amp;_nc_oc=AdpJD4W4-f1x0YCXItgf6O7r6aRXJCHIMEqGI21Pge6Km3PIq5hW0pALg9Ua3Ca2Tus&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQJWch2n7khE1ICSCdeMvAZDsgsXxbjrfAmuzdNvZJCrG5W_V22uGEGkiyBzEiafktm3onI4RSDGmg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTWPLXHyga0-VFNkkVekxYKD8pz2wDt4lLpAweHGC6wEg&amp;oe=6B0BB821" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=sxTVw5ABe7EQ7kNvwHDd6Ey&amp;_nc_oc=Adp107XYp9FKeRo6Fk43y2KYGSP4WQ0Wi2YIbFAYidYQcEnienrzFU4u3RM-XTQiw-E&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQJhmA9DL3htYgV6mfyhv29KW10SFoLHAXcSngaoNg9KxDNI_8vKtYIiQ_aLR7WNowuyrM4pNdYcBA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSZZRmmPzZ9H5dTmOPethEwK2NxmHZQ07nHPpbXsh3bDA&amp;oe=6B0BDE45" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=pYZ_67YSwmIQ7kNvwHHMJH_&amp;_nc_oc=AdrB9JwHYF3q5-LEQ0OpjaAP7TYy43bBxw0HA3HN2qMuJhP8FmmHp9jDwxJGDtV0N1k&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQK4Y1HoRVNiznEaSFt4yXSkBNeqeDVXK1mNiQKbzknrPRf1Lv0IFWCKb_ZJ_NbcffzjbTrs7xLN1Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRlneWLj8xOayMZRs3sJLMd8ZrdYrB8xPLV-7h5anxH1A&amp;oe=6B0BB765" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MyScwFbb7WoQ7kNvwFDs2g1&amp;_nc_oc=AdquWr0iD5YogJlm8Tt1SMbV3UZoaoXbb4BLJrhHNtBSQ45R_KG89k44L0tHSom4e3U&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQI-hX1QCWdgqqTjFmnn5X9D5H_Pwv1Dt5qyanA8iSBmGxmQ2yP1V4ucQW2yWU08XejsyHnI2H_7fg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSqhW5mpT_w8xioacRlS9KxPpKdUAfASsO0xjjguTJBjw&amp;oe=6B0BC79D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=5Ai76PbClGcQ7kNvwGtoHr0&amp;_nc_oc=Adr9QOAMtlJ_LEV_MCqYL0ZOfNrHPHbB94KrWAfcRTx08Ef_FQFYBLPOj7UmkS_SkhI&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQK4o2jRjSM3oHjH6ZyVtS_O70zhczxJKIYyMQbFCWowyJPxbpkgEop455Z5FjEURczdDLsFLz3bVg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTDDCMMs-wGJu3UT_eEy0atpY4kVEUfcmtV_Nh1v98Tdg&amp;oe=6B0BE25E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S5XyIqwGJqgQ7kNvwFOdw4i&amp;_nc_oc=Adpy7TnYFIlmzwqGOv4t4trVOBMq-CEks3SDctD-Hd9o09nsP2jZOLHbtCSaoDdTwjs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQLdwyBRrXslRrnjMGxWSIcAszkFCRRIhi7Flb7rwUnG7qhzYW33kkg5Mk8cOovFmprv9YmeJfrm4Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQReb8u6wBRHU9OOZ-BMta55yXMHJ04mnhArT0AbISI8HA&amp;oe=6B0BE0E5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_RPOb-PgzY0Q7kNvwHs1CnZ&amp;_nc_oc=AdoytYo-hfWWAQ0qoi5y2H2ColW1QQXUYjo_V0diJ5ySU6TU1LMK5V9G66MSJ8SaB_s&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQLm7TIWXH0HcYWGMsomRsX5SYwGZdFAwgj8x5KqY--fGjUeRTq1hgvVqdbhgJqbvQf0Fl7gvNfndA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQB27rO7pTSG43eQ1CVkvhJaWh_hie1j2UeDR5bfS-CWw&amp;oe=6B0BE259" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=GI5DN-TQ-0gQ7kNvwHJ88SW&amp;_nc_oc=Adr-7zxpOrUBot2QqNfwNEFrm4D4fN-reMrWxFAzAbUoZ0uddo6WtsusTmtBt8eU3i8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQK9_UubVncsc554uSRTEy_g6v6H5BJj8cjclshuOKqMsiZfIJj6TRCxEerB3SNKWD7xc32h1ZRHdw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRZT2tF3oOVYthUj9BA5D8xS12ztN36posnR0jJadRAXQ&amp;oe=6B0BDF6E" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ohf87Nojt0EQ7kNvwFL6Ell&amp;_nc_oc=Adp4W0d0v118fjCvEKmM8hws4RpeCFL_JMn2mhZesEwKncelIxTYP8mD5SsHKBG0ccc&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQJQS7rmzpM9avMHQz0YOGHmk_q9GMtMABRmSPigh3HvxsRm2UBvA_KA8kHRaTaYR5rhtDWCFk7r5w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTIMdMyRobi-XeMM0Uv9PEOZFE6F-whACNNWD64kZVXoA&amp;oe=6B0BE2DE" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=n5OR5aIDs34Q7kNvwG1kSbz&amp;_nc_oc=Adof9gyPVSo1_uUFmlCxd6Q8BfmbxefLYPK-V9KnEpzxtS0iCAcQlc6Ruz9aPSvhYpU&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQLOQzWb4ooehTq4OlliSQTW5wca5eeZOA_RL1GftrnzgVsXqgyiGzVGAz61YBeG6uPePNkPWebDNw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSxND0gK5gIYoVQhn-5V2HkEvk6HCFLji80VIo59mL5fw&amp;oe=6B0BBB75" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ih4UpxJVRusQ7kNvwEZNDjf&amp;_nc_oc=AdpnIC8Bj8Yy9lGj8AUqtkv_A-NTYfnaARfzyDGAM7F4CasnpTIb8TJnD1GW2cp_ZB8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQLdyKbOaJQOVkuUhjoucGV5pb7vxPHFzhctuA4ExGM_L69evh091GIVuw8PRkthcJDr0rycK_FDRg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSnHpEQxPBWloTaczV1p_u6Bvw3WHliB1Mx3bLsRgoExg&amp;oe=6B0BDF36" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7UaQqSrN4NQQ7kNvwEz8VL7&amp;_nc_oc=AdqcWQ5Q7CcICZcAu0mV76fpk_Sq_MXlGEQXzw3ROxwhmPxAOZ7gxjVtJVqGqqNWFCE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQIUjMDLkdNfO7D9eRQh0xgoFKnMuXfvA9cO_BNZkzfoudfGnDQKlq036uTyoaN_BzA1cDYS9Xz_lQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSzAqCeUz7fbJzEgtRlVo3ARIwpbRXG6g9gOCrepeGeEA&amp;oe=6B0BB726" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kTWGxyC9Wu8Q7kNvwEs2ULo&amp;_nc_oc=AdqcOdrapJ2PE3D_FuZco1RfoTNe8Mi4-odan1TEPTlTsrK6njIGxI5M5GEHuVAvWoM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQI8NtR9a1yadfdVcA9XJlZspevu8JlAuQ6IEUA9wE-8Ef9bwzEHSw5whmJj2ADsIIyZBY0Ke5nR6w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT2uJibdN1C_dwIlidM7X_hilmC3vRE4PADhDTxhp8GIg&amp;oe=6B0BE281" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bjBrf8U-b4cQ7kNvwG6QBAT&amp;_nc_oc=AdobaH0p-MkF28hCMHBolB3tBwXOEwbasSrD221P5tRVO-BcnO29RzRpoEQgiTnJpIo&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQIGeMhLwDaI0VJ_oE4-1FxBnLGF0af_j6RYdK3sbSO8orHWvKMXltbaNl7rrEaJ9UoRB02Q4g_feg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTmQ786WozwM9_EemYRaXj-tvmG4J-ET3x8qa-8-my14A&amp;oe=6B0BE2DF" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9pZmLTqmVVQQ7kNvwE-g0s-&amp;_nc_oc=Adq6BjX3bg_Dx7MU4y8kc00VpAFN0_ymmWpzbtC_Yt-pDWHZm2nnPwvpwNNjsfH-1bE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=WBm9qVRrj4Jgvxq6r1ICZA&amp;_nc_tpa=Q5bMBQKXe-fvcX_4NSBft_9QQaB14nLL6yGQ3pCcTNTZGIWZcCT_AJFsktgVSWC4p-IO8LGvnk1G2iKPKw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRVd5ZOXnBh_lV_WLwSzXpCPHNPecI-fGhOdn7qwmmXfg&amp;oe=6B0BC16A" alt="" class="t-thumb">
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
  <div class="spotify-card" title="8号車との歌 (EUPHORIA Live ver.) - chotokkyu">
    <img src="https://i.scdn.co/image/ab67616d0000b273e8a7264fd908d006d958ecf5" alt="8号車との歌 (EUPHORIA Live ver.)">
    <div class="t-name">8号車との歌 (EUPHORIA Live ver.)</div>
    <div class="t-artist">chotokkyu</div>
    <a class="t-open" href="https://open.spotify.com/track/6FZALqHoOxd0sFQ8uEqsWm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="会いたくて 会いたくて - Kana Nishino">
    <img src="https://i.scdn.co/image/ab67616d0000b27311f9fa546e03d8ce188732b6" alt="会いたくて 会いたくて">
    <div class="t-name">会いたくて 会いたくて</div>
    <div class="t-artist">Kana Nishino</div>
    <a class="t-open" href="https://open.spotify.com/track/5yp5wFjiFMI5TiYKBTUSzs" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="DON-DON-DON - SixTONES">
    <img src="https://i.scdn.co/image/ab67616d0000b273ea16f576af7c77b8a9e6ef7f" alt="DON-DON-DON">
    <div class="t-name">DON-DON-DON</div>
    <div class="t-artist">SixTONES</div>
    <a class="t-open" href="https://open.spotify.com/track/3DlCUluAs9BQsc80kYa0sK" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Hold On - Wilson Phillips">
    <img src="https://i.scdn.co/image/ab67616d0000b2733168e1f416b81862ccc83594" alt="Hold On">
    <div class="t-name">Hold On</div>
    <div class="t-artist">Wilson Phillips</div>
    <a class="t-open" href="https://open.spotify.com/track/4VZDv8sASBS8UruUBGTFdk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Radio Ga Ga - Queen">
    <img src="https://i.scdn.co/image/ab67616d0000b2730b6e29757c37fb90e4587f65" alt="Radio Ga Ga">
    <div class="t-name">Radio Ga Ga</div>
    <div class="t-artist">Queen</div>
    <a class="t-open" href="https://open.spotify.com/track/6N717o83wbmahFGUqkjQj7" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Come On Eileen - Dexys Midnight Runners">
    <img src="https://i.scdn.co/image/ab67616d0000b2738bd8adbdc4727d9080240905" alt="Come On Eileen">
    <div class="t-name">Come On Eileen</div>
    <div class="t-artist">Dexys Midnight Runners</div>
    <a class="t-open" href="https://open.spotify.com/track/3MrWxJaD2AT0W9DjWF64Vm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Winner Takes It All - ABBA">
    <img src="https://i.scdn.co/image/ab67616d0000b2734d08fc99eff4ed52dfce91fa" alt="The Winner Takes It All">
    <div class="t-name">The Winner Takes It All</div>
    <div class="t-artist">ABBA</div>
    <a class="t-open" href="https://open.spotify.com/track/3oEkrIfXfSh9zGnE7eBzSV" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Every Breath You Take - The Police">
    <img src="https://i.scdn.co/image/ab67616d0000b273c8e97cafeb2acb85b21a777e" alt="Every Breath You Take">
    <div class="t-name">Every Breath You Take</div>
    <div class="t-artist">The Police</div>
    <a class="t-open" href="https://open.spotify.com/track/1JSTJqkT5qHq8MDJnJbRE1" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dress Down - Kaoru Akimoto">
    <img src="https://i.scdn.co/image/ab67616d0000b273836acd8a3ec906b36c3e2ccf" alt="Dress Down">
    <div class="t-name">Dress Down</div>
    <div class="t-artist">Kaoru Akimoto</div>
    <a class="t-open" href="https://open.spotify.com/track/4M9Op6UQ36mhtjMBuevRYN" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="う、ふ、ふ、ふ、 - EPO">
    <img src="https://i.scdn.co/image/ab67616d0000b27305e0d091d113e687913e91fb" alt="う、ふ、ふ、ふ、">
    <div class="t-name">う、ふ、ふ、ふ、</div>
    <div class="t-artist">EPO</div>
    <a class="t-open" href="https://open.spotify.com/track/1rUwkDtpGOztJ0j0GUnl0I" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Shake Hip! - Kome Kome Club">
    <img src="https://i.scdn.co/image/ab67616d0000b27373963e04d1828ac296810cee" alt="Shake Hip!">
    <div class="t-name">Shake Hip!</div>
    <div class="t-artist">Kome Kome Club</div>
    <a class="t-open" href="https://open.spotify.com/track/5BwMJMrRRKNpve3huEHTic" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="BE MY BABY - COMPLEX">
    <img src="https://i.scdn.co/image/ab67616d0000b273ea4adb20da4035a8567fde72" alt="BE MY BABY">
    <div class="t-name">BE MY BABY</div>
    <div class="t-artist">COMPLEX</div>
    <a class="t-open" href="https://open.spotify.com/track/2k3kCCpZ9ZGTYMJUSBlENJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="ONLY YOU - BOØWY">
    <img src="https://i.scdn.co/image/ab67616d0000b273039bea39433265a9ba2fe4da" alt="ONLY YOU">
    <div class="t-name">ONLY YOU</div>
    <div class="t-artist">BOØWY</div>
    <a class="t-open" href="https://open.spotify.com/track/6Y0AubW8Kk45RSgy8lgykS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="DOWNTOWN BOY - Yumi Matsutoya">
    <img src="https://i.scdn.co/image/ab67616d0000b27363bcc2884c5430c0465a1e92" alt="DOWNTOWN BOY">
    <div class="t-name">DOWNTOWN BOY</div>
    <div class="t-artist">Yumi Matsutoya</div>
    <a class="t-open" href="https://open.spotify.com/track/7Kk5e6Ipnm2uJQ6IrKbghy" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="街のドルフィン - Kingo Hamada">
    <img src="https://i.scdn.co/image/ab67616d0000b273d175d8963d44efb4cce117ae" alt="街のドルフィン">
    <div class="t-name">街のドルフィン</div>
    <div class="t-artist">Kingo Hamada</div>
    <a class="t-open" href="https://open.spotify.com/track/5w6EvyvomUSWsF430iixmc" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="LOVE SONG - CHAGE and ASKA">
    <img src="https://i.scdn.co/image/ab67616d0000b2734618db4506605db64ee4832a" alt="LOVE SONG">
    <div class="t-name">LOVE SONG</div>
    <div class="t-artist">CHAGE and ASKA</div>
    <a class="t-open" href="https://open.spotify.com/track/7vAcRz6gXkPcklJ53L28vf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="うれしい！たのしい！大好き！ - DREAMS COME TRUE">
    <img src="https://i.scdn.co/image/ab67616d0000b273ccada37f29851e60ff8d3d15" alt="うれしい！たのしい！大好き！">
    <div class="t-name">うれしい！たのしい！大好き！</div>
    <div class="t-artist">DREAMS COME TRUE</div>
    <a class="t-open" href="https://open.spotify.com/track/7tqltihMt6Z2DAFAi6eNzH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="悲しみがとまらない　I CAN&#x27;T STOP THE LONELINESS - Anri">
    <img src="https://i.scdn.co/image/ab67616d0000b273cfd93d36fe2365f9436587d1" alt="悲しみがとまらない　I CAN&#x27;T STOP THE LONELINESS">
    <div class="t-name">悲しみがとまらない　I CAN&#x27;T STOP THE LONELINESS</div>
    <div class="t-artist">Anri</div>
    <a class="t-open" href="https://open.spotify.com/track/3FYDqY5BRtx3IVSaiQZSze" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="B・BLUE - BOØWY">
    <img src="https://i.scdn.co/image/ab67616d0000b273039bea39433265a9ba2fe4da" alt="B・BLUE">
    <div class="t-name">B・BLUE</div>
    <div class="t-artist">BOØWY</div>
    <a class="t-open" href="https://open.spotify.com/track/2jTBjozRvi81DWyJ3B2adJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Faith in This Colour - Alternate Slow Mix; 2010 Remaster - Duran Duran">
    <img src="https://i.scdn.co/image/ab67616d0000b273b66a8f4f3f57f2cc43c88775" alt="Faith in This Colour - Alternate Slow Mix; 2010 Remaster">
    <div class="t-name">Faith in This Colour - Alternate Slow Mix; 2010 Remaster</div>
    <div class="t-artist">Duran Duran</div>
    <a class="t-open" href="https://open.spotify.com/track/2Qp5BTAvzxiVSV7txiHLHs" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

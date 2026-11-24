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
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=2AGUaHy8mhYQ7kNvwGvXFAA&amp;_nc_oc=AdoJg7nLhVcUHFSPil4vfeyGtIf4CRYv0MeLHPlDIqO9qSpOGDkHy1xLqGy8vGh1CeY&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQI82qRs6DApR3sdMshMBHntym1nU_6-78MDR6yZRHe9BC1HRbA6il_6TncPRD5z83ADaopSJxVJSg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTWeEG4WVLSfr6zPdITWdlZQqM4l1bc8JlPT1zZuy8wlQ&amp;oe=6B0A9EE1" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rXuRZJrsXnkQ7kNvwF4HnU4&amp;_nc_oc=AdoVi5hQXy4YaYczTp8fFGEyRd4tYYxipbjnmGwUEqQtRL2mSg7LPgMLe9JC3E2DpjA&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQJHwmTBNt5RbyzgvtNcKZMx6d0_v5wHMWIV2VFXTwr4r83OdIi3hMERCZOrc-yAV2nUdFFSGPBN4w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRMDZX_iXAtKZsvbSRdtIGvU_ngmyFoZRZgN1GPY2bWug&amp;oe=6B0AC505" alt="" class="t-thumb">
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
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=EUp1yF6oXZkQ7kNvwGiWvAB&amp;_nc_oc=AdquxaVq1JkDfBDWa9AR6QF0Ibw1zP7i_Fpu5YeY_i0KMtRKqLFznh2WPvE3L9H4L0M&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQLKZv07SlN4Im5ofz49aF2I-kl19nQ9kS1Y22JTp1MHvIOcDTzXoHxjWQi30Vb6iJA0BJPiSZdDXw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSFs5EZgNaEREwU2HUjmv-GrftUnLg4rriuYznrs52ATw&amp;oe=6B0A9E25" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MyScwFbb7WoQ7kNvwHulVHE&amp;_nc_oc=Adobo1aRgq9izD3OVjc4HP1hZOFALbBLDi6bVXpPSlsUp61JJagWN6ZXgu7OJt-ON3k&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQIvbekq3ddwvgXghTurEFCxV90Yj7O5CiotPXxxB-QmhuZ-A-1nqKHuraDY_EFl19ZzHsqD7hqQeg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTSgKHf8ONpkyLrY1pIya_MsKGleoS7wKUByx9w0l-Oig&amp;oe=6B0AAE5D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=5Ai76PbClGcQ7kNvwGe0vPF&amp;_nc_oc=AdoFeV0QOWFQdO3WFZpFpTSNfx2cb02p4vo6VGK7_RrswJT_OfZRq-eDsqJmiY1Ocmo&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQLBMTj8qhbTSt_-LXUGsw_y6aru5Tj2-M6711imup2c9dxd3eU5JOS4bxlOIcxoBEWU5GHb0xEDuQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSwYR6x_yyFnUPLid0fmezABn3Xn9dHyag5EL9BUu2OHQ&amp;oe=6B0AC91E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=zrvrjio-CpcQ7kNvwH4drau&amp;_nc_oc=Adrsaxft480v9oD8skcJePvtgTGaw9FZhcVqSQk5u-Dc8WKifFacjHiHMYdYLrwhBCE&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQK4UuCgwZYJvE1X2dL6j7_6cCuib3K14rArQ2qzaRw-32tniD6PFHehjbF8iPpJTJprTfUrli7aEA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS0XPkHO5HFhSvdgzJPcPS9YAlhIiIO5WwNxqRUfn1lCg&amp;oe=6B0AC7A5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_RPOb-PgzY0Q7kNvwHXkGsC&amp;_nc_oc=AdqOaGeW-2NTP4Ginm5ek-ZHTGlmRcfZnkFOY01LjC4dQ6KPfshCxpSyDZgxesZ0TuM&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQLVjn92x9KfC6c37SlB1kR671vjUrbZgcgc2--ziATcmfdMVUWEaQq3y1hxnOnb_pdpYKrxC2NwVg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS_zeLGpdQe5CyGzFkR1ZmRiw0OKa0Loe0c8hVJIvSghw&amp;oe=6B0AC919" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=GI5DN-TQ-0gQ7kNvwEK73C9&amp;_nc_oc=AdrZkYJqONGZ9og9FKgjG4lygihTRs_KxFSKpkHAxtlzBSLwMX13dst8OcG87CHjYdk&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQLodImKVwjvlKSG9FX-Q2E0Mx1xD8cjT4k7jdZaW-kBcDUzk38yp7NsiVkRlQ8OBQZijxOZfXhzAA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT7-GChAPodrzUQy_sP_kS7udN5e82FLLnkKzf_dR79FA&amp;oe=6B0AC62E" alt="" class="t-thumb">
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
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hzeG_bN-E-IQ7kNvwE3JAeJ&amp;_nc_oc=Adq-PnVPFv_VjLg-dZOZLV6Q2rstExVTiYlNuaFeFuJAP7YgBesEJ-3xdc_BZMIoQd8&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQKnsJV00dDPGL1awDgPB6yWhe-Ang9KCzTVbSb5EJs77OoOVN4gaxDdBhu76VFygvK9hbfT5PoOag&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTsny1ePQD1QCTuc53FecSruukOIL_x_IPXzQ8lhHxg5Q&amp;oe=6B0AC99E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-Oo3nH0uvZUQ7kNvwGAQOt3&amp;_nc_oc=AdroIfh_JyLunq1LyJK1FDtUnNP_LnNbOXqOL-5E7oGSQI6ApIRskyQXNWK03Ku6fDc&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQJsNZ9p3rHuaa3WFI9D1KJzIg9rZCZ1XxEJitFkwaM9D1Lgpjv6wk6ZMNgp1D31_UNcrVgEy3GJwQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTwOyiTQ7iK01XivyYeXO9Gff--zl2aNCHm3XoJT_rnwg&amp;oe=6B0AA235" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ih4UpxJVRusQ7kNvwFGgJq-&amp;_nc_oc=Adryb_-3i7wfX_25Ijyvg8oCDsb6Ym9BmZihAx-EiqLOhhYOqrpXhAHLs-euVt4zg2k&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQJfQRsiNJgoz7IGulqsmJ2CJSWQuZY0DajJX6dc3r7KJyAYGr_hYWnQkbPO8fF81imOa61ECTsD8w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQqX5SurtisWohyk1GmgpoMwev7Ptsl-t0ih2cfREgwDA&amp;oe=6B0AC5F6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=aByTwbk48ugQ7kNvwEpPsXE&amp;_nc_oc=AdrDnQEb-IPgf0_W8gWMrrO4MEn714EC5m26eeOJvwGjq-waCvXxFg8HVQBpX_rkb4o&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQKmst5VRGZFgxwBMNtC6q36XunwGP2marGDp-pURXIuBm3B3-DvfeDKMpTCDpsrSUh0iu8JtBwf1w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRr6dHIVBH08zgjQGLOXQ5ogrCAkHucUNPNNzRtBbTiSw&amp;oe=6B0A9DE6" alt="" class="t-thumb">
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
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kTWGxyC9Wu8Q7kNvwHNw0VH&amp;_nc_oc=Adq07PbnnoxjtZ9_3S9CW2uCwWeDLJL_vP1EQVCwRkJUrffVWgVT3_fFWqZVUgXlM8c&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQLTHX31lI7R709lPfRzFcuOH68_t79iuSFDVNutE1rJfveRfzt_hF-HjQ3WGSJCeKFc4KY9L10v3A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRsN2xPsvfbQ9fanXEIkEmnbOD-S0QEoxEnUZiT2tpKFA&amp;oe=6B0AC941" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bjBrf8U-b4cQ7kNvwFGzRxD&amp;_nc_oc=AdpOk1yEKK_A374Jq_ROB-AgU87C3FtlgtYSLbeN39JKHi14t7kF5f780nL9i11T_RM&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQIumqCDcGpYHno2uEniHdwMy1OijgZ4WDrYqFOvk9-VRC_QVMYn7TDpXrZkon2SFG2fVpNOPCqLFw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQScfdu4RfmYis2nomyGOeCgX6_RYvctdEzckU77fkr19w&amp;oe=6B0AC99F" alt="" class="t-thumb">
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
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7yJnJhoQJmIQ7kNvwHGGOFy&amp;_nc_oc=AdrFZnX4sxo0T1c40lhD764Z7iqgwQAvX_WZTb-eMopcKxJUY-GlsWx3Ajrd9yR_i7o&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=qMp-VrBFlIk5Tl2YVELahw&amp;_nc_tpa=Q5bMBQL3AZiDLyJLvngFTCJCqrnoD5ntzBro1SmZUKhxtsVTHqJK248ieXcBSifXs-Bc-3sucIihAPaRzg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSloKerZ9imb8fzQfbvYqP6gMyCs8EDHY4NsdO-d0j3zw&amp;oe=6B0AA82A" alt="" class="t-thumb">
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
  <div class="spotify-card" title="愛のままに - BASI">
    <img src="https://i.scdn.co/image/ab67616d0000b273c0fb329a2e1d454c0b4fd06c" alt="愛のままに">
    <div class="t-name">愛のままに</div>
    <div class="t-artist">BASI</div>
    <a class="t-open" href="https://open.spotify.com/track/3Z3ldilmAxJccTZv0GeUfq" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="恋愛レボリューション21 - モーニング娘。">
    <img src="https://i.scdn.co/image/ab67616d0000b273d5ce4b850f55bdd565712794" alt="恋愛レボリューション21">
    <div class="t-name">恋愛レボリューション21</div>
    <div class="t-artist">モーニング娘。</div>
    <a class="t-open" href="https://open.spotify.com/track/1pgmgpwz6iMYzZKAq2nb6n" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Loretta - Ginger Root">
    <img src="https://i.scdn.co/image/ab67616d0000b2738e9876be6bd512f0ff86de9e" alt="Loretta">
    <div class="t-name">Loretta</div>
    <div class="t-artist">Ginger Root</div>
    <a class="t-open" href="https://open.spotify.com/track/4v3icU8NQfjM8uwIz9Ug1h" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Georgy Porgy - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273105ef588df1ef91bfa811f94" alt="Georgy Porgy">
    <div class="t-name">Georgy Porgy</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/5jQcJ2st6yHWhUBjoDoZPH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Waiting for Your Love - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273ebd6d20c0082524244ef83df" alt="Waiting for Your Love">
    <div class="t-name">Waiting for Your Love</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/1CP967dCzbdR2RMejYyPFz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Stop Loving You - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273fc14cd7b4f461e14e57e281c" alt="Stop Loving You">
    <div class="t-name">Stop Loving You</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/73bzcsDjx9FqzqKWcPLMiH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="You&#x27;re the Only Woman - You &amp; I - Ambrosia">
    <img src="https://i.scdn.co/image/ab67616d0000b27306fa32a1ead2c464ec2e2511" alt="You&#x27;re the Only Woman - You &amp; I">
    <div class="t-name">You&#x27;re the Only Woman - You &amp; I</div>
    <div class="t-artist">Ambrosia</div>
    <a class="t-open" href="https://open.spotify.com/track/11qmuUlW5q5diLiVSOlsSF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All I Want for Christmas Is You - Mariah Carey">
    <img src="https://i.scdn.co/image/ab67616d0000b273c0862332847213b151ffab31" alt="All I Want for Christmas Is You">
    <div class="t-name">All I Want for Christmas Is You</div>
    <div class="t-artist">Mariah Carey</div>
    <a class="t-open" href="https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Higher Love - Single Version - Steve Winwood">
    <img src="https://i.scdn.co/image/ab67616d0000b2730225711dc520d382bf0d0b45" alt="Higher Love - Single Version">
    <div class="t-name">Higher Love - Single Version</div>
    <div class="t-artist">Steve Winwood</div>
    <a class="t-open" href="https://open.spotify.com/track/17Ng10tIgnYmAitl0SgT3R" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Peg - Steely Dan">
    <img src="https://i.scdn.co/image/ab67616d0000b273cf39e4261576717ff4737bb6" alt="Peg">
    <div class="t-name">Peg</div>
    <div class="t-artist">Steely Dan</div>
    <a class="t-open" href="https://open.spotify.com/track/5emxp4RqsF6QoAWXW2Afrk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Only You - Ginger Root">
    <img src="https://i.scdn.co/image/ab67616d0000b273eb7e5ecc0e1513ee7a3313a5" alt="Only You">
    <div class="t-name">Only You</div>
    <div class="t-artist">Ginger Root</div>
    <a class="t-open" href="https://open.spotify.com/track/0I50Bs22HqESirPg66IkE2" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="After the Love Is Gone - Airplay">
    <img src="https://i.scdn.co/image/ab67616d0000b27322596cf6aeb42444b32b39be" alt="After the Love Is Gone">
    <div class="t-name">After the Love Is Gone</div>
    <div class="t-artist">Airplay</div>
    <a class="t-open" href="https://open.spotify.com/track/06SfqJmXEWvO9V92l1yzJ6" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Cha Cha Cha - Bruno Mars">
    <img src="https://i.scdn.co/image/ab67616d0000b2733eb8dc748f7efb1470f74395" alt="Cha Cha Cha">
    <div class="t-name">Cha Cha Cha</div>
    <div class="t-artist">Bruno Mars</div>
    <a class="t-open" href="https://open.spotify.com/track/6QletrrmpkUpeJkipX9pgf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Slipped Away - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b27384bb3ed07820b1b818abd2c9" alt="Slipped Away">
    <div class="t-name">Slipped Away</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/5c4Gjttd1A4NQCdyYhEVog" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="No Choice - Fly By Midnight">
    <img src="https://i.scdn.co/image/ab67616d0000b27363f215c50f7ee4746584507a" alt="No Choice">
    <div class="t-name">No Choice</div>
    <div class="t-artist">Fly By Midnight</div>
    <a class="t-open" href="https://open.spotify.com/track/74G0T9Zo5TAJQabpW4gIs3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Star Guitar - The Chemical Brothers">
    <img src="https://i.scdn.co/image/ab67616d0000b273a84e1d8c3a99de8e2e1e6c1a" alt="Star Guitar">
    <div class="t-name">Star Guitar</div>
    <div class="t-artist">The Chemical Brothers</div>
    <a class="t-open" href="https://open.spotify.com/track/19mC6xktT1JyyycK6cQaXA" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Valerie - Steve Winwood">
    <img src="https://i.scdn.co/image/ab67616d0000b273475f52997f4a82ff0740bcc9" alt="Valerie">
    <div class="t-name">Valerie</div>
    <div class="t-artist">Steve Winwood</div>
    <a class="t-open" href="https://open.spotify.com/track/3aAuIvgJGdp4wWd60riWfB" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Da Du Dah - Kokoroko">
    <img src="https://i.scdn.co/image/ab67616d0000b27395ee9ba6913b82d4724ec1f7" alt="Da Du Dah">
    <div class="t-name">Da Du Dah</div>
    <div class="t-artist">Kokoroko</div>
    <a class="t-open" href="https://open.spotify.com/track/0VcvKN17fqyvbznfwypjDB" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Material Lover - from The Devil Wears Prada 2 Original Motion Picture - SIENNA SPIRO">
    <img src="https://i.scdn.co/image/ab67616d0000b27331990a335ce5d02dc159e5c4" alt="Material Lover - from The Devil Wears Prada 2 Original Motion Picture">
    <div class="t-name">Material Lover - from The Devil Wears Prada 2 Original Motion Picture</div>
    <div class="t-artist">SIENNA SPIRO</div>
    <a class="t-open" href="https://open.spotify.com/track/2aQcGu5C6qFcicPsaywTEK" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

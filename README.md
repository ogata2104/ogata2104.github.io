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
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=Vr-1zZHrsHwQ7kNvwFYad3T&amp;_nc_oc=Adrh0R7RgVonZ5j-60rl4eVD9c6_WehI7eGg6XuYe2b57xJKwGtAgGV5cE8XiUQw-Go&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQI-3BgJvIW2z4J8C6gfur4U23RkfAzMOvo-RJXc-e8bhC4jH6mZy9YMmX-HsTyB-HTUbWrLjk3DFQ&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQTOPwu63CMqQC5oXvUOaObLKIzvFVvNiZG2udQ_3nEefA&amp;oe=6B043EE5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=XE0KclzW5xUQ7kNvwEiiJsa&amp;_nc_oc=AdrEueBZ-kJR93PmplE6UMOa8c_WyuHmaCX4LVYSskG02Eea-nKf5FcvJiilF6U0acA&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQI2tDT_czf7b2sqSo7tGbO4ChNgQFfVWDe-l46mcmN0VNBraZBVJ9GCXAsPAooA7aLzCbR-44FDxQ&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQS4rBRTkhl1r_ny9uRtNrp9E3QEmt8R0A5w-dNsMMd3pQ&amp;oe=6B044F1D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=Ok-cGax8GA4Q7kNvwHXMmuR&amp;_nc_oc=AdpTCczhQBHiDpcOottiIANQyMNmjnQhuzE_pdfweA0Lw7lu_lbEjLO3QBq3_W_A5yQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQLQa7_NP8CiB3Iw1ItYqoNK5k5lVJQwXlDwPk2MNL6Ix9cyatgrzQTEnX7pY0lbiRIA9tzJQzztow&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQRA9KOFGPLni1YFU4K25cOI7i337O9mkY6xt_EEEc-7Xw&amp;oe=6B04319E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=T3mNwtpgZfUQ7kNvwHjmxZ7&amp;_nc_oc=AdrHy_ZTh4edyfxqnMU_l8rXufIIs_QpQfSAoH9osiDoGAwSzQIgF824nxt8VoWnZCY&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQLnidgTwPC9JVmSahXBf-qma5VDGv0l335eJs2xvhyKZ1d5SRazjIB6JzMfNFQRoOrffxTdIjILGA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQTTrlYycdzS4WiCjKr9zygciGk-L7OP-eJ0Vhm8RJBIxA&amp;oe=6B043025" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=tLcfJQ91ZUgQ7kNvwFMC2bK&amp;_nc_oc=AdpUNEH0gcF3a913HB5AkeY5yA38_5JVjxQJNf8nzEkUL2vK-19xJrBaprjuIwY6eLQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQLLHeECNcMpNhNGSNATlsn3bllNrTaKTdsbUlUnOMJFSFvgt1yAeCdq8xh4OUw7s72mO2hPCJOLcA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQShOXqb-Nzx6-3b8wD1cGrhz73NUUPy0-fD1M0nQOb3NQ&amp;oe=6B043199" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=rNOKgHzkKs0Q7kNvwFmQfhG&amp;_nc_oc=Adqo1cYf-fLGCpqP9oiZAyGj-syJlzP_AYCevhYtap0zoDmmT8Blft4yVk1Y-PcUwJk&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQL_o1-Ll8sRREHl97XnJj0a8OgQ6vHdSv0ib1MeecTK2DWTEzv7W6QDQWLS1GN-y-d0DKMz7NbhuA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQRfZa2JLud_AuCy90suzqX3hvGJSHTavBO8S-G59hSZ9A&amp;oe=6B042EAE" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=R8nIGnx8dEQQ7kNvwGOfgNr&amp;_nc_oc=AdqQHMjIgzh_vCMcjjCA65ReKVLQB9Sny-ua5gK3OUOkIvJ5g9yAc286wVKIh3Ka9T8&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQI4QjsWUNEbe2jqSIzgXW1av7nB_N4OyEtsToEmfVklMUPLf7SNtJxaLMFoQ8qHN4qp7VTsgEMt-A&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQQ0enwEoibykKkx61R_ZhMafS5_4yt6N2eNjyucQl7nRg&amp;oe=6B04321E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=4HOFkUSIwjUQ7kNvwE3P6vm&amp;_nc_oc=AdrpYQR-NPznYLjoUghAbgidTmvX_qPSuEIJNLBuDfI40bZqjqEMMGCFt0ZnvdjOeh8&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQJeUrnz7OtB27slYer46nfuUpsaKAXnySlX0vFfl1dnBWFE34nr_vhfXeXRHgeq6qnCESNJ33EoOg&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQTLoE7GdrdXkQMEDUMWWzgCOx74l9ZHcZo-2Wya9YlbKg&amp;oe=6B0442F5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=-3Nc8se2CHcQ7kNvwGKwWrO&amp;_nc_oc=Ado50UBkxmSBYDFhgyArQNNv906IdKLIBwCZO35BLGZU2mFh6tNBn8XgbEW24ZLju6I&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQKd-BcMxxS2OC4_DGrhH6dp1o0QFQoZDTLsdKwqFhFPT0eYnz6Do5mWHm2KQoMYNw_I1p7Mc-Z_QA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQT4wJPlOE7rMugqt066ZpaskIB4ecxX_yx1x_RGPhs1Lg&amp;oe=6B042E76" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=yCLLjF1eU3wQ7kNvwGFssNK&amp;_nc_oc=AdoYkt2F7sPopDmoKV7DdTjq5Cxjjt-Lsap8vJ8u42Tavm80I091ngYpL0gQZkRk8Yw&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQJl5sAkVHY3tpDQ6coiTF5Y0J3UIMK3yktLY9ca7wyrQ9ZtBNPpHyYYO100JN8UCVykXNq_gl8ttg&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQTs-hcSjLkPIuPzBVxvqWQYyN8EvYFq9RLcz1se1tlz8w&amp;oe=6B043EA6" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=4-6g72QQ6fsQ7kNvwFni0X0&amp;_nc_oc=AdpzkH3as2uiesA-hv3jatYiBI-cdvGWsUWaTQR3IiiVhM-OCF_66zyJ1aWw5DKtcTU&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQJPb5___hVp5QaZGwy08tyTPckaTc2upz7ZWSYnWNUQYyHHhr1sF-14yhaMd4dJe6kjhA-D8PkNag&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQRc2xot6HHFXCYDx4kEjXXzz-Ql7YznfI7TmV_d7qvmXg&amp;oe=6B0431C1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=2paT3Tc7WCsQ7kNvwFAXftZ&amp;_nc_oc=AdpWDk_ncCLAFqn8bS6uk3epr2T5l5Zptkf4EL6jdtW1-9ikfpkchHH3LLhxnNBkvC8&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQKkZEZ2mIuUMlJrsLvgTo3JM8QdMS2qk9O50_KpKP0gPf6UxeJzMBRUKS74PhDrHgLIkwnHz_p4pg&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQRsO9ssyud513peOFqrXza1qHLMMZOI1z3ao4xeoLF1xw&amp;oe=6B04321F" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=WvhigryquigQ7kNvwG3W4pe&amp;_nc_oc=AdrOGAFKjjvXoQZo6HV79FsDA_ezjfp1W7cz8qmV2YLydKTF_Nvlv5TQNJqTslHBT5c&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQIfDqyhoozoVjs-0k0hxyy8u3XTINPkYp9dIcIMHDuwV2q227c3Q9II0kVE53RJWPpKYxgy0GD5oQ&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQS-CzD4zYTxAayF1qQ3NXqOe9q_zepc4PwsZgI8G8dx3g&amp;oe=6B0448EA" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=VLIgWgptvXEQ7kNvwGWz-a2&amp;_nc_oc=Adquom40tP6-D6V1Qj_zm0bZ5prNxVeLKFz_nsIEvNvnV839glIysFprGMt1PMofskQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQKYavUtMculvFa2AlYbziuum4w2KGlWLbAQQV4mA0TvIMc0l-t_LR00H2tTcPs9eRDvCKVYWQCLAA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQSmxDs82azCGtqOOetoEtuuZNX2gnVRXIdxe9rnsn-tTw&amp;oe=6B043C5C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMiJ9&amp;_nc_ohc=tFaRz8mZovsQ7kNvwHuUu7c&amp;_nc_oc=AdqhV1TuB-cUGjgLoEeSDwXs9tKPaAsb_Irezk-a8i4BDTvULpfEm38h5muS6dGyjq4&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnYrKO7WRUtt7l9oE9LPMg&amp;_nc_tpa=Q5bMBQIVS65gODfXXvTUU0W3CYy116evM0IkeBq_-iBIepJtABiuOI_142B11UIp56SY13k0lBxE6QR8XA&amp;_nc_ct=RQgsPBUKFQIAAAA&amp;oh=00_AQRIeb7MSt90xlhDwdfeZ55QI7cNfcAP51Pqav9tjTlMbQ&amp;oe=6B044C76" alt="" class="t-thumb">
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
  <div class="spotify-card" title="人間なんて - Takuro Yoshida">
    <img src="https://i.scdn.co/image/ab67616d0000b273b4b6cc9a8c40f1a398f89e1c" alt="人間なんて">
    <div class="t-name">人間なんて</div>
    <div class="t-artist">Takuro Yoshida</div>
    <a class="t-open" href="https://open.spotify.com/track/4Dl2WAzB3dsjJ9Br19uXZc" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="TOWN - Minako Yoshida">
    <img src="https://i.scdn.co/image/ab67616d0000b273e5f2d8aff6114400c6939b90" alt="TOWN">
    <div class="t-name">TOWN</div>
    <div class="t-artist">Minako Yoshida</div>
    <a class="t-open" href="https://open.spotify.com/track/13ulUUzvqr34si1Es8qbPS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Lucky To Be Me - Bill Evans">
    <img src="https://i.scdn.co/image/ab67616d0000b27386ae75aef90b01b817da4378" alt="Lucky To Be Me">
    <div class="t-name">Lucky To Be Me</div>
    <div class="t-artist">Bill Evans</div>
    <a class="t-open" href="https://open.spotify.com/track/253MlEWhgOkU3ncefccjMR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Moonlight In Vermont - Stan Getz">
    <img src="https://i.scdn.co/image/ab67616d0000b273cbeddc817202bc83a4272d11" alt="Moonlight In Vermont">
    <div class="t-name">Moonlight In Vermont</div>
    <div class="t-artist">Stan Getz</div>
    <a class="t-open" href="https://open.spotify.com/track/2PoTPPNyExmShy24Mkm9Ii" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Summertime Daydream - Peter Sandberg">
    <img src="https://i.scdn.co/image/ab67616d0000b2731c07868248885ea7d8376039" alt="Summertime Daydream">
    <div class="t-name">Summertime Daydream</div>
    <div class="t-artist">Peter Sandberg</div>
    <a class="t-open" href="https://open.spotify.com/track/21OfFSZFdsghlJ0HEkn4fp" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="When Sunny Gets Blue - McCoy Tyner">
    <img src="https://i.scdn.co/image/ab67616d0000b273e2ad553a9862224408dedf0b" alt="When Sunny Gets Blue">
    <div class="t-name">When Sunny Gets Blue</div>
    <div class="t-artist">McCoy Tyner</div>
    <a class="t-open" href="https://open.spotify.com/track/1J9iVCaEriyoMXpj2XszhU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="サーカスナイト - Tavito Nanao">
    <img src="https://i.scdn.co/image/ab67616d0000b273f3eea33cdd0429a65d438a53" alt="サーカスナイト">
    <div class="t-name">サーカスナイト</div>
    <div class="t-artist">Tavito Nanao</div>
    <a class="t-open" href="https://open.spotify.com/track/1bhF1dbIKLXbVW2QupmvJl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Asleep Talking - Magnus Ferrell">
    <img src="https://i.scdn.co/image/ab67616d0000b2730a0f50681631065bd6c5024a" alt="Asleep Talking">
    <div class="t-name">Asleep Talking</div>
    <div class="t-artist">Magnus Ferrell</div>
    <a class="t-open" href="https://open.spotify.com/track/5dBXBY5CsYxEjC20ewA9EU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Docodemo - JURIANA">
    <img src="https://i.scdn.co/image/ab67616d0000b27387c74e9882dcb48604a98607" alt="Docodemo">
    <div class="t-name">Docodemo</div>
    <div class="t-artist">JURIANA</div>
    <a class="t-open" href="https://open.spotify.com/track/7ayzezVyT0sSvHfgMf5Imk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Gift Of Faith - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b27384bb3ed07820b1b818abd2c9" alt="Gift Of Faith">
    <div class="t-name">Gift Of Faith</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/6h65IMvC7UxaO3JR7KXmAQ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="七里ヶ浜スカイウォーク - ASIAN KUNG-FU GENERATION">
    <img src="https://i.scdn.co/image/ab67616d0000b27374cde1ce458ff27a75997f42" alt="七里ヶ浜スカイウォーク">
    <div class="t-name">七里ヶ浜スカイウォーク</div>
    <div class="t-artist">ASIAN KUNG-FU GENERATION</div>
    <a class="t-open" href="https://open.spotify.com/track/2TtIo7b1IIyjY1TWoC6fRA" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="B・BLUE - BOØWY">
    <img src="https://i.scdn.co/image/ab67616d0000b273039bea39433265a9ba2fe4da" alt="B・BLUE">
    <div class="t-name">B・BLUE</div>
    <div class="t-artist">BOØWY</div>
    <a class="t-open" href="https://open.spotify.com/track/2jTBjozRvi81DWyJ3B2adJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Through Being Cool - DEVO">
    <img src="https://i.scdn.co/image/ab67616d0000b2739a9850a67086009c64dbc369" alt="Through Being Cool">
    <div class="t-name">Through Being Cool</div>
    <div class="t-artist">DEVO</div>
    <a class="t-open" href="https://open.spotify.com/track/7KgabRHMtg4fDaNTutYrDE" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Ride Like the Wind - Christopher Cross">
    <img src="https://i.scdn.co/image/ab67616d0000b27330b2be1b59f27ee3527fe643" alt="Ride Like the Wind">
    <div class="t-name">Ride Like the Wind</div>
    <div class="t-artist">Christopher Cross</div>
    <a class="t-open" href="https://open.spotify.com/track/7gUMShP1l20tC0xf17Zplk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Here Comes The Hammer - MC Hammer">
    <img src="https://i.scdn.co/image/ab67616d0000b273f5e5babccf665ef8c912b190" alt="Here Comes The Hammer">
    <div class="t-name">Here Comes The Hammer</div>
    <div class="t-artist">MC Hammer</div>
    <a class="t-open" href="https://open.spotify.com/track/4yjM4lHNqVOaLwuD2TAThH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Stop Loving You - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273fc14cd7b4f461e14e57e281c" alt="Stop Loving You">
    <div class="t-name">Stop Loving You</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/73bzcsDjx9FqzqKWcPLMiH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Slipped Away - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b27384bb3ed07820b1b818abd2c9" alt="Slipped Away">
    <div class="t-name">Slipped Away</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/5c4Gjttd1A4NQCdyYhEVog" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Moments In Love - The Art Of Noise">
    <img src="https://i.scdn.co/image/ab67616d0000b2738e14857f3ed3aa6e8bd818b3" alt="Moments In Love">
    <div class="t-name">Moments In Love</div>
    <div class="t-artist">The Art Of Noise</div>
    <a class="t-open" href="https://open.spotify.com/track/2bsczk82MWGPmTbe6IWYsa" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Kiss (feat. Tom Jones) - The Art Of Noise">
    <img src="https://i.scdn.co/image/ab67616d0000b273d248c466c04233c09ddc54ac" alt="Kiss (feat. Tom Jones)">
    <div class="t-name">Kiss (feat. Tom Jones)</div>
    <div class="t-artist">The Art Of Noise</div>
    <a class="t-open" href="https://open.spotify.com/track/58UEwo2r86awBBUSMZCP5X" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

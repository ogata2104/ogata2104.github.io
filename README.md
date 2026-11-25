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
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/930725029_18659712334027991_3881358735396705569_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=YMvXcTE8kQQQ7kNvwEDQEvs&amp;_nc_oc=AdrGAPy2REVDqiQqDSDe9ok8eT_TbPc0F-WrhJy3OukuB3fQWXiXro3A99Q7IsUyHt4&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQIL8fLFuGnOLRmwwHvLpfcdvwZekRNlL4bdlM5t5YtjuuufZrE5jsieGf2t0hpQ3qxnMFOxVYIRHA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRhtuqa-f_IfjHF2tNb3eQT_IktElp0oj2bADTj9Eq4SA&amp;oe=6B0C39B1" alt="" class="t-thumb">
      <div class="t-text">つなぐ練習してます。<br>#reloop <br>#reloopmixtourpro</div>
    </div>
    <div class="t-date">2026-11-25 08:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgJLU0_gVaJ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/921302594_18659180587027991_9163568910566789203_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=v0DUHwZ1sa4Q7kNvwGbzlF5&amp;_nc_oc=AdovAu9kN-2n5RevMro_J9n0wk5SjOnQG2wtl6Zb79FxMR-rS2EYIwNICfr3Sd0G2Jc&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQLpw_CnMVtNj8yRkl5NDaWdWvB2lJobzftcFPNAiitxEvYxiRHUnlbeFh1hWKo5WJTYbSyWtwzXKA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTcZi77JQ5BpPgOto6Fs7zZ5Fvhk74m_kxvo46D_nXoEg&amp;oe=6B0C28A1" alt="" class="t-thumb">
      <div class="t-text">池袋から散歩</div>
    </div>
    <div class="t-date">2026-11-23 17:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DgE7ktVgW3F" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=sxTVw5ABe7EQ7kNvwEA_uaH&amp;_nc_oc=Adq4KUsc9jD5IeKix2TlsT6Co5SyKBQJ8XpGoB3hj5yAB1vEgAoOwM6ZFbt3G3c7e_8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQJeAvk-i529Ve6xqqysCheQCD7XbLGHBgAzAZnCTdQJAwRlwJbwalbNLK8kv-B1xD4OiTCk3Bn9Sg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSMuXQdOdXdEV4kIsmqD-LMigVfKvprdf7tRru_2WiEFg&amp;oe=6B0C4EC5" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=pYZ_67YSwmIQ7kNvwG3UkTF&amp;_nc_oc=Ado2SEWIExt54dwbHC6flGeG9S17PQC4-rMLAuvxtFG69LLHVa_eoZOjKasRNAIAiA0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQIHV19i5YF_ORCmreCcq9j7mAQ6-CzVBPt4_3uLHh0mWx0K-S7nfafPtD4FqlBgHdsmRHvZ3ILzTg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRJCxv0_IGVX1G7CN_wZZUCG3e1C1SHb8A0VuARvImmwg&amp;oe=6B0C27E5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MyScwFbb7WoQ7kNvwH2mIZ2&amp;_nc_oc=AdortALpxWPRuKmyVWVQLe39fUOMennd4MYuQXfRK_MvV6JV9hyJH1YFrqQYrWtKEjw&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQKSrUZDERlWh0lLWeC9p8gFWBkzCEzWZsQNzbv5tNzvZ_QkOLqkGHtVMmckMj_28a65PKNYvMRtNg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS0reI0WC-QSofZdjLvz7ro4Y8xOlexM4CZ001jF23D9w&amp;oe=6B0C381D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=5Ai76PbClGcQ7kNvwGnHB9H&amp;_nc_oc=AdobAHVW4b1aXhcDecMMB2HNSpNHphxSw0JHXOZK7SKVmIAxzOj-iUzoMdTnYeEUHaM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQJpPNSu_pPtYv-J0gFKYerb_sFtuY9IyAJTdTOR8iPA5XMOXHskNx9em_zhBVYcKtK7lZyjLN3waA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSEwJPu-81d14COy3vmlZ4fPduNSGLVA77CTbXv_uTsMg&amp;oe=6B0C52DE" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S5XyIqwGJqgQ7kNvwFniLws&amp;_nc_oc=AdoxKNEDyc_UOEUJhZeR4YJUs4MXaBCwVdrD5RyaN2Aj2a6LUD-LKWEhAHPbPlynvw0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQID-cY_iBdFU2AFDzpR4KiCl0iO2cGHpcRl0krzbcukrkOHf5_UcfqyJtmCa2dC-6CQRfoQ2Nb9Tg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTc7oe76DKaKC9JZzED7YpWxEAQAa4_GuKuPo7ltjhlIw&amp;oe=6B0C5165" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_RPOb-PgzY0Q7kNvwGnjbvB&amp;_nc_oc=AdonqJrikTz9WY5n63MJ8UmvMG_v-TDgrmmUALggc9n6Y2Y863nQmNFEmBOxaMN20zw&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQK21KqV3eIp6khpTD6lT_w48koxqXtw7t_wzdS7aU7lpdaUcz5qK7K-NtXpH5EjzXAf5KnKa61O0Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSOAUHq-VMPK5E55jDq7KlZ9ZHaedxsTly5Tiz0BtCC4A&amp;oe=6B0C52D9" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=GI5DN-TQ-0gQ7kNvwHo-Tj_&amp;_nc_oc=AdpCio3GAH3iVbbdLxfNQRExcQAv0c12ZpJgGvqmJU5ATE9fIMvyYK8ZZlbfdGZPhcs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQLDzo2POD7PT8szs6mFjBUHcSPF_gHwRQlOW2KsEO4zAvRbnKGM28yJKITqKhO7AZemoJ2a5QcRLQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRpA-MyMNOMIG4S4GY8GeSX9JFNTqyZMgFBCvyh8nWv7g&amp;oe=6B0C4FEE" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ohf87Nojt0EQ7kNvwHOf6Zy&amp;_nc_oc=AdrTjQ4-WqfDDJ8p4lPFoel06Pj0KC-pgm_kRRFozp6vhTmyA7PLD7f7nwptk0rY9OQ&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQJlWuhoXCbTFDoW13cIe2VzEVK69_06crPSZkzRfNMbYN1qmygeS0-SY9gDeCt7uOyXmY-LOvVrrg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS-1pGs8lAElsrpMOhfAElD7gA1InTMoqp6ArGZjmOisA&amp;oe=6B0C535E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=n5OR5aIDs34Q7kNvwECDALI&amp;_nc_oc=Ado_E4TC11gO_OHV-g6f2SCRdZXjeaPntsnAdIJJp3pDliPVYOzGQEFZ6m5Dr4ddCrs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQI8iJUIxRyr55kPLOqHXHeN1w0-Lyo6GNddzREQqN7Ni8dQsuy_-qxMCIQZfYNsLElgltWmtMz3GA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRmMh0ed8hJJO6VEryCpxUiK9jFpL-oey2U3aL1JEcFLQ&amp;oe=6B0C2BF5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ih4UpxJVRusQ7kNvwGFh0be&amp;_nc_oc=AdoV0ONJwjtF1ORkl-zv_8_Vgcnsythr6vGxAnG-g4iIjH4tFiRmDDnNGdOAHBTVBjA&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQKnHapN0d_M0MArVVBUSzAJV0V8B2-XeHyj-mB8ETSm1ivaBpT-qpb2Y-ZnUZixCWW7phzAQeDhrw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS7vG2xz5oYv8_j737Mb0CvH6n6o16g92UM8PLv6Pa--A&amp;oe=6B0C4FB6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7UaQqSrN4NQQ7kNvwHQz6Z7&amp;_nc_oc=Adp4H9U-F5ozrWDkj8eJQcCB3IJm3RoGGEZHKfqvlOvJi1f-JKKP36rmksagmr38oAE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQIEmqsyI4NXMyXGjD3ezPNRzYHAc4VBkHggQWJ-is3HI5xTRKfR6W42S0KPhmSJiuRJG8IZAyxzWg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR3nsAZJ0tINoaLCzJwmVWqzNTzvVI31-3o-weHn6ZNNw&amp;oe=6B0C27A6" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kTWGxyC9Wu8Q7kNvwEr2Ts0&amp;_nc_oc=Adoe8CohJbLuL3roc61M8xplJbgkBMVFH_Vju1Mjsy1WAL-1d4UhV6xSqoEEz8MgcM0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQIJKWf-wIVLVKjRUQjGrPqwC_Y3XjoeDnJrqQrstEAhE01jsqfxUtM9ciuu1Y0iLWXfeFmT-1GrIw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTIYK42Hf_UcTm0riYleCve6PF5dP7HbQse3WCS7Viavg&amp;oe=6B0C5301" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bjBrf8U-b4cQ7kNvwHsbg2V&amp;_nc_oc=AdqOQ34Yh9FJwKtz-hTg_ISxNgH-SVdxNRAmBgwmTRpkjHxfCGxLBWFyT3y2QCjk5VM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQKc66tNF42QVO6Y_NPft0sNw7p1zdnSJFLBRflKAgQQFmmd6YL9-tT1PYapmVL0o52hcSi2-S3MfQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSX5XR_gLe_oNATS0Ji7G82dkRIp8dwlPNK7DcLeisKRA&amp;oe=6B0C535F" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9pZmLTqmVVQQ7kNvwG5YFEB&amp;_nc_oc=AdoQ5P50I2Nwz47FU0KuIU5quR8mxk5GdquPZ_lprWpkN0Dss1KF-c9fWyXYi4j6hYs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=y8w_vRpZZ5S8qmdW3OrYpw&amp;_nc_tpa=Q5bMBQISyyFLx74gb7KyaBTWAxslnVOyY9_8iZxE6aQ8a7phHFTPK7PEBE4JS9fcb20MPlplXBbg1ip0rg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQYXu2EV1tfHKhBlVoSzzJb5EzwkZdPg8O0jmNlrHis_w&amp;oe=6B0C31EA" alt="" class="t-thumb">
      <div class="t-text">iOSアプリがクラッシュしまくり</div>
    </div>
    <div class="t-date">2026-09-29 10:32</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dd2llzin-Xw" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
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
.spotify-card:nth-child(1) { z-index: 18; }
.spotify-card:nth-child(2) { z-index: 17; }
.spotify-card:nth-child(3) { z-index: 16; }
.spotify-card:nth-child(4) { z-index: 15; }
.spotify-card:nth-child(5) { z-index: 14; }
.spotify-card:nth-child(6) { z-index: 13; }
.spotify-card:nth-child(7) { z-index: 12; }
.spotify-card:nth-child(8) { z-index: 11; }
.spotify-card:nth-child(9) { z-index: 10; }
.spotify-card:nth-child(10) { z-index: 9; }
.spotify-card:nth-child(11) { z-index: 8; }
.spotify-card:nth-child(12) { z-index: 7; }
.spotify-card:nth-child(13) { z-index: 6; }
.spotify-card:nth-child(14) { z-index: 5; }
.spotify-card:nth-child(15) { z-index: 4; }
.spotify-card:nth-child(16) { z-index: 3; }
.spotify-card:nth-child(17) { z-index: 2; }
.spotify-card:nth-child(18) { z-index: 1; }
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
  <div class="spotify-card" title="Emotional Intelligence - Chaos In The CBD">
    <img src="https://i.scdn.co/image/ab67616d0000b2730d8286776d39d70c27bea553" alt="Emotional Intelligence">
    <div class="t-name">Emotional Intelligence</div>
    <div class="t-artist">Chaos In The CBD</div>
    <a class="t-open" href="https://open.spotify.com/track/3yMYs3jJdAPxMgqb0CYZUG" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="APT. - ROSÉ">
    <img src="https://i.scdn.co/image/ab67616d0000b27346085aa1855bd888abc51a5a" alt="APT.">
    <div class="t-name">APT.</div>
    <div class="t-artist">ROSÉ</div>
    <a class="t-open" href="https://open.spotify.com/track/5vNRhkKd0yEAg8suGBpjeY" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Can&#x27;t Do Without (My Baby) - Cosmo&#x27;s Midnight">
    <img src="https://i.scdn.co/image/ab67616d0000b273e3439c31982a8c4801044924" alt="Can&#x27;t Do Without (My Baby)">
    <div class="t-name">Can&#x27;t Do Without (My Baby)</div>
    <div class="t-artist">Cosmo&#x27;s Midnight</div>
    <a class="t-open" href="https://open.spotify.com/track/4hG6H7xPvEleJD9QUEqaAS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="NG - CHANMINA">
    <img src="https://i.scdn.co/image/ab67616d0000b27344a8d5c3ebd2eb029ea2f899" alt="NG">
    <div class="t-name">NG</div>
    <div class="t-artist">CHANMINA</div>
    <a class="t-open" href="https://open.spotify.com/track/12jwNYJiHCSnXwbCmOm8Up" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Light the Way - Leon Bridges">
    <img src="https://i.scdn.co/image/ab67616d0000b273bb0c51f02a25bef0a34f3dd1" alt="Light the Way">
    <div class="t-name">Light the Way</div>
    <div class="t-artist">Leon Bridges</div>
    <a class="t-open" href="https://open.spotify.com/track/3G1hTUddM2diIyYA0yy9kS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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
  <div class="spotify-card" title="flowers - Nujabes">
    <img src="https://i.scdn.co/image/ab67616d0000b27328e6909795cc2c798fc9e1da" alt="flowers">
    <div class="t-name">flowers</div>
    <div class="t-artist">Nujabes</div>
    <a class="t-open" href="https://open.spotify.com/track/00P7qBMdsxcgS4EnnAhf43" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b273dce91774924868ea69bd4b87" alt="イケナイ太陽">
    <div class="t-name">イケナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/7emibp3qHeqNNYqZ2Y09xb" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="電気グルーヴ35周年の歌（試聴用動画） - Denki Groove">
    <img src="https://i.scdn.co/image/ab6742d3000053b7cbcdbec1ee01752b821ae25b" alt="電気グルーヴ35周年の歌（試聴用動画）">
    <div class="t-name">電気グルーヴ35周年の歌（試聴用動画）</div>
    <div class="t-artist">Denki Groove</div>
    <a class="t-open" href="https://open.spotify.com/track/0Bw3vMuXVDyJiTfRCELMov" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Set you Free - Video Edit - Denki Groove">
    <img src="https://i.scdn.co/image/ab6742d3000053b77e0265ca82f943bfda4a879e" alt="Set you Free - Video Edit">
    <div class="t-name">Set you Free - Video Edit</div>
    <div class="t-artist">Denki Groove</div>
    <a class="t-open" href="https://open.spotify.com/track/6zLec4tULnyWfKDmicBtsT" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="N.O. - Denki Groove">
    <img src="https://i.scdn.co/image/ab67616d0000b273cd6dfed922f09a160a9cebbb" alt="N.O.">
    <div class="t-name">N.O.</div>
    <div class="t-artist">Denki Groove</div>
    <a class="t-open" href="https://open.spotify.com/track/78mnqVs0eo5h3gR0E7pKwe" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Ding Dong Express - ZOO">
    <img src="https://i.scdn.co/image/ab67616d0000b273c3cafedc06f726cf858ecb7a" alt="Ding Dong Express">
    <div class="t-name">Ding Dong Express</div>
    <div class="t-artist">ZOO</div>
    <a class="t-open" href="https://open.spotify.com/track/4DTeBZRyYtUGGt8wnO2oMf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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
  <div class="spotify-card" title="Believe - ARASHI">
    <img src="https://i.scdn.co/image/ab67616d0000b273bafb5db86a45e011e1c144bf" alt="Believe">
    <div class="t-name">Believe</div>
    <div class="t-artist">ARASHI</div>
    <a class="t-open" href="https://open.spotify.com/track/2vXuVpGXqIXF6KB2jeWhXI" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Don&#x27;t Stop Believin&#x27; (2022 Remaster) - Journey">
    <img src="https://i.scdn.co/image/ab67616d0000b27323290120a609a65e14cfe018" alt="Don&#x27;t Stop Believin&#x27; (2022 Remaster)">
    <div class="t-name">Don&#x27;t Stop Believin&#x27; (2022 Remaster)</div>
    <div class="t-artist">Journey</div>
    <a class="t-open" href="https://open.spotify.com/track/5RKQ5NdjSh2QzD4MaunT91" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="8号車との歌 (EUPHORIA Live ver.) - chotokkyu">
    <img src="https://i.scdn.co/image/ab67616d0000b273e8a7264fd908d006d958ecf5" alt="8号車との歌 (EUPHORIA Live ver.)">
    <div class="t-name">8号車との歌 (EUPHORIA Live ver.)</div>
    <div class="t-artist">chotokkyu</div>
    <a class="t-open" href="https://open.spotify.com/track/6FZALqHoOxd0sFQ8uEqsWm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

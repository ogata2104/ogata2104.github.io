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
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ukxcv0m3Rj0Q7kNvwHoBd9l&amp;_nc_oc=AdreWd2WrCCphRid7onWRwWieu16FISNFszrogYaQqMEJ9txx9341HkC2ekbLJDdhk0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQI355EA2PBPDDrkr_1QHGRTRmPRqEmxLi0kKLW4XEj7XBy22bGCOi8pa3Am_xjhymDgoTwrHYqZdA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSzX3b_A1R0rFfPM48twKBBAFcwaaoQUwV30e_Vf8USBA&amp;oe=6B012B65" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XE0KclzW5xUQ7kNvwEECpc1&amp;_nc_oc=AdoAU4HCKGryxXpMMR7JUKvehb_Kpv4Y5s-8OMceC8q15a0C2_H78PecBAnfoHldg7Q&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIzOmROjQIQn7Ntl-ZRrlI6d1L5wkwbezrNBzFLy98Fjrtkla5RZiQt4Z83dIwdvM8lbslfGmT3SQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQt3-2u3f05gDiEKqMqi-vi21_zIZLMbUY1wm34geSvsg&amp;oe=6B013B9D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ok-cGax8GA4Q7kNvwF2pf5k&amp;_nc_oc=Ado0U0YF9xZGvuGblOW9pBsUFPAoUN_PpLN6cj_XBgdulx1bFOw2SJDn4xqmPih_sfc&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQKR5BlGyAY7dJ8EpIJsrrW8pSsXirbqXXH76xBfvr3b9BIJ7wh6Be5o7r1cVQ-DAzJ7O96uABGKmg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTJtPL6BSX0xJBXh85WXpKOhV8KN3SM02qWe-lWiP9s9Q&amp;oe=6B011E1E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4P2NmKQR0ZoQ7kNvwGaG9CP&amp;_nc_oc=AdoXycpKiA6rWW7BBCdE01IrlYQTPteckTUHUxc9g6jlNQ-70mx0g15g6tcOhQ6zrUs&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQK0SZIi8oMDZvQMn6eV_MP5pirsqNpS5arZhqAP4UCHK8LWY-yJhXKrf2gQKbCp-wlnhtDq-94AzA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTZ0ru0mocpkHsr0xbWbngxxL70jcjuiUsjYZRRtCD6Tg&amp;oe=6B0154E5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=CiC_u11QyUIQ7kNvwFNCixQ&amp;_nc_oc=Adr7w3blWbRSRxrF5boxqHshb17I6E3nMpS7H1BPCBjdQgeVGZVXr7t1c1dYJBS_Qec&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIbFDqvXU8ySNUAHOVIjkXGfUCm00-RYbOotoV3rS9XOkDTU8p5RSO_gyIvYskHhOGRKBzp8OnJog&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS2pkR8ifLyIuOy-pHzOiLToAPDO0MXVsGxAFsZsRhJ6A&amp;oe=6B011E19" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7YsI9zT8BR0Q7kNvwFFgFsA&amp;_nc_oc=Adp9L7IXGRCRwdCqfm-i2G9ye4BB9noinx_tZ4fKBI14LXHf32IL9WzXv70FXNNXrrc&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIHHkdRyQH7TYIx1nQ_R2cXtFR3U0lxMtcFt_32c4j8aYTOnXpLB-03a9cZWxYX2SVawL632nv6wA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTVXJ7wnFt9juV8YH2vWUrLFaDNHDf1S0Wm4-uKAbgpkQ&amp;oe=6B01536E" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Rz4F_ge4AL8Q7kNvwF7oV_-&amp;_nc_oc=AdpS1XBXLUAgSzl3ZBEewDq9UaYZAZsPJHd1aMT6MpQ-tPa70AID8QPmk6q8ffdKpEQ&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQKcwr0BEYkbcV0Mmyk-wIiaWKnIl_e4UNA7DyYwBSc2WYaiZUGgsCqfIWSTnFs4CGtRU2TsMaHW5Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRpFmxAU6NY3PTe4h1rmqOrkfMO1locV0_FOvP1csg5Ww&amp;oe=6B011E9E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=f3XgNVFnN7EQ7kNvwFjqTaI&amp;_nc_oc=AdoWmeVZHdncw4F04VBGZld4Rgo66QMrp_3kOTESuui0AOAJXEx_SIVOvSWyhXEiJVM&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIsQpqY6aJxKdVNzoNt5Y9hg-EoDIwnTeWuJUqDuZ31qOkHmPg9LoNEjYuMZ4RmU22WZf9W4kHPwg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT2noVbSq2jTlrWWz1bI9gYJgXLWdhx1aT6Dehr58JFRg&amp;oe=6B012F75" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MZ_n9EAlP5AQ7kNvwHQA7Lk&amp;_nc_oc=AdrsZwCTJwFUPenkV6Y5010vFJZxyjfU5puaVwdqhERhUAnCK43iRlPxydHU48OT_Z8&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQKQIw_V4rk-bLWnB_koydHkI8jFAPzK2XfPdSjX_YrA2cHV4eLNJW-8SNDTJSq-3xcfGyWTE9PG2g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQYEGTwf61ZYW4m08sZ2sAF2lkZe1Xu6c11REsO6XbvHw&amp;oe=6B015336" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=6J1dNTaPjzIQ7kNvwFvTusp&amp;_nc_oc=Ado910YdDBu3nzk4bITo-uAxr0nIUH9LG_FSE-IviRqZD6mttKNzCthzSXtzghlXoPo&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIbLCnOdV6nkgp1dJXsmNy4cYj3H8-x_u7_jNhMnp3VTo3D4IZ0ZF78EBfvYDa5AN_w67G6g6pQEQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTGgNtyBCVHVRgAn6CVie8JbkFOc0DyNfXiTrbpuzstzw&amp;oe=6B012B26" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=NNv2uQXsiEAQ7kNvwFG0wWw&amp;_nc_oc=Adr-IjpkURLPMebhgPhWeGn5tvoJ4u_B2mTCm3i3NhxHVZlqIFSlQm1GPXuxahaWpU8&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQJxdETeoWF2W6AJ6T8-Ab5aKEg35aIfhqE0zUXhPkTKE3YNyxa7XEbUcjad2vwcbvrdGZAoq9SG-w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQDwhWKDJC2XvXQv4LvsuyF3-zzcf8SY2_qSC8HUyWmQQ&amp;oe=6B011E41" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Fn--GVOi_7wQ7kNvwHJNsZ7&amp;_nc_oc=Adoge4my90aCE44g5-zrYkXkxjRnBV4IMYMo87lGh93ZrViKfI0MJmctWHH3agWW6mA&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIcBnv3lRdYCc1EupLwaojGKjPU0_saN5v-an1sUjAgCTlhTjJDM_m0YHVkfjS2Wo_xb56EKudy0w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSgjglVximH2NLIkyDwGL_hA8cpdceINEZ-Ln2mWpF5cg&amp;oe=6B011E9F" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-306fbG4B-kQ7kNvwFjBVW4&amp;_nc_oc=Adqkzcyknp7dp7uLiuFdzjIRIiQFTxNM45E0DaJE-aoRkY8sXkMniLXsz7v8g8DEZM8&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQLdw1bSPQj_U2ak_r8erk-2sxXzLU8hjPCvt_JlbOSAgUcevGZPjmWe6ZG82s15GPl8Kh-no3xvaA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSHrwQNIZpU8AaWNfORVWuKryKV3cU8ym761_ricPmnkA&amp;oe=6B01356A" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hGUrTmchzBAQ7kNvwGsbQjz&amp;_nc_oc=Adp89qsCCHOssy_bfeZO4cbAO7xhFXCmiC73sBalChdVWcNqKOOFKlJDzFdjWlI3Uwc&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQIH_NLAng5DUEv-cE6Qp-KrIrqvCFO7rg6HBf2bhCZTCUU21xn2CZSm6dRMyQrn_20tzLp57nQBnQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSbYhMXn3sR6AJGH29icm1ixoX_6TRe_8qZQIhntANm7w&amp;oe=6B0128DC" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=FCZEN9GI0W0Q7kNvwGUsCxA&amp;_nc_oc=AdpJbB4a214zYBaqGUCfaIy77H1xz28caExBmBbDifKFJhoGBO3yvGwUv5XYVLd7z4o&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQJJXJx5CM7h2bxFENq-fo09VTFntt4-VUyWpyMFsZxdrd5-r_RIqw7eLddyZIa5Q4UsK4NxRC9eOg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTGgib5FqiQBHMCxnYgDg2fZUum-7V9e2qL5l4d9RY8sg&amp;oe=6B0138F6" alt="" class="t-thumb">
      <div class="t-text">台風接近中の中、2年ぶりのTGS。<br>始発で行って雨の中2時間半並んだ甲斐あって、…</div>
    </div>
    <div class="t-date">2026-09-20 20:52</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Ddgha79ibTF" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/814470857_17988626214105617_8431201690405807241_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S4ubk_1CmvAQ7kNvwGSuiQi&amp;_nc_oc=AdqsYGAPpWxbF1h7T5rmgTYQ6SBtDGaS-485y5u11TXSucwF7qm_6K3DzUzrdygWQmM&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=M8Y29E4bFgKSFakEDOs3dQ&amp;_nc_tpa=Q5bMBQL7DAijzHAucmjp6m4UOegZ_O0EGjYd_Xy2nn8AlE5HJXpcLmzCRyPwTitG7LrE79I2meV6if4pEQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTQ9QIZ7_WmpFmOWjPbRPpEyYB2hxatQzSfruO34aBFWA&amp;oe=6B015300" alt="" class="t-thumb">
      <div class="t-text">TGS、月曜の最終日、開催中止になってしまった。</div>
    </div>
    <div class="t-date">2026-09-19 16:18</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdddPfhGhKv" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
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
  <div class="spotify-card" title="TOUCH - TOWA TEI">
    <img src="https://i.scdn.co/image/ab67616d0000b273d348c6843f4ae660cdceb5bc" alt="TOUCH">
    <div class="t-name">TOUCH</div>
    <div class="t-artist">TOWA TEI</div>
    <a class="t-open" href="https://open.spotify.com/track/7nz1Skh9UvcfcG1vvoAwyY" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Monsoon - Tokio Hotel">
    <img src="https://i.scdn.co/image/ab67616d0000b2737fb7bd287f256b0f194d39bf" alt="Monsoon">
    <div class="t-name">Monsoon</div>
    <div class="t-artist">Tokio Hotel</div>
    <a class="t-open" href="https://open.spotify.com/track/2pxqMhbQ9xN4epXsaJg6Qe" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Worth It. - RAYE">
    <img src="https://i.scdn.co/image/ab67616d0000b27394e5237ce925531dbb38e75f" alt="Worth It.">
    <div class="t-name">Worth It.</div>
    <div class="t-artist">RAYE</div>
    <a class="t-open" href="https://open.spotify.com/track/7JgNAnCjJvL8hBR1kmCOFF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Cha Cha Cha - Bruno Mars">
    <img src="https://i.scdn.co/image/ab67616d0000b2733eb8dc748f7efb1470f74395" alt="Cha Cha Cha">
    <div class="t-name">Cha Cha Cha</div>
    <div class="t-artist">Bruno Mars</div>
    <a class="t-open" href="https://open.spotify.com/track/6QletrrmpkUpeJkipX9pgf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="So Easy (To Fall In Love) - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b2739a336bfb6d40bbd90a507417" alt="So Easy (To Fall In Love)">
    <div class="t-name">So Easy (To Fall In Love)</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/6sGIMrtIzQjdzNndVxe397" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Gorilla Grip - Greg Shilling">
    <img src="https://i.scdn.co/image/ab67616d0000b273252a6a02526412e1ad455ea3" alt="Gorilla Grip">
    <div class="t-name">Gorilla Grip</div>
    <div class="t-artist">Greg Shilling</div>
    <a class="t-open" href="https://open.spotify.com/track/6bt3Hq6ce61MnDgspiu2Kq" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="A Million Signs - Vividry">
    <img src="https://i.scdn.co/image/ab67616d0000b27334e5930e29b7c0f6a315d8fa" alt="A Million Signs">
    <div class="t-name">A Million Signs</div>
    <div class="t-artist">Vividry</div>
    <a class="t-open" href="https://open.spotify.com/track/3ddEFgl4hnCwC0N7Wa0Vg9" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Weightless - WILSN">
    <img src="https://i.scdn.co/image/ab67616d0000b27357266ff3d126cc69ab9670bc" alt="Weightless">
    <div class="t-name">Weightless</div>
    <div class="t-artist">WILSN</div>
    <a class="t-open" href="https://open.spotify.com/track/3r1aAlW4y7c8nJaXhUxL9Z" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Value - John Splithoff">
    <img src="https://i.scdn.co/image/ab67616d0000b2730dff0e825782b7c546d5a3b7" alt="Value">
    <div class="t-name">Value</div>
    <div class="t-artist">John Splithoff</div>
    <a class="t-open" href="https://open.spotify.com/track/3uGctp8Tbj0ghjvJiozesq" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="New Light - John Mayer">
    <img src="https://i.scdn.co/image/ab67616d0000b273779063301154e835a91a35e0" alt="New Light">
    <div class="t-name">New Light</div>
    <div class="t-artist">John Mayer</div>
    <a class="t-open" href="https://open.spotify.com/track/4T6FWA703h6H7zk1FoSARw" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Reason To Stay - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b273b05c07b076354a0542c92544" alt="Reason To Stay">
    <div class="t-name">Reason To Stay</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/56DxR1jHbX6xlGwZdUuN0v" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Flower Moon - Durand Jones &amp; The Indications">
    <img src="https://i.scdn.co/image/ab67616d0000b27387f2de2e1146cb764c32a69a" alt="Flower Moon">
    <div class="t-name">Flower Moon</div>
    <div class="t-artist">Durand Jones &amp; The Indications</div>
    <a class="t-open" href="https://open.spotify.com/track/16fiL1QD7x9FeoGu8ktxrz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Day &amp; Night - Tonique &amp; Man">
    <img src="https://i.scdn.co/image/ab67616d0000b27315ec492bc23f0c4a5a560a6a" alt="Day &amp; Night">
    <div class="t-name">Day &amp; Night</div>
    <div class="t-artist">Tonique &amp; Man</div>
    <a class="t-open" href="https://open.spotify.com/track/7B2RswVcMbBs70dFyxVGak" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Walk - Mayer Hawthorne">
    <img src="https://i.scdn.co/image/ab67616d0000b27369069f0a19609de8db3e7152" alt="The Walk">
    <div class="t-name">The Walk</div>
    <div class="t-artist">Mayer Hawthorne</div>
    <a class="t-open" href="https://open.spotify.com/track/4nd8rHES5zOlFhwDxDdugW" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Da Du Dah - Kokoroko">
    <img src="https://i.scdn.co/image/ab67616d0000b27395ee9ba6913b82d4724ec1f7" alt="Da Du Dah">
    <div class="t-name">Da Du Dah</div>
    <div class="t-artist">Kokoroko</div>
    <a class="t-open" href="https://open.spotify.com/track/0VcvKN17fqyvbznfwypjDB" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Tom and Jerry - John Mayer">
    <img src="https://i.scdn.co/image/ab67616d0000b2738be2adbc6f0b0d4dc82e2db1" alt="Tom and Jerry">
    <div class="t-name">Tom and Jerry</div>
    <div class="t-artist">John Mayer</div>
    <a class="t-open" href="https://open.spotify.com/track/071WCTT7JXeHRFjMMX5MaT" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Out of Time - The Weeknd">
    <img src="https://i.scdn.co/image/ab67616d0000b2734ab2520c2c77a1d66b9ee21d" alt="Out of Time">
    <div class="t-name">Out of Time</div>
    <div class="t-artist">The Weeknd</div>
    <a class="t-open" href="https://open.spotify.com/track/2SLwbpExuoBDZBpjfefCtV" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="One on One - Wildson">
    <img src="https://i.scdn.co/image/ab67616d0000b273d886a5f7a7f6d6509aec1a2c" alt="One on One">
    <div class="t-name">One on One</div>
    <div class="t-artist">Wildson</div>
    <a class="t-open" href="https://open.spotify.com/track/6dKstPF4kcF1j0oKAAaAET" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Baby Come Back - Player">
    <img src="https://i.scdn.co/image/ab67616d0000b27381eae9a98487ae512df29469" alt="Baby Come Back">
    <div class="t-name">Baby Come Back</div>
    <div class="t-artist">Player</div>
    <a class="t-open" href="https://open.spotify.com/track/41sGGCCoHI2GLV9qadX80A" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Asleep Talking - Magnus Ferrell">
    <img src="https://i.scdn.co/image/ab67616d0000b2730a0f50681631065bd6c5024a" alt="Asleep Talking">
    <div class="t-name">Asleep Talking</div>
    <div class="t-artist">Magnus Ferrell</div>
    <a class="t-open" href="https://open.spotify.com/track/5dBXBY5CsYxEjC20ewA9EU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

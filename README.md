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
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ELCqIXYiPVAQ7kNvwFMF-oD&amp;_nc_oc=AdqVeNTf7kjYJJYOw6kR9HS1opqGuH3WP0PoZHJj_ZkB9smuaHUKOfP3TQd9mJRHXcg&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQKl49ZyAYO4yhvysfY19Kotilss3OPdViwRUmberlHFbFLjUmJWgczlnnrTD__5tmDXtN3D4jpe5g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQStPKprf3yalkBVVhWQIHJe8MbgLAGONGzys0eHyDxdrg&amp;oe=6AFE605D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-Pg6txvdhO0Q7kNvwGUa01L&amp;_nc_oc=AdoJbgVPnaJBiNHxM0gsn5t40WmunMEOaQtBb6cWHqEfGDm87dFMdb7o_WaC_x7C92c&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQIvw1taLJl8alUTfl3t4270BAxHyyiHpKxh-dOx43_OlQzj7U4z5k0X6Hh6ZsOlEt1Rk8VOd01S_w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT4e7_AdoRZHcORyhWrR_Dp3btdJRRaWXVSzIFL9QSzUw&amp;oe=6AFE7B1E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=jeV0wgwRwdsQ7kNvwGAClHM&amp;_nc_oc=AdqaTYoA4a-kYEMWMbXsNdyoapz24rhG3zFlsM_ZZpOCNfxyop0OG5lzsHLjD6gvaFk&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQLx6OOqkonAP3P6Ux94mFKXDpUXSsanue5sAvzbn6ZNxT0NdEMWua2oZ4wFZlho58tx3iVUOpeKkg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSLmO1xWD_q3eZFcYtGGE8IJqxoZrvACIqAavxyW2mHlg&amp;oe=6AFE79A5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=uDVqkeflcJUQ7kNvwH0gZj-&amp;_nc_oc=AdpsCkpuxl76w4n_ZVfMsp61TpzlxCCvWWOGY_Ag6hBGjvDuPger3zF5LCyc3OtyJxY&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQIy-deNqvPW_moq6RzHjMyrQQlFZd2C4D60mbgrZMgW36ij3LTSHeJvNV15qbiIwoOVNik8li_5lA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSosYX2LCtvJqEFqXaDL0ZQ1-D-tu2Ecm4rVWAybvWbkg&amp;oe=6AFE7B19" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7YsI9zT8BR0Q7kNvwEEdM6x&amp;_nc_oc=Adp9i_qGRBJ68T3SkKB8DXnqJjZxjAQQloaANkgKPz5_SSLO2LhA5wOsqzgheC0RbMo&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQLe2EBy0tAQPL_DzeB8NDD5wQuIDOUEGh_7k7ID0aUDkEsr7BgXd_c6hrQ1ar_gPI3cCRSueOnMFg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTDf7RgtwnydG6PFjWzP0oMVOP4Ydj1iYMkm1EENxWcfg&amp;oe=6AFE782E" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=jbi5-m-7AGYQ7kNvwGnLIqj&amp;_nc_oc=AdowT2q_USSiMwR_FA2tx-nw5D-IR2_3WbwIlSxwKnVisI2NkNgQuXBAWQb5frM3LnE&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQICHeyzvtCbwqrBmtQZ524k2Q_LTAhkbsJHSdR5706eWFx11NFAh9UaLX0NLdV75boLfbpmJsGJbw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSO9lBOSiWnp6ZjMW8MgeSHW6uB7PRAn4K60ZC7bE98oQ&amp;oe=6AFE7B9E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=nl8Bgo-KOYMQ7kNvwEFDrsH&amp;_nc_oc=AdpaEN_DVOovlq17Hq_7hut5fQUSWu3Fi7UyKpWzKd3QMtfVSsZTBdAcxOcHl2uXfj4&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQJXmS7i8LrSns3E308AferaxaP0EQd-FH747RhADdPQetnOawAQchivt--sMybtKL0f-AxcjNTuEA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTyT0j5oEmhVfysSPUHRMtYSaebwBpIfXHXk2CF5yhDvg&amp;oe=6AFE5435" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MZ_n9EAlP5AQ7kNvwG86DUn&amp;_nc_oc=Ado2gHwbuINSdaOVibW_09Y0MYb7O7IK8aMzRIP1SKt009JiBaRGmYcEFY5kvsbIG_g&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQK6PzH4w_0HCdIFL8dNcq5PYQPHhVILo7Q6NzBR1oGbydJR1i03IA0Xttn4kaz4dxRa_0tQaB1VNQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSz0ZFr4SsFIrFB3DJShXjMnGCR_7uXyKmoH-KaLO8sNQ&amp;oe=6AFE77F6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=iO1cFkl3V3sQ7kNvwH5nZUf&amp;_nc_oc=AdpLqZrk9vWoMPH7b7Gudyw6nkq_cX5eg--Ou6tXrFDalHzPoGAsYOyMGgIpS1pqlWw&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQKFFAT0fM70tcTCYp_Ijm61_8t2Rubsqllg0JLIWdcsFvHEJVLA4X1KDbOoxzbOo4Ls9LYQkmJMRQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT1QXezTdABsCE-aZzn39iaOWeGG98tvppurgyheVTpCw&amp;oe=6AFE4FE6" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=NNv2uQXsiEAQ7kNvwET4RX7&amp;_nc_oc=Ado2yFfVebe7zGCRuNK-CoNnoxQpU3MGQz86CjXKfJaLM6ijTQXMbDJw0KoNTqXFkqw&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQJYtgqymWy5t2fD5aBvWrd7e14DavEoGjsXc-HX03GR90w6jKaRO9XTIXWvd-wQvGC8yJ7EIFMOgw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT9Z0ZKux4L38KPzO43rOk6s5b6-SmEiSClz_ZYeU0yKw&amp;oe=6AFE7B41" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Fn--GVOi_7wQ7kNvwH3qaTX&amp;_nc_oc=AdoZjuqQpl3Wvfl9Zxw1Hd765wv_38ulC2psapQ4s1Vn8R7Wj_G55TzcApQKhSjeHpA&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQI6K1KG8YUa3ligLzddYpESP3CAjo1tTMPL1iaoxleXTQgHKk1Fzl4bw9bvUq5eYvDdFxGFZscSgg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT4VoMWXhXa8CkBktB2rARK-knlNR7llF2-Y-Dm8vPhyg&amp;oe=6AFE7B9F" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=b3UH0DqjbzAQ7kNvwFQ8tZh&amp;_nc_oc=AdqiCUeyvDSlws1m8c2uSjrFX1snGbErhp81LXvmKCXKrSvkz_GIu1UiRnNse8hlmAY&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQIP-oCIEbB2tvCvLnEc2mZoHT2q7MMr9anxeWnURU8II8DLXIIaFsRTG1I_3iFKaBF-iij7-ZcdFg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSfqaPzF7rNCtb_hhXUxL3CmzJELftSQHKHrcuBFmAc5Q&amp;oe=6AFE5A2A" alt="" class="t-thumb">
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
    <img src="https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hGUrTmchzBAQ7kNvwECKEYQ&amp;_nc_oc=Ado9W2O376lkeTLXTUumodq4Y1ts6zJmB0yg3OBJvnUkL3ANaVy-AACOp4fkECMvDZ0&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQICMisdbq_IYTkoUWW3rSRefDXtxn-eSne_bUZ2csSUoMF_OsRV3b6k-oCFCSJwjBdYVDopjcfCFw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSLe9s_dgIMN8-24RV6FaO1v8KhZCV7c0gteuW8axHSPw&amp;oe=6AFE4D9C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-dfw6-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=FCZEN9GI0W0Q7kNvwGnzDh2&amp;_nc_oc=AdrkIyl-zrnnxMtnQo2-3xhVDPY86GwYBlw4karXt1KGMI9Osr_JZF3JlzLdhjjTAmA&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw6-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQIVNo0XNv05tTMqpLWv87oXQsgt0Sn_1zS7LFYLfI26Dp6bhUwGASAhg4H9Cx2qpSkie3nVrOADxw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSVxsHNjaNKYx9yWW3ObjV6XiCxMfdhzIW7iuxARnJcnw&amp;oe=6AFE5DB6" alt="" class="t-thumb">
      <div class="t-text">台風接近中の中、2年ぶりのTGS。<br>始発で行って雨の中2時間半並んだ甲斐あって、…</div>
    </div>
    <div class="t-date">2026-09-20 20:52</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Ddgha79ibTF" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/814470857_17988626214105617_8431201690405807241_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=S4ubk_1CmvAQ7kNvwGjqcCx&amp;_nc_oc=Adq6Mep-7dBKrV3x3oyre8-XlylTOKy1hW2wWVV8fr_ZaCRif0-nNscrB2NNoRUgbz0&amp;_nc_zt=23&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=XyWocCakLPR29MWZO9_WJA&amp;_nc_tpa=Q5bMBQIpILJ-U6mFHQjMtOy-_GnZtPiKbPd-zuB1lR9L-SG2Cql2TgpMs6daWMj8nAeJJrihLDKkrg_H1g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTNpOH0zL3lpThI_JEil0ZdkxyyaXE_VtdsRgLLRca6Vw&amp;oe=6AFE77C0" alt="" class="t-thumb">
      <div class="t-text">TGS、月曜の最終日、開催中止になってしまった。</div>
    </div>
    <div class="t-date">2026-09-19 16:18</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdddPfhGhKv" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text t-text-long">とにかく各登場人物の「顔」に圧倒されます。今年の個人的顔映画オブザイヤーです。こんな凄い映画がなぜ都内で3館、全国でも9館でしか上映されないのか？この映画を広く公開されると何が不都合がある人でもいるのかな？などとメタな考察もしてみたり。音と…</div>
    </div>
    <div class="t-date">2026-09-17 12:08</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdX3D8Rmjnr" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
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
.spotify-card:nth-child(1) { z-index: 17; }
.spotify-card:nth-child(2) { z-index: 16; }
.spotify-card:nth-child(3) { z-index: 15; }
.spotify-card:nth-child(4) { z-index: 14; }
.spotify-card:nth-child(5) { z-index: 13; }
.spotify-card:nth-child(6) { z-index: 12; }
.spotify-card:nth-child(7) { z-index: 11; }
.spotify-card:nth-child(8) { z-index: 10; }
.spotify-card:nth-child(9) { z-index: 9; }
.spotify-card:nth-child(10) { z-index: 8; }
.spotify-card:nth-child(11) { z-index: 7; }
.spotify-card:nth-child(12) { z-index: 6; }
.spotify-card:nth-child(13) { z-index: 5; }
.spotify-card:nth-child(14) { z-index: 4; }
.spotify-card:nth-child(15) { z-index: 3; }
.spotify-card:nth-child(16) { z-index: 2; }
.spotify-card:nth-child(17) { z-index: 1; }
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
  <div class="spotify-card" title="ファンファーレがきこえる - Base Ball Bear">
    <img src="https://i.scdn.co/image/ab67616d0000b2736713542f83aa31b91a5ffb91" alt="ファンファーレがきこえる">
    <div class="t-name">ファンファーレがきこえる</div>
    <div class="t-artist">Base Ball Bear</div>
    <a class="t-open" href="https://open.spotify.com/track/7nHQr8zBVrZio8CgjVvSk3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Don&#x27;t Speak - Loaded Honey">
    <img src="https://i.scdn.co/image/ab67616d0000b2738e515a0c788f14697d9c6faa" alt="Don&#x27;t Speak">
    <div class="t-name">Don&#x27;t Speak</div>
    <div class="t-artist">Loaded Honey</div>
    <a class="t-open" href="https://open.spotify.com/track/2sKjOX72UX1HiCDhI2HdlR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Just The Way You Are - Milky">
    <img src="https://i.scdn.co/image/ab67616d0000b2735054a99f9ce5b356db8d5852" alt="Just The Way You Are">
    <div class="t-name">Just The Way You Are</div>
    <div class="t-artist">Milky</div>
    <a class="t-open" href="https://open.spotify.com/track/7K3Lc3TfSR14aTOjIH7TUj" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Man I Need - Olivia Dean">
    <img src="https://i.scdn.co/image/ab67616d0000b273e3d69e17dde129037a1f09e2" alt="Man I Need">
    <div class="t-name">Man I Need</div>
    <div class="t-artist">Olivia Dean</div>
    <a class="t-open" href="https://open.spotify.com/track/1qbmS6ep2hbBRaEZFpn7BX" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Last Train to London - Rikas">
    <img src="https://i.scdn.co/image/ab67616d0000b2731a61a0637f0d90538a950303" alt="Last Train to London">
    <div class="t-name">Last Train to London</div>
    <div class="t-artist">Rikas</div>
    <a class="t-open" href="https://open.spotify.com/track/5fewYZz1bCsj72vjSwSxzq" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Set Adrift On Memory Bliss - P.M. Dawn">
    <img src="https://i.scdn.co/image/ab67616d0000b2735423456a99eaf4218893d20a" alt="Set Adrift On Memory Bliss">
    <div class="t-name">Set Adrift On Memory Bliss</div>
    <div class="t-artist">P.M. Dawn</div>
    <a class="t-open" href="https://open.spotify.com/track/7vo0ILIm1He4wo30ikYBHh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Walk - Mayer Hawthorne">
    <img src="https://i.scdn.co/image/ab67616d0000b27369069f0a19609de8db3e7152" alt="The Walk">
    <div class="t-name">The Walk</div>
    <div class="t-artist">Mayer Hawthorne</div>
    <a class="t-open" href="https://open.spotify.com/track/4nd8rHES5zOlFhwDxDdugW" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Moon So High - Remi Wolf">
    <img src="https://i.scdn.co/image/ab67616d0000b273fa3db827a24dd8dbaa1bf245" alt="Moon So High">
    <div class="t-name">Moon So High</div>
    <div class="t-artist">Remi Wolf</div>
    <a class="t-open" href="https://open.spotify.com/track/2aST6n3igBIOhdoCZQcmmX" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Cha Cha Cha - Bruno Mars">
    <img src="https://i.scdn.co/image/ab67616d0000b2733eb8dc748f7efb1470f74395" alt="Cha Cha Cha">
    <div class="t-name">Cha Cha Cha</div>
    <div class="t-artist">Bruno Mars</div>
    <a class="t-open" href="https://open.spotify.com/track/6QletrrmpkUpeJkipX9pgf" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Verano! - Ivana June">
    <img src="https://i.scdn.co/image/ab67616d0000b27349f3bbad1cc5f0627ae87b4e" alt="Verano!">
    <div class="t-name">Verano!</div>
    <div class="t-artist">Ivana June</div>
    <a class="t-open" href="https://open.spotify.com/track/7cN5M5xQgljTIDX65h9EF3" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Asleep Talking - Magnus Ferrell">
    <img src="https://i.scdn.co/image/ab67616d0000b2730a0f50681631065bd6c5024a" alt="Asleep Talking">
    <div class="t-name">Asleep Talking</div>
    <div class="t-artist">Magnus Ferrell</div>
    <a class="t-open" href="https://open.spotify.com/track/5dBXBY5CsYxEjC20ewA9EU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Worth It. - RAYE">
    <img src="https://i.scdn.co/image/ab67616d0000b27394e5237ce925531dbb38e75f" alt="Worth It.">
    <div class="t-name">Worth It.</div>
    <div class="t-artist">RAYE</div>
    <a class="t-open" href="https://open.spotify.com/track/7JgNAnCjJvL8hBR1kmCOFF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Don&#x27;t Walk Away - Jade">
    <img src="https://i.scdn.co/image/ab67616d0000b27329cf454757f957fb528cb18e" alt="Don&#x27;t Walk Away">
    <div class="t-name">Don&#x27;t Walk Away</div>
    <div class="t-artist">Jade</div>
    <a class="t-open" href="https://open.spotify.com/track/7tsRp7QKUBp6hc9bth0h7x" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Every Little Step - Bobby Brown">
    <img src="https://i.scdn.co/image/ab67616d0000b27353cf43170dc29787984cf6b4" alt="Every Little Step">
    <div class="t-name">Every Little Step</div>
    <div class="t-artist">Bobby Brown</div>
    <a class="t-open" href="https://open.spotify.com/track/0s6e7ZafqOAUBDoQYGmxrc" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Live and Learn - Joe Public">
    <img src="https://i.scdn.co/image/ab67616d0000b273233b6404ed87261ad2d8cc36" alt="Live and Learn">
    <div class="t-name">Live and Learn</div>
    <div class="t-artist">Joe Public</div>
    <a class="t-open" href="https://open.spotify.com/track/4eoli5b55cvAkvwP4tB1TF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Right Here - Human Nature Radio Mix - SWV">
    <img src="https://i.scdn.co/image/ab67616d0000b273f56546aac4f5d002c4c3d705" alt="Right Here - Human Nature Radio Mix">
    <div class="t-name">Right Here - Human Nature Radio Mix</div>
    <div class="t-artist">SWV</div>
    <a class="t-open" href="https://open.spotify.com/track/7tUEDtHchueeUJTfEFEhii" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Lost Weekend - Simply Red">
    <img src="https://i.scdn.co/image/ab67616d0000b27317a3d8e105d4f872fc66893d" alt="Lost Weekend">
    <div class="t-name">Lost Weekend</div>
    <div class="t-artist">Simply Red</div>
    <a class="t-open" href="https://open.spotify.com/track/6l0NUzEkcdXQqiC8FCtqlv" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

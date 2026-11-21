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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=EUp1yF6oXZkQ7kNvwFjN-13&amp;_nc_oc=AdpMgzbS7Hn7Qi7-UJ7kRWih8FSseIDKfJqiZMi6N3FyBH6ZcZK2EkLSOIZ5vptEacE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQLCLvAI48Z0g5reT4eHjdAc-wErZAOo4tXbPqZ-htQc0xpQ5rXt3bpHVIFkx1j8oK543UqVVzgoJQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTm3DHOtuzqNPqDbslvZANlkvZVUDqDxwcL5BgOEgO2Lw&amp;oe=6B07C2E5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ieTbCsvd2fMQ7kNvwHu2sqD&amp;_nc_oc=Adrm0bYvTDEs0aYdxWWLpflsGR_fbS004ZUcNhOXPp6iCf5LThmpHWAbIXCIGuudX-k&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQLhojvDdmIs_9zhBF7KqK2M-ibwiY9tSKfN1PqeKH3C3679Li2afaUaIRTu2W8_UaVkLsvtGfIaeQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQHt7f_yqcg8K3-WOG2Davlk43UFPbFU7-P0JXfVVbkYg&amp;oe=6B079ADD" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WtyzJYc2-bgQ7kNvwG2-hGd&amp;_nc_oc=AdpPSNuHKCsj1-hiFJJ1E9x6RJwYwn4HdIWUE5GvrZkVGleOT4cZujKY7BNe9CUDAVU&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQJPKiGNc_2s6yxfRJMZERHuUVG-QJkgpev_-M02kNd_QaBSRYUVjMiPQXqJjzOekMD3luRVSaKSyQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSQWif1e048o2AxsUKbE8aJxCBHxiqPe4Uy8Nnk6Teb-g&amp;oe=6B07B59E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=zrvrjio-CpcQ7kNvwEaH7bT&amp;_nc_oc=Adox_ALN_FMTiNzjF8_2iIS546RVy5Y-GDtms93sx1m4NW0DhZetnsu7Y_p89IYUS4g&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQJcTIMNGesiaE7AD_vztjYk0-Qr19vIf41cVs4GTzHWpZDoja76TMUaZskbDytxv1sMRZptl6tz1w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQS9q7n82mq4MJpcqcxgP2qeYeGYwN3khfJFC2f9553Vw&amp;oe=6B07B425" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9YSLF_Ac-yQQ7kNvwHY9IDp&amp;_nc_oc=AdqimVpCTVaxtDlI0mCVPkjmDTAA1AnDzO7TQ2OERW6q8p2oGPCQCtdKf7O7MznYmCI&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQI41yn9wXqPupp749Mb98TAQQaH7OVmSsrKipari-xKQMwhOHDrjz24YUcZLJa3-qW1XT-hcHQQOg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRs80AlW-OibyZepYEtLFvU6sXRAl5zCFTio2O2ljT_DQ&amp;oe=6B07B599" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=eIqcC5m-AWEQ7kNvwFqXTpi&amp;_nc_oc=Adp33pFG2r4qAnC8PgNqd2GwMzKfPuvR1bo1TDoBI-1I1c3ODNy9bofkB2wKWEpFHX0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQK5UQDFFxiPrp1qvJNhwe2ZCxnG56JyHPbmxFAqr03nfGEf2j4WXcHPQbYWRqBfz5vdW5qmbxY4IQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSGXjD-HG49r71I6Yjy-Df2DIBtEKMZJi3RW-QvSoIvlQ&amp;oe=6B07B2AE" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hzeG_bN-E-IQ7kNvwFsts3-&amp;_nc_oc=Adot41gMRF9xOj8i_i4qP9IsUjxfENAeiVLDho0wtY94AqqOYagPCrI5nWrXTSKW5qk&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQLX5qB-GKOHny0CHIkCKS_KNYLigHrGqTBDJCWSS7xYYdIKH46wMKBIUINHf1zyHWP2iylWlD8XiQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQLQLs5aB-0_iUWJZF0vFXvWbcDoMDhtXwsq40vKHn9BA&amp;oe=6B07B61E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-Oo3nH0uvZUQ7kNvwGu7RbL&amp;_nc_oc=AdqlpeBfPy8ijAV3C8XdwTrQBQ8em0mabHLTRx00VcsLJ3RZhFmm100-tSqar9apjLk&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQI5ykaUh77K786awCNQLyYEYubuiDJtkZbk2rdGJ_xed5XHIbtJdbOCPa1G-oSU13KEbCZd3E2q5Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSLY19kV_jWbNsUlBOKDOFUuRgyL3mZFpBPcoSxjVxSoA&amp;oe=6B07C6F5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kZrOmlk3180Q7kNvwFOvhIP&amp;_nc_oc=Ado5VA1r0lFds3rh8j0jYK1tOyzcEZsh7iM5lWjzZ982N8CXgtQtFZS3QWfPPQ10s5Y&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQKrsyNivLcjtg1PDmkvPgO_a4wpPPSgGklq1ii_KJySfHGzXOUZEiuteg35udf9Kxltudu7Zks1Mg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSgUZoOt_yMXvTCepJ8v4Zu7d1dCC-jMjnnL0wmKkEnJA&amp;oe=6B07B276" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=aByTwbk48ugQ7kNvwF5x37h&amp;_nc_oc=AdpspH99gsckwzu9W6gt5lLM0Bbnvb_ULfLUlqIdr-PzQTFM1vWuFIs5x_kN11-QMCE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQK1B73hFJ0g1w-jhFbGl2FndH6smJ3XK9FYqhh8CqrTcopP7CH1jcUBFYXUoe6eAqEoHiYS0-4QCA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ8Ugjb2vH1xWz3HhlKCvDWETmw2Uwju0t49-zmx55_rA&amp;oe=6B07C2A6" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=BMhmi_2p-LMQ7kNvwHRvNzv&amp;_nc_oc=AdqxKkooDiDJeei2PGswHzMxvDG7EgBjsjUj5rzUTnogvjKnsLF0R2krUxI00dhPAE8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQIilpMDMDic2UCIYp7FWMSdyoRC9pADcO0rGukJwvctw_2P9_LlxZ9F-omtbzJ_j2tYGF3zNcLDVg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRnYkNf5NyKdxVvTVrAqQEhk55j5QYUxCMEL9bZgsU2Sg&amp;oe=6B07B5C1" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=fbRJmrSwkvsQ7kNvwHVQiUH&amp;_nc_oc=Adqh6L1ctG4B21M98SuN19NZ7VJdwr4lUvM2jt4QAcFR0rhXcpFc7meYR4828WefRKQ&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQLxkK3GAb_XintLK0IHqqnh6Mwi5apRPRePeIKUocJHl8o7ggE9DitTysEppIqd2ElCuUf1dlrpZA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTz53ol0S9HqLL-w6L1XgvEZRhMizVtXVPrNS48EsOM_A&amp;oe=6B07B61F" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7yJnJhoQJmIQ7kNvwG7NtFU&amp;_nc_oc=AdpaTF9tvfuENllTFmvdleJgIDvymzpH2O1l3MW0PMVAFTePpG_XsFvGLJISLF_zzJU&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQJuHNI_hGQ02BhQ7CwUMYcs9jOyzcXlYIYiIHLoJwe6fg-4qY6vJ_OzikhKFtKeHIBGt92d_EreJQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQA7EByrim44YkJvPhVolqJV7rC4H35UaB_2OvjjsPFdg&amp;oe=6B0794AA" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_EHfebc1SeIQ7kNvwH5qpSA&amp;_nc_oc=AdqnpNb-Ggt5aYiTfEUCCWBd90hnI-AuIYmlTnJS0HOBnRVXk5P6oTN9cvV78HTkdBw&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQIq6u4UMPD3scd_m0YC6yOjFLPjTFQXl5UqePdS2rKrJchPPwKQH51kBsTEUVGt7taJyOxqO7dGUg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRCy2T6XoRYlixLlKaugwtVCr9ayicnyqkqMNx9NhQEgQ&amp;oe=6B07C05C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7dOZo3JmgeQQ7kNvwHBAvqx&amp;_nc_oc=AdpuVmtS0ccUkAAGmrYhgHR5QjMWOqhaxa7AhKFqTYwN0OV9zDw2iuGL87NV1Y2jQw8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=JIM2V1_HxfEg_r3OpbnUEg&amp;_nc_tpa=Q5bMBQKUj5ZQY5IdXFIz40QnS_GnM5-xew5nBMcHAewQxxCId0Jk4XmctpilCSr9eaNQ28oARuNYvfB5Ug&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQROqQpNAxoGGrNLV-ytPXyxRdtCzu-TbR5jIT6vkvWHuQ&amp;oe=6B079836" alt="" class="t-thumb">
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
  <div class="spotify-card" title="Higher Love - Single Version - Steve Winwood">
    <img src="https://i.scdn.co/image/ab67616d0000b2730225711dc520d382bf0d0b45" alt="Higher Love - Single Version">
    <div class="t-name">Higher Love - Single Version</div>
    <div class="t-artist">Steve Winwood</div>
    <a class="t-open" href="https://open.spotify.com/track/17Ng10tIgnYmAitl0SgT3R" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="What a Fool Believes - The Doobie Brothers">
    <img src="https://i.scdn.co/image/ab67616d0000b273ba6340ac3b1653b6ea0e5da5" alt="What a Fool Believes">
    <div class="t-name">What a Fool Believes</div>
    <div class="t-artist">The Doobie Brothers</div>
    <a class="t-open" href="https://open.spotify.com/track/2yBVeksU2EtrPJbTu4ZslK" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="どON - RIP SLYME">
    <img src="https://i.scdn.co/image/ab67616d0000b273eb8a9e0301b3af3977df375d" alt="どON">
    <div class="t-name">どON</div>
    <div class="t-artist">RIP SLYME</div>
    <a class="t-open" href="https://open.spotify.com/track/6RVVkxX67l3hPtJf3ggO2J" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Livin&#x27; It Up - Bill LaBounty">
    <img src="https://i.scdn.co/image/ab67616d0000b273695e765fc5265f56940bf33b" alt="Livin&#x27; It Up">
    <div class="t-name">Livin&#x27; It Up</div>
    <div class="t-artist">Bill LaBounty</div>
    <a class="t-open" href="https://open.spotify.com/track/0lwHorTzvh8D4pQaWFYqnn" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="99 - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273801ed6b1316f1bbbc41ac3f5" alt="99">
    <div class="t-name">99</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/2R3E4xKmy7lyieBKONkIMT" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Stick to the Status Quo - High School Musical Cast">
    <img src="https://i.scdn.co/image/ab67616d0000b27386ea2533f3bfc5f1f08ab168" alt="Stick to the Status Quo">
    <div class="t-name">Stick to the Status Quo</div>
    <div class="t-artist">High School Musical Cast</div>
    <a class="t-open" href="https://open.spotify.com/track/5aNagthlHAudbDZozQMjYP" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dream Weaver - Gary Wright">
    <img src="https://i.scdn.co/image/ab67616d0000b2730c51c850e900c074c093fce6" alt="Dream Weaver">
    <div class="t-name">Dream Weaver</div>
    <div class="t-artist">Gary Wright</div>
    <a class="t-open" href="https://open.spotify.com/track/74DrA5fFoGSy4xgkZarZtP" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All I Want for Christmas Is You - Mariah Carey">
    <img src="https://i.scdn.co/image/ab67616d0000b273c0862332847213b151ffab31" alt="All I Want for Christmas Is You">
    <div class="t-name">All I Want for Christmas Is You</div>
    <div class="t-artist">Mariah Carey</div>
    <a class="t-open" href="https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Last Christmas - Wham!">
    <img src="https://i.scdn.co/image/ab67616d0000b273f2d2adaa21ad616df6241e7d" alt="Last Christmas">
    <div class="t-name">Last Christmas</div>
    <div class="t-artist">Wham!</div>
    <a class="t-open" href="https://open.spotify.com/track/2FRnf9qhLbvw8fu4IBXx78" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケテナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b27378823b4e368a816a90378780" alt="イケテナイ太陽">
    <div class="t-name">イケテナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/7hA4kaAFiM3Vr61JaFGzvy" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="うさぎラップ (ソロver.) - うさぎ（CV.小澤亜李）">
    <img src="https://i.scdn.co/image/ab67616d0000b273f991d9ccecdbade375f6b0dd" alt="うさぎラップ (ソロver.)">
    <div class="t-name">うさぎラップ (ソロver.)</div>
    <div class="t-artist">うさぎ（CV.小澤亜李）</div>
    <a class="t-open" href="https://open.spotify.com/track/4EXp6T9ou0y6BCLiaoYg0R" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="イケナイ太陽 - ORANGE RANGE">
    <img src="https://i.scdn.co/image/ab67616d0000b27378823b4e368a816a90378780" alt="イケナイ太陽">
    <div class="t-name">イケナイ太陽</div>
    <div class="t-artist">ORANGE RANGE</div>
    <a class="t-open" href="https://open.spotify.com/track/3rYx4H5RpE6tp4x1ZU01QS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="come again - m-flo">
    <img src="https://i.scdn.co/image/ab67616d0000b27340b9da3f4fc33ebdcae34c84" alt="come again">
    <div class="t-name">come again</div>
    <div class="t-artist">m-flo</div>
    <a class="t-open" href="https://open.spotify.com/track/477CB93mH986mrIheQD0RR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Jamboree Mickey! - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b2737d6027d98eeaa6d5e9af4847" alt="Jamboree Mickey!">
    <div class="t-name">Jamboree Mickey!</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/2O70g7QJJRskIbAF596CHm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary - Ken Ishii">
    <img src="https://i.scdn.co/image/ab67616d0000b27373918e960a1fd4f240df6686" alt="JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary">
    <div class="t-name">JOIN THE PAC - Original Mix - Official Theme Song for PAC-MAN 40th Anniversary</div>
    <div class="t-artist">Ken Ishii</div>
    <a class="t-open" href="https://open.spotify.com/track/7wr97Scn0CfH3b1AJBW8Zh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dancing Queen - ABBA">
    <img src="https://i.scdn.co/image/ab67616d0000b273ec5de82891e542d4877c6d98" alt="Dancing Queen">
    <div class="t-name">Dancing Queen</div>
    <div class="t-artist">ABBA</div>
    <a class="t-open" href="https://open.spotify.com/track/1rMfDvE2C8ne8UZj847rKM" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Shine - Original Mix - Chuck New">
    <img src="https://i.scdn.co/image/ab67616d0000b2732ff89e5c56347ccac1fae742" alt="Shine - Original Mix">
    <div class="t-name">Shine - Original Mix</div>
    <div class="t-artist">Chuck New</div>
    <a class="t-open" href="https://open.spotify.com/track/6uYCP6MK1oxgQZAxxXOTLH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Thinking - Louis Cole">
    <img src="https://i.scdn.co/image/ab67616d0000b27369f27ac28a49aadfd395b4ae" alt="Thinking">
    <div class="t-name">Thinking</div>
    <div class="t-artist">Louis Cole</div>
    <a class="t-open" href="https://open.spotify.com/track/1JDS6yAk0wCsfkFLN9Tr7i" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Hold Me Now - キャロル&amp;チューズデイ(Vo.Nai Br.XX&amp;Celeina Ann)">
    <img src="https://i.scdn.co/image/ab67616d0000b2734378d9eb85031d774e94d17f" alt="Hold Me Now">
    <div class="t-name">Hold Me Now</div>
    <div class="t-artist">キャロル&amp;チューズデイ(Vo.Nai Br.XX&amp;Celeina Ann)</div>
    <a class="t-open" href="https://open.spotify.com/track/7KYQfBt49UM0GYBHkD9TgF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

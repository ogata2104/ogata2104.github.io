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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Vr-1zZHrsHwQ7kNvwEZD3p-&amp;_nc_oc=AdqZnKCWqws-lLH2HlReeBCNYp0r4eVnUH3kDQUwDA4Y6B-DhfT70CHS9IIRoqQPuFA&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQLHv2eMK0dI5ibOKH33jlipBKGANxVP8RWms1QN76uU3lYuVPenNkhRLO3H33HGA1G1kQcy92b7aQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTsA_CDuje5aB7U2FB4rl0m1hXXLn1DUKDASr6OgVWk0Q&amp;oe=6B059065" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ieTbCsvd2fMQ7kNvwFaNZYX&amp;_nc_oc=AdoL6DKBuNyGytzjESFgJmAj2wr-per8-y_g5fsnqTRrg87JyFcopvExn1y0AbIAlaQ&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQKYmQDkUoItCdZzyH5wgj_ov9-CHQ7cdIohofQm5_ZfkJhEIjHmL85rytpfcnYCfDXnFBwvPMsPtg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT4a9zR_rOT_vne4jJ_aSZYGU_Dg58E6ixdJvr0QCj5ag&amp;oe=6B05A09D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WtyzJYc2-bgQ7kNvwHiBA2_&amp;_nc_oc=Adp0oa-ESN0VAKWfAKME-O-xYovPP78Unu_kxcpn7u6ZE6c_TJ1PNqm9FZ1LKW8DBDY&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQJXwhupqZyjS4N3SwPjEs2SQCQAydA-PB7tgsnu60JRVuLK4RS2Vzdtj7qsWny8yMoEVdB4usM6gA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTXcK8V5ddVh4wTswzOIG6QvaO1LB8sfCCKYPe01WPztg&amp;oe=6B05831E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=T3mNwtpgZfUQ7kNvwHFUJbU&amp;_nc_oc=Adqyalx2PJMxie5C_JWFVGhU89w_YiY2k0E5W21CbkPhkzPT3BsCmp4Lcdf4TKetcUw&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQK6ZTQpG5VzXvbmKhob2XCeP772gV57lJWNurnuBla1h1AqJvueJk6dLZXhsTnv_0NXKDGwvw_iOQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQlPfqZpWPiJWUk-IoIzfDGAztf67sEVKKfDJLp1f_KdA&amp;oe=6B0581A5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tLcfJQ91ZUgQ7kNvwErA3IO&amp;_nc_oc=AdpQezbpnYvwV0KB9YMrfhktnCIE2I4To-BnfEqgAlKFLK1DhWxBmiHzlLWXvsDfyes&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQL7ZtqIa3xPei79FrM5aWykp_P-eAiubLbjfGJW3OQGEy3kh7KsFTUvac09KnfvaB4n6TfWOqzkpg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQdGV-PULJhTOC4toBc7JVuCeuv-IeG-s72bROn9lTdfg&amp;oe=6B058319" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rNOKgHzkKs0Q7kNvwEWlMPg&amp;_nc_oc=AdrS7G0inQBmP2cfKL8qbmkMO2kPy2VSTJPgxGauzZfFIAwjsiI3uvZxVXrty_cWr3E&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQKiDPoNmWjwaGkjA8Sm4gLzNz5Ipl3cCSFYJdj2hCbv8NpILl2FRFiC0ZWqBfhVBsluieFr_6rGig&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQuJQqzNm3snBzFsMyFkvGtN4ODMCSBHV8UiHmhQ1cnTg&amp;oe=6B05802E" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=R8nIGnx8dEQQ7kNvwH2GkeD&amp;_nc_oc=AdodAhFt5vgtppge6a8GY1jLmAyvir5h7Z_zqClQfRG9u_P7rTQsSngcw8WLTVYWfRM&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQL11Zgqwb1I3n47XOGnyncA261Ur2Q9rgB5jO1QH702yLeCg7ehb0dNBxfOqk9IbPMT2B8BB_Dh_A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTKMw7YcbCxs-iWk1MvYV6i5QErV8_Q0l3bktmweOkkzQ&amp;oe=6B05839E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4HOFkUSIwjUQ7kNvwGQO410&amp;_nc_oc=Adr9dUWyYLr0ov2Pku7iIsEEqSsnH-P5i5LRlOmfza9sxnSUYuxi_p_SapYNsZZy1mI&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQKdkxBQMnfYPE705ljbBzRwqGyDHpiZmvKUqGPl9Zy6ISeMnSMovQx5VL4qiEIwfa4GMNL8cXsMLg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQek6h7LZrGZUYRx6t9pCnDs9cimgmDrmFR0CoKcmzS1A&amp;oe=6B059475" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-3Nc8se2CHcQ7kNvwEdIDBL&amp;_nc_oc=Ado6ErVBtcTMfwIJpXGNOlKNA-6ENQaTRXV5tFPEiZ8eUh8n-Z5Nl7fjd1KKzTeZxA4&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQLu4uUFGtPYvB6CKDAh-EgcF_2TLOh9H87fueJs2ZMryot8FCSKgSwq97jAv_fIanOM1Vww12yL-w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ24uLL1fBJ6ueHiS0KJcpUpag_xApBgvRcuHryhFjmzg&amp;oe=6B057FF6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yCLLjF1eU3wQ7kNvwH8tFIv&amp;_nc_oc=AdqEG5C9Lsdjo6p6Ibv1sPuCtaEwrqcOqVRPWZGacezTAPVVzhAmWYgXlxd4EsdHW2I&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQKncSLA9xNsJCummxPIhCmL9cfHCdlfasF-Mo4RQ_tzkQ0WtMgaoWRk9ZVLfB8mOevxC4oqYFMt3A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSFhfeBjfs8TK2PuAUqPAi98mwKJTAHXy7LOFIk-KWuSQ&amp;oe=6B059026" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4-6g72QQ6fsQ7kNvwHmJFwg&amp;_nc_oc=Adr2GDHCOruUVuA14Yy28VQjzAXLBj41WRRM3bDnEV-vJTUPwFODOAwNN4cw14VF_iA&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQIJWtHZagjjlZxdb34dXQWUoQQJ-KbhImEKBDQFfu5ZWfRUGU6vvpI33jn4d79fpM9SGPvoUhDPgA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTb9lW7JdW3UaCTFKq-CuS4-HTsf65vsSk1jNTb_hS31A&amp;oe=6B058341" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=2paT3Tc7WCsQ7kNvwHlXLGB&amp;_nc_oc=AdpkuETmM2NBwfyqE6kmYooslighRWvUo-OrRVG-DlXJlJZzIOTPd-wKO0FxGxquwC4&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQLYbAbNv9B-MCaqguGDZ_YLiCERwpKPzWVCsaeA8btMGhwORY3yh0Zsd8o_pHIGP8T954VS7747nA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSJnuvjLX0OC_GsXq6V7fuHL5XmuwdIYIy8oxrXwdI8sg&amp;oe=6B05839F" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WvhigryquigQ7kNvwE26wCn&amp;_nc_oc=Adr2dFK2VNGVjC-y6469sw6PlAXdNlVX3BtZI6OHodaAx2AeelSPR3mXE8ADypP8lCE&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQKAAqsgVolGmDXIPSf4HGudE8qbXNBMkasSgz0wvP3r2MatWaH-sVtZbpNKV5nG6bHX3bg9JOFtoQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS7ym6DXVEl2bFB_8WPWdi6Hoy1voc9BBL5TS3kBTGWQg&amp;oe=6B059A6A" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=VLIgWgptvXEQ7kNvwHULkqp&amp;_nc_oc=Adrq_PnNdUlnNmqcQ2xm9tt7vSvLMqLUT8Yk_k3Yy1Bf4y9hr5156Bz6BJT3UgdGh-M&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQJANJExXbtb57rfHokrN1KXxIIyTHgU3bnWHlPPUdzAY9tMzUl8R11_KvEDSxz8qsEYloy6UFNTBg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRvYVws4GrXVZdE5Yb-4Dfh_p1mu1AzkvpZSjGWQSr0yA&amp;oe=6B058DDC" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tFaRz8mZovsQ7kNvwESZtcb&amp;_nc_oc=Adrt1NZNGwR4JApVqoK7hPNyyMy5HFTVm95q4vYffu84GWv_38iLDJOW7QWnERlU3AI&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=GpW3uqEx-vEMfnteaR6byQ&amp;_nc_tpa=Q5bMBQIfGOCnpZmVXhGSGf5f5fu79vVZS83m26vu3zt6CzgXnTaqJhlb1YNwBmK3MpCp3H3wmsbgtZHnnA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT1L_KS5uQHSJTXAwnDNwoeGMGmAv4DrAb8zPYOkIUjfQ&amp;oe=6B059DF6" alt="" class="t-thumb">
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
  <div class="spotify-card" title="California Dreamin&#x27; - The Mamas &amp; The Papas">
    <img src="https://i.scdn.co/image/ab67616d0000b273cbd56c3a8faf8cf8c8bea0df" alt="California Dreamin&#x27;">
    <div class="t-name">California Dreamin&#x27;</div>
    <div class="t-artist">The Mamas &amp; The Papas</div>
    <a class="t-open" href="https://open.spotify.com/track/1ZEOIhSn6BKErV59bIgn76" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Marvel Studios Fanfare - Michael Giacchino">
    <img src="https://i.scdn.co/image/ab67616d0000b273df0b8480336e407d174bf040" alt="Marvel Studios Fanfare">
    <div class="t-name">Marvel Studios Fanfare</div>
    <div class="t-artist">Michael Giacchino</div>
    <a class="t-open" href="https://open.spotify.com/track/5xdTdPiQVFhI5iVEw2ctbk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score - Brian Tyler">
    <img src="https://i.scdn.co/image/ab67616d0000b273f7522b5f7b34e774cfba81f5" alt="Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score">
    <div class="t-name">Marvel Studios Fanfare - From &quot;Thor: The Dark World&quot;/Score</div>
    <div class="t-artist">Brian Tyler</div>
    <a class="t-open" href="https://open.spotify.com/track/0y6nWKlwppOXeprZxMsHQ2" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="B-A-Y-M-A-X - Without Dialogue - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b273045ffc089890c9c7993ace19" alt="B-A-Y-M-A-X - Without Dialogue">
    <div class="t-name">B-A-Y-M-A-X - Without Dialogue</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/4l29cPGOSXh9TRcYp1t5d9" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Happy Song - Tokyo Disneyland">
    <img src="https://i.scdn.co/image/ab67616d0000b273045ffc089890c9c7993ace19" alt="Happy Song">
    <div class="t-name">Happy Song</div>
    <div class="t-artist">Tokyo Disneyland</div>
    <a class="t-open" href="https://open.spotify.com/track/3CTvENkGrXC47vyQNti7J4" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="SHUT UP AND EXPLODE - BOOM BOOM SATELLITES">
    <img src="https://i.scdn.co/image/ab67616d0000b2736efc076b0f1f602a8c82e56e" alt="SHUT UP AND EXPLODE">
    <div class="t-name">SHUT UP AND EXPLODE</div>
    <div class="t-artist">BOOM BOOM SATELLITES</div>
    <a class="t-open" href="https://open.spotify.com/track/3fD5HVFpDIAQ0tsPTFPDPl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="島のうた (島二郎ver.) - 島二郎（CV.最上嗣生）">
    <img src="https://i.scdn.co/image/ab67616d0000b2731bf3fb5516a583db659b5cac" alt="島のうた (島二郎ver.)">
    <div class="t-name">島のうた (島二郎ver.)</div>
    <div class="t-artist">島二郎（CV.最上嗣生）</div>
    <a class="t-open" href="https://open.spotify.com/track/6qmMb8SRbNyyBdeofzho3s" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="夢中人 - Faye Wong">
    <img src="https://i.scdn.co/image/ab67616d0000b273f9db763072c2ed8eb137532b" alt="夢中人">
    <div class="t-name">夢中人</div>
    <div class="t-artist">Faye Wong</div>
    <a class="t-open" href="https://open.spotify.com/track/0T15exEGIIFqUaqr0LQCca" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="まだ見ぬ朝 - Takuro Yoshida">
    <img src="https://i.scdn.co/image/ab67616d0000b27329adc4b2b8662512df45f8d7" alt="まだ見ぬ朝">
    <div class="t-name">まだ見ぬ朝</div>
    <div class="t-artist">Takuro Yoshida</div>
    <a class="t-open" href="https://open.spotify.com/track/6IL4VN5uuK0PKtSlUZGa3p" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

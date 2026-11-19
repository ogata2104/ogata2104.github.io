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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Vr-1zZHrsHwQ7kNvwF3Dnj6&amp;_nc_oc=Adq36tjpe40L-u3bt_41bRLSFBxtBSsoBnUeNXl1VJkuw3yCfdBFxS8Zs9V5MfU3_BE&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJkiVktyJJMD59MO7N5GjSAQtkQ_rLGNxQRU0Y0eh5qcGQoV7cP4fcj7kqvGn8tll3ziiyc6_lTvg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSMr9DkS8_dGHb7mXy66JdsgPNQzlVdgPPmdJJLaZVsdQ&amp;oe=6B04AF65" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ieTbCsvd2fMQ7kNvwFtvnd8&amp;_nc_oc=AdoS6rZZpb-ta5u8aoX7QHzPVsCOI_qFfQbfrH4bPU6qXHTCYxbmOg0M6W96xZIMSTo&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKZJ7SJwa95XdfJc0in-oilcwlxkKstl4QQsUxgA-09LUJ6o3gZth5IvAg_PjSBpaOjPCidc8nGfQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSFYOvA4pDHedjkUO3iSAXudCkHARqPP_2uiZLIaGFWOQ&amp;oe=6B04BF9D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ok-cGax8GA4Q7kNvwG8CxrI&amp;_nc_oc=Adou4HEPymM7hDHTpkNTa_Sd6qp5evZy5y3ZDrmlM6ZxED_lC7oGbkH_nXFzaMfa_WI&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKPO0MCe4lZnLLD1OVI8hcGVuQxCToOBqFtvSk0H2F0v1Q04o7F2hiIr3xk6pq2Nycl3-DS6Qob7Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRnWPmgZZb9DkjH4YBef1r9nOWwFMRWOfJWYWqaUt7VHg&amp;oe=6B04DA5E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=T3mNwtpgZfUQ7kNvwH8HhJi&amp;_nc_oc=AdpS0hTxYsaO-wA09QVjZQ1jXvh7s5nGvHLGd1oE5qprx1MlbDZX8EJoRmQnk3qFyfg&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKn4gGYsZy469BGihq5E8d_0g6KAjqUUToc-7PeBRY_cbX6QstAK0Jjurmm1si5733qUCoJLCKUOQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRq7koGRWxVQR_SVwfpN7td9LukGeIukBV6lk5t3IjpZw&amp;oe=6B04D8E5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tLcfJQ91ZUgQ7kNvwEbXW2J&amp;_nc_oc=AdrSDHche-bPwVAJJyuxDAWg_MZU9CQ_OlfMI53zasd7YizmJIVaNkZevRKZ0YemITU&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJCbO-AyXQ4-MYE3qU769J9uiizsFeuK1qikEiD1kY9BH4d1qVkiZtGRn6SdR8RPOyer4lQuPLqIA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRmVPWmWhB3qaCJgzDBvDaj5YHqiM0wcoZBJhbzXSn9EQ&amp;oe=6B04DA59" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rNOKgHzkKs0Q7kNvwEiv1Rr&amp;_nc_oc=AdoKhRoE1vyvuWQXm6Bv8g0FAfOlR9WnYZPUXuUBLu130qR7HRozWDlNZsV7cs0CNG8&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKF2-7BfF9-jaaMyTxKk2JxJeGVZDHbYD0kbyLuVZx2dO5FhKl0LwVJArBFDntkLZLF7_UwFM2o9Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTv3EznHL_BMGYqLM5qRInrX2s07oSCK8Saz9k4fBExZw&amp;oe=6B04D76E" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=R8nIGnx8dEQQ7kNvwETwIMu&amp;_nc_oc=AdrhS_0rwf075-S5GUxmx5vhv2dJPFYF6C_CeTn9P6yRUCWNuA8PJvtLhCVHgs8oQM0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJqgbXYI9Am-gvH9-daQCdung1t7J5bUb2cjOguDrGY0s6PzTBX-X2cJN6w0-Aw53HeMHarvAQNoQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQgONZ20NQvzVzW2X89TTBHL042H-oZYwu7lpNOdsAAog&amp;oe=6B04DADE" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4HOFkUSIwjUQ7kNvwGgotYq&amp;_nc_oc=Adq9YWErBfIW0G_4o9-G-XRGFgGJ9bqExcfo99hnvEd6_XBIu-QVo2pMmzB3pKMneDE&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQLy8veOFgZEDy9K0ArzkRCJabYihG51VLC9yhXmjPgD_8JzmOEDi5ZRe5shjCj689SlJwSBie-dVQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRG1RXSuJUJm20toVbs3jD5mtMdytRIYMROAvvEgeKJrA&amp;oe=6B04B375" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-3Nc8se2CHcQ7kNvwHjcwRn&amp;_nc_oc=Adr643sUKxdIX2qW3Dk5jsoYYT4tSfIjOuw_o-IK5jggdIFSn-9JviVivN1OeRspYYU&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJ9sEdiwsiKxqRiEOql_1vzHZTsAE8LD1oLeDamGQ-poaOnTkvHBEy0oqz539FeSCdnUvG9ZNTWQA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRqKyOZPfOfmkQbCYS88F4oBJf8Qo-G12dHn7UK8tjSog&amp;oe=6B04D736" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=yCLLjF1eU3wQ7kNvwFYA27d&amp;_nc_oc=AdqvAOxg9YmWH88KhuZdWQyG-8W65IT_rOjpG8ytUIWWRXtV-raY9Dm_ll1ibJOEn8A&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKrmOoQ4e0XExi0gkc_kR6jGhzNkaUeFxZ7ww0H4S6kZbNfyOZUtldj4SqTxP9NVcp7mx87RjRczA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTx6JFIozEj9nb-MnatMetmN0ULciBRPDkfF4I2hKTX8A&amp;oe=6B04AF26" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4-6g72QQ6fsQ7kNvwFCvIKR&amp;_nc_oc=AdoJ4eTdBGanw_FW2CGvyxIwi3OQVqHBWalxaGGQbmXEWDaAkzG7F5P7SizfVAL0UwA&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJyFUNi5M-9BKZTlEmkx0Qchuip1q2bllRwYDeQZX3byjvnq1n2gVE_7qRwM6LJcOA3pXZepzo1rA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR8MkS3TspVQdDEmgBgYTNjwTjmEADa3y7D1WjJicBMSA&amp;oe=6B04DA81" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=2paT3Tc7WCsQ7kNvwGGg33K&amp;_nc_oc=AdoBiYcY2cUc_WQnQ5w01KwYuBh8f0YTuOP0tCkbnXpIDCN0QBCp2zkDh90pl8dCF8o&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQLS07QsKURDFZ1Og8i7aSwlAhX9lIzTxjAL949NBvXIWuoR68nXhjs7rViEqUzsJnY43xyj0JtlAA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQR1fkd5hg6_2lRnyYyaWh4jlZ9a-hiQjjDpKCFLNsD23A&amp;oe=6B04DADF" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=WvhigryquigQ7kNvwHyLYRs&amp;_nc_oc=Adr2DDdsKdvQiVU_piIFOek7_f1NYqtkD4CZRwqnaLERe_nsD_YU2O5szDYiUWAE1J0&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJCMjWjp9PDsSN0RomNXllhr9vrI8Vn9fWcrEB4iuESzYNP-TVw5u90XWrSmmzecMXq7h_vNyZzlA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ6GMyW3xtNOpwuRR6mbgB4k-Gwch-JQ-Rxj9YvOV-JxA&amp;oe=6B04B96A" alt="" class="t-thumb">
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
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=VLIgWgptvXEQ7kNvwGHCCcq&amp;_nc_oc=AdrE1LYI4w5UaGjbE7idiWtyTobMsZW8-xH4O-tTAZp4I3lbfKxHlwjIOjl2StbBlUM&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQKSTEWNUSJuMVjZ5XEa7zuAjJZv32h5Kgw_6ctq9lvM9sIIUuUrlMYIi4rp6aF7gSRPOFT42F7B3g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQw1bV8Y_iBlZZ95B3hpCzGBF-1ayeb7yqq-BC_LlmmkA&amp;oe=6B04ACDC" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tFaRz8mZovsQ7kNvwH4my0H&amp;_nc_oc=AdobV1FEdLpCq2GX3oqnMsyMrsklS950eyzH8AkbSCTEDA37czsdnNodaURATErttQw&amp;_nc_zt=23&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=cgneHtuhZtzQStXjpb2nJw&amp;_nc_tpa=Q5bMBQJKkYyUPapJwm8WHjoIfZqRjSk7Ff1Gy7jv73DFOdREONhSLdPRFixfCHk8n2Y-dxcQbJAPEMNbVg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTUPIABq-OsUlHtsM1ap1m3DM7xbGIUOkToqtTNFlNIEg&amp;oe=6B04BCF6" alt="" class="t-thumb">
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

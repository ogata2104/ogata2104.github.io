# <span style="display:none;">2104's Ordinary World</span>
ただただ平穏に暮らしていきたい

<!-- THREADS_START -->
### 🧵 Latest Threads Posts

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
  scroll-padding-inline: 50%;
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
/* 隣のカードと半分(=幅の50%)ずつ重なるよう、先頭以外は左に寄せる */
.threads-card:not(:first-child) {
  margin-left: -90px;
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
/* CSSのscroll-driven animationはtransition/:hoverより優先度が高いため、対応ブラウザでは
   これがhoverの代わりとして効き、「中央に来たカードが自動で拡大」を実現する */
@supports (animation-timeline: view()) {
  .threads-card {
    animation: threads-card-focus linear both;
    animation-timeline: view(inline);
    animation-range: cover 0% cover 100%;
  }
}
@keyframes threads-card-focus {
  0%, 100% { transform: scale(0.88); box-shadow: 0 2px 6px rgba(0,0,0,0.08); z-index: 1; }
  50% { transform: scale(1.08); box-shadow: 0 12px 28px rgba(0,0,0,0.22); z-index: 999; }
}
.threads-card .t-content {
  position: absolute;
  top: 12px;
  left: 12px;
  right: 12px;
  bottom: 34px;
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
.threads-card .t-date {
  position: absolute;
  left: 12px;
  bottom: 10px;
  font-size: 10px;
  color: #767676;
}
.threads-card .t-external {
  position: absolute;
  right: 12px;
  bottom: 10px;
  z-index: 2;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background-color: rgba(255,255,255,0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.15);
  transition: background-color 0.2s;
}
.threads-card .t-external:hover {
  background-color: #ffffff;
}
.threads-card .t-external img {
  width: 13px;
  height: 13px;
  pointer-events: none;
}
</style>
<div class="threads-stack-wrapper">
  <div class="threads-stack">
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text">とにかく各登場人物の「顔」に圧倒されます。今年の個人的顔映画オブザイヤーです。こ…</div>
    </div>
    <div class="t-date">2026-09-17 12:08</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdX3D8Rmjnr" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f8f2fd; border-color: #ead9f5;">
    <div class="t-content">
      <div class="t-text">Xで見かけたこちらの投稿を参考に、ベーマガのアーカイブからゲームプログラム部分の…</div>
    </div>
    <div class="t-date">2026-09-14 21:43</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdRKfjQmlI_" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text">夏は終わってなかったぜ</div>
    </div>
    <div class="t-date">2026-09-14 18:12</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdQySD3GlqJ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f8f2fd; border-color: #ead9f5;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/806474026_18633008524027991_8051060962185525360_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7_Rwqj60VFIQ7kNvwH-Xn8P&amp;_nc_oc=AdpKZr_dt8EmMB1Yg9flSkqzi1-1PpoS2cP9PapL4XQeC_eBJlArcSBoN7rC91i8y1I&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQJtd1vDIsJpxVh0jXHI0DZeqi9q4h6ixN_BBDfffAbQgr_ClLl67FF-bQI74oDom24iNEeQT7KRJw&amp;oh=00_AQK42ilSAUhgA8q3M8Ego0-TK2X5hNDvieFBf514LT-oqQ&amp;oe=6AB3C4F0" alt="" class="t-thumb">
      <div class="t-text">『バックルームズ』観たよ。<br>この手のはアタリハズレが大きいよなぁと観るまで不安で…</div>
    </div>
    <div class="t-date">2026-09-12 22:30</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdMGQCeidgZ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/802988973_18632299381027991_6271974641923046696_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=q_9DM3bonBkQ7kNvwHvuJ5j&amp;_nc_oc=AdrYkWkngtzkH3_3DsiXtDfQIgELe-aIgorbkFHllhDHekjTMhJnbY5vmN9rrmqTU-0&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQLoBkLRlKKmquXLejABmMupTQ44mZDpo0Wyinnckd3hSAfBQ2EHHWyhJ0rUms9zOoa2AGjqq9CGyw&amp;oh=00_AQIsgsA_aues0ZDiaBAWxbD09nk_r-6H1Kw66c5Eu_A5xQ&amp;oe=6AB3CAA5" alt="" class="t-thumb">
      <div class="t-text">きらくのきろく<br>#渋谷系</div>
    </div>
    <div class="t-date">2026-09-10 22:52</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdG_Hj9gbkO" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
      <div class="t-text">トルネコは買います。<br>iPhoneは買いません。</div>
    </div>
    <div class="t-date">2026-09-10 12:01</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdF0rs0mvCa" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
      <div class="t-text">トルネコ！</div>
    </div>
    <div class="t-date">2026-09-09 23:41</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdEf7H1Grsd" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/798316686_18630761044027991_9137306186417153623_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Hc-I4E21tNcQ7kNvwFmscot&amp;_nc_oc=AdpjU7eQ6FWB8f8_2Na5eZxNJ6xaYYQmfPrwzzaQxwMz6WjlemLNapdTg0OwXu-7hZw&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQKZ1jYOWEXhaofmDrssVIVVqZo6rIjP9tv4QxCX7_q01qm6oxGPZxioosGdOPOCbBqbUKcBlNgTWg&amp;oh=00_AQLXfLsD8KP3FY4y5VNBAJ5xLF7e3VVwuulOcAk_nA5uZw&amp;oe=6AB3C7DD" alt="" class="t-thumb">
      <div class="t-text">今年のふぐ会も美味しゅうございました。<br>#ふぐ</div>
    </div>
    <div class="t-date">2026-09-06 09:56</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Dc7TLSSiUrT" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/790301302_18628965418027991_3733784461889033592_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=JiuWOFjOU58Q7kNvwEX2a-h&amp;_nc_oc=AdoGzveQZsEjU8xq9MpMQM1Gvigh6mLLDdSPRNRL0gPF5afEIirTFXGO-OxgiEWqaN0&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQL7C-1aOHwYGolZF2j_o1AhZ1w0gtqeMLnFQuV56yzKh2KFYfLUtx9JQgnPaAadnu2YBka3X-gVbg&amp;oh=00_AQJynk6Vo-B7APd7c_qc1pbnpwKM7Z6RPYPfc11Px03KuA&amp;oe=6AB3DEDD" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-09-01 01:05</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcteedrCfKo" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/787435258_18627554014027991_6823652663317638022_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=U3yBhMXcIRcQ7kNvwGkTur-&amp;_nc_oc=AdrLCw9QFklNkM0asMz_uJQzgZsOeBVjO0kWM4xrT-OJPppSuTqN4dGuhcJopEFmmQ4&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQI64-RI4VMylEjzQ1ujHc6md4xO5vqC6BwwGdAAPdwCNRNVKHHVm16ZXzhVmACh14npe6jqwIhGJA&amp;oh=00_AQJgrY6a_IxHsIQWmacWdS0yp7F3-6ltFfgzGvBukXBaFw&amp;oe=6AB3E2DE" alt="" class="t-thumb">
      <div class="t-text">#10年前はラッパー <br>10年以上前だけどね<br>#splatoon3 <br>#spla…</div>
    </div>
    <div class="t-date">2026-08-28 00:25</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcjGqB8gXnJ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/777352697_18625074976027991_6709459502108065474_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Rwo1NcP2WNoQ7kNvwGoEy_h&amp;_nc_oc=Ado6PibYPR9ZOYFu2BiOy5gLfLTQBO6LFw1RIE6TltxtB7s2DYT4EsXVlDUljjnq0QA&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQLrQc2jbhcMJFCJqhMwxy_XpDWk3gbve-uMLGitQDKMO3HdKCrVp40DXOUcmuMuIKRskAhNlSklvA&amp;oh=00_AQLwVwClpqaNWBstocjGhUsP3C3tK2KG2IFuQlAhEg979g&amp;oe=6AB3D73D" alt="" class="t-thumb">
      <div class="t-text">久々に「買い物」をした。<br>#楳図かずお <br>#まことちゃん <br>#墓場の画廊 <br>#俺…</div>
    </div>
    <div class="t-date">2026-08-20 20:31</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcQqVHDCb9r" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/777382070_18624987067027991_7389481295785245777_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=YssXPdVknbcQ7kNvwE_9cwN&amp;_nc_oc=AdoT-1KR7GcbV1l3hYwz9VE1xjrZHdKb_FejrK2N03HrUY4QW1m6pitJPjP1vbvrfNI&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQKQAcNNVm47rZ0Sj_Wc6JKezBzp7q_rWADDQr_tlLF9tKbtjXAl02RKsA4iXezyEdEJ1--3d9RrzA&amp;oh=00_AQJFTa6LV0DQrkCtRGpaMIY5rQvQuJqshS9zQ97F4aAW4A&amp;oe=6AB3D794" alt="" class="t-thumb">
      <div class="t-text">久々に中野で降りた。<br>駅周辺でゴリゴリ開発しているのを横目に圧倒的威厳で聳え立つ…</div>
    </div>
    <div class="t-date">2026-08-20 13:47</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcP8FCtn64L" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/777328276_18623817964027991_7021757795281075069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=uSVTiQY-nPMQ7kNvwEYXga3&amp;_nc_oc=Adr4_iVzUQ4j7nq_a8rQfUn2x78axPiqAG_26y4F_QhcbR266jSqpp2ebLfSj-z5Jf0&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQJ0FOdAbl1uzaLzVLXnw6PCsg54-VB_9id2TkNQqUAg6ZhL2iiwOc7JpEXsCKwTOKqZy5auoE2T4Q&amp;oh=00_AQJZBkvsVxgigy2rtyDEt156OAr7k4wkYmkXVjQIQDAXhQ&amp;oe=6AB3D903" alt="" class="t-thumb">
      <div class="t-text">ちいかわリテラシーが低かったせいか、映画が難解過ぎたので、再挑戦に向けて猛勉強中…</div>
    </div>
    <div class="t-date">2026-08-17 21:10</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcJAc5ygbPf" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text">コンプラや現代の価値観云々などから、昔のドラマや映画が地上波TVで放映しづらくな…</div>
    </div>
    <div class="t-date">2026-08-15 02:31</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcB20SHGgKt" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-15/771814721_18621255310027991_1838943870137628452_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=0Owu5M1ia54Q7kNvwG-UoA8&amp;_nc_oc=AdoedvR8NiQU78ur89AOkFbr0Rla8_jAPUygocthMNEII-BA-eHHa0Be8iDcI0IZdKY&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQIocibYD2ag9tayeahiKJ8foMaNo60fuMVEj2_eIfN3ZczdN9qcqnLJq0eLik89RBY7Hxj9e6AY1Q&amp;oh=00_AQLISLiDQq1DPnqeAZmHGDC3-WhmgDCf8y1PwhPxhTy3Og&amp;oe=6AB3B32C" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-08-11 12:37</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Db4o6Xsifl1" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
      <div class="t-text">あー面倒！面倒！面倒！<br>このままおねがい！</div>
    </div>
    <div class="t-date">2026-07-26 22:14</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DbQeQiBGm21" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f8f2fd; border-color: #ead9f5;">
    <div class="t-content">
      <div class="t-text">TLに大江千里関連の投稿がやたら出てくるんだけど、これ、ほんとに祭りが起こってい…</div>
    </div>
    <div class="t-date">2026-07-23 21:40</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DbIr9zoGnbx" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/755220959_18614890231027991_4235132249041683948_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=epX-13tK3qgQ7kNvwHoJdh3&amp;_nc_oc=AdozFIJcnq8lXbyyGMgGiIOu7LbJOP7HHvlLm8EULTpGQ_4ibANO1XEuh-hY0rWV_ss&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQJ7rAuoybYeklZysUlo6kfOWQSI1POEi3OpnhYZp-KCQSUYhp0ugU-d3NyL2QWHZQqALgUdNRZD4Q&amp;oh=00_AQLNHTT3FOx-RT934WIOYm3oIrB5Iy4V3GHApeSpHCbrew&amp;oe=6AB3C1D3" alt="" class="t-thumb">
      <div class="t-text">こんな感じで、オタカラ・ハント始めました。<br>スプラトゥーンでハクスラ、めっちゃ楽…</div>
    </div>
    <div class="t-date">2026-07-23 01:40</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DbGirb-Aade" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/753298481_18614199868027991_6979282962032146883_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Jd1zSIHNv9wQ7kNvwEjXw37&amp;_nc_oc=AdpYwCReClRgpeLVX1q4_rfyHOYRXgWADYGpPU4RBH64y5xOKPkyMvTjoJsT6mpkcTI&amp;_nc_zt=23&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=xp8kvbDrtgsQGlMMJyK9Ow&amp;_nc_tpa=Q5bMBQLuTPuUWwf5Ez2dZ-SB5aKUNZ-7Z2McN3i98Czlv96azo1lJCNhwF65i-43v9Lsq0gbzF1vXgqNGA&amp;oh=00_AQK6NcnF3q-iBuNcjLLkycc6SphJh8hcr_MuBHh9DG1E3g&amp;oe=6AB3D136" alt="" class="t-thumb">
      <div class="t-text">この三連休、唯一の思い出は吉野家に通ったこと。<br><br>#吉野家 <br>#ドラゴンクエスト…</div>
    </div>
    <div class="t-date">2026-07-20 16:29</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DbAZ8dQgbX_" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
      <div class="t-text">世代的には『いとしのエリー』いうたら、<br>岩田と仲手川とみのるの話なんよ。</div>
    </div>
    <div class="t-date">2026-07-18 22:09</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Da73RA0GmQn" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  </div>
</div>

<!-- THREADS_END -->

---

<!-- SPOTIFY_START -->
### 🎧 Recently Played by Spotify

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
  scroll-padding-inline: 50%;
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
/* 隣のカードと半分(=幅の50%)ずつ重なるよう、先頭以外は左に寄せる */
.spotify-card:not(:first-child) {
  margin-left: -80px;
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
/* CSSのscroll-driven animationはtransition/:hoverより優先度が高いため、対応ブラウザでは
   これがhoverの代わりとして効き、「中央に来たカードが自動で拡大」を実現する */
@supports (animation-timeline: view()) {
  .spotify-card {
    animation: spotify-card-focus linear both;
    animation-timeline: view(inline);
    animation-range: cover 0% cover 100%;
  }
}
@keyframes spotify-card-focus {
  0%, 100% { transform: scale(0.88); box-shadow: 0 2px 6px rgba(27,31,35,0.12); z-index: 1; }
  50% { transform: scale(1.08); box-shadow: 0 12px 28px rgba(27,31,35,0.35); z-index: 999; }
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
  <div class="spotify-card" title="プリンとマフィンのポムポムビート☆ - ポムポムプリン">
    <img src="https://i.scdn.co/image/ab67616d0000b273b6647209bed331ade838a908" alt="プリンとマフィンのポムポムビート☆">
    <div class="t-name">プリンとマフィンのポムポムビート☆</div>
    <div class="t-artist">ポムポムプリン</div>
    <a class="t-open" href="https://open.spotify.com/track/5JzW5UnfWJQKQxdh18YNos" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Wife - METAFIVE">
    <img src="https://i.scdn.co/image/ab67616d0000b2732cbbc1e43811c690c7de3ef3" alt="Wife">
    <div class="t-name">Wife</div>
    <div class="t-artist">METAFIVE</div>
    <a class="t-open" href="https://open.spotify.com/track/33EK6j3B2DWkkIGOmc5ubx" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Look What You&#x27;ve Done to Me - Boz Scaggs">
    <img src="https://i.scdn.co/image/ab67616d0000b27389ec4b314cae875a077bee78" alt="Look What You&#x27;ve Done to Me">
    <div class="t-name">Look What You&#x27;ve Done to Me</div>
    <div class="t-artist">Boz Scaggs</div>
    <a class="t-open" href="https://open.spotify.com/track/6WIVLU2b1Dzz1lvRE4EcBu" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All About The Heaven - The Brothers Johnson">
    <img src="https://i.scdn.co/image/ab67616d0000b273b3dd4b1619bac722e29c7624" alt="All About The Heaven">
    <div class="t-name">All About The Heaven</div>
    <div class="t-artist">The Brothers Johnson</div>
    <a class="t-open" href="https://open.spotify.com/track/5nXFuJEvxEi2k4MfKUBSZH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Fade To Black - Dire Straits">
    <img src="https://i.scdn.co/image/ab67616d0000b273ee92e1d463ee63440431179c" alt="Fade To Black">
    <div class="t-name">Fade To Black</div>
    <div class="t-artist">Dire Straits</div>
    <a class="t-open" href="https://open.spotify.com/track/7N0iCGxTzN2gJPxnTdIRiT" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="What About - Blaxian">
    <img src="https://i.scdn.co/image/ab67616d0000b27349f5a7e05c8b08b31a9c1490" alt="What About">
    <div class="t-name">What About</div>
    <div class="t-artist">Blaxian</div>
    <a class="t-open" href="https://open.spotify.com/track/74RNMSxi9get9yK90yC5se" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Out of Time - The Weeknd">
    <img src="https://i.scdn.co/image/ab67616d0000b2734ab2520c2c77a1d66b9ee21d" alt="Out of Time">
    <div class="t-name">Out of Time</div>
    <div class="t-artist">The Weeknd</div>
    <a class="t-open" href="https://open.spotify.com/track/2SLwbpExuoBDZBpjfefCtV" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Tip Toe - HYBS">
    <img src="https://i.scdn.co/image/ab67616d0000b2733f58c8ae420f64a314d54781" alt="Tip Toe">
    <div class="t-name">Tip Toe</div>
    <div class="t-artist">HYBS</div>
    <a class="t-open" href="https://open.spotify.com/track/0MJ5wKsPEeihONNfugHGy7" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="In This Darkness - Clara La San">
    <img src="https://i.scdn.co/image/ab67616d0000b273787a0dbfa43cdc88d0c484dc" alt="In This Darkness">
    <div class="t-name">In This Darkness</div>
    <div class="t-artist">Clara La San</div>
    <a class="t-open" href="https://open.spotify.com/track/0bmVH05tjN9jVh3kB1TfpR" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Before spring ends（在春天消失之前） - Wang OK">
    <img src="https://i.scdn.co/image/ab67616d0000b2735f8e5c0a5cc2fa99eb585756" alt="Before spring ends（在春天消失之前）">
    <div class="t-name">Before spring ends（在春天消失之前）</div>
    <div class="t-artist">Wang OK</div>
    <a class="t-open" href="https://open.spotify.com/track/0OgOvU69S4QuJYTMlIurn0" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="I Know, Didn&#x27;t I - DJ Nu-Mark">
    <img src="https://i.scdn.co/image/ab67616d0000b27319b57532081c9343b3384136" alt="I Know, Didn&#x27;t I">
    <div class="t-name">I Know, Didn&#x27;t I</div>
    <div class="t-artist">DJ Nu-Mark</div>
    <a class="t-open" href="https://open.spotify.com/track/0Q4G1CEv3AmaE6jbagSvRB" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Samurai - Lupe Fiasco">
    <img src="https://i.scdn.co/image/ab67616d0000b273afd65b04748aff25b77071f4" alt="Samurai">
    <div class="t-name">Samurai</div>
    <div class="t-artist">Lupe Fiasco</div>
    <a class="t-open" href="https://open.spotify.com/track/0wJw5QXDKXTYn8IVyh3wqz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="FIND GOD (feat. Dominic Fike) - Kenny Mason">
    <img src="https://i.scdn.co/image/ab67616d0000b273004cee1bd1f5e2c6adc8b7e8" alt="FIND GOD (feat. Dominic Fike)">
    <div class="t-name">FIND GOD (feat. Dominic Fike)</div>
    <div class="t-artist">Kenny Mason</div>
    <a class="t-open" href="https://open.spotify.com/track/51RDaTRAEHSitpeucJiHyU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Ottolenghi - Loyle Carner">
    <img src="https://i.scdn.co/image/ab67616d0000b273b8fc4ee31953f1133106d64a" alt="Ottolenghi">
    <div class="t-name">Ottolenghi</div>
    <div class="t-artist">Loyle Carner</div>
    <a class="t-open" href="https://open.spotify.com/track/64I9byMYBlS1ARsC3vtpgW" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Feel The Music - Guru">
    <img src="https://i.scdn.co/image/ab67616d0000b273f2571dd034e195686ea35958" alt="Feel The Music">
    <div class="t-name">Feel The Music</div>
    <div class="t-artist">Guru</div>
    <a class="t-open" href="https://open.spotify.com/track/77QvKUhVeyPVVHGFRgAmQd" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Feather - Nujabes">
    <img src="https://i.scdn.co/image/ab67616d0000b273421d647a4f604d79943f4dad" alt="Feather">
    <div class="t-name">Feather</div>
    <div class="t-artist">Nujabes</div>
    <a class="t-open" href="https://open.spotify.com/track/4aK4LNijbD7kkCg54UoIij" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="New Home (Slowed) - Austin Farwell">
    <img src="https://i.scdn.co/image/ab67616d0000b273e74e9e3b8b1d6be3b0c44052" alt="New Home (Slowed)">
    <div class="t-name">New Home (Slowed)</div>
    <div class="t-artist">Austin Farwell</div>
    <a class="t-open" href="https://open.spotify.com/track/6h6runZeeczWEuEW2pFvYW" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="氤氲之森 - CMJ">
    <img src="https://i.scdn.co/image/ab67616d0000b273b99bcb73660b15f214b6edc7" alt="氤氲之森">
    <div class="t-name">氤氲之森</div>
    <div class="t-artist">CMJ</div>
    <a class="t-open" href="https://open.spotify.com/track/4yGbLjBwaf0Ec1U9ilgOLl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  </div>
</div>

<!-- SPOTIFY_END -->

---

### 🌐 Social Links

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

</div>

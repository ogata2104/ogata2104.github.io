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
.threads-card .t-text-long {
  -webkit-line-clamp: 12;
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
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
      <div class="t-text t-text-long">コロナ禍のステイホーム期間中にFODで『北の国から』イッキ観しました。<br>ドラマシリーズやSPをリアタイでずっと追っかけてましたが、その時とはまた違う味わいや発見がありましたね。<br>純と蛍がその後、どんな人生を歩むかわかっているだけに、子供時代…</div>
    </div>
    <div class="t-date">2026-10-01 08:26</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Dd7gu2Xn_nk" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=a0UZWMfX3EEQ7kNvwFzOBpx&amp;_nc_oc=AdocnUv3n8YbxHufd38fWh0lXab48Vhc40f8-oW4b5xxYsfFrBo_GDdnbVGxQkFBnEc&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJ0m71qQrvV6Ot42aYolIr56HysY9-zTi304RgCscVGIC92NfPUBDaOso_aapvOO_FwO8w3GY9sMA&amp;oh=00_AQPZJtfOC0qlM2EYfHdGwk0NnGHbWwA4T6D4xweE7Xl8Aw&amp;oe=6AC41FEA" alt="" class="t-thumb">
      <div class="t-text">iOSアプリがクラッシュしまくり</div>
    </div>
    <div class="t-date">2026-09-29 10:32</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Dd2llzin-Xw" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
      <div class="t-text t-text-long">早稲田松竹で『鉄男』がかかるのね。<br>『ネルソンさん、あなたは人を殺しましたか？』で塚本晋也監督を知った人は是非観て欲しい。<br>CGが普及してなかった時代に一コマ一コマ丁寧に撮影された映像は、ある意味とても贅沢で豊かだし、今観ると手作りの温かみ…</div>
    </div>
    <div class="t-date">2026-09-23 00:59</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdmHNLQmo3G" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XKzfFEl38YkQ7kNvwHlh5gH&amp;_nc_oc=Adr3blG6kUCWWjDQJoufkn-sr21iY7L_n-y46m10Jx9lm39yivYbD6WdJOdznm-EOYg&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJizk7EaJ96JjleKjiD59T5WTncBt6YJIahPaflhXkRoYs3F9nkUra66xnNXcjWqHuqEWnLEnUmSg&amp;oh=00_AQNUxQLa_DxnK_nnjMF26UmwQkzatxflkj5xV5sW_F887A&amp;oe=6AC4135C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ZeI_-LxNkjYQ7kNvwG-87Yx&amp;_nc_oc=Adp8yTOCDZzvs3CEiijWyUlqhYWriGcgdDmwAj5yQxCh0v7xAikGRZ6g_QV0ZTdmFBs&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJeBJo2DfR9fXW6y5hKayKjAwWcDtIcagV9BvgYijtmFE1jJCA6WF5BXuUl8E89bbKJQnbv9wpozg&amp;oh=00_AQPtAVTFc2OAO0YleJ2gD9r18roIca5sktE-0tCe18Klxw&amp;oe=6AC42376" alt="" class="t-thumb">
      <div class="t-text">台風接近中の中、2年ぶりのTGS。<br>始発で行って雨の中2時間半並んだ甲斐あって、…</div>
    </div>
    <div class="t-date">2026-09-20 20:52</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Ddgha79ibTF" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/814470857_17988626214105617_8431201690405807241_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Z2oE1KUSr-0Q7kNvwGuEIGf&amp;_nc_oc=AdqKJDBiCyQmEEcptzhuW8w9fajNOzdatOlbWzFIqs0m5-QVd8g5dBmcMMEdf5flFEQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQKFtmUOcYp2gORYgvIAeiNBb47ztnMS9G6LI3p4JLxo3mdgfYmtfZx87uimW1AfqsGWYURuDvyYdw&amp;oh=00_AQPh0-xLKFSMY-0SxBgx9J8I_GDI6KlQWo0IBysSHXmo9g&amp;oe=6AC40540" alt="" class="t-thumb">
      <div class="t-text">TGS、月曜の最終日、開催中止になってしまった。</div>
    </div>
    <div class="t-date">2026-09-19 16:18</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdddPfhGhKv" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text t-text-long">とにかく各登場人物の「顔」に圧倒されます。今年の個人的顔映画オブザイヤーです。こんな凄い映画がなぜ都内で3館、全国でも9館でしか上映されないのか？この映画を広く公開されると何が不都合がある人でもいるのかな？などとメタな考察もしてみたり。音と…</div>
    </div>
    <div class="t-date">2026-09-17 12:08</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdX3D8Rmjnr" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f8f2fd; border-color: #ead9f5;">
    <div class="t-content">
      <div class="t-text t-text-long">Xで見かけたこちらの投稿を参考に、ベーマガのアーカイブからゲームプログラム部分のキャプチャーをClaude code入れたら、ちゃんとブラウザで遊べるゲームになった！まさか2026年にベーマガのゲームが遊び放題になるなんて思ってもみなかった…</div>
    </div>
    <div class="t-date">2026-09-14 21:43</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdRKfjQmlI_" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text t-text-long">夏は終わってなかったぜ</div>
    </div>
    <div class="t-date">2026-09-14 18:12</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdQySD3GlqJ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f8f2fd; border-color: #ead9f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/806474026_18633008524027991_8051060962185525360_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=qNbZVlS3nWAQ7kNvwENtJsK&amp;_nc_oc=AdqHW7N4l4Q0kM0QnoGW4LB_eC9hUhreEA5kchZBsiVIVkHbY77fQK5cxhFJRwhSO9M&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQL7OFJAzZlTIB2rnV5lMWoFnZvKgUWDyr7OLRCmaMQkOTh_-R9bJY_FWpZ3AJC9fOhrsd6gBY2U8A&amp;oh=00_AQP6dyEmrK-vA7J-eGGWCKmrf07Sz7RC5FNBZP2eHEhRDw&amp;oe=6AC40770" alt="" class="t-thumb">
      <div class="t-text">『バックルームズ』観たよ。<br>この手のはアタリハズレが大きいよなぁと観るまで不安で…</div>
    </div>
    <div class="t-date">2026-09-12 22:30</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdMGQCeidgZ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/802988973_18632299381027991_6271974641923046696_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=5imL8VEzU4sQ7kNvwGFXOVk&amp;_nc_oc=Adqk01aRk_EQwcVE3y8zYa5XfS-BS-ZWHaOHK8uBEYSzXwuK05yw78hkmryMM63VzcQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQIA1tJPOyDcx-Xp4RPVQKjXJmUo4KiyntJJqT_S5tYyzkl_Mh7EIwViRXeXsJrNqlbr1CDl2GefXg&amp;oh=00_AQMwNgTf4ngGvy1hSoKup3snv7eZQmM0lrKrQUm1UDCl8w&amp;oe=6AC40D25" alt="" class="t-thumb">
      <div class="t-text">きらくのきろく<br>#渋谷系</div>
    </div>
    <div class="t-date">2026-09-10 22:52</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdG_Hj9gbkO" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
      <div class="t-text t-text-long">トルネコは買います。<br>iPhoneは買いません。</div>
    </div>
    <div class="t-date">2026-09-10 12:01</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdF0rs0mvCa" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
      <div class="t-text t-text-long">トルネコ！</div>
    </div>
    <div class="t-date">2026-09-09 23:41</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DdEf7H1Grsd" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/798316686_18630761044027991_9137306186417153623_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=LBrrf-zi3RgQ7kNvwFjahwW&amp;_nc_oc=Ado2zgrqr3A7h0MH4AcxCe_zo8eJX-cIphh_WtMRLzvufWjAvVKCAzCnLmVjBJEK6ds&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQLQ0EQ6N1DUu-_7JkI4r05dLIKCC4XiK3123ZnEbm11oqAkRqf3QbhZitUZVOaAh7jDrOvdm_Js3g&amp;oh=00_AQMH5shjMAuJwlBWy2eCx0dFkapWcfNnKX043h7GC9f8hg&amp;oe=6AC40A5D" alt="" class="t-thumb">
      <div class="t-text">今年のふぐ会も美味しゅうございました。<br>#ふぐ</div>
    </div>
    <div class="t-date">2026-09-06 09:56</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/Dc7TLSSiUrT" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/790301302_18628965418027991_3733784461889033592_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=xGg4UsXnVtQQ7kNvwGpSQCK&amp;_nc_oc=Adrl3Hg2aLDy2VtGIPTrmEfUp_PwHg2LXvVQPB3AuF7PDH8qt6pUDHSNrJp3XVoVOy0&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJobwTKL0SQ80MYKUnwIRoHTFz7T1h6ZAgoIsPWxY6wkFXgcQf_H5pHhKh-flH-W0QLlFnKHq9DJQ&amp;oh=00_AQOfTfYvFACkPZueMLQE8MgocCIjAFOijWCuJ6RMY4deSg&amp;oe=6AC4215D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-09-01 01:05</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcteedrCfKo" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/787435258_18627554014027991_6823652663317638022_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=zA5TmKbAl1cQ7kNvwE05DK2&amp;_nc_oc=AdqZaUSzAYDSjgOUDl-5synGc-E66UJ-OsA_4zGinWp9xxz1FUXKvof9ki6tjcisr-A&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJZh9bsDC28OvFGRHFHkaYMVpaRgH4359D7ZXkQ-4JFLY4vVS5RmYtObJK_P8EO53-8O-OnlprwKQ&amp;oh=00_AQPoArlr4XHMt2_LTzohGG5J_OuFFAVVtE3sI8kwpJVUDQ&amp;oe=6AC4255E" alt="" class="t-thumb">
      <div class="t-text">#10年前はラッパー <br>10年以上前だけどね<br>#splatoon3 <br>#spla…</div>
    </div>
    <div class="t-date">2026-08-28 00:25</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcjGqB8gXnJ" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/777352697_18625074976027991_6709459502108065474_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Mzye2UAmKhwQ7kNvwHZ8LK-&amp;_nc_oc=AdqIR1SRkmWi8D5oEfyATsHv0UCZi7gDPymCXHKRG9y5L4Ugj9kGuUCjfPViID-5clk&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQI7_-_c9dxmH9lEM2rghRxLSqL6czeRp5Cuef0kXHa9fOuKaCxI7cmNFU9J9_nP-ys2eRoqhVYa4Q&amp;oh=00_AQNAtaLcHtPr5pCAVFtcx82knFndoGq93rSnUgjSLiuIaA&amp;oe=6AC419BD" alt="" class="t-thumb">
      <div class="t-text">久々に「買い物」をした。<br>#楳図かずお <br>#まことちゃん <br>#墓場の画廊 <br>#俺…</div>
    </div>
    <div class="t-date">2026-08-20 20:31</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcQqVHDCb9r" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/777382070_18624987067027991_7389481295785245777_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=bEuEJdW9B9EQ7kNvwF_Sws7&amp;_nc_oc=AdpzwZ8W6wcJZqXXvszajl3scpqotfoXB-gbhsNjRKnHxWxCdeUXe2XNRbYOEd9F7jY&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQJO4x6OkOGF1IWYr8md9Y-i4fXY6wUuFio5bWO2q3A3LJHGntKpakskgcrK68jtMbYfrUlvU-xAZQ&amp;oh=00_AQNGdks9NJG316ir_1R98DNg6U0I_OfkKYwWz_aHbXCRlg&amp;oe=6AC41A14" alt="" class="t-thumb">
      <div class="t-text">久々に中野で降りた。<br>駅周辺でゴリゴリ開発しているのを横目に圧倒的威厳で聳え立つ…</div>
    </div>
    <div class="t-date">2026-08-20 13:47</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcP8FCtn64L" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #fdf2f2; border-color: #f5dede;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/777328276_18623817964027991_7021757795281075069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=vKPjXkF4bRMQ7kNvwEabwPl&amp;_nc_oc=AdqTpfosEDg8annCwJh8LVLP3yi6hkGctBLmn-9TtBaduyRLKvijLTVOy_60O68ndBQ&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=ACx9VUEEAAAA&amp;_nc_gid=MiXSvR0sf1xQbTUfTgjKtA&amp;_nc_tpa=Q5bMBQIoZ7RzXdiYsrQBWj8Tfl_TxHS5T7YaBkakp-gQ2Gp7j_LbJmxnXBCeujOo5AK7av7YrddL6Ppipg&amp;oh=00_AQMblnxxvcK5qZfyKtkKt5hkYXW6w_a7ZBcgja1MPU8H7g&amp;oe=6AC41B83" alt="" class="t-thumb">
      <div class="t-text">ちいかわリテラシーが低かったせいか、映画が難解過ぎたので、再挑戦に向けて猛勉強中…</div>
    </div>
    <div class="t-date">2026-08-17 21:10</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcJAc5ygbPf" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
      <div class="t-text t-text-long">コンプラや現代の価値観云々などから、昔のドラマや映画が地上波TVで放映しづらくなってる昨今、40年以上前のアニメーション映画が普通に放映されていることはシンプルにすごいことだと思う。</div>
    </div>
    <div class="t-date">2026-08-15 02:31</div>
    <a class="t-external" href="https://www.threads.com/@ogata2104/post/DcB20SHGgKt" target="_blank" rel="noopener noreferrer" aria-label="元の投稿を見る" title="元の投稿を見る">
      <img src="https://cdn.simpleicons.org/threads/%23000000" alt="">
    </a>
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
  <div class="spotify-card" title="夏風ペダル - Ryo Gakucho">
    <img src="https://i.scdn.co/image/ab67616d0000b273ac17858e9fe0167c7a5d3707" alt="夏風ペダル">
    <div class="t-name">夏風ペダル</div>
    <div class="t-artist">Ryo Gakucho</div>
    <a class="t-open" href="https://open.spotify.com/track/5YrYIo7utkX0Ulhf1FjKkc" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Call On Me - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b2735f0f3b769d9bafee041cb8c1" alt="Call On Me">
    <div class="t-name">Call On Me</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/1G32fy7VMCDLl92iGXvBEm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Any Time, Any Place - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b273e63518d50aff63f57d2b8ead" alt="Any Time, Any Place">
    <div class="t-name">Any Time, Any Place</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/2yOm4lN7aTygtXanJFNFWU" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Got &#x27;Til It&#x27;s Gone - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b2732416d363e4220c21c5454efe" alt="Got &#x27;Til It&#x27;s Gone">
    <div class="t-name">Got &#x27;Til It&#x27;s Gone</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/1EhvYd5e7vkoN3udEN1Vyl" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Together Again - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b2732416d363e4220c21c5454efe" alt="Together Again">
    <div class="t-name">Together Again</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/1aJnGme5ZRltYTp8FJ52eZ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="All For You - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b27312da16fd0dec009d45f7dca3" alt="All For You">
    <div class="t-name">All For You</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/5X8kkUaUlAyAUr9TYqDFTH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="That&#x27;s The Way Love Goes - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b273e63518d50aff63f57d2b8ead" alt="That&#x27;s The Way Love Goes">
    <div class="t-name">That&#x27;s The Way Love Goes</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/29rQJydAlO0uMyWvRIZxQg" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Scream - Michael Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b273b4a878f008a0eda552446701" alt="Scream">
    <div class="t-name">Scream</div>
    <div class="t-artist">Michael Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/4LD5dhQ3kqpqe14sGPDtBC" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Someone To Call My Lover - Janet Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b27312da16fd0dec009d45f7dca3" alt="Someone To Call My Lover">
    <div class="t-name">Someone To Call My Lover</div>
    <div class="t-artist">Janet Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/43zr9kKkeiQrshvYuvNtfM" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Baby Come Back - Player">
    <img src="https://i.scdn.co/image/ab67616d0000b27381eae9a98487ae512df29469" alt="Baby Come Back">
    <div class="t-name">Baby Come Back</div>
    <div class="t-artist">Player</div>
    <a class="t-open" href="https://open.spotify.com/track/41sGGCCoHI2GLV9qadX80A" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Ride Like the Wind - Christopher Cross">
    <img src="https://i.scdn.co/image/ab67616d0000b27330b2be1b59f27ee3527fe643" alt="Ride Like the Wind">
    <div class="t-name">Ride Like the Wind</div>
    <div class="t-artist">Christopher Cross</div>
    <a class="t-open" href="https://open.spotify.com/track/7gUMShP1l20tC0xf17Zplk" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Give Me the Night - George Benson">
    <img src="https://i.scdn.co/image/ab67616d0000b2739877c2b01fca3367809f9e27" alt="Give Me the Night">
    <div class="t-name">Give Me the Night</div>
    <div class="t-artist">George Benson</div>
    <a class="t-open" href="https://open.spotify.com/track/5gaUkg5JNk8c4mr2jnpX8H" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Just the Two of Us (feat. Bill Withers) - Edit - Grover Washington, Jr.">
    <img src="https://i.scdn.co/image/ab67616d0000b273f8560af696925c50080dcc35" alt="Just the Two of Us (feat. Bill Withers) - Edit">
    <div class="t-name">Just the Two of Us (feat. Bill Withers) - Edit</div>
    <div class="t-artist">Grover Washington, Jr.</div>
    <a class="t-open" href="https://open.spotify.com/track/2tH28YyKYOldxhuBHoI79M" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="What a Fool Believes - The Doobie Brothers">
    <img src="https://i.scdn.co/image/ab67616d0000b273ba6340ac3b1653b6ea0e5da5" alt="What a Fool Believes">
    <div class="t-name">What a Fool Believes</div>
    <div class="t-artist">The Doobie Brothers</div>
    <a class="t-open" href="https://open.spotify.com/track/2yBVeksU2EtrPJbTu4ZslK" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Worth It. - RAYE">
    <img src="https://i.scdn.co/image/ab67616d0000b27394e5237ce925531dbb38e75f" alt="Worth It.">
    <div class="t-name">Worth It.</div>
    <div class="t-artist">RAYE</div>
    <a class="t-open" href="https://open.spotify.com/track/7JgNAnCjJvL8hBR1kmCOFF" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Dreamin&#x27; - Radio Mix - Christopher Williams">
    <img src="https://i.scdn.co/image/ab67616d0000b2738b2a17aea2445bdff19ea620" alt="Dreamin&#x27; - Radio Mix">
    <div class="t-name">Dreamin&#x27; - Radio Mix</div>
    <div class="t-artist">Christopher Williams</div>
    <a class="t-open" href="https://open.spotify.com/track/6nhrMTQT2ehVD7mFESk82D" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Rub You The Right Way - Extended Hype 1 - Johnny Gill">
    <img src="https://i.scdn.co/image/ab67616d0000b273740c6c9566460da3cf614f50" alt="Rub You The Right Way - Extended Hype 1">
    <div class="t-name">Rub You The Right Way - Extended Hype 1</div>
    <div class="t-artist">Johnny Gill</div>
    <a class="t-open" href="https://open.spotify.com/track/0SvAJbrDvE9Rk4DcS0nPfz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Feels Good - Tony! Toni! Toné!">
    <img src="https://i.scdn.co/image/ab67616d0000b2737d0fa81881e9313e77463eaa" alt="Feels Good">
    <div class="t-name">Feels Good</div>
    <div class="t-artist">Tony! Toni! Toné!</div>
    <a class="t-open" href="https://open.spotify.com/track/4cRR2gUTOerkUOW5iZpm91" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Kicking It - After 7">
    <img src="https://i.scdn.co/image/ab67616d0000b2736f96aad749cb6d09d4fe8394" alt="Kicking It">
    <div class="t-name">Kicking It</div>
    <div class="t-artist">After 7</div>
    <a class="t-open" href="https://open.spotify.com/track/43W4SFa3gwUMc37y9HArAd" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

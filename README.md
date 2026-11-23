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
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/921586103_18658804939027991_6808657905146015000_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=rXuRZJrsXnkQ7kNvwEYA8Gq&amp;_nc_oc=AdoGt7LXLmHgJnzv0GW5wPvTFGQwJa3sAvf2I67Tat5AeunDYhzRLYHRREKSDQSMkXM&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQLttKadSQH4VzuQl2S6r6fT80mEYDQVd7IU9LjIM-4yWAox7LaEv6iOLvqgeE0c5WkB-FCjugKHzQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQxMMmpiJYFnTZKJY-i8zZteD7A2rdMudk6J99zEScxBQ&amp;oe=6B090305" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=EUp1yF6oXZkQ7kNvwErn6zt&amp;_nc_oc=AdpDBATWKHaAIbTU7Uces1pygk4g6YvQp688JpfSoCwL7eaPyEenmKXuuP9ewmY0asI&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQIQn9MmtX6pcQRgc8TZf2Og8w64m_4Ro8TeBM7zRWO4Le4xD6LLPg_6HeFVIQCwC0PgRWphr1aC2A&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQBa438uEKZu6-5cdXt9YhdpyqL9RmPbP_q58OW9l7ObQ&amp;oe=6B091465" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MyScwFbb7WoQ7kNvwF8WrpL&amp;_nc_oc=AdrR1UeiQ8yYaunpYZja9141xsYvkIE2hOVVUEgC9MSo-g1YzwC1lR6Tb_WeiGSzEvY&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQJPXza4mGFJKQ-3Fu1cBdqzJaYv4O8h_-tGt-9R3aQbi5Enesv1Q2Cj3e9blj97Z0mLuiwcA9GaFg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTEviJ0n9iELIsX4PhMxU5SFqCMSWUBn84kLWDUJs5HHQ&amp;oe=6B08EC5D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=5Ai76PbClGcQ7kNvwFOa4Xj&amp;_nc_oc=AdrhQZa1hHQdMt3lWrMH4YbC0A1fmjuV2SLycoZzeAcSLnOc6SaLf2f1T2fkid2TQRo&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQIt8-KdXFW6ykrL1q8RydoC3B215fFPuteJUPwKntK6bjEuwa6TIXYcEUTlkkaD9J6ZtSG5DT8xjw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSmE9vPuFPQPK9fZpJpy2uaxOuv6gUwHzEob0fHILmvsg&amp;oe=6B09071E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=zrvrjio-CpcQ7kNvwHYflAi&amp;_nc_oc=AdpSgUICJ8d5XW8HF622jZyde0MT-mzC87D5zNLDScaflbsqOd6lp8HtaQfR0L0-L2Y&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQIbvnlWS7gpHyAEU8gyRpIG-QYMxSQxRmkiEpymHKZwvqDaVLzFw2t1GR1aC_ctYrHWH3wV-FZUKQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTKfLwSyMhGpBE8gdmeo3wzSj7NgYevPz1mL5ORRnlSSA&amp;oe=6B0905A5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=9YSLF_Ac-yQQ7kNvwGQMhki&amp;_nc_oc=Adrd13ACcy9c-q3_QGtQla9ZNxWCVxL77I0MkLMJPr1n4V-tewkVs6xSK20QxGkSDEw&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQK6NN9fOViKB-Gs51I462TWdsaNu-Xb9e_6ua5od7NtqUfHFb4osNS0ccR_7ru2uK6oh__TSi9AIA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQFslaOV_vT5E3RDeVqZVUomQheCin3KVtpaWEwcdOLWQ&amp;oe=6B090719" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=eIqcC5m-AWEQ7kNvwG3-z-U&amp;_nc_oc=AdoozJS3OancXTDzv4PSWQTmipXJrXaSNtsknMLC-IlPeDo3dbVGSI08Yo46tEiToF8&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQKv9kXYjEsYszq-u1p1mRdAOm-M4JPU0Fikg8FpaxIMSwNlf9HbxFZwcGGsWneqk8EZVAMnsCLmnQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQaV_pNeS-xpKRO1qOUKe2IHk_Ik6rMUStKEdLd9w8rwA&amp;oe=6B09042E" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hzeG_bN-E-IQ7kNvwGvNna9&amp;_nc_oc=AdqktRNfvcJakrASBDuOlmvfSKUEm013AuZTtqG151CelN21M1sLf2ts7_-80uutza0&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQKBurpD_MYy7chloT2qxtk1cOYVro2ZJn7ubmOfqDX0s4u2FX_YN6yv7zCjzYR0Tut2pDnnuTV33w&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ3YGMrc_UvWNaS-uobGKNLU6JfqA5zkfYvWVSPDYSuLQ&amp;oe=6B09079E" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-Oo3nH0uvZUQ7kNvwHdfXOK&amp;_nc_oc=Adq70MJQ9t2am_dGcb1FqTeRtqYtdWaKQ-xF2UcB9yRM8I80m4eEl4jH2eHaGzJz6Hs&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQIsTDKVNhcfSUp7Ih0YBKGSIXlBe1nUWpyOIEJV5apDVyvDpu3jFtL-nToxa4uSCczTB-haPaq6_g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRWg7qD0NGn0u5TNEzXu7dmuJty_rf8U2U6BERfe7BJDw&amp;oe=6B091875" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=kZrOmlk3180Q7kNvwGGbA7U&amp;_nc_oc=AdpVPBilA5fX_6MjZbzieoZRanQQ0_24ZsgJzR0T6e5eLnF_c0e6iTIUdwYtss8dLcg&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQKd79i3-GAy0QjM7Jx7afC7il49PfoF8sofwC8DkcZwrbQMHkQJuUkLoU50HzYZGhjSLpvL-qqnCg&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTK3qmH8qouYeoBzskoXcUY_WH4F9nW-qjdQrJgWZJqtQ&amp;oe=6B0903F6" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=aByTwbk48ugQ7kNvwEw3mec&amp;_nc_oc=Adp1La7tKH9zDg31ifivPXee4cfDStWAoY8zQ391cWymcsDmkl50JUmQOiwnwqoZ_IY&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQK2j3WcWRBGnxJZakv53ELLm8ncDvckthfr_rgyxFxEbAaQ2Y5z1DyD1xb6rlQfTatN-xmKMEZiLw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTg6Pvcm7dJMy_HRrbDUx10KogQ4RR7jV3ouQCUkoY5UA&amp;oe=6B091426" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=BMhmi_2p-LMQ7kNvwF3zXUL&amp;_nc_oc=AdpmYpu2Jb2VWYwkq4h-Qyt5IThL_AArvr8CCv5X0Bu9qndYH-NKNIXJZRMWF5FhpQE&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQKOykZKyxEjmGYNY3qv1wjWOadKFO37XkkPE48GruFofk-LT9Oz3CV5PYDpOKYVztlKB7hWnnBcIw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQREOl74E-mayCcENgMlXUCOFVe0WIL3iligcBp-N2UHmw&amp;oe=6B090741" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=fbRJmrSwkvsQ7kNvwGRU8Ie&amp;_nc_oc=AdoPPjJe4wWjbWLUgxgQa-VSWOaPe6MIMsLZ-CDElXTrEkTZTgLedgkaPOfyaXIX18g&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQK3VZoEm6CaVXhRkyxBfZyowl5sU49k8_f1Pat4vjtXr4gGrmZHbJ1pfRtJXps4dl7_h8UolanifA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS3Udn5sSIROsUUuQgu0FXFJGMn8RAjsWFqWEpxZwFdsA&amp;oe=6B09079F" alt="" class="t-thumb">
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
    <img src="https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7yJnJhoQJmIQ7kNvwHYmmvP&amp;_nc_oc=Adqf-h_pxV9gp2SAzDszf50shefngZYhgDCCtPxmxcQtZJDX55akiRP3KuWaC2iBQeI&amp;_nc_zt=23&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQIdL9EPDABGQHHTlaWAJU59OZBl4wBdppJbZu9iqZbXhMQmeNeL9QFY0NjncLvj6fw3ieSNUFIwPw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS6Tv0HAzAbk0HDrIYy_OxpwZIZNER9oxvbioVP724JKw&amp;oe=6B08E62A" alt="" class="t-thumb">
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
    <img src="https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=_EHfebc1SeIQ7kNvwGwCq-Q&amp;_nc_oc=AdqxwE7KD6RFJwqSnS5QlggtpHoH5BdW8nJr3TbujDixmssCcqYrALdoUd0T8C9Kge4&amp;_nc_zt=23&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=NnjMLmxhsTntn6Xu5v6pkQ&amp;_nc_tpa=Q5bMBQJgFdJ15S_ps8Q9OR92arwSlW5oaT8s76NUxpWliN1CsVSoLwg5PCHttJ050Ra85lQjzTaHWgD4sQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQS69aSKT_r4hnuWKe9_5JIOJAdWC3vFAmM8ssFFRGExAg&amp;oe=6B0911DC" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
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
  <div class="spotify-card" title="TECHNOVA - TOWA TEI">
    <img src="https://i.scdn.co/image/ab67616d0000b273f7e2dc293bed7503de291791" alt="TECHNOVA">
    <div class="t-name">TECHNOVA</div>
    <div class="t-artist">TOWA TEI</div>
    <a class="t-open" href="https://open.spotify.com/track/1e2M83FZ6T13KjSFSWpNmg" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Life Or Death - Magnus Ferrell">
    <img src="https://i.scdn.co/image/ab67616d0000b2735468ec8cc5d91166e7536b55" alt="Life Or Death">
    <div class="t-name">Life Or Death</div>
    <div class="t-artist">Magnus Ferrell</div>
    <a class="t-open" href="https://open.spotify.com/track/1Z6GBZOuKQIVGpb5An51Up" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="蛍の光 - TENDER SOUND JAPAN">
    <img src="https://i.scdn.co/image/ab67616d0000b273aaf119edbf565b38d92e339a" alt="蛍の光">
    <div class="t-name">蛍の光</div>
    <div class="t-artist">TENDER SOUND JAPAN</div>
    <a class="t-open" href="https://open.spotify.com/track/1O4Ydqe6JZQq3DpO33l1w8" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="P.Y.T. (Pretty Young Thing) - Michael Jackson">
    <img src="https://i.scdn.co/image/ab67616d0000b27332a7d87248d1b75463483df5" alt="P.Y.T. (Pretty Young Thing)">
    <div class="t-name">P.Y.T. (Pretty Young Thing)</div>
    <div class="t-artist">Michael Jackson</div>
    <a class="t-open" href="https://open.spotify.com/track/1CgmY8fVN7kstVDZmsdM5k" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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
  <div class="spotify-card" title="Feelz - Yelloo Hill">
    <img src="https://i.scdn.co/image/ab67616d0000b2732f3193129b16e1e8766db53c" alt="Feelz">
    <div class="t-name">Feelz</div>
    <div class="t-artist">Yelloo Hill</div>
    <a class="t-open" href="https://open.spotify.com/track/110dGMGjs2nFHC2pTurMB4" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="California Dreamin&#x27; - The Mamas &amp; The Papas">
    <img src="https://i.scdn.co/image/ab67616d0000b273cbd56c3a8faf8cf8c8bea0df" alt="California Dreamin&#x27;">
    <div class="t-name">California Dreamin&#x27;</div>
    <div class="t-artist">The Mamas &amp; The Papas</div>
    <a class="t-open" href="https://open.spotify.com/track/1ZEOIhSn6BKErV59bIgn76" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
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

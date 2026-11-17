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
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/904749021_18656931739027991_433454879039659302_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=ukxcv0m3Rj0Q7kNvwGtmqJA&amp;_nc_oc=AdqzzvvKogIL5J3ksoznwuQxGtgEw11GFh6zjjYJv96HT92lxcocK-EPkv4O57mziDo&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQI_t_IKn9z6Hz_wCmj1pm6UOEbTq7pV4-oYW0OG71GsEWis80_iFErKDUez9dxX78djhGXUy2TJnA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTWtTm094oUQDzX8ajjPO4ZLxLg0hu1BUH6myYbAyxxyA&amp;oe=6B0244A5" alt="" class="t-thumb">
      <div class="t-text">14日から始まってたガチャ。ダメ元で行ってみたら残り3個。どれが出てもいいやと思…</div>
    </div>
    <div class="t-date">2026-11-16 21:02</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfzT4JfAQLM" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f2f6fd; border-color: #dde8f5;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/898101417_18654497953027991_6536157268058947321_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=XE0KclzW5xUQ7kNvwHFMf5G&amp;_nc_oc=AdrXqBlg2jP09LPD5DsOyM5Ut_e3rpvOSTIybE_LvAtMM3jTos1_GUzSKYrU5JGoEeA&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQIBv9cuRenVZgA8ck_F3JK7gObPcdxw3CcTZQMmXI5KKSSGoH_EyUxnxcqL2zWudZXHP48k1fdwQQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQT7RKFWNv3Ju0Ja9fav2HFzaZvFoYLRbkCzWxxNlUCiqA&amp;oe=6B021C9D" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-11-10 00:51</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfhshWviXqk" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/893633443_18653981236027991_7236061296758598069_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=104&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Ok-cGax8GA4Q7kNvwGLdrJH&amp;_nc_oc=AdrQQ0iwWwHfHea8HB9U5BITE8LweL6Y4YOEIexpklvKdVSWBhCDN-_rFNJvVDB53Ew&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQIhEq94Sdvh5YnMqMbDloEqkFdoVty0SDD9mDS3xILb_U69Xhrzx-xQzNrTf6m4So7zwej2SLV4HA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRVXZ4esEB20q_OAaCWyQAjIaoWh1KsyPZUdkyyRuIxUQ&amp;oe=6B02375E" alt="" class="t-thumb">
      <div class="t-text">杉並麺博で荻窪の手もみラーメン十八番とラーメン久保田のコラボラーメン頂いてきまし…</div>
    </div>
    <div class="t-date">2026-11-08 13:49</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dfd78ErAeU3" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/893731854_18653757709027991_7505637550548605648_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=101&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4P2NmKQR0ZoQ7kNvwHcY3i4&amp;_nc_oc=AdoPbbi3VSyyXAcrpXuPUHQ4Z9SiMBN5J70PEMys8cPHkBUdAU8R0kIVhPyHPPky2rE&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQLRhAXsU9dvcs2f6jj9NWYP7ef_BXkjneqGiSiywNGnr-tGw_a8tXfI0fis6LejYfOtDsXghC-hIQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSjYImxI-Gh-vMUIRD8jCRGb6nVCUkVlAKwrwQNoLJUjA&amp;oe=6B0235E5" alt="" class="t-thumb">
      <div class="t-text">「彼女じゃないですデートじゃないです」のフレーズが面白くて、最近よく動画を観てし…</div>
    </div>
    <div class="t-date">2026-11-07 23:05</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfcWxybCa6a" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/867635185_18651044143027991_4608932839270804387_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=103&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=CiC_u11QyUIQ7kNvwFXR0kS&amp;_nc_oc=Adq3EkCE8BONiPxiaBhf8sPcbwvKzIuuKGo59f6PlTbvAVYUEQ5rP9C-2JGBE--TdCM&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQJqBsmVZEnzY6KsvhVpGElKyRNntC1fRZ9eZi7ttYA3ODNsfPgBC-Hs54bSPuunhp_6bGXovJnW0Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTgcCzQap2256y-M38OAysOaIORy56znFp42aU_wjPs7w&amp;oe=6B023759" alt="" class="t-thumb">
      <div class="t-text">吉祥寺のドムドムバーガー、やっと来られた。<br>開店したばかりなのでまあまあ混んでた…</div>
    </div>
    <div class="t-date">2026-10-31 19:27</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DfJ8My7iRe-" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/866048677_18649167214027991_4009439321067173636_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=106&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=7YsI9zT8BR0Q7kNvwHJmZOv&amp;_nc_oc=AdqSJQLiEpOLQM19HaaIA-sMAFD-GTHu6A1hVdE9hmSInoqq99EsNesEObpwBrEW2qM&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQIskFPixLtiZobEYaVWGocxs64EKxNlu3TVBnrYCPwsOSvlbf_qD9vjMTSZMjmIJ_iOUXGUym_ZXA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQFC-AUjQdCLTMoDJmKsR72nG8EHmZrgV3jHIdt25mIUA&amp;oe=6B02346E" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/859770126_18647590798027991_1999259896194795594_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=100&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=Rz4F_ge4AL8Q7kNvwERpY63&amp;_nc_oc=AdpNbkJXaDCL8a8004aDto2iZf9LrEkvREDSTXtlBpkZV_c8mZ1DF83-CLmqyuXSFqE&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQLX5l6rf5SFzI7YLFtOm0gBNJ2SQ1SZMyl7P7SukebPSU5Wm_R9VwC1jETvF_gWx6x5V9b9ArBarQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSuE9q47DIFCxwZB7_bav_xVVQ9RflcfFeEFrjM8hf1vw&amp;oe=6B0237DE" alt="" class="t-thumb">
      <div class="t-text">幻影（ビジョン）とクリスタルを巡る冒険に旅立ちます。<br>#ファイナルファンタジーレ…</div>
    </div>
    <div class="t-date">2026-10-22 20:24</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/Dey3o6VgY_A" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f0fbfa; border-color: #d7efec;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851718625_18646155523027991_6014022125073095588_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=110&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=f3XgNVFnN7EQ7kNvwHjB4jg&amp;_nc_oc=AdrftyuBK0wn8OEVH-gvoJhXwMh3QngBqQR0SDSSv-C6MJoEW5Q8azBp8ky10w-dS7E&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQL-lg81RozOvxebCEcEE_hLArka9gi1vj5NQXC_SvadNhHd_3L630QaGJ__JbIT-VBlSj81dAYPuw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTF6NF8SV8HFTtaPoKYwzEh1xpbPy5rDCLWXc_H2vXztA&amp;oe=6B0248B5" alt="" class="t-thumb">
      <div class="t-text">ここ最近、トイカメラに写っていたモノたち<br>#トイカメラ<br>#スリコトイカメラ <br>#…</div>
    </div>
    <div class="t-date">2026-10-18 19:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeohGsYFYtf" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf1f6; border-color: #f5d9e6;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/851459123_18645378745027991_6053858774232142271_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=MZ_n9EAlP5AQ7kNvwFCNrAM&amp;_nc_oc=AdpYxx3Il2BOk_tjhAkyP8cfWliOtLVzJfK4akxp64drR5dhTIUdPNNMV5ZjsNWF4zs&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQJp-XTWDCrGe5u2ezj-Ve3JCZZTaMt83hC7fnppCoEUHkEpq8U2DNl-ra26pYLP6iTzZgBY8aCNrQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSpOveTlr9yDCQfW1GLrqcZ-E46UpI42TtDop4dKuQJ6w&amp;oe=6B023436" alt="" class="t-thumb">
      <div class="t-text">初めての #南町田グランベリーパーク 。<br>楽しいところですね！<br>そして、やはりサ…</div>
    </div>
    <div class="t-date">2026-10-16 22:55</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DejsFkylRBW" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdfaf0; border-color: #f5ecd0;">
    <div class="t-content">
    <img src="https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/844890011_18645131539027991_5892416747751645589_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=6J1dNTaPjzIQ7kNvwEAE1Gq&amp;_nc_oc=AdqWGHVKjgdR1eIiTeHu-tTuSkMoDu-mwngrAFwtKvQJVXGXZQEbhlwTMQjBOmDQJNM&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQLqczGXhGoh73aXhv2yEiracZNOSr2__A4U3uqNvNUl49hlB8otqT5P1PFV36DXLrI5Zz1PXo8m0g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQRYSEJkS3qBfLAkkE9t9pq0zk5GKS4AJD9tidev3FNBjg&amp;oe=6B024466" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/837632219_18640785406027991_3004173811934432104_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=4-6g72QQ6fsQ7kNvwE7I_Z-&amp;_nc_oc=Ado3fnYDUsjke8qMSLuqx7owlzbuAe90IuI8QAsJ0C7n3MUpdhUoSLbhTGIEfUDlYco&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQIlPZo3_aOOd2o7cbt-G4Ss8Zbx2UqpeHN5r3h3naO616VarrJ2uh6trKoi3syJzXnuqyOvxdMN4g&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQDsbc31Vpl4LyoDeRb-iKkPaT-PfDEIO6jaTWrc665wQ&amp;oe=6B023781" alt="" class="t-thumb">
      <div class="t-text">監督スティーブン・スピルバーグ、音楽ジョン・ウィリアムズで◯◯◯モノって何故今w…</div>
    </div>
    <div class="t-date">2026-10-04 20:54</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DeEkvVRgb9R" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #f3fbf3; border-color: #ddefdd;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/835657708_18640424515027991_1173341551165914443_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=105&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=2paT3Tc7WCsQ7kNvwFlh3py&amp;_nc_oc=AdoaX4uNAnNTV-7uyGSAteVYJf4eyU7WRDWnUs98Nw7JFT8rKyiF4woyrbjZ76GdaHA&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQKFhC5PTJMphgLV8LAakeRf9Hw8qbzF8QFzQs4ughleIA3YdQdLDsWVX50ja5ZZzcyE9Ejaoged0Q&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSBNKvWUZ7IwRpjH1HRon8XEZ2MQduw_V8BfZm87NR0ww&amp;oe=6B0237DF" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/829380911_17989954749105617_4062963381675522656_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=108&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=-306fbG4B-kQ7kNvwEa1EHM&amp;_nc_oc=Adq1MrA1lJ9Z_PAqjoVF4cBPLS1Jd5jpo5iSsLTcJ7KcjPjPg6GOMMbNzhIf2yYLzkw&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQKx-H_9DAdTXH4uL6v9CtgH58M4xZtLZDw6cRv4xmCHNIP1RTLdZMciE7Qh1QDVf3YZcGG5lJGUyQ&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQQ7UPNNRtvYJ8wLuO9qFIOk2QS6dHpmMExFmZ1hIcVP-Q&amp;oe=6B024EAA" alt="" class="t-thumb">
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
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/796250294_18636321391027991_6360255075401647643_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=107&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=hGUrTmchzBAQ7kNvwHNd7uU&amp;_nc_oc=AdqPHyNUBSPPsYly-97H1nPmhB3VJuZ1zNk83pZpBQqJrcTNcy34mLYC45X5tAqyiO8&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQIEnAoQpB7HWNcr8sXTdKVulHywHFy642L3Ww9C3ECZXnzIuEsftmoFzD6hTsMban6mlBRlxnSiUA&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQSUd9MT1pD1C3YciaIcA29gSolmWWP7euaXlxbTmUmEtg&amp;oe=6B02421C" alt="" class="t-thumb">
      <div class="t-text">ゲーム内で沖縄満喫中のシルバーウィーク。<br>『ラヴ上等』シーズン2観た後に、『龍が…</div>
    </div>
    <div class="t-date">2026-09-22 08:16</div>
    <a class="t-open" href="https://www.threads.com/@ogata2104/post/DdkUcEQkwhQ" target="_blank" rel="noopener noreferrer">Threadsで表示 &#9654;</a>
  </div>
  <div class="threads-card" style="background-color: #fdf5ef; border-color: #f5e0cf;">
    <div class="t-content">
    <img src="https://scontent-sea5-2.cdninstagram.com/v/t51.82787-15/795485663_18635776435027991_9049835800620332632_n.jpg?stp=dst-jpg_e35_tt6&amp;_nc_cat=102&amp;_nc_map=urlgen_bucketless&amp;ccb=7-5&amp;_nc_sid=18de74&amp;efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&amp;_nc_ohc=tFaRz8mZovsQ7kNvwGTM8g1&amp;_nc_oc=AdpurdNx3DGD6dNFn8wO-coNqLnUYKqT07p00hravYJ3BR-3rFSN88prOl2U-qYfP6g&amp;_nc_zt=23&amp;_nc_ht=scontent-sea5-2.cdninstagram.com&amp;edm=AIMHve8EAAAA&amp;_nc_gid=ubNTlo13ZjdGwiCNmBNGxA&amp;_nc_tpa=Q5bMBQK3o3nv6jCINwVx_G8nKxm25vggIvuz6bzXT7n0XCus9NLB0opvtj__yrBp1UvF0yHHsa9t_xlwqw&amp;_nc_ct=RQosPBUKFQIAAAA&amp;oh=00_AQTLTfqm9j4604-ZbkG_uUaQj9fk_uJKfCzcLcMYMbrDAA&amp;oe=6B0219F6" alt="" class="t-thumb">
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
  <div class="spotify-card" title="Star Guitar - The Chemical Brothers">
    <img src="https://i.scdn.co/image/ab67616d0000b273a84e1d8c3a99de8e2e1e6c1a" alt="Star Guitar">
    <div class="t-name">Star Guitar</div>
    <div class="t-artist">The Chemical Brothers</div>
    <a class="t-open" href="https://open.spotify.com/track/19mC6xktT1JyyycK6cQaXA" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="福は内 鬼は外 (feat. The Mizuhara Sisters) - John Carroll Kirby">
    <img src="https://i.scdn.co/image/ab67616d0000b2739fa64012371b07ed31beaeb2" alt="福は内 鬼は外 (feat. The Mizuhara Sisters)">
    <div class="t-name">福は内 鬼は外 (feat. The Mizuhara Sisters)</div>
    <div class="t-artist">John Carroll Kirby</div>
    <a class="t-open" href="https://open.spotify.com/track/6hCjUu1CkVppX0ue6g8W0I" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="恋は桃色 - Pearl &amp; The Oysters">
    <img src="https://i.scdn.co/image/ab67616d0000b27373e7e22dbb7e19f39336cf56" alt="恋は桃色">
    <div class="t-name">恋は桃色</div>
    <div class="t-artist">Pearl &amp; The Oysters</div>
    <a class="t-open" href="https://open.spotify.com/track/6zEO7maDyQ0Y8NOLR0BQTS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="スポーツマン - 2019 Remastering - Haruomi Hosono">
    <img src="https://i.scdn.co/image/ab67616d0000b27340a8891322831968457944cb" alt="スポーツマン - 2019 Remastering">
    <div class="t-name">スポーツマン - 2019 Remastering</div>
    <div class="t-artist">Haruomi Hosono</div>
    <a class="t-open" href="https://open.spotify.com/track/5I8Ld9qUriIBoYISAaQUTt" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Heaven - Ebo Taylor">
    <img src="https://i.scdn.co/image/ab67616d0000b27395c2db41b2c8152cf9560504" alt="Heaven">
    <div class="t-name">Heaven</div>
    <div class="t-artist">Ebo Taylor</div>
    <a class="t-open" href="https://open.spotify.com/track/1XE4iQ35cADqpZeAOTmvOS" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Enjoy - Tekno">
    <img src="https://i.scdn.co/image/ab67616d0000b273956ada26d88a0e264a2f7535" alt="Enjoy">
    <div class="t-name">Enjoy</div>
    <div class="t-artist">Tekno</div>
    <a class="t-open" href="https://open.spotify.com/track/2S81GqH8jtb6ZUM0wrux4v" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Abraka - The Funkees">
    <img src="https://i.scdn.co/image/ab67616d0000b273d569d7877376c20c3cdc111b" alt="Abraka">
    <div class="t-name">Abraka</div>
    <div class="t-artist">The Funkees</div>
    <a class="t-open" href="https://open.spotify.com/track/1tzQYuBIeGuTwfCWh0yFKz" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Commas - Ayra Starr">
    <img src="https://i.scdn.co/image/ab67616d0000b273fa88b93bb6dde97f7258cdec" alt="Commas">
    <div class="t-name">Commas</div>
    <div class="t-artist">Ayra Starr</div>
    <a class="t-open" href="https://open.spotify.com/track/4GXW3Ne1jzdORKHvHjK31V" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Calm Down - Rema">
    <img src="https://i.scdn.co/image/ab67616d0000b273d68842aec8d8a5deec2c664c" alt="Calm Down">
    <div class="t-name">Calm Down</div>
    <div class="t-artist">Rema</div>
    <a class="t-open" href="https://open.spotify.com/track/2IwCg4vsBwWgbtSKnq38no" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Africa - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b273ebd6d20c0082524244ef83df" alt="Africa">
    <div class="t-name">Africa</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/2374M0fQpWi3dLnB54qaLX" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Reelin&#x27; In The Years - Steely Dan">
    <img src="https://i.scdn.co/image/ab67616d0000b2730ddd7e736f870994f4707947" alt="Reelin&#x27; In The Years">
    <div class="t-name">Reelin&#x27; In The Years</div>
    <div class="t-artist">Steely Dan</div>
    <a class="t-open" href="https://open.spotify.com/track/1x1XQqhBViz4opcpwc7FVs" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="Baby He&#x27;s Your Man - TOTO">
    <img src="https://i.scdn.co/image/ab67616d0000b27384bb3ed07820b1b818abd2c9" alt="Baby He&#x27;s Your Man">
    <div class="t-name">Baby He&#x27;s Your Man</div>
    <div class="t-artist">TOTO</div>
    <a class="t-open" href="https://open.spotify.com/track/5w2PPpREIfphI1XayqcxqH" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="サ上とロ吉 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273370f9c1c7fccc0b7d95d2b6b" alt="サ上とロ吉">
    <div class="t-name">サ上とロ吉</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/373WK4HGaoZ0n9n4oYGkKJ" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="PRINCE OF YOKOHAMA 2222 - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273a0ae148c841c81f9abc95d0c" alt="PRINCE OF YOKOHAMA 2222">
    <div class="t-name">PRINCE OF YOKOHAMA 2222</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/1UKOYk4ZVxIqeQjw9ENSfY" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27303e728a9ad440c4a7cfe1f49" alt="RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL">
    <div class="t-name">RUN AND GUN feat. LEON a.k.a. 獅子, DOLLARBILL</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/5HcQ7gGLdsxNxURUmJB1fm" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="The Three Musketeers Mic Relay - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b273825ca2f52579817a1828ece2" alt="The Three Musketeers Mic Relay">
    <div class="t-name">The Three Musketeers Mic Relay</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/3JFK10dXAHjv2zeJ0QTCYo" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
  </div>
  <div class="spotify-card" title="More &amp; More feat. ももいろクローバーZ - Cypress Ueno To Robert Yoshino">
    <img src="https://i.scdn.co/image/ab67616d0000b27355f8c188a6300394b31f101c" alt="More &amp; More feat. ももいろクローバーZ">
    <div class="t-name">More &amp; More feat. ももいろクローバーZ</div>
    <div class="t-artist">Cypress Ueno To Robert Yoshino</div>
    <a class="t-open" href="https://open.spotify.com/track/6tyDJit7oCemK3KXDXMCfh" target="_blank" rel="noopener noreferrer">Spotifyで再生 &#9654;</a>
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

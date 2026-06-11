(function () {
  "use strict";
  // TERMS and TALIAS are injected inline above this script.
  var tip = document.getElementById("tip");
  var tf = document.getElementById("tf");
  var tfBody = tf.querySelector(".tf-body");
  var tfClose = tf.querySelector(".tf-close");

  function resolve(k) {
    if (!k) return null;
    if (TERMS[k]) return TERMS[k];
    var a = TALIAS[k.toLowerCase()];
    if (a && TERMS[a]) return TERMS[a];
    for (var key in TERMS) { if (key.toLowerCase() === k.toLowerCase()) return TERMS[key]; }
    return null;
  }

  function esc(s) {
    return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  // -------- HOVER tooltip (short) --------
  function buildTip(t) {
    var h = '<div class="t-ko">' + esc(t.ko || t.key) + "</div>";
    if (t.en) h += '<div class="t-en">' + esc(t.en) + "</div>";
    if (t.category) h += '<div class="t-cat">' + esc(t.category) + "</div>";
    if (t.desc) h += '<div class="t-desc">' + esc(t.desc) + "</div>";
    if (t.formula) h += '<div class="t-formula">' + esc(t.formula) + "</div>";
    if (t.related && t.related.length)
      h += '<div class="t-rel">관련: ' + t.related.map(esc).join(", ") + "</div>";
    h += '<div class="t-rel" style="margin-top:6px;color:#5fe0bd">↻ 클릭하면 자체완결형 상세 풀이</div>';
    return h;
  }

  var curEl = null;
  function showTip(el, x, y) {
    var k = el.getAttribute("data-k");
    var t = resolve(k);
    if (!t) {
      tip.innerHTML = '<div class="t-ko">' + esc(k) + "</div><div class='t-desc'>(정의 없음)</div>";
    } else {
      tip.innerHTML = buildTip(t);
    }
    tip.classList.add("show");
    place(x, y);
  }
  function place(x, y) {
    var pad = 14, w = tip.offsetWidth, h = tip.offsetHeight;
    var left = x + 16, top = y + 18;
    if (left + w + pad > window.innerWidth) left = x - w - 16;
    if (left < pad) left = pad;
    if (top + h + pad > window.innerHeight) top = y - h - 16;
    if (top < pad) top = pad;
    tip.style.left = left + "px";
    tip.style.top = top + "px";
  }
  function hideTip() { tip.classList.remove("show"); curEl = null; }

  // -------- CLICK modal (self-contained) --------
  function buildTipFull(t, k) {
    var displayKo = esc(t.ko || k);
    var h = '<div class="tfh-ko">' + displayKo + '</div>';
    if (t.en) h += '<div class="tfh-en">' + esc(t.en) + '</div>';
    var meta = '';
    if (t.abbr && t.abbr !== "—") meta += '<span class="tfh-abbr">' + esc(t.abbr) + '</span>';
    if (t.category) meta += '<span class="tfh-cat">' + esc(t.category) + '</span>';
    if (meta) h += '<div class="tfh-meta">' + meta + '</div>';

    // primary description: prefer desc_full (self-contained extended) over short desc
    var primaryDesc = t.desc_full || t.desc;
    if (primaryDesc) {
      h += '<div class="tf-section first"><h5>설명</h5><p class="tf-desc">' + esc(primaryDesc) + '</p></div>';
    }
    if (t.formula) {
      h += '<div class="tf-section"><h5>수식</h5><pre class="tf-formula">' + esc(t.formula) + '</pre></div>';
    }

    // embedded_terms — the self-contained sub-glossary
    var emb = t.embedded_terms;
    if (emb && typeof emb === "object") {
      var keys = Object.keys(emb);
      if (keys.length) {
        var items = keys.map(function (ek) {
          return '<li><span class="ekey">' + esc(ek) + '</span><span class="edef">' + esc(emb[ek]) + '</span></li>';
        }).join("");
        h += '<div class="tf-section"><h5>설명 내 용어 풀이 (자체완결)</h5><ul class="tf-emb">' + items + '</ul></div>';
      } else {
        h += '<div class="tf-section"><h5>설명 내 용어 풀이</h5><p class="tf-empty">하위 용어 풀이가 비어 있습니다.</p></div>';
      }
    } else {
      h += '<div class="tf-section"><h5>설명 내 용어 풀이</h5><p class="tf-empty">(이 항목은 자체완결형 풀이가 아직 작성되지 않았습니다.)</p></div>';
    }

    // related — clickable to re-open modal
    if (t.related && t.related.length) {
      h += '<div class="tf-section"><h5>관련 용어</h5><p class="tf-rel">' +
        t.related.map(function (r) { return '<a data-jump="' + esc(r) + '">' + esc(r) + '</a>'; }).join(", ") + '</p></div>';
    }
    h += '<div class="tf-section"><h5>근거 기준</h5><p class="tf-source">이 용어 풀이는 기반 PDF <i>Technology Landscape Review of In-Sensor Photonic Intelligence</i>, 본문 Figure 1-11 해설, 원 논문 DOI <a href="https://doi.org/10.3390/aisens1010005" target="_blank" rel="noopener">10.3390/aisens1010005</a>, 그리고 연결된 reference 번호의 문맥을 기준으로 작성되었습니다.</p></div>';
    h += '<div class="tf-hint">ESC 또는 바깥 클릭으로 닫기</div>';
    return h;
  }
  function showFull(k) {
    var t = resolve(k);
    if (!t) {
      tfBody.innerHTML = '<div class="tfh-ko">' + esc(k) + '</div><p class="tf-empty">정의가 없습니다.</p>';
    } else {
      tfBody.innerHTML = buildTipFull(t, k);
    }
    hideTip();
    tf.classList.add("show");
    tf.scrollTop = 0;
    // focus close button for a11y
    setTimeout(function () { tfClose.focus(); }, 0);
  }
  function hideFull() { tf.classList.remove("show"); tfBody.innerHTML = ""; }

  // -------- event wiring --------
  document.addEventListener("mouseover", function (e) {
    var el = e.target.closest(".term");
    if (el && el !== curEl) { curEl = el; showTip(el, e.clientX, e.clientY); }
  });
  document.addEventListener("mousemove", function (e) {
    if (curEl && tip.classList.contains("show")) place(e.clientX, e.clientY);
  });
  document.addEventListener("mouseout", function (e) {
    var el = e.target.closest(".term");
    if (el && el === curEl) hideTip();
  });
  // keyboard accessibility: focus shows hover-style tip
  document.addEventListener("focusin", function (e) {
    var el = e.target.closest(".term");
    if (el) { var r = el.getBoundingClientRect(); curEl = el; showTip(el, r.left, r.bottom); }
  });
  document.addEventListener("focusout", function (e) {
    if (e.target.closest(".term")) hideTip();
  });
  // CLICK: open self-contained modal (instead of toggling hover tip)
  document.addEventListener("click", function (e) {
    // related-term anchor inside the modal: re-open with new key
    var jump = e.target.closest("[data-jump]");
    if (jump && tf.contains(jump)) {
      e.preventDefault();
      showFull(jump.getAttribute("data-jump"));
      return;
    }
    var el = e.target.closest(".term");
    if (el) {
      e.preventDefault();
      e.stopPropagation();
      showFull(el.getAttribute("data-k"));
    }
  });
  // close modal: click on backdrop or close button
  tf.addEventListener("click", function (e) {
    if (e.target === tf || e.target === tfClose) hideFull();
  });

  // lightbox (figure zoom)
  var lb = document.getElementById("lb"), lbimg = document.getElementById("lbimg");
  document.addEventListener("click", function (e) {
    if (tf.classList.contains("show")) return; // don't open lightbox while modal is open
    var img = e.target.closest("img.zoom");
    if (img) { lbimg.src = img.src; lb.classList.add("show"); }
  });
  lb.addEventListener("click", function () { lb.classList.remove("show"); lbimg.src = ""; });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (tf.classList.contains("show")) { hideFull(); return; }
      lb.classList.remove("show"); hideTip();
    }
  });

  // scrollspy for TOC
  var links = Array.prototype.slice.call(document.querySelectorAll("nav#toc a.figlink"));
  var map = {};
  links.forEach(function (a) { var id = a.getAttribute("href").slice(1); map[id] = a; });
  var secs = Array.prototype.slice.call(document.querySelectorAll("section.fig"));
  var obs = new IntersectionObserver(function (ents) {
    ents.forEach(function (en) {
      if (en.isIntersecting) {
        links.forEach(function (l) { l.classList.remove("active"); });
        if (map[en.target.id]) map[en.target.id].classList.add("active");
      }
    });
  }, { rootMargin: "-15% 0px -75% 0px", threshold: 0 });
  secs.forEach(function (s) { obs.observe(s); });

  // ===================== PRESENTATION (발표) MODE =====================
  var deck = document.getElementById("deck");
  var pop = document.getElementById("pop");
  if (deck && pop) {
    var stage = deck.querySelector(".deck-stage");
    var barFig = deck.querySelector(".deck-fig");
    var barKind = deck.querySelector(".deck-kind");
    var barCount = deck.querySelector(".deck-count");
    var progFill = deck.querySelector(".deck-progress-fill");
    var popInner = pop.querySelector(".pop-inner");
    var presentBtn = document.getElementById("present-btn");

    var slides = null, idx = 0, deckOpen = false, popOpen = false, popPanels = null, popIdx = 0;
    var NAV = { "ArrowRight": 1, "PageDown": 1, " ": 1, "ArrowLeft": -1, "PageUp": -1 };
    function navDelta(k) { return Object.prototype.hasOwnProperty.call(NAV, k) ? NAV[k] : 0; }

    function buildSlides() {
      if (slides) return;
      slides = [];
      secs.forEach(function (sec) {
        var num = (sec.querySelector(".fig-num") || {}).textContent || "";
        var title = (sec.querySelector(".fig-title") || {}).textContent || "";
        slides.push({ sec: sec, type: "overview", num: num, title: title });
        var panels = Array.prototype.slice.call(sec.querySelectorAll(".panel"));
        if (panels.length) slides.push({ sec: sec, type: "detail", num: num, title: title, panels: panels });
      });
    }

    function renderOverview(s) {
      var c = document.createElement("div"); c.className = "card card-overview";
      var ff = s.sec.querySelector(".figfull"); if (ff) c.appendChild(ff.cloneNode(true));
      var cap = s.sec.querySelector(".caption"); if (cap) c.appendChild(cap.cloneNode(true));
      var lead = s.sec.querySelector(".lead"); if (lead) c.appendChild(lead.cloneNode(true));
      stage.appendChild(c);
    }

    function renderDetail(s) {
      var c = document.createElement("div"); c.className = "card";
      var grid = document.createElement("div"); grid.className = "deck-panels";
      s.panels.forEach(function (panel, pi) {
        var thumb = document.createElement("button"); thumb.type = "button"; thumb.className = "deck-thumb";
        var img = panel.querySelector(".pimg img");
        if (img) { var im = img.cloneNode(true); im.classList.remove("zoom"); im.removeAttribute("loading"); thumb.appendChild(im); }
        var h4 = panel.querySelector(".ptext h4");
        if (h4) {
          var hc = h4.cloneNode(true);
          Array.prototype.forEach.call(hc.querySelectorAll(".term"), function (x) { x.classList.remove("term"); x.removeAttribute("data-k"); });
          var td = document.createElement("div"); td.className = "deck-thumb-title"; td.innerHTML = hc.innerHTML;
          thumb.appendChild(td);
        }
        var hint = document.createElement("div"); hint.className = "hintclick"; hint.textContent = "클릭하면 상세 해설";
        thumb.appendChild(hint);
        thumb.addEventListener("click", function () { openPopAt(s.panels, pi); });
        grid.appendChild(thumb);
      });
      c.appendChild(grid);
      stage.appendChild(c);
    }

    function render() {
      closePop();
      stage.innerHTML = "";
      var s = slides[idx];
      if (s.type === "overview") renderOverview(s); else renderDetail(s);
      barFig.textContent = (s.num ? s.num + " · " : "") + s.title;
      barKind.textContent = s.type === "overview" ? "개괄설명" : "상세설명";
      barKind.className = "deck-kind " + s.type;
      barCount.textContent = (idx + 1) + " / " + slides.length;
      progFill.style.width = ((idx + 1) / slides.length * 100) + "%";
      stage.scrollTop = 0;
    }

    function go(d) { var n = Math.min(slides.length - 1, Math.max(0, idx + d)); if (n !== idx) { idx = n; render(); } }
    function gotoIdx(n) { idx = Math.min(slides.length - 1, Math.max(0, n)); render(); }

    function startIndex() {
      var y = window.scrollY + 90, best = secs[0];
      secs.forEach(function (sec) { if (sec.offsetTop <= y) best = sec; });
      for (var i = 0; i < slides.length; i++) if (slides[i].sec === best && slides[i].type === "overview") return i;
      return 0;
    }

    function openPopAt(panels, i) {
      popPanels = panels;
      popIdx = Math.min(panels.length - 1, Math.max(0, i));
      renderPanel();
      pop.classList.add("show"); pop.setAttribute("aria-hidden", "false"); popOpen = true;
    }
    function renderPanel() {
      var panel = popPanels[popIdx];
      popInner.innerHTML = "";
      var head = document.createElement("div"); head.className = "pop-head";
      var h4 = panel.querySelector(".ptext h4");
      var pl = h4 ? h4.querySelector(".pl") : null;
      var label = pl ? pl.textContent : "";
      head.innerHTML = '<span class="pop-badge">' + (label ? "패널 (" + esc(label) + ")" : "상세") +
        '</span><span class="pop-count">' + (popIdx + 1) + " / " + popPanels.length + "</span>";
      popInner.appendChild(head);
      var pimg = panel.querySelector(".pimg"); if (pimg) popInner.appendChild(pimg.cloneNode(true));
      var ptext = panel.querySelector(".ptext"); if (ptext) popInner.appendChild(ptext.cloneNode(true));
      pop.scrollTop = 0;
    }
    // ←/→ within the detail popup: flip between panel cards of the figure;
    // past the last panel → next figure, before the first → back to the thumbnail grid
    function popGo(d) {
      if (!popOpen) return;
      var ni = popIdx + d;
      if (ni < 0) { closePop(); }
      else if (ni > popPanels.length - 1) { closePop(); go(1); }
      else { popIdx = ni; renderPanel(); }
    }
    function closePop() { if (!popOpen) return; pop.classList.remove("show"); pop.setAttribute("aria-hidden", "true"); popInner.innerHTML = ""; popOpen = false; }

    function enterDeck(start) {
      buildSlides();
      idx = (typeof start === "number") ? start : startIndex();
      document.body.classList.add("deck-open");
      deck.classList.add("show"); deck.setAttribute("aria-hidden", "false");
      deckOpen = true; render();
    }
    function exitDeck() {
      closePop();
      deck.classList.remove("show"); deck.setAttribute("aria-hidden", "true");
      document.body.classList.remove("deck-open"); deckOpen = false;
      if (document.fullscreenElement) { try { document.exitFullscreen(); } catch (e) {} }
      var s = slides && slides[idx]; if (s && s.sec) s.sec.scrollIntoView({ block: "start" });
    }
    function toggleFs() {
      if (!document.fullscreenElement) { if (deck.requestFullscreen) deck.requestFullscreen(); }
      else { if (document.exitFullscreen) document.exitFullscreen(); }
    }

    if (presentBtn) presentBtn.addEventListener("click", function () { enterDeck(); });
    deck.querySelector(".deck-nav.prev").addEventListener("click", function () { go(-1); });
    deck.querySelector(".deck-nav.next").addEventListener("click", function () { go(1); });
    deck.querySelector(".deck-exit").addEventListener("click", exitDeck);
    deck.querySelector(".deck-fs").addEventListener("click", toggleFs);
    pop.addEventListener("click", function (e) { if (e.target === pop) closePop(); });
    var popClose = pop.querySelector(".pop-close"); if (popClose) popClose.addEventListener("click", closePop);
    var popPrev = pop.querySelector(".pop-nav.prev"); if (popPrev) popPrev.addEventListener("click", function () { popGo(-1); });
    var popNext = pop.querySelector(".pop-nav.next"); if (popNext) popNext.addEventListener("click", function () { popGo(1); });

    // capture-phase keys: only act in presentation mode, so reading-mode handlers stay intact
    document.addEventListener("keydown", function (e) {
      if ((e.key === "p" || e.key === "P") && !tf.classList.contains("show") && !lb.classList.contains("show")) {
        e.preventDefault(); if (deckOpen) exitDeck(); else enterDeck(); return;
      }
      if (!deckOpen) return;
      // a term modal / lightbox is layered above the deck → let their own ESC handlers run
      if (tf.classList.contains("show") || lb.classList.contains("show")) {
        if (navDelta(e.key)) e.preventDefault();
        return;
      }
      if (e.key === "Escape") { e.preventDefault(); e.stopImmediatePropagation(); if (popOpen) closePop(); else exitDeck(); return; }
      if (popOpen) { var pd = navDelta(e.key); if (pd) { e.preventDefault(); e.stopImmediatePropagation(); popGo(pd); } return; }
      var d = navDelta(e.key);
      if (d) { e.preventDefault(); e.stopImmediatePropagation(); go(d); return; }
      if (e.key === "Home") { e.preventDefault(); e.stopImmediatePropagation(); gotoIdx(0); return; }
      if (e.key === "End") { e.preventDefault(); e.stopImmediatePropagation(); gotoIdx(slides.length - 1); return; }
      if (e.key === "f" || e.key === "F") { e.preventDefault(); e.stopImmediatePropagation(); toggleFs(); return; }
    }, true);
  }
  // =================== END PRESENTATION MODE ===================

  // ===================== AUTHORS / JOURNAL MODAL =====================
  var authorsBtn = document.getElementById("authors-btn");
  var authorsModal = document.getElementById("authors");
  if (authorsBtn && authorsModal) {
    var authorsClose = authorsModal.querySelector(".au-close");
    function openAuthors() { authorsModal.classList.add("show"); authorsModal.setAttribute("aria-hidden", "false"); }
    function closeAuthors() { authorsModal.classList.remove("show"); authorsModal.setAttribute("aria-hidden", "true"); }
    authorsBtn.addEventListener("click", function (e) { e.preventDefault(); openAuthors(); });
    authorsModal.addEventListener("click", function (e) { if (e.target === authorsModal) closeAuthors(); });
    if (authorsClose) authorsClose.addEventListener("click", closeAuthors);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && authorsModal.classList.contains("show")) {
        e.preventDefault(); e.stopImmediatePropagation(); closeAuthors();
      }
    }, true);
  }
  // =================== END AUTHORS MODAL ===================
})();

(function () {
  "use strict";
  // TERMS and TALIAS are injected inline above this script.
  var tip = document.getElementById("tip");

  function resolve(k) {
    if (!k) return null;
    if (TERMS[k]) return TERMS[k];
    var a = TALIAS[k.toLowerCase()];
    if (a && TERMS[a]) return TERMS[a];
    // try matching by exact key case-insensitively
    for (var key in TERMS) { if (key.toLowerCase() === k.toLowerCase()) return TERMS[key]; }
    return null;
  }

  function esc(s) {
    return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function buildTip(t) {
    var h = '<div class="t-ko">' + esc(t.ko || t.key) + "</div>";
    if (t.en) h += '<div class="t-en">' + esc(t.en) + "</div>";
    if (t.category) h += '<div class="t-cat">' + esc(t.category) + "</div>";
    if (t.desc) h += '<div class="t-desc">' + esc(t.desc) + "</div>";
    if (t.formula) h += '<div class="t-formula">' + esc(t.formula) + "</div>";
    if (t.related && t.related.length)
      h += '<div class="t-rel">관련: ' + t.related.map(esc).join(", ") + "</div>";
    return h;
  }

  var curEl = null;
  function showTip(el, x, y) {
    var k = el.getAttribute("data-k");
    var t = resolve(k);
    if (!t) { // mark unknown so it can be fixed
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
  // keyboard / touch accessibility
  document.addEventListener("focusin", function (e) {
    var el = e.target.closest(".term");
    if (el) { var r = el.getBoundingClientRect(); curEl = el; showTip(el, r.left, r.bottom); }
  });
  document.addEventListener("focusout", function (e) {
    if (e.target.closest(".term")) hideTip();
  });
  document.addEventListener("click", function (e) {
    var el = e.target.closest(".term");
    if (el) { e.preventDefault(); var r = el.getBoundingClientRect();
      if (curEl === el && tip.classList.contains("show")) hideTip();
      else { curEl = el; showTip(el, r.left, r.bottom); } }
  });

  // lightbox
  var lb = document.getElementById("lb"), lbimg = document.getElementById("lbimg");
  document.addEventListener("click", function (e) {
    var img = e.target.closest("img.zoom");
    if (img) { lbimg.src = img.src; lb.classList.add("show"); }
  });
  lb.addEventListener("click", function () { lb.classList.remove("show"); lbimg.src = ""; });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { lb.classList.remove("show"); hideTip(); }
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
})();

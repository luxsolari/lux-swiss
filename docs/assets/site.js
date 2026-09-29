// Lux Swiss docs — shared behaviour: theme / flavor / Jost toggles (persisted in
// localStorage under "theme", "flavor", "jost"), the mobile nav, the current-page
// marker in the sidebar, and live palette values. The head of every page applies
// the saved classes before first paint (see the inline script there); this file
// only wires the controls.
(function () {
  var root = document.documentElement;

  function bind(attr, key, onValue, offValue, cls, storeOn, storeOff, initial) {
    function apply(on) {
      root.classList.toggle(cls, on);
      document.querySelectorAll("[" + attr + "]").forEach(function (b) {
        var v = b.getAttribute(attr);
        b.setAttribute("aria-pressed", String(v === (on ? onValue : offValue)));
      });
    }
    apply(initial);
    document.addEventListener("click", function (e) {
      var btn = e.target.closest("[" + attr + "]");
      if (!btn) return;
      var on = btn.getAttribute(attr) === onValue;
      try { localStorage.setItem(key, on ? storeOn : storeOff); } catch (err) {}
      apply(on);
    });
  }

  var saved = null, flavor = null, jost = null;
  try { saved = localStorage.getItem("theme"); flavor = localStorage.getItem("flavor"); jost = localStorage.getItem("jost"); } catch (e) {}
  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;

  bind("data-theme-btn", "theme", "dark", "light", "dark", "dark", "light", saved ? saved === "dark" : !!prefersDark);
  bind("data-flavor-btn", "flavor", "geist", "space", "geist", "geist", "space", flavor === "geist");
  bind("data-jost-btn", "jost", "jost", "mono", "jost", "on", "off", jost === "on");

  // Mobile nav.
  var btn = document.querySelector("[data-nav-toggle]");
  var list = document.querySelector("[data-nav-list]");
  if (btn && list) {
    btn.addEventListener("click", function () {
      var open = list.classList.toggle("open");
      btn.setAttribute("aria-expanded", String(open));
    });
    list.addEventListener("click", function (e) {
      if (!e.target.closest("a")) return;
      list.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    });
  }

  // Current page in the sidebar.
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".sidebar-nav a").forEach(function (a) {
    var target = (a.getAttribute("href") || "").split("#")[0] || "index.html";
    if (target === here) a.setAttribute("aria-current", "page");
  });

  // Live palette values (hex / rgb / hsl) beside each chip, recomputed on theme change.
  function pad(n) { return n.toString(16).padStart(2, "0"); }
  function toHsl(r, g, b) {
    r /= 255; g /= 255; b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b), d = max - min, h = 0, s = 0, l = (max + min) / 2;
    if (d) {
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      h = max === r ? (g - b) / d + (g < b ? 6 : 0) : max === g ? (b - r) / d + 2 : (r - g) / d + 4;
      h *= 60;
    }
    return [Math.round(h), Math.round(s * 100), Math.round(l * 100)];
  }
  function fill() {
    document.querySelectorAll(".palette figure").forEach(function (fig) {
      var chip = fig.querySelector(".pal-chip"), dl = fig.querySelector(".pal-vals");
      if (!chip || !dl) return;
      var m = getComputedStyle(chip).backgroundColor.match(/\d+/g);
      if (!m) return;
      var r = +m[0], g = +m[1], b = +m[2], H = toHsl(r, g, b);
      dl.innerHTML = "<div>HEX #" + pad(r) + pad(g) + pad(b) + "</div>" +
        "<div>RGB " + r + " " + g + " " + b + "</div>" +
        "<div>HSL " + H[0] + " " + H[1] + "% " + H[2] + "%</div>";
    });
  }
  if (document.querySelector(".palette")) {
    fill();
    new MutationObserver(fill).observe(root, { attributes: true, attributeFilter: ["class"] });
  }
})();

/* Shared case-study behaviour: film player with chapters, beat jumps, still lightbox, reveal. */
(() => {
  document.documentElement.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Contra link lives in one place per page: <body data-contra="...">
  const contra = document.body.dataset.contra;
  if (contra) $$('.contra-link').forEach(a => a.href = contra);

  /* ---------- film player ---------- */
  const player = $('.player');
  if (player) {
    const vid = $('video', player), screen = $('.screen', player), tl = $('.tl', player);
    const ph = $('.ph', tl), tip = $('.tip', tl), tc = $('.tcode', player);
    const CH = JSON.parse(player.dataset.chapters);
    const FPS = 60;
    let dur = +player.dataset.duration || 1, userPaused = false;
    const fmt = s => { s = Math.max(0, s); return `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(Math.floor(s % 60)).padStart(2, '0')}:${String(Math.floor((s % 1) * FPS)).padStart(2, '0')}`; };
    const mmss = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
    const at = s => { let i = 0; CH.forEach((c, k) => { if (s >= c.t) i = k; }); return i; };
    const end = i => CH[i + 1]?.t ?? dur;

    const segs = $('.segs', tl), chaps = $('.chaps', player);
    chaps.style.setProperty('--n', CH.length);
    CH.forEach((c, i) => {
      const sg = document.createElement('div'); sg.className = 'seg'; sg.innerHTML = '<i></i>'; segs.appendChild(sg);
      const b = document.createElement('button'); b.type = 'button'; b.className = 'chap';
      b.innerHTML = `<span>${mmss(c.t)}</span><b>${c.label}</b>`;
      b.addEventListener('click', () => seek(c.t, true));
      chaps.appendChild(b);
    });
    const layout = () => $$('.seg', segs).forEach((sg, i) => sg.style.flex = end(i) - CH[i].t);
    layout();

    function render() {
      const s = vid.currentTime, ci = at(s);
      ph.style.left = `calc(${(s / dur) * 100}% - 1px)`;
      tc.innerHTML = `${fmt(s)} <small>/ ${fmt(dur)}</small>`;
      tl.setAttribute('aria-valuenow', s.toFixed(1));
      tl.setAttribute('aria-valuetext', `${mmss(s)}, ${CH[ci].label}`);
      $$('.seg i', segs).forEach((f, i) => f.style.transform = `scaleX(${Math.min(1, Math.max(0, (s - CH[i].t) / (end(i) - CH[i].t)))})`);
      $$('.chap', chaps).forEach((c, i) => c.classList.toggle('on', i === ci));
    }
    function ui() {
      const on = !vid.paused;
      screen.classList.toggle('playing', on);
      const pb = $('.pp', player);
      pb.setAttribute('aria-label', on ? 'Pause' : 'Play');
      pb.innerHTML = on ? '<svg viewBox="0 0 24 24"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>' : '<svg viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z"/></svg>';
    }
    function seek(s, play) {
      vid.currentTime = Math.min(Math.max(0, s), dur - 0.02); render();
      if (play) { userPaused = false; vid.play().catch(() => {}); }
    }
    window.caseSeek = (t) => {
      player.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block: 'center'});
      setTimeout(() => seek(t, true), reduce ? 0 : 450);
    };
    const toggle = () => { if (vid.paused) { userPaused = false; vid.play().catch(() => {}); } else { userPaused = true; vid.pause(); } };

    vid.addEventListener('loadedmetadata', () => { if (isFinite(vid.duration)) { dur = vid.duration; tl.setAttribute('aria-valuemax', dur.toFixed(1)); layout(); render(); } });
    vid.addEventListener('play', () => { ui(); const tick = () => { render(); if (!vid.paused) requestAnimationFrame(tick); }; tick(); });
    vid.addEventListener('pause', () => { ui(); render(); });
    vid.addEventListener('seeked', render);
    screen.addEventListener('click', toggle);
    $('.pp', player).addEventListener('click', toggle);
    $('.slow', player).addEventListener('click', e => {
      const on = vid.playbackRate === 1; vid.playbackRate = on ? 0.5 : 1;
      e.currentTarget.setAttribute('aria-pressed', on);
    });
    $('.fs', player).addEventListener('click', () => {
      if (document.fullscreenElement) { document.exitFullscreen().catch(() => {}); return; }
      const r = player.requestFullscreen?.(); if (r) r.catch(() => vid.webkitEnterFullscreen?.()); else vid.webkitEnterFullscreen?.();
    });

    const toTime = x => { const r = tl.getBoundingClientRect(); return Math.min(1, Math.max(0, (x - r.left) / r.width)) * dur; };
    let drag = false, was = false;
    tl.addEventListener('pointerdown', e => { drag = true; was = !vid.paused; vid.pause(); tl.setPointerCapture(e.pointerId); seek(toTime(e.clientX)); });
    tl.addEventListener('pointermove', e => {
      const s = toTime(e.clientX); tip.style.left = `${(s / dur) * tl.clientWidth}px`; tip.textContent = `${mmss(s)} · ${CH[at(s)].label}`;
      if (drag) seek(s);
    });
    const release = () => { if (!drag) return; drag = false; if (was) vid.play().catch(() => {}); };
    tl.addEventListener('pointerup', release); tl.addEventListener('pointercancel', release);
    tl.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight') { seek(vid.currentTime + 1); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { seek(vid.currentTime - 1); e.preventDefault(); }
      if (e.key === 'Home') { seek(0); e.preventDefault(); }
    });
    let visible = false;
    addEventListener('keydown', e => {
      if (!visible || e.target.closest('input,textarea,button,a,[role=slider]') || $('.lb')) return;
      if (e.code === 'Space') { toggle(); e.preventDefault(); }
      else if (e.key === 'ArrowRight') seek(vid.currentTime + 1);
      else if (e.key === 'ArrowLeft') seek(vid.currentTime - 1);
      else if (e.key === '.') { vid.pause(); seek(vid.currentTime + 1 / FPS); }
      else if (e.key === ',') { vid.pause(); seek(vid.currentTime - 1 / FPS); }
    });
    new IntersectionObserver(es => es.forEach(e => {
      visible = e.isIntersecting;
      if (e.intersectionRatio >= .5 && !userPaused && !reduce) vid.play().catch(() => {});
      if (!e.isIntersecting && !vid.paused) vid.pause();
    }), {threshold: [0, .5]}).observe(screen);
    render();
  }

  $$('[data-seek]').forEach(b => b.addEventListener('click', () => window.caseSeek?.(+b.dataset.seek)));

  /* ---------- still lightbox ---------- */
  $$('.shot').forEach(s => s.addEventListener('click', () => {
    const img = $('img', s), prev = document.activeElement;
    const lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', img.alt);
    lb.innerHTML = `<img src="${img.getAttribute('src')}" alt="${img.alt}"><button class="x" type="button" aria-label="Close">×</button>`;
    const close = () => { lb.remove(); removeEventListener('keydown', esc); prev?.focus(); };
    const esc = e => { if (e.key === 'Escape') close(); };
    lb.addEventListener('click', close); addEventListener('keydown', esc);
    document.body.appendChild(lb); $('.x', lb).focus();
  }));

  /* ---------- reveal ---------- */
  if (!reduce && 'IntersectionObserver' in window) {
    const els = $$('.rv');
    els.forEach(el => { if (el.getBoundingClientRect().top > innerHeight) el.classList.add('pre'); });
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }), {rootMargin: '0px 0px -6% 0px'});
    els.forEach(el => io.observe(el));
  }

  /* ---------- count-up numbers ---------- */
  const nums = $$('[data-count]');
  if (nums.length) {
    const run = el => {
      const to = +el.dataset.count;
      if (reduce) { el.textContent = to; return; }
      const t0 = performance.now();
      const step = n => { const p = Math.min(1, (n - t0) / 1300); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    };
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } }), {threshold: .6});
    nums.forEach(n => io.observe(n));
  }
})();

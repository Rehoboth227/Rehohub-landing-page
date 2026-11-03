/* Rehohub — interactions */
(() => {
  const doc = document.documentElement;
  const header = document.querySelector('.header');
  const toggle = document.querySelector('.nav-toggle');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header state on scroll
  const onScroll = () => header && header.classList.toggle('is-scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile nav
  if (toggle) {
    const setOpen = (open) => {
      doc.classList.toggle('nav-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    toggle.addEventListener('click', () => setOpen(!doc.classList.contains('nav-open')));
    document.querySelectorAll('.nav a').forEach((a) => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (e) => e.key === 'Escape' && setOpen(false));
  }

  // Scroll reveal
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add('is-in'));
  }

  // Rotating hero word
  const swap = document.querySelector('.swap[data-words]');
  if (swap && !reduce) {
    const words = swap.dataset.words.split('|');
    let i = 0;
    setInterval(() => {
      i = (i + 1) % words.length;
      swap.animate([{ opacity: 1, transform: 'translateY(0)' }, { opacity: 0, transform: 'translateY(-12px)' }], { duration: 250, easing: 'ease-in' })
        .onfinish = () => {
          swap.textContent = words[i];
          swap.animate([{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'translateY(0)' }], { duration: 350, easing: 'ease-out' });
        };
    }, 2600);
  }

  // Count-up stats
  document.querySelectorAll('[data-count]').forEach((el) => {
    if (reduce) return;
    const target = +el.dataset.count;
    let n = 0;
    el.textContent = '0';
    const tick = () => { n++; el.textContent = n; if (n < target) setTimeout(tick, 900 / target); };
    setTimeout(tick, 700);
  });

  // Current year
  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });
})();

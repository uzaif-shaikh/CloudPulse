document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Nav item selection ---------- */
  const navItems = document.querySelectorAll('.nav-item');
  const toast = document.getElementById('toast');
  let toastTimer = null;

  navItems.forEach(item => {
    item.addEventListener('click', () => {
      // Real pages (rendered as <a> in base.html) navigate normally —
      // only the still-unwired mockup items (plain <div>) get the toast.
      if (item.tagName === 'A') return;

      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');

      const view = item.dataset.view;
      if (view && view !== 'dashboard') {
        showToast(`"${item.querySelector('.nav-label').textContent}" is a mockup — no live view wired up yet.`);
      }
    });
  });

  /* ---------- Dashboard action buttons (mockup only) ---------- */
  document.querySelectorAll('[data-toast]').forEach(el => {
    el.addEventListener('click', () => showToast(el.dataset.toast));
  });

  function showToast(message){
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 3200);
  }

  /* ---------- Sidebar collapse toggle ---------- */
  const collapseBtn = document.getElementById('collapseBtn');
  const sidebar = document.getElementById('sidebar');

  if (collapseBtn && sidebar) {
    collapseBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
    });
  }

  /* ---------- Live "last refresh" ticker ---------- */
  const refreshEl = document.getElementById('refreshTime');
  let secondsAgo = 4;

  if (refreshEl) {
    setInterval(() => {
      secondsAgo++;
      if (secondsAgo > 60) secondsAgo = 0;
      refreshEl.textContent = `last refresh ${secondsAgo}s ago`;
    }, 1000);
  }

});

(() => {
  const $ = (s, root=document) => root.querySelector(s);
  // Missing user-supplied source images are replaced by the branded fallback until uploaded.
  document.querySelectorAll('img[data-fallback]').forEach(img => {
    img.addEventListener('error', () => {
      if (img.dataset.fallbackUsed) return;
      img.dataset.fallbackUsed = '1';
      img.src = img.dataset.fallback;
    });
  });
  const toggle = $('.menu-toggle');
  const nav = $('.nav');
  if (toggle && nav) toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
  const cards = [...document.querySelectorAll('[data-product-card]')];
  const search = $('#product-search');
  const brand = $('#brand-filter');
  const condition = $('#condition-filter');
  const count = $('#result-count');
  const empty = $('#empty-state');
  function filterProducts(){
    const q = (search?.value || '').toLocaleLowerCase('tr');
    const b = brand?.value || '';
    let visible = 0;
    cards.forEach(card => {
      const text = (card.dataset.search || '').toLocaleLowerCase('tr');
      const brands = (card.dataset.brand || '').split('|');
      const ok = (!q || text.includes(q)) && (!b || brands.includes(b));
      card.hidden = !ok;
      if(ok) visible++;
    });
    if(count) count.textContent = `${visible} ürün listeleniyor`;
    if(empty) empty.hidden = visible !== 0;
  }
  [search, brand].forEach(el => el && el.addEventListener('input', filterProducts));
  document.querySelectorAll('[data-brand-chip]').forEach(btn => btn.addEventListener('click', () => {
    if(brand) brand.value = btn.dataset.brandChip;
    document.querySelectorAll('[data-brand-chip]').forEach(x => x.classList.toggle('active', x===btn));
    filterProducts();
  }));
  filterProducts();
  document.querySelectorAll('[data-condition]').forEach(btn => btn.addEventListener('click', () => {
    const type = btn.dataset.condition;
    const title = document.body.dataset.productTitle || 'Volkswagen motor';
    const message = `Merhaba, ${title} için ${type} motor seçeneği, stok ve uyumluluk bilgisi almak istiyorum.`;
    const url = `https://wa.me/905537383806?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank', 'noopener');
  }));
})();

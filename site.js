// Gemeinsames Skript für Startseite und Katalogseite (DE und EN): Menü, Hell/Dunkel, Katalogfilter, Einblenden.
(function(){
const nav=document.getElementById('nav'),yr=document.getElementById('yr');
if(yr)yr.textContent=new Date().getFullYear();
addEventListener('scroll',()=>nav.classList.toggle('solid',scrollY>40),{passive:true});

// Menü auf schmalen Bildschirmen
(function(){const b=document.getElementById('menu'),x=document.getElementById('navx');
  const set=o=>{nav.classList.toggle('open',o);b.setAttribute('aria-expanded',o)};
  b.addEventListener('click',()=>set(b.getAttribute('aria-expanded')!=='true'));
  x.addEventListener('click',e=>{if(e.target.closest('a'))set(false)});
  addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){set(false);b.focus()}});
  document.addEventListener('click',e=>{if(!nav.contains(e.target))set(false)});
  matchMedia('(min-width:941px)').addEventListener('change',()=>set(false))})();

// Hell/Dunkel
document.getElementById('theme').addEventListener('click',()=>{const d=document.documentElement,
  cur=d.dataset.theme||(matchMedia('(prefers-color-scheme: light)').matches?'light':'dark'),t=cur==='light'?'dark':'light';
  d.dataset.theme=t;try{localStorage.setItem('theme',t)}catch(e){}});

// Katalogfilter (nur auf der Katalogseite): Bereich und Gerät wirken zusammen.
// Vorauswahl über die Adresse, z. B. apps/#geraet=Windows oder #bereich=spiele – es werden keine Daten gespeichert.
(function(){const kat=document.getElementById('kat');if(!kat)return;
  const f={k:'all',p:'all'},none=document.getElementById('none'),has=(key,v)=>!!document.querySelector('#apps .chip[data-'+key+'="'+v+'"]');
  const run=()=>{let any=0;
    document.querySelectorAll('#apps .group').forEach(g=>{let n=0;
      g.querySelectorAll('.app').forEach(a=>{const ok=(f.k==='all'||g.dataset.k===f.k)&&(f.p==='all'||a.dataset.pf.split(' ').includes(f.p));a.classList.toggle('hide',!ok);if(ok)n++});
      g.classList.toggle('hide',!n);any+=n});
    none.hidden=any>0;
    for(const key of ['k','p'])document.querySelectorAll('#apps .chip[data-'+key+']').forEach(x=>{const on=x.dataset[key]===f[key];x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)})};
  const read=()=>{const q=new URLSearchParams(location.hash.slice(1)),p=q.get('geraet')||q.get('device'),k=q.get('bereich')||q.get('category');
    f.p=p&&has('p',p)?p:'all';f.k=k&&has('k',k)?k:'all';run()};
  const write=()=>{const q=[];if(f.k!=='all')q.push('bereich='+f.k);if(f.p!=='all')q.push('geraet='+f.p);
    history.replaceState(null,'',q.length?'#'+q.join('&'):location.pathname+location.search)};
  document.querySelectorAll('#apps .chip').forEach(ch=>ch.addEventListener('click',()=>{if('k' in ch.dataset)f.k=ch.dataset.k;else f.p=ch.dataset.p;run();write()}));
  addEventListener('hashchange',read);read()})();

// Alte Sprungziele der Startseite (#katalog) landen beim Streifen „Jetzt verfügbar“
(function(){const go=()=>{if(location.hash==='#katalog'){const t=document.getElementById('apps');if(t)t.scrollIntoView()}};
  addEventListener('hashchange',go);go()})();

// Reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
})();

/* FRDTLAB · Signal Room C · site nav behaviour (scrolled state + mobile menu). No copy, no tracking. */
(function(){var d=document.documentElement;function s(){d.style.setProperty('--sbw',Math.max(0,innerWidth-d.clientWidth)+'px');}s();addEventListener('resize',s,{passive:true});addEventListener('load',s);})();
(function(){
  var nav=document.getElementById('nav');
  if(!nav)return;
  function onScroll(){nav.classList.toggle('scrolled',(window.scrollY||0)>40);}
  addEventListener('scroll',onScroll,{passive:true});onScroll();
  var btn=document.getElementById('menuBtn'),links=document.getElementById('navLinks');
  if(!btn||!links)return;
  function close(){links.classList.remove('open');btn.setAttribute('aria-expanded','false');}
  btn.addEventListener('click',function(){var o=links.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');});
  links.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
  addEventListener('keydown',function(e){if(e.key==='Escape'&&links.classList.contains('open')){close();btn.focus();}});
})();

/* FRDTLAB · Signal Room B · nav state and mobile menu (same behavior as in-motion). No copy, no tracking. */
(function(){
  var nav=document.getElementById('nav'),mb=document.getElementById('menuBtn'),nl=document.getElementById('navLinks');
  if(!nav||!mb||!nl)return;
  function onScroll(){nav.classList.toggle('scrolled',(window.scrollY||0)>40);}
  addEventListener('scroll',onScroll,{passive:true});onScroll();
  function setMenu(o){nl.classList.toggle('open',o);mb.setAttribute('aria-expanded',o?'true':'false');}
  mb.addEventListener('click',function(){setMenu(!nl.classList.contains('open'));});
  nl.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setMenu(false);});});
  addEventListener('keydown',function(e){if(e.key==='Escape'&&nl.classList.contains('open')){setMenu(false);mb.focus();}});
})();

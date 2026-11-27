/* FRDTLAB · Signal Room v1 · reading progress. No copy, no tracking. */
(function(){
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var b=document.createElement('div');b.className='sr-progress';b.setAttribute('aria-hidden','true');
  document.body.appendChild(b);var q=false;
  function u(){q=false;var h=document.documentElement.scrollHeight-innerHeight;b.style.setProperty('--p',h>0?Math.min(1,(scrollY||0)/h):0);}
  addEventListener('scroll',function(){if(!q){q=true;requestAnimationFrame(u);}},{passive:true});u();
})();

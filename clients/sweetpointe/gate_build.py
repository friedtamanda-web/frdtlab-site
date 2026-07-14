import os, base64, json, sys
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PASSPHRASE = sys.argv[1]
SRC = "growth-system.html"
OUT = "index.html"

with open(SRC, "r", encoding="utf-8") as f:
    plaintext = f.read().encode("utf-8")

salt = os.urandom(16)
iv = os.urandom(12)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=310000)
key = kdf.derive(PASSPHRASE.encode("utf-8"))
ct = AESGCM(key).encrypt(iv, plaintext, None)

b64 = lambda b: base64.b64encode(b).decode()
payload, salt_b64, iv_b64 = b64(ct), b64(salt), b64(iv)

shell = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Client Proposal · FRDT Lab</title>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root { --blue:#2f6bff; --pink:#ff2e7e; --navy:#0d0d0f; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family:'Inter',system-ui,sans-serif; background:var(--navy); color:#f4f4f6; }
  #gate { min-height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center;
    background:radial-gradient(1000px 560px at 70% 20%,rgba(47,107,255,.16),transparent 60%),radial-gradient(800px 460px at 22% 88%,rgba(255,46,126,.12),transparent 60%),var(--navy); }
  .gate-card { width:min(430px,90vw); text-align:center; padding:40px 22px; }
  .gate-brand { font-size:12px; font-weight:600; letter-spacing:5px; color:rgba(255,255,255,.45); margin-bottom:28px; font-family:'Manrope',sans-serif; }
  .gate-brand .lab { color:var(--blue); }
  .gate-card h1 { font-family:'Manrope',sans-serif; color:#fff; font-size:32px; font-weight:800; letter-spacing:-1px; margin-bottom:10px; }
  .gate-rule { width:48px; height:3px; background:var(--pink); border-radius:2px; margin:0 auto 18px; }
  .gate-card p { color:rgba(255,255,255,.5); font-size:14px; margin-bottom:26px; }
  .gate-card input { width:100%; padding:14px 16px; border-radius:10px; border:1px solid rgba(255,255,255,.14); background:rgba(255,255,255,.06); color:#fff; font-size:15px; margin-bottom:12px; outline:none; }
  .gate-card input:focus { border-color:var(--blue); }
  .gate-card button { width:100%; padding:14px; border:none; border-radius:10px; background:var(--pink); color:#fff; font-size:15px; font-weight:700; cursor:pointer; font-family:'Manrope',sans-serif; box-shadow:0 8px 30px rgba(255,46,126,.3); }
  .gate-card button:hover { transform:translateY(-1px); }
  #gate-err { color:#ff7b8a; font-size:13px; margin-top:14px; display:none; }
</style>
</head>
<body>
<div id="gate">
  <div class="gate-card">
    <div class="gate-brand">F R D T <span class="lab">L A B</span> &middot; GROWTH SYSTEMS</div>
    <h1>Sweet Pointe</h1>
    <div class="gate-rule"></div>
    <p>This page is private. Enter the passcode you were given to view it.</p>
    <input type="password" id="pw" placeholder="Passcode" autocomplete="off" onkeydown="if(event.key==='Enter')unlock()">
    <button onclick="unlock()">View Proposal</button>
    <div id="gate-err">That passcode didn't work — check it and try again.</div>
  </div>
</div>
<script>
const PAYLOAD="__PAYLOAD__", SALT="__SALT__", IV="__IV__";
function b64ToBuf(b64){const s=atob(b64);const b=new Uint8Array(s.length);for(let i=0;i<s.length;i++)b[i]=s.charCodeAt(i);return b.buffer;}
async function unlock(){
  const pw=document.getElementById('pw').value; const err=document.getElementById('gate-err'); err.style.display='none';
  try{
    const km=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
    const key=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64ToBuf(SALT),iterations:310000,hash:'SHA-256'},km,{name:'AES-GCM',length:256},false,['decrypt']);
    const plain=await crypto.subtle.decrypt({name:'AES-GCM',iv:b64ToBuf(IV)},key,b64ToBuf(PAYLOAD));
    const html=new TextDecoder().decode(plain);
    document.open(); document.write(html); document.close();
  }catch(e){ err.style.display='block'; }
}
</script>
</body>
</html>'''

shell = shell.replace("__PAYLOAD__", payload).replace("__SALT__", salt_b64).replace("__IV__", iv_b64)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(shell)
print("wrote", OUT, os.path.getsize(OUT), "bytes")

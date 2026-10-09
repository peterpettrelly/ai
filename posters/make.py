import subprocess, pathlib
CSS = """@page{size:A4 landscape;margin:0}*{margin:0;padding:0;box-sizing:border-box}
html,body{width:297mm;height:210mm}
body{background:#F6F3EE;font-family:Inter,sans-serif;color:#1d1d1b;position:relative;overflow:hidden}
.num{position:absolute;top:18mm;left:18mm;font-weight:300;font-size:11pt;letter-spacing:.3em;color:%(c)s}
.art{position:absolute;top:0;bottom:0;left:12mm;width:125mm;display:flex;align-items:center;justify-content:center}.art svg{width:118mm;height:auto}
.q{position:absolute;left:142mm;right:18mm;top:50%%;transform:translateY(-50%%);font-family:"Inter Display",Inter,sans-serif;font-weight:800;font-size:%(fs)s;line-height:1.02;letter-spacing:-.025em}
.bar{position:absolute;left:142mm;top:26mm;width:16mm;height:1.6mm;background:%(c)s}
.foot{position:absolute;bottom:16mm;left:142mm;right:18mm;border-top:.3mm solid #1d1d1b33;padding-top:5mm;font-weight:300;font-size:9pt;letter-spacing:.3em;color:#1d1d1b88}"""
S='fill="none" stroke="#1d1d1b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
pages=[
 ("#C8553D","Не говори<br>плохое,<br>никогда,<br>про никого.","58pt",
  f'''<svg width="420" height="360" viewBox="0 0 420 360"><circle cx="210" cy="180" r="150" fill="#C8553D" opacity=".12"/>
  <path {S} d="M110 110 h200 a30 30 0 0 1 30 30 v90 a30 30 0 0 1 -30 30 h-120 l-45 40 v-40 h-35 a30 30 0 0 1 -30 -30 v-90 a30 30 0 0 1 30 -30z"/>
  <path fill="#C8553D" d="M210 232 C150 190 168 140 196 150 C204 153 208 160 210 166 C212 160 216 153 224 150 C252 140 270 190 210 232z"/></svg>''',"ДОБРОЕ СЛОВО"),
 ("#2F6B4F","Меньше слов,<br>больше<br>дела.","66pt",
  f'''<svg width="420" height="360" viewBox="0 0 420 360"><circle cx="210" cy="180" r="150" fill="#2F6B4F" opacity=".12"/>
  <path {S} d="M70 290 h70 v-60 h70 v-60 h70 v-60 h70"/>
  <circle cx="315" cy="78" r="16" fill="#2F6B4F"/>
  <path {S} stroke-width="2" opacity=".4" d="M80 120 h40 M80 140 h26"/></svg>''',"ДЕЙСТВИЕ"),
 ("#2E4A7D","Слушай<br>сильных!","84pt",
  f'''<svg width="420" height="360" viewBox="0 0 420 360"><circle cx="210" cy="180" r="150" fill="#2E4A7D" opacity=".12"/>
  <path {S} d="M40 300 L170 120 L215 180 L250 140 L380 300 Z"/>
  <path fill="#2E4A7D" d="M170 120 L140 162 L158 155 L170 170 L184 152 L198 160 Z"/>
  <path fill="none" stroke="#2E4A7D" stroke-width="3" stroke-linecap="round" d="M150 92 a30 30 0 0 1 40 0 M134 70 a54 54 0 0 1 72 0 M118 48 a78 78 0 0 1 104 0"/></svg>''',"СИЛА"),
]
for i,(c,q,fs,svg,tag) in enumerate(pages,1):
    html=f'<!doctype html><meta charset="utf-8"><style>{CSS%{"c":c,"fs":fs}}</style><body><div class="num">0{i} / 03</div><div class="art">{svg}</div><div class="bar"></div><div class="q">{q}</div></body>'
    p=pathlib.Path(f"poster-{i}.html"); p.write_text(html)
    base=["/opt/pw-browsers/chromium","--headless","--no-sandbox","--disable-gpu","--hide-scrollbars"]
    subprocess.run(base+["--no-pdf-header-footer",f"--print-to-pdf=poster-{i}.pdf",str(p.resolve())],check=True,capture_output=True)
    subprocess.run(base+["--window-size=1123,794",f"--screenshot=poster-{i}.png",str(p.resolve())],check=True,capture_output=True)

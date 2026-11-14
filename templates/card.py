# Builds a 1080x1350 brand card HTML from a small spec. Usage: python3 card.py spec.json out.html
import json,sys,html
s=json.load(open(sys.argv[1])); e=html.escape
rows=''.join(f'<li><span class="n">{i+1:02d}</span><span class="t">{e(r)}</span></li>' for i,r in enumerate(s.get('rows',[])))
big=f'<div class="big">{e(s["big"])}</div><div class="biglabel">{e(s.get("biglabel",""))}</div>' if s.get('big') else ''
h1=f'<h1>{e(s["headline"])}</h1>' if s.get('headline') else ''
lead=f'<p class="lead">{e(s["lead"])}</p>' if s.get('lead') else ''
rl=f'<div class="rowlabel">{e(s["rowlabel"])}</div>' if s.get('rowlabel') else ''
note=f'<div class="note">{e(s["note"])}</div>' if s.get('note') else ''
bg=s.get('bg','#FFFFFF')
open(sys.argv[2],'w').write(f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@500&family=Geist:wght@400;500;600&display=block" rel="stylesheet">
<style>
:root{{--navy:#0A1A33;--purple:#6D4CFF;--ink:#172036;--border:#D8DBE2}}
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{bg};font-family:Geist,sans-serif;color:var(--ink);padding:100px 90px 80px;display:flex;flex-direction:column}}
.eyebrow{{font-weight:600;letter-spacing:.12em;color:var(--purple);font-size:24px;margin-bottom:34px}}
h1{{font-family:Lora,serif;font-weight:500;color:var(--navy);font-size:{s.get('hsize',84)}px;line-height:1.08;letter-spacing:-.01em}}
.big{{font-family:Lora,serif;font-weight:500;color:var(--navy);font-size:230px;line-height:1;letter-spacing:-.02em}}
.biglabel{{font-size:36px;line-height:1.35;margin-top:22px;max-width:820px;color:var(--navy);font-weight:500}}
p.lead{{font-size:33px;line-height:1.45;margin-top:36px;max-width:880px}}
.rowlabel{{margin-top:60px;font-weight:600;font-size:24px;letter-spacing:.08em;color:var(--navy)}}
ul{{list-style:none;padding:0;margin-top:20px;border-top:1px solid var(--border)}}
li{{display:flex;align-items:baseline;border-bottom:1px solid var(--border);padding:30px 0}}
li .n{{font-weight:600;color:var(--purple);font-size:24px;width:76px;letter-spacing:.06em;flex:none}}
li .t{{font-family:Lora,serif;font-weight:500;color:var(--navy);font-size:40px;line-height:1.2}}
.note{{font-size:20px;line-height:1.45;color:#5A6275;margin-top:36px;max-width:900px}}
footer{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;padding-top:30px}}
footer img{{height:60px}}footer span{{font-size:25px;color:var(--navy);font-weight:500}}
</style></head><body>
<div class="eyebrow">{e(s['eyebrow'])}</div>{big}{h1}{lead}{rl}<ul>{rows}</ul>{note}
<footer><img src="logo.svg"><span>energyplainly.com</span></footer></body></html>''')

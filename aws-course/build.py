#!/usr/bin/env python3
"""Wrap _src/dayNN.html fragments into modules/dayNN.html and build index.html.
Fragment first line:  <!--meta {"n":1,"title":"...","time":"1.5h","week":1,"tag":"Concepts"} -->"""
import json, re, pathlib
R = pathlib.Path(__file__).parent
mods = []
for f in sorted((R/"_src").glob("day*.html")):
    s = f.read_text()
    m = json.loads(re.match(r"<!--meta (.*?) -->", s).group(1))
    m["body"] = s.split("-->",1)[1]; m["file"] = f.name; mods.append(m)

JS = """<script>
(function(){var k=document.body.dataset.k;function g(){try{return JSON.parse(localStorage.getItem(k)||'{}')}catch(e){return{}}}
function s(o){try{localStorage.setItem(k,JSON.stringify(o))}catch(e){}}
var st=g();document.querySelectorAll('input[type=checkbox][data-id]').forEach(function(c){c.checked=!!st[c.dataset.id];
c.addEventListener('change',function(){var o=g();o[c.dataset.id]=c.checked;s(o);bar()})});
function bar(){var a=document.querySelectorAll('input[data-id]'),n=0;a.forEach(function(c){if(c.checked)n++});
var b=document.getElementById('pb');if(b&&a.length)b.style.width=(100*n/a.length)+'%'}bar()})();
</script>"""

def page(title, body, root, key):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="{root}assets/style.css"></head><body data-k="{key}">
<header class="top"><div class="wrap"><a href="{root}index.html">☁ AWS Cloud Engineer Journey</a><span style="color:var(--mut);font-size:14px">Beginner → Cloud Practitioner → Solutions Architect</span></div></header>
<main class="wrap">{body}</main>{JS}</body></html>"""

for i,m in enumerate(mods):
    prev = mods[i-1] if i else None; nxt = mods[i+1] if i+1<len(mods) else None
    nav = '<nav class="pn">'+(f'<a href="{prev["file"]}">← Day {prev["n"]}: {prev["title"]}</a>' if prev else '<span></span>')+(f'<a href="{nxt["file"]}">Day {nxt["n"]}: {nxt["title"]} →</a>' if nxt else '<a href="../index.html">Course home →</a>')+'</nav>'
    head = f'<p style="margin:26px 0 0"><span class="badge">Day {m["n"]}</span><span class="badge">{m["tag"]}</span><span class="badge">⏱ {m["time"]}</span></p><h1>{m["title"]}</h1><div class="bar"><i id="pb"></i></div>'
    (R/"modules"/f'day{m["n"]:02d}.html').write_text(page(f'Day {m["n"]} - {m["title"]}', head+m["body"]+nav, "../", f'aws-day{m["n"]}'))

weeks = {}
for m in mods: weeks.setdefault(m["week"], []).append(m)
cards = ""
for w, ms in weeks.items():
    cards += f"<h3>Week {w}</h3><div class='grid'>" + "".join(f"<a class='card' href='modules/day{m['n']:02d}.html'><b>Day {m['n']}: {m['title']}</b><br><small>{m['tag']} · {m['time']}</small></a>" for m in ms) + "</div>"
idx = (R/"_src"/"index_top.html").read_text().replace("{{MODULES}}", cards)
(R/"index.html").write_text(page("AWS Cloud Engineer Journey", idx, "", "aws-index"))
print("built", len(mods), "modules")

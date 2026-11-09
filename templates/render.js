// usage: node render.js <template.html> <out.png> [width] [height]
const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [,,src,out,w='1080',h='1350']=process.argv;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:1});
await p.goto('file://'+path.resolve(src));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const f=await p.evaluate(()=>[...document.fonts].filter(x=>x.status==='loaded').map(x=>x.family+' '+x.weight));console.error('fonts:',f.join(', '));
await p.screenshot({path:out});await b.close();})();

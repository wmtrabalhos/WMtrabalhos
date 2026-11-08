// Render still frames for review: node tools/frames.js OUTDIR t1 t2 ...
const { chromium } = require('playwright'); const path = require('path');
const ROOT = path.resolve(__dirname, '..');
(async () => {
  const [out, ...ts] = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 540, height: 960 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.route('**/three.min.js', r => r.fulfill({ path: path.join(ROOT, 'vendor/three.min.js'), contentType: 'application/javascript' }));
  await p.goto('file://' + path.join(ROOT, 'dist/index.html') + '?export');
  await p.waitForFunction(() => window.__ready, null, { timeout: 60000 });
  for (const t of ts) { await p.evaluate(t => window.__rizei.render(t), +t); await p.screenshot({ path: path.join(out, `f_${t}.png`) }); }
  console.log(errs.join('\n') || 'no errors'); await b.close();
})();

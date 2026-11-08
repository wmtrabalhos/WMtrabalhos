// Render dist/index.html to a silent MP4 + events.json: node tools/render.js
const { chromium } = require('playwright'); const { spawn } = require('child_process'); const path = require('path'); const fs = require('fs');
const ROOT = path.resolve(__dirname, '..'); const FPS = 30;
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.route('**/three.min.js', r => r.fulfill({ path: path.join(ROOT, 'vendor/three.min.js'), contentType: 'application/javascript' }));
  await p.goto('file://' + path.join(ROOT, 'dist/index.html') + '?export');
  await p.waitForFunction(() => window.__ready, null, { timeout: 60000 });
  const ev = await p.evaluate(() => window.__rizei.events);
  fs.writeFileSync(path.join(ROOT, 'dist/events.json'), JSON.stringify(ev, null, 1));
  const out = path.join(ROOT, 'dist/video_sem_audio.mp4');
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'slow', '-crf', '16', '-r', String(FPS), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const N = Math.round(ev.total * FPS);
  for (let i = 0; i < N; i++) { await p.evaluate(t => window.__rizei.render(t), i / FPS); const buf = await p.screenshot({ type: 'jpeg', quality: 95 }); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); if (i % 150 === 0) console.log('frame', i, '/', N); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('video done', out);
})();

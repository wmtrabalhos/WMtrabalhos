"""Instrumental soundtrack for the RIZEI Reels, synthesised and synced to dist/events.json.

Usage: python3 tools/audio.py   ->  dist/trilha.wav (44.1 kHz, stereo, 16-bit)
Everything is generated here (no samples), so the track can be re-timed by editing the
timeline in the HTML, re-rendering events.json and running this script again.
"""
import json, os, wave
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = json.load(open(os.path.join(ROOT, 'dist', 'events.json')))
SR = 44100
DUR = float(EV['total'])
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)
L = np.zeros(N); R = np.zeros(N)
send = np.zeros(N)  # reverb send (mono)


def hz(note):
    names = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    n, o = note[:-1], int(note[-1])
    return 440.0 * 2 ** ((names[n] + 12 * (o + 1) - 69) / 12)


def add(sig, start, gain=1.0, pan=0.0, rev=0.3):
    i = int(start * SR)
    if i >= N: return
    if i < 0: sig = sig[-i:]; i = 0
    sig = sig[: N - i]
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    L[i:i + len(sig)] += sig * gain * l
    R[i:i + len(sig)] += sig * gain * r
    send[i:i + len(sig)] += sig * gain * rev


def bandnoise(dur, lo, hi):
    n = int(dur * SR)
    spec = np.fft.rfft(rng.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    spec[(f < lo) | (f > hi)] = 0
    x = np.fft.irfft(spec, n)
    return x / (np.abs(x).max() + 1e-9)


def bell(f, dur=2.2, partials=((1, 1, 1.6), (2.0, .35, 2.6), (2.76, .22, 3.4), (5.4, .08, 6))):
    tt = np.arange(int(dur * SR)) / SR
    s = sum(a * np.sin(2 * np.pi * f * m * tt) * np.exp(-d * tt) for m, a, d in partials)
    att = np.minimum(1, tt / .004)
    return s * att


def blip(f, dur=.05):
    tt = np.arange(int(dur * SR)) / SR
    return np.sin(2 * np.pi * f * tt) * np.exp(-tt * 70) * np.minimum(1, tt / .002)


def kick(f0=88, f1=44, dur=.45):
    tt = np.arange(int(dur * SR)) / SR
    ph = 2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-tt * 28)) / SR
    return np.sin(ph) * np.exp(-tt * 7)


def whoosh(dur=.8, lo=300, hi=7000, peak=.82):
    x = bandnoise(dur, lo, hi)
    tt = np.linspace(0, 1, len(x))
    env = np.where(tt < peak, (tt / peak) ** 2.2, np.exp(-(tt - peak) * 22))
    return x * env


# ---------------- pad: one chord per section, cross-faded ----------------
S = EV['scenes']
chords = [
    (0.0, ['D3', 'A3', 'E4', 'F4']),                 # opening: suspended, D minor colour
    (S['s2'], ['A#2', 'F3', 'A3', 'D4']),            # strategy
    (S['s3'], ['G2', 'D3', 'A#3', 'F4']),            # execution
    (S['s4'], ['F2', 'C3', 'E3', 'A3']),             # hub
    (S['s5'], ['C3', 'G3', 'A#3', 'D4']),            # cycles
    (S['s6'], ['D2', 'A2', 'D3', 'F3', 'A3']),       # brand build
    (S['s7'], ['A#2', 'F3', 'A3', 'C4', 'D4']),      # close: open, resolved
]
pad = np.zeros((2, N))
xf = 1.4
for ci, (st, notes) in enumerate(chords):
    en = chords[ci + 1][0] if ci + 1 < len(chords) else DUR
    a, b = max(0, st - xf / 2), min(DUR, en + xf / 2)
    i0, i1 = int(a * SR), int(b * SR)
    tt = t[i0:i1]
    env = np.clip((tt - a) / xf, 0, 1) * np.clip((b - tt) / xf, 0, 1)
    if ci == 0: env = np.clip(tt / .35, 0, 1) * np.clip((b - tt) / xf, 0, 1)
    for side, det in ((0, -1), (1, 1)):
        sig = np.zeros(len(tt))
        for nI, n in enumerate(notes):
            f = hz(n) * (1 + det * .0018 * (nI % 2 * 2 - 1))
            for h in range(1, 6):
                sig += np.sin(2 * np.pi * f * h * tt + nI + h) / h ** 1.7
        sig *= (1 + .12 * np.sin(2 * np.pi * .18 * tt + side))
        pad[side, i0:i1] += sig * env
pad /= np.abs(pad).max()
growth = np.interp(t, [0, 3, 11, 20, 26, 28, 31, 33.6, DUR], [.55, .6, .7, .78, .74, .9, .85, .8, 0])
L += pad[0] * .16 * growth; R += pad[1] * .16 * growth
send += (pad[0] + pad[1]) * .05 * growth
# low root drone
roots = [(c[0], hz(c[1][0]) / 2) for c in chords]
fr = np.zeros(N)
for ci, (st, f) in enumerate(roots):
    fr[int(st * SR):] = f
sub = np.sin(2 * np.pi * np.cumsum(fr) / SR) * .06 * np.interp(t, [0, 2, 26, 28.0, 28.1, 34, DUR], [0, 1, 1, .4, 1, 1, 0])
L += sub; R += sub

# ---------------- pulse and texture (enters with research) ----------------
beat = 60 / 100
k = S['s1']
while k < S['s6'] - .05:
    g = np.interp(k, [S['s1'], S['s3'], S['s5'], S['s6']], [.16, .24, .3, .26])
    add(kick(), k, g, 0, .05)
    k += beat
h = S['s3']; i = 0
while h < S['s6'] - .1:
    acc = .055 if i % 2 == 0 else .03
    add(bandnoise(.03, 6000, 14000) * np.exp(-np.arange(int(.03 * SR)) / SR * 120), h, acc, .35 if i % 2 else -.35, .1)
    h += beat / 2; i += 1

# ---------------- transitions ----------------
for b in [S['s1'], S['s2'], S['s3'], S['s4'], S['s5'], S['s5b'], S['s6'], S['s7']]:
    w = whoosh(.9); add(w, b - .74, .11, rng.uniform(-.4, .4), .5)
# opening: rising shimmer from the first frame
add(whoosh(1.1, 1500, 9000, .2), 0, .07, 0, .6)

# ---------------- text locks in: one bell per headline ----------------
scale = ['D5', 'F5', 'A5', 'C6', 'E5', 'A5', 'D6']
for idx, (name, hl) in enumerate(EV['headlines'].items()):
    add(bell(hz(scale[idx % len(scale)])), hl['land'] - .02, .085, (-.3, .3)[idx % 2], .6)
    for j in range(5):  # a few small glints as pieces settle
        add(bell(hz(rng.choice(['D6', 'F6', 'A6', 'C7'])), .6), hl['land'] - .45 + j * .09, .018, rng.uniform(-.6, .6), .7)

# research: clusters connect; strategy: the choice
for j in range(6): add(bell(hz(['A5', 'D6', 'E6', 'A6', 'D6', 'F6'][j]), 1.2), EV['clusters'] + j * .12, .025, (j - 3) / 4, .7)
add(bell(hz('A5'), 2.5), EV['choice'] + .1, .06, 0, .7); add(bell(hz('D6'), 2.5), EV['choice'] + .3, .04, .2, .7)
# execution: markers tick in rhythm
for m in EV['markers']: add(blip(1760), m, .035, rng.uniform(-.5, .5), .2)
# hub: rows registered
for r in EV['rows']: add(blip(1318.5, .06), r, .045, rng.uniform(-.4, .4), .25)
# cycles: each month a soft tick, every second month a refresh tone
for tk in EV['ticks']: add(blip(2093, .05), tk, .04, 0, .3)
for rf in EV['refresh']: add(bell(hz('A5'), 1.4), rf, .045, 0, .6); add(blip(2637, .05), rf, .03, 0, .3)

# ---------------- brand ----------------
for li, lt in enumerate(EV['letters']): add(bell(hz(['D5', 'F5', 'A5', 'C6', 'D6'][li]), 1.6), lt - .02, .05, (li - 2) / 3, .6)
add(whoosh(.55, 800, 9000, .9), EV['swordIn'], .1, .5, .3)                     # blade drawn in
cut = EV['cut']
add(whoosh(.2, 2500, 14000, .85), cut - .17, .2, -.2, .3)                       # slash air
ring = sum(a * np.sin(2 * np.pi * f * np.arange(int(1.6 * SR)) / SR) * np.exp(-np.arange(int(1.6 * SR)) / SR * d)
           for f, a, d in ((1870, 1, 3), (2960, .6, 4), (4410, .4, 5.5), (6230, .25, 7)))
add(ring, cut, .09, -.1, .8)
add(kick(70, 34, .9), cut, .5, 0, .2)
for (a, b) in EV['strokes']:                                                   # the blade writing 理性
    n = bandnoise(b - a + .02, 2500, 7000) * np.hanning(int((b - a + .02) * SR))
    add(n, a, .05, .45, .2)
add(kick(60, 30, 1.2), EV['descr0'], .35, 0, .3)                                # signature settles
for j, n in enumerate(['D5', 'A5', 'D6', 'F6']): add(bell(hz(n), 3.5), EV['descr0'] + j * .06, .05, (j - 1.5) / 3, .9)

# ---------------- reverb (exponential noise tail) + master ----------------
ir_len = int(2.4 * SR)
ir = rng.standard_normal(ir_len) * np.exp(-np.arange(ir_len) / SR * 2.6)
ir[: int(.012 * SR)] = 0
nfft = 1 << int(np.ceil(np.log2(N + ir_len)))
wet = np.fft.irfft(np.fft.rfft(send, nfft) * np.fft.rfft(ir, nfft), nfft)[:N]
wet /= np.abs(wet).max() + 1e-9
L += wet * .12; R += np.roll(wet, int(.011 * SR)) * .12
fade = np.clip((DUR - t) / 1.4, 0, 1) * np.clip(t / .02, 0, 1)
mix = np.stack([L, R]) * fade
mix /= np.abs(mix).max() + 1e-9
mix = np.tanh(mix * 1.6) / np.tanh(1.6) * .89          # gentle limiting, peak about -1 dBFS
pcm = (mix.T * 32767).astype('<i2')
out = os.path.join(ROOT, 'dist', 'trilha.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print(out, f'{DUR:.1f}s')

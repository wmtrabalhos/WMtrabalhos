# RIZEI · Reels "Inteligência Estratégica"

Reels vertical de 35 segundos (1080 × 1920, 30 fps) que apresenta a RIZEI. Usa a mesma linguagem visual do `RIZEI_Story.mp4`.

## Entregas (`dist/`)

| Arquivo | O que é |
|---|---|
| `RIZEI_Reels.mp4` | Vídeo final com trilha (H.264 + AAC), pronto para postar |
| `trilha.wav` | Trilha instrumental separada (44,1 kHz, estéreo, −14 LUFS) |
| `video_sem_audio.mp4` | Vídeo sem som, para quem for montar outra trilha |
| `index.html` | Animação interativa: linha do tempo, pausa e visualização das margens do Instagram |
| `events.json` | Momentos exatos de cada evento (usado para sincronizar a trilha) |

## Roteiro

| Tempo | Cena | Texto |
|---|---|---|
| 0–3 s | Abertura | Seu marketing começa antes da primeira publicação. |
| 3–7 s | Pesquisa | Mercado. Público. Concorrência. / Investigamos o cenário do seu negócio. |
| 7–11 s | Estratégia | A análise define a direção. / Posicionamento • Prioridades • Canais |
| 11–15 s | Execução | Da estratégia à execução. / Conteúdo • Presença digital • Campanhas |
| 15–20 s | Central | Uma central para acompanhar tudo. / Pesquisas • Planos • Ações |
| 20–23 s | Acompanhamento | Relatórios mensais. |
| 23–26 s | Acompanhamento | Pesquisa atualizada a cada dois meses. |
| 26–31 s | Marca | RIZEI · 理性 · INTELIGÊNCIA ESTRATÉGICA (corte do Z e kanjis feitos pela katana) |
| 31–35 s | Encerramento | Clareza para compreender. Precisão para agir. / Converse com a RIZEI pelo Direct. |

## Como editar

Todo o projeto é código e arquivos abertos. Não depende de programa pago.

- **Textos:** objeto `COPY`, no início do script em `src/reels.template.html`.
- **Tempos das cenas:** chamadas `headline(...)` e `subline(...)` (entrada e saída de cada texto), além de `K` (katana) e `L0` (montagem da logo).
- **Cores:** fundo no bloco `scene.background`; feixes prateados nas cores das `Ribbon`.
- **Logo:** recortes da arte original em `assets/`. `Z.png` tem o corte, e `Zfull.png` é o Z inteiro que aparece antes da espada passar.
- **Trilha:** `tools/audio.py` gera a trilha por síntese (não usa amostras de terceiros) e se sincroniza sozinha pelo `events.json`.

## Como gerar de novo

Requisitos: Python 3 com numpy, Node com Playwright e ffmpeg.

```bash
python3 tools/build.py          # src + assets -> dist/index.html
node tools/render.js            # -> dist/video_sem_audio.mp4 e dist/events.json
python3 tools/audio.py          # -> dist/trilha.wav
ffmpeg -y -i dist/video_sem_audio.mp4 -i dist/trilha.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart dist/RIZEI_Reels.mp4
node tools/frames.js <pasta> 3 8.6 17.5   # quadros soltos para revisão
```

O `three.min.js` (r128, licença MIT) está em `vendor/` para que a renderização funcione sem internet.

## Margens do Instagram

Os textos ficam entre y ≈ 520 e y ≈ 1400 px. A área de cima (0–220 px) e a de baixo (a partir de ≈ 1540 px) ficam livres para a interface do app. Nada importante encosta na lateral direita, onde ficam os botões. Na página interativa, o botão "Margens do Instagram" marca essas áreas.

## Observações

- A central é uma interface conceitual: não mostra números, resultados nem depoimentos.
- A ordem dos traços de 理性 é uma aproximação. O kanji final é a arte original, sem alteração.
- As fontes Cormorant Garamond e Inter têm licença OFL e estão em `assets/fonts/`.

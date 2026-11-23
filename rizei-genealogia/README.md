# Rizei · Origem e Ancestralidade dos Clientes

Campo de pesquisa sobre a **origem do sobrenome e a ancestralidade** de clientes e prospects da Rizei.
Objetivo: ter **repertório para conversar** e **personalizar propostas** (narrativa, estética, referências culturais).

## Como pedir (o mínimo que o Claude precisa)

Basta mandar uma linha. Quanto mais dado, mais fundo a pesquisa vai:

```
Pesquisa: Nome completo do cliente
Nível: 1 (sobrenome) ou 2 (árvore)
Extras (opcional): cidade natal, nomes dos pais/avós, datas, o que o cliente já contou da família
Uso: conversa de relacionamento / proposta de <projeto>
```

Exemplo: `Pesquisa: Mariana Tedesco Albuquerque · Nível 1 · Uso: proposta de rebranding`

## Os dois níveis

| | Nível 1 · Raio-X do Sobrenome | Nível 2 · Árvore Genealógica |
|---|---|---|
| Precisa de | Só o nome completo | Nomes de pais/avós, cidades, datas, **dados vindos do próprio cliente** |
| Entrega | Etimologia, região de origem, rota de imigração para o Brasil, personagens e lugares ligados ao nome, ganchos de conversa | Tudo do N1 + árvore (até onde houver registro), linha do tempo migratória, perguntas para completar com o cliente |
| Tempo | Rápido (1 sessão) | Iterativo (vai sendo completada ao longo do relacionamento) |
| Quando usar | Todo prospect antes da 1ª reunião | Clientes ativos / propostas de alto valor, idealmente com o cliente participando |

## Protocolo de pesquisa (o que o Claude faz)

1. **Separar os sobrenomes** (paterno, materno, de casamento). Cada um é uma linha de investigação.
2. **Etimologia e tipo do sobrenome**: toponímico (lugar), patronímico (filho de), ofício, apelido, religioso/devocional, adotado.
3. **Geografia**: região de origem e concentração atual (Brasil e exterior).
4. **Rota para o Brasil**: ondas migratórias compatíveis (portuguesa colonial, italiana 1875–1920, alemã, japonesa 1908+, sírio-libanesa, espanhola etc.) e onde se concentraram no Brasil.
5. **Nível 2 apenas**: cruzar os dados fornecidos com registros públicos (índices de batismo/casamento, listas de navios, hospedarias de imigrantes, registros de naturalização).
6. **Classificar cada afirmação** por confiança (ver abaixo) e **citar a fonte**.
7. **Traduzir em uso**: ganchos de conversa + ideias para a proposta.

## Regras de honestidade (obrigatórias)

- **Sobrenome não é ancestralidade.** Mesmo sobrenome ≠ mesma família. No N1 falamos da *história do nome*, nunca afirmamos "seus antepassados eram X" sem documento.
- **Níveis de confiança** em toda afirmação:
  - ✅ **Documentado**: registro primário ou fonte genealógica citável
  - 🟡 **Provável**: padrão forte (região + época + sobrenome raro), sem documento da pessoa
  - ⚪ **Hipótese / tradição familiar**: o que se conta, sem comprovação
- **Brasões e "significados nobres"** de sites comerciais são quase sempre genéricos: não usar como fato.
- **Ancestralidade afro-brasileira e indígena**: muitos registros foram perdidos ou nunca existiram, e sobrenomes foram impostos. Tratar com respeito, sem suposições; é tema que o cliente traz, não que a gente puxa.
- **Cristãos-novos, nobreza, "descendente de fulano famoso"**: só com documento.

## Privacidade e LGPD

- **Este repositório é público.** Aqui ficam só método, modelo e fontes. **Dossiês de clientes não entram no git** (a pasta `clientes/` está no `.gitignore`).
- Onde guardar os dossiês: Google Drive (pasta `Rizei/Genealogia`) ou Notion, ou neste repo **se ele for tornado privado**.
- Pesquisar só **pessoas falecidas** e a **história do nome**. Dados de parentes vivos: só o que o próprio cliente contou.
- Na conversa, a pesquisa entra como **curiosidade e presente**, não como dossiê: "Pesquisei a origem do seu sobrenome, olha que história bonita…". Nunca revelar algo sensível (adoção, ilegitimidade, conflitos) que o cliente não trouxe.

## Arquivos

- `_modelo-dossie.md`: estrutura padrão de cada pesquisa
- `fontes.md`: onde pesquisar e o que cada fonte resolve
- `clientes/`: dossiês (local, fora do git)

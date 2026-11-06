# Raio de recarga: Rifaina como polo de abastecimento elétrico
**HI Energy** · estudo de 06/11/2026 · v1 (estimativa, ver "O que validar" no final)

Pergunta: carros elétricos que saem com a bateria cheia precisam parar em Rifaina? Com que probabilidade, em cada rota de SP ↔ MG que passa pela cidade, e na ida e volta de quem vem visitar Rifaina?

---

## 1. Resumo

1. **O corredor de Rifaina é a SP-334 + MG-428.** O trajeto é Ribeirão Preto → Batatais → Franca → Pedregulho → **Rifaina** → (ponte do Rio Grande) → Sacramento → **Araxá**, e depois segue para o Alto Paranaíba (Ibiá, Patrocínio, Patos de Minas). A SP-334 termina em Rifaina, na divisa com Minas ([Wikipedia](https://en.wikipedia.org/wiki/Rodovia_C%C3%A2ndido_Portinari)).
2. **Atenção:** **Uberaba e Uberlândia → Ribeirão Preto NÃO passam por Rifaina.** Esse trajeto vai pela BR-050/Anhanguera, por Igarapava, com cerca de 172 km. **Belo Horizonte → Ribeirão Preto também não**: vai pela MG-050 e Passos, com 505 a 519 km. Do Triângulo Mineiro, o público que passa por Rifaina vem de **Araxá, Sacramento e do Alto Paranaíba**. Uberaba entra como **turista** que vem até Rifaina.
3. **Entre Franca e Araxá há um "vazio" de cerca de 173 km sem carregador rápido** confirmado. Pedregulho e Sacramento não têm nenhum mapeado. Esse é o espaço da HI Energy.
4. **Rifaina fica no fundo do vale do Rio Grande** (cerca de 570 m de altitude, contra cerca de 1.000 m em Franca e Araxá). Todo carro sai da cidade **subindo**, para qualquer lado, e isso gasta mais bateria.
5. **Quem mais precisa parar (porcentagem da frota elétrica estimada):**
   - Ribeirão Preto ↔ Araxá: **83%** precisa parar ao menos uma vez, e para **75%** Rifaina é a parada que resolve.
   - Ribeirão/Batatais → Sacramento ou Ibiá: de 44% a 95%.
   - Turista de **Ribeirão Preto** fazendo ida e volta: **94%** precisa recarregar em Rifaina para voltar para casa (Batatais 68%, Araxá 54%, Uberaba 51%).
6. **Quem quase nunca precisa por autonomia:** Pedregulho, Franca, Sacramento e Igarapava (ida e volta de até 140 km). Esse público vem pela **experiência e conveniência** (o Market, a prainha, a carga enquanto passeia), não por necessidade.

---

## 2. O corredor (distâncias por estrada a partir de Rifaina)

```
 SP ◄──────────────────────────────── RIFAINA ─────────────────────────────► MG
 São Paulo  Campinas   Ribeirão  Batatais  Franca  Pedregulho │ Sacramento  Araxá   Ibiá  Patrocínio  Patos de Minas
  ~475       ~385       ~160      ~115      70       ~26     │    35        103    ~165    ~208         ~265
                         ⚡DC                ⚡?              │                     ⚡DC
                                    ◄─────── ~173 km sem rápido confirmado ───────►
```
⚡DC = carregador rápido confirmado. ⚡? = falta confirmar.

| Cidade | km até Rifaina | Fonte |
|---|---|---|
| Pedregulho | ~26 | Franca–Pedregulho 44 km ([Busca Ônibus](https://www.buscaonibus.com.br/en/ticket/franca/pedregulho)) subtraído de Franca–Rifaina |
| Franca | 70 | Sites de rota |
| Batatais | ~115 | Estimativa (Franca + ~45 km) |
| Ribeirão Preto | ~160 | Estimativa pela SP-334 via Franca. Um site indica 98,7 km, o que não bate com a geografia (só Franca–Rifaina já tem 70 km) |
| Sacramento (MG) | 35 | [adistanciaentre](https://www.adistanciaentre.com/br/distancia-entre-sacramento-mg-e-rifaina-sp-brasil/DistanciaHistoria/2765822.aspx), [rotamapas](https://www.rotamapas.com.br/distancia-entre-sacramento-e-rifaina) |
| Araxá (MG) | 103 | [achedistancia](https://www.achedistancia.com.br/distancia-de-araxa-a-rifaina.html), pela MG-428 |
| Uberaba (MG) | ~100 | Estimativa |
| Ibiá / Patrocínio / Patos | ~165 / ~208 / ~265 | Estimativa (Araxá + trecho) |
| Campinas / São Paulo | ~385 / ~475 | Estimativa (Ribeirão + Anhanguera) |

> As distâncias marcadas como estimativa foram calculadas pela linha reta × 1,38. Esse fator foi calibrado com 4 trechos conhecidos da região (Rifaina–Araxá, Rifaina–Sacramento, Franca–Pedregulho e Franca–Rifaina), que deram fatores entre 1,36 e 1,46. A margem de erro é de cerca de ±10%.

**Carregadores rápidos na região** (diretório colaborativo [Carregados](https://carregados.com.br/estacoes) e vídeos, nov./2026):
- **Ribeirão Preto:** sim, incluindo um hub com 8 portas CCS2 de até 120 kW ([vídeo do Primo Auto](https://www.youtube.com/watch?v=-7TiQVbgWmE)).
- **Araxá:** 11 eletropostos, sendo 3 rápidos (por exemplo, o Hotel Dona Beja).
- **Uberaba:** 24 eletropostos, sendo 5 rápidos.
- **Franca:** aparece como cidade com eletropostos, mas **não consegui confirmar se há carregador rápido**. É o dado que mais muda o resultado.
- **Pedregulho e Sacramento:** nenhum encontrado.
- A NuCharge (de Uberlândia) anunciou +155 eletropostos em MG em 2027, incluindo Triângulo e Alto Paranaíba ([Regionalzão](https://regionalzao.com.br/economia/empresa-uberlandia-expansao-155-eletropostos-minas-2027/)). A concorrência do lado mineiro tende a crescer.

---

## 3. Autonomia útil na estrada (o "raio" de cada carro)

"Autonomia útil" é o quanto o carro roda **saindo com 100% e chegando com cerca de 15% de reserva**, na estrada (100–110 km/h, ar-condicionado ligado). É sempre menor que o número do Inmetro (PBEV).

| Classe | Exemplos | Autonomia oficial (PBEV) | **Autonomia útil na estrada** | Peso estimado na frota |
|---|---|---|---|---|
| Compacto | BYD Dolphin Mini (GL 30 kWh / GS 38 kWh), Renault Kwid E-Tech | ~180–280 km | **150–210 km** | 45% |
| Médio | BYD Dolphin, GWM Ora 03, Geely EX2, GAC Aion UT | ~290–320 km | **200–260 km** | 35% |
| Longo | BYD Seal, Yuan Plus, Volvo EX30, BMW iX3 | 300–400+ km | **260–360 km** | 20% |

Fontes de autonomia: Dolphin Mini GS com 280 km PBEV e uso real entre 180 e 238 km ([EVblog](https://evblog.com.br/modelo/byd-dolphin-mini/), [Hachiroku](https://hachiroku.com.br/eletricos/byd/dolphin-mini/), [Localiza](https://assinatura.localiza.com/blog/post/byd-dolphin-mini-2026)); Ora 03 com 310–315 km ([EVblog](https://evblog.com.br/modelo/byd-dolphin-mini/)).
O peso de cada classe na frota é uma **suposição** baseada no domínio do Dolphin Mini nas vendas e nos vídeos virais. Os **híbridos plug-in** (como o BYD Song Pro) ficam fora: não precisam parar, mas podem carregar por oportunidade.

### Raio útil a partir de Rifaina (ida e volta sem recarregar)
É a metade da autonomia útil, menos a subida para sair do vale:

| Classe | Vem e volta sem carregar se a origem estiver a até… |
|---|---|
| Compacto | **70–100 km** (Franca, Pedregulho, Sacramento, Igarapava) |
| Médio | **95–125 km** (+ Araxá, Uberaba, Batatais no limite) |
| Longo | **125–175 km** (+ Ribeirão Preto no limite) |

**Quem vem de mais longe que isso precisa carregar em Rifaina (ou no caminho) para voltar.**

---

## 4. Probabilidade de precisar parar em Rifaina

**Como foi calculado:** simulação com 200 mil carros sorteados dentro das faixas de autonomia útil e dos pesos da frota acima. A subida para sair do vale foi contada como mais 10 km de consumo. Depois da recarga em Rifaina, o carro segue com cerca de 80%.

### 4.1 Turista: ida e volta até Rifaina, sem carregar em outro lugar

| Origem | Ida e volta | Compacto | Médio | Longo | **Frota** |
|---|---|---|---|---|---|
| Pedregulho | 52 km | 0% | 0% | 0% | **0%** |
| Sacramento | 70 km | 0% | 0% | 0% | **0%** |
| Igarapava | 96 km | 0% | 0% | 0% | **0%** |
| Franca | 140 km | 0% | 0% | 0% | **0%** |
| Uberaba | 200 km | 100% | 16% | 0% | **51%** |
| Araxá | 206 km | 100% | 27% | 0% | **54%** |
| Batatais | 230 km | 100% | 67% | 0% | **68%** |
| Perdizes | 230 km | 100% | 67% | 0% | **68%** |
| **Ribeirão Preto** | 320 km | 100% | 100% | 70% | **94%** |
| Ibiá | 330 km | 100% | 100% | 80% | **96%** |
| Patrocínio | 416 km | 100% | 100% | 100% | **100%** |

**Leitura:** quem vem de **mais de 100 km** quase sempre vai precisar carregar para voltar, e o turista de **Ribeirão Preto** é o caso mais claro. Quem dorme numa pousada com tomada ou carregador AC reduz essa necessidade, por isso **vale mapear e fazer parceria com as pousadas**.

### 4.2 Passagem: origem com 100% → destino, com Rifaina no meio

| Viagem | Total | **Precisa parar** (frota) | **Rifaina resolve** | Observação |
|---|---|---|---|---|
| Ribeirão Preto → Araxá | ~273 km | **83%** | **75%** | 7% (compactos) não chegam a Rifaina sem parar antes em Franca |
| Araxá → Ribeirão Preto | ~273 km | **83%** | **60%** | Mais 23% (compactos) carregam em Rifaina e ainda precisam de uma parada rápida em Franca |
| Batatais → Araxá | ~228 km | **61%** | **61%** | Rifaina é a parada natural |
| Ribeirão Preto → Sacramento | ~205 km | **44%** | **37%** | |
| Franca → Araxá | ~183 km | **25%** | **25%** | Só compactos |
| Ribeirão Preto → Ibiá | ~335 km | **95%** | **68%** | |
| Ibiá → Ribeirão Preto | ~335 km | **95%** | **72%** | |
| Ribeirão Preto → Patrocínio | ~378 km | **100%** | 37% | A maioria precisa de 2 paradas (Rifaina + Araxá) |
| Patrocínio → Ribeirão/Franca | 288–378 km | 86–100% | 37–52% | Compactos e parte dos médios param antes, em Araxá |
| Patos de Minas → Franca/Ribeirão | 345–435 km | 97–100% | 16–19% | Quase todos param em Araxá. Rifaina vira a 2ª parada |
| Araxá → Campinas/São Paulo | 500–590 km | 100% | 0% como única parada | Rifaina é uma das 2 ou 3 paradas da viagem |

### 4.3 Trechos entre carregadores rápidos (os "vazios")

| Vazio | km (com a subida) | Frota que não cruza sem parar |
|---|---|---|
| **Ribeirão Preto ↔ Araxá** (se Franca **não** tiver carregador rápido) | ~273 | **83%** |
| **Franca ↔ Araxá** (se Franca **tiver** carregador rápido) | ~183 | **25%** (os compactos) |

**Conclusão:** a demanda de passagem depende muito de **Franca ter ou não carregador rápido**. Sem ele, Rifaina é parada obrigatória para mais de 8 em cada 10 elétricos no eixo Ribeirão–Araxá. Com ele, Rifaina segue essencial para os compactos (o carro mais vendido) e para quem vem de Minas subindo a serra.

---

## 5. O que isso muda na estratégia da HI Energy

**Público prioritário** (onde a probabilidade é alta):
1. Turistas de Ribeirão Preto, Batatais, Uberaba e Araxá, que vêm para a prainha e voltam no mesmo dia (de 50% a 94% precisam carregar).
2. Viajantes do eixo Ribeirão/Campinas/SP ↔ Araxá/Alto Paranaíba (de 60% a 83%).
3. Donos de **Dolphin Mini e outros compactos**, para quem Rifaina resolve quase todas as rotas.

**Público de conveniência** (probabilidade perto de 0% por autonomia): Franca, Pedregulho e Sacramento. Para eles a mensagem não é "você precisa carregar", e sim "**carregue enquanto curte a prainha** / tome um café".

**Ideias de conteúdo que saem deste estudo:**
- Reel **"Dá para ir de Ribeirão até a prainha de Rifaina e voltar sem carregar?"** (Resposta: quase nunca. 94% precisam carregar.)
- Carrossel **"Seu elétrico vai e volta de Rifaina sem parar?"** com a tabela do raio útil por modelo (Dolphin Mini, Dolphin, Seal).
- Reel **"Rifaina fica num buraco… e seu carro sente isso"**, explicando a subida para sair do vale e por que é melhor sair com a bateria cheia.
- **"Do Triângulo para SP pela rota mais bonita"**: Araxá → Sacramento → Rifaina, com o mapa do vazio de 173 km.

**Ações fora do Instagram:**
- Aparecer no **PlugShare e no Google Maps** com destaque para "único ponto entre Franca e Araxá" (se for confirmado).
- **Placas** na SP-334 (Pedregulho) e na MG-428 (Sacramento): "Recarga elétrica a X km".
- **Parcerias com pousadas e ranchos** da represa, e com influenciadores de Ribeirão e Araxá.

---

## 6. O que validar antes de usar os números publicamente
1. **Carregador rápido em Franca:** conferir no PlugShare/Carregados (o site não abriu nesta sessão). É o que mais altera o resultado.
2. **Distâncias estimadas** (Ribeirão, Batatais, Ibiá, Patrocínio, Uberaba): confirmar no Google Maps. Ribeirão–Rifaina é a mais importante.
3. **Peso de cada classe na frota:** se a HI Energy registrar o modelo de cada carro que carrega, os números podem ser recalculados com dados reais.
4. **Altitude de Rifaina e da serra:** os valores (~570 m contra ~1.000 m) são aproximados.
5. **Dados da HI Energy:** potência e preço. Com eles, dá para calcular quanto tempo cada perfil fica parado e quanto gasta no Market.

> Recomendação para a operação: perguntar a cada cliente **"de onde vem / para onde vai / qual carro / com quantos % chegou"**. São as mesmas perguntas da série R2 do plano de conteúdo. Em 1 mês isso substitui as suposições deste estudo por dados reais.

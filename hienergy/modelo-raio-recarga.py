import numpy as np
rng=np.random.default_rng(7); N=200000
cls=[('Compacto',0.45,150,210),('Médio',0.35,200,260),('Longo',0.20,260,360)]
L=np.concatenate([rng.uniform(a,b,int(N*w)) for _,w,a,b in cls]); lab=np.concatenate([[n]*int(N*w) for n,w,a,b in cls])
PEN=10  # km equivalentes da subida para sair do vale do Rio Grande
D={'Pedregulho':26,'Franca':70,'Batatais':115,'Ribeirão Preto':160,'Igarapava':48,'Sacramento':35,'Araxá':103,
   'Uberaba':100,'Perdizes':115,'Ibiá':165,'Patrocínio':208,'Patos de Minas':265,'Campinas':385,'São Paulo':475}
def p(mask): return {n:round(100*mask[lab==n].mean()) for n,*_ in cls}|{'Frota':round(100*mask.mean())}
print('== IDA E VOLTA até Rifaina, sem recarregar no caminho')
for o in ['Pedregulho','Igarapava','Sacramento','Franca','Uberaba','Araxá','Batatais','Perdizes','Ribeirão Preto','Ibiá','Patrocínio']:
    need=2*D[o]+PEN>L; print(o, 2*D[o], p(need))
print('== PASSAGEM: origem com 100% -> destino, Rifaina no meio, sem outra recarga')
pairs=[('Ribeirão Preto','Araxá'),('Franca','Araxá'),('Batatais','Araxá'),('Ribeirão Preto','Sacramento'),('Franca','Patrocínio'),
       ('Ribeirão Preto','Patrocínio'),('Ribeirão Preto','Ibiá'),('Araxá','Ribeirão Preto'),('Ibiá','Ribeirão Preto'),('Patrocínio','Ribeirão Preto'),
       ('Patrocínio','Franca'),('Patos de Minas','Franca'),('Patos de Minas','Ribeirão Preto'),('Araxá','Campinas'),('Araxá','São Paulo')]
for o,d in pairs:
    tot=D[o]+D[d]+PEN; need=tot>L; reach=D[o]<=L
    # após carregar em Rifaina até ~80%, consegue terminar?
    finish=D[d]+PEN<=0.8/0.85*L
    rif=need&reach&finish
    print(f"{o} -> {d}: {tot} km | precisa parar: {p(need)} | parada em Rifaina resolve: {p(rif)} | nem chega a Rifaina: {p(~reach)} | precisa 2a parada após Rifaina: {p(need&reach&~finish)}")
print('== Trechos entre carregadores rápidos (gap)')
for name,g in [('Ribeirão Preto <-> Araxá (sem rápido em Franca)',263),('Franca <-> Araxá (se houver rápido em Franca)',173),('Franca <-> Uberaba via Rifaina',170)]:
    print(name,g+PEN,p(g+PEN>L))
print('== Raio útil de ida e volta (L/2) por classe')
for n,w,a,b in cls: print(n,(a-PEN)//2,(b-PEN)//2)

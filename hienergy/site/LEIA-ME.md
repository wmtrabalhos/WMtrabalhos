# Publicar o cofre no wmperformance.com.br

A pasta `hienergy/` é um site estático completo, com um único arquivo (`index.html`). Não precisa de banco de dados nem de servidor especial.

Depois de publicado, o cofre fica no endereço **https://wmperformance.com.br/hienergy/**.

## Hospedagem com gerenciador de arquivos (Hostinger, HostGator, Locaweb, cPanel)
1. Abra o Gerenciador de Arquivos do painel da hospedagem.
2. Entre na pasta `public_html`.
3. Crie a pasta `hienergy`.
4. Envie o arquivo `index.html` para dentro dela.

## WordPress
Opção A: envie a pasta `hienergy` para o `public_html` pelo gerenciador de arquivos, como no item anterior. O WordPress não interfere em pastas que existem fisicamente no servidor.

Opção B: crie uma página e cole este bloco "HTML personalizado":

```html
<iframe src="https://wmperformance.com.br/hienergy/" style="width:100%;height:90vh;border:0;border-radius:12px" title="Cofre de pesquisa HI Energy"></iframe>
```

Esse bloco só funciona depois que a opção A já estiver feita.

## Netlify, Vercel ou GitHub Pages
Publique a pasta `site/`. O cofre fica em `/hienergy/`.

## Wix, Squarespace ou Lovable
- **Wix e Squarespace:** use um elemento de "Embed / HTML" apontando para um endereço onde o arquivo já esteja publicado.
- **Lovable:** peça para adicionar a página na rota `/hienergy` e envie o `index.html` como referência.

## Privacidade
- O arquivo tem `noindex`, então o Google não vai indexar a página.
- Mesmo assim, qualquer pessoa com o link consegue abrir. Para restringir o acesso, proteja a pasta com senha pelo painel da hospedagem ("Proteger diretório" / "Password protect directories").

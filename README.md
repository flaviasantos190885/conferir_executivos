# Conferir executivos

Favorito (bookmarklet) que confere os contatos da gestão no Rubeus com a planilha de distribuição de clientes.
A planilha é a que vale. Não usa API nem token: só lê a tela de **Contatos**.

## Como instalar (uma vez)

1. Abra `favorito.txt` aqui no GitHub e clique em **Copy raw file**.
2. No Chrome: `Ctrl+Shift+O` → três pontinhos → **Adicionar novo favorito**.
3. Nome: "Conferir gestão". URL: cole o texto copiado (começa com `javascript:`). Salve.

## Como usar

1. Abra **Contatos** no Rubeus (visão com as colunas Nome e RpR - Responsável comercial).
2. Clique no favorito. Cole o link da planilha (a aba certa) e clique em **Conferir**. O último link fica salvo.
3. Se o Google bloquear a leitura do link, baixe a aba como CSV e escolha o arquivo no painel.

## O que mostra

- **Divergentes:** cliente nos dois lados com executivo diferente (mostra o que deveria ser).
- **Faltando na gestão:** está na planilha e não nos contatos.
- **Só na gestão:** está nos contatos e não na planilha.
- **Nome parecido:** nomes escritos de forma diferente (abreviação, parte do nome, erro de digitação), com executivo igual ou diferente.
- **Certos.**

Alternativa sem favorito: cole o conteúdo de `conferir-gestao.js` no Console (F12) da página de Contatos.

Depois de alterar `conferir-gestao.js`, rode `python3 -I gerar-favorito.py` para atualizar o `favorito.txt`.

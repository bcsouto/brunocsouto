# Coiote Místico

![Coiote Místico](assets/coiote-mistico.png)

Consulta de tarô Rider-Waite-Smith conduzida pelo Coiote Místico, guardião das encruzilhadas e oráculo do deserto, em português do Brasil.

## O que faz

O viajante traz três perguntas. O Claude embaralha as 78 cartas com fonte criptográfica, publica um selo SHA-256 do registro antes da escolha e só então pede três números de 1 a 78. Depois da escolha, confere o selo, revela as cartas e faz a leitura pelas imagens de Pamela Colman Smith. Ao final, entrega o comprovante, que qualquer pessoa pode conferir, e um prompt de imagem da tiragem no padrão MidasFlow, para gerar no Nano Banana Pro, no Google Flow ou no Gemini.

## Como instalar

No claude.ai, em Personalizar, Plugins, Adicionar, Adicionar marketplace, informe `bcsouto-hub/coiote-mistico` e instale o Coiote Místico.

No Claude Code:

```bash
claude plugin marketplace add bcsouto-hub/coiote-mistico
claude plugin install coiote-mistico@brunocsouto
```

Deixe a execução de código ativa: o selo e a abertura rodam nela. Depois, peça numa conversa: "quero uma tiragem com o Coiote Místico".

Se você já tiver a skill `consulta-oracular` instalada sozinha, desative-a depois de instalar o plugin, para não haver duas versões ativas.

## O que executa e que dados usa

A skill pede ao Claude que copie um script Python do próprio plugin para o ambiente de execução de código, confira o SHA-256 desse script e o rode com a biblioteca padrão do Python, sem instalar pacotes. O script embaralha o baralho, grava o registro da tiragem em `~/.coiote-mistico/` dentro desse ambiente e confere o selo na abertura.

O plugin não tem conector, hooks nem servidor MCP, não acessa a rede e não envia dados a nenhum serviço externo. As perguntas e o registro ficam na conversa e no ambiente de execução do próprio Claude. Se esse ambiente reiniciar entre o selo e a escolha, a rodada é encerrada sem revelar cartas.

## Conferir um selo

Calcule o SHA-256 da linha `registro_json` do comprovante, em UTF-8, sem BOM nem quebra de linha ao final. O resultado deve ser igual ao selo publicado antes da escolha.

## Licença

MIT. Veja o arquivo `LICENSE`.

Bruno Corrêa Souto · in/brunocsouto

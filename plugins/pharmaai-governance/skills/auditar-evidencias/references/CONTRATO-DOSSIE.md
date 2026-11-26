# Contrato de dossiê 1.1.0

Use JSON somente sob pedido, conforme ../schemas/dossie.schema.json. O contrato registra escopo, fontes, evidências, afirmações e pendências; seus estados são declarações fundamentadas na análise, não certificados.

A raiz contém schema_version, titulo, escopo, fontes, evidencias, afirmacoes, pendencias e cobertura. IDs são únicos em cada coleção. Localizadores apontam página, seção, tabela ou dispositivo real. Campos desconhecidos aceitam null onde previsto; não invente metadados. Toda afirmação solicitada consta em escopo.afirmacoes_solicitadas e na coleção afirmacoes.

Fonte registra localização, natureza, origem (fornecida/web), acesso, data documental e de acesso, temporalidade e sha256_texto opcional. O hash é dos bytes UTF-8 do texto decodificado, sem BOM, sem normalização ou troca de quebras; não é hash do PDF original. Em universo fechado, fontes são fornecidas; nenhuma afirmação recebe verificacao_atual true.

Evidência liga fonte a trecho literal curto e localizador. Afirmação liga evidências com relacao APOIA, CONTRADIZ ou CONTEXTO. SUSTENTADA exige apoio sem contradição; PARCIALMENTE_SUSTENTADA exige apoio e limitações; CONTRADITA exige contradição; NAO_VERIFICADA exige limitação e pendência ligada à afirmação. Justificativa pode resumir ou interpretar, sem se apresentar como citação literal.

Alegação de verificação atual requer universo aberto, apoio de fonte web marcada consulta_atual e acessada no mesmo dia da consulta, com acesso efetivo. Esses requisitos não comprovam atualidade factual: a análise ainda precisa conferir versões, alcance e condições da afirmação. O validador não lê a web.

Cobertura integral significa todas as afirmações solicitadas examinadas com acesso completo às evidências usadas, sem afirmação NAO_VERIFICADA nem pendência. Uma afirmação CONTRADITA ou parcialmente sustentada pode ter sido integralmente examinada; estado de suporte não é estado de obtenção. Se houver fonte parcial usada, pendência ou afirmação não verificada, use parcial.

## Validação opcional

Com Python 3, usando o diretório-base informado quando a skill é carregada (`<skill>` abaixo):

```text
python3 -I <skill>/scripts/validate_dossier.py dossie.json
python3 -I <skill>/scripts/validate_dossier.py dossie.json --texts textos.json
```

textos.json é um objeto fonte_id → texto integral efetivamente obtido. Com --texts, todas as fontes usadas em evidências ou com hash declarado devem ter texto; o script confere presença literal dos trechos e hashes declarados. Não envie este arquivo a serviço externo para validar. CLI usa somente biblioteca padrão, sem rede nem chave de API.

Sem --texts, o resultado se limita a estrutura e coerência referencial; não declare trechos conferidos automaticamente. Mesmo com textos, a presença literal não comprova que o trecho apoia a afirmação nem que o arquivo é autêntico. Saída: valido, erros, escopo e limite; código 0 válido, 1 inconsistência, 2 erro de leitura/execução. O script implementa apenas os termos usados no schema incluído e rejeita termos desconhecidos, sem se apresentar como validador genérico Draft 2020-12.

Sem executor, revise o contrato manualmente e declare validação automatizada não executada. Os exemplos em ../assets são fictícios.

## Material auditado e versões

A versão 1.1.0 acrescenta material_auditado, versao_dossie, revisao_anterior e mudancas. O material auditado é o alvo da auditoria, distinto das fontes usadas para avaliá-lo. Registre id, titulo, localizacao, versao, data_documento, sha256_arquivo e sha256_texto; campos desconhecidos aceitam null onde previsto. sha256_arquivo é o hash dos bytes do arquivo original, enquanto sha256_texto segue a convenção UTF-8 do texto descrita acima. O helper verifica o formato desses hashes do alvo, mas não os recalcula sem o arquivo-alvo; não declare integridade do alvo conferida automaticamente.

versao_dossie identifica esta entrega. revisao_anterior é null na primeira auditoria; em comparação, identifica localizacao, versao_dossie, material_id, versao_material e sha256_arquivo do dossiê anterior quando disponível. A versão do dossiê atual deve ser distinta.

Cada mudança informa afirmacao_id, tipo (incluida, alterada, removida), estado_anterior, estado_atual, motivo e evidencia_ids atuais. Inclusão não tem estado anterior; remoção não possui estado atual nem reaparece nas afirmações atuais. Alteração preserva o ID e explica mudança de texto, evidência ou suporte, mesmo quando o estado permaneceu igual. Vínculos apontam evidências atuais; evidência histórica permanece no dossiê anterior. ID só muda quando a unidade verificável mudou de identidade.

## Importação legada

O helper aceita 1.0.0 usando ../schemas/dossie-1.0.0.schema.json e preserva seus limites. Para exportar 1.1.0, obtenha os novos dados ou use null apenas onde previsto; não invente material, datas, revisão anterior ou hashes. Importação não recebe uma auditoria nova por mera alteração de schema_version. Testes distribuídos: `python3 tests/test_dossier.py` a partir da raiz do plugin.

## Conferência efetiva entre versões

`python3 -I <skill>/scripts/validate_dossier.py atual.json --previous anterior.json --texts textos.json`

--previous é opcional, mas necessário para afirmar cotejo automatizado entre versões. O helper valida o anterior, confere sua identificação disponível, estados anteriores, inclusões, remoções e mudanças materiais de texto, camada, limites, justificativa e suporte. Mudança de evidência inclui trecho, localizador e identificação documental da fonte; mero novo horário de acesso não obriga registrar alteração material. IDs removidos inexistentes, mudanças omitidas e mudanças declaradas sem diferença são rejeitados. Hash anterior declarado é conferido contra os bytes originais pela CLI.

Sem --previous, a validação verifica apenas consistência interna e informa esse limite. Metadados ausentes em contrato anterior 1.0.0 não são inventados nem considerados conferidos. O cotejo não comprova verdade das afirmações nem equivalência científica dos textos.

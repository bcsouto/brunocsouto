---
name: acompanhar-mudancas
description: Consulta mudanças regulatórias em uma janela de datas e em autoridades definidas, filtra materialidade, acompanha consultas públicas, prorrogações e prazos, e registra a cobertura de fontes. Usar quando o usuário pedir novidades regulatórias, o que mudou entre datas, consultas abertas, prazos de contribuição ou um monitoramento periódico. Trabalha sob demanda; agendamento só existe quando criado por ferramenta real da sessão.
---

# Mudanças regulatórias

Leia o [núcleo](../../references/NUCLEO.md). Retome a lista de autoridades e temas fornecida; para criar uma, use o [perfil](../../templates/PERFIL.md). Se faltarem período e jurisdição, aproveite o contexto ou peça o mínimo antes de afirmar cobertura. Não use uma única autoridade por padrão para representar o mundo.

1. Defina janela de publicação, data da consulta, território, setores, temas e critério de materialidade. Diferencie evento publicado no período de conteúdo antigo atualizado.
2. Consulte fontes oficiais adequadas e registre para cada fonte: consultada com resultado, consultada sem resultado, falha ou não consultada. Use o [mapa de fontes](../../references/FONTES.md). Sem conectores, use páginas oficiais acessíveis; sem acesso externo, analise os alertas recebidos e explicite a cobertura.
3. Confirme tipo e status de cada evento, documento afetado, alteração, datas e destinatários. Elimine duplicidades entre notícia, consulta e ato sobre o mesmo evento sem apagar diferenças materiais. Não trate proposta como obrigação vigente.
4. Classifique: ação prioritária (prazo, obrigação, segurança ou exposição relevante), analisar (efeito plausível ainda dependente de aplicação) ou acompanhar (sinal sem ação imediata). Explique a razão; não invente limiares numéricos.
5. Para comentários públicos, confirme órgão, identificador da consulta, canal, fuso, prazo e eventual prorrogação. Conte prazos somente com regra e termo inicial confirmados; diferencie prazo legal e meta interna. Não protocole contribuição automaticamente.
6. Compare com o último registro apenas se ele estiver disponível. Sem linha de base, entregue panorama datado; não chame de “novo desde a última rodada”. Registre lacunas com IDs e preserve histórico em atualizações autorizadas.

Entregue uma síntese e tabela `evento | autoridade/fonte | status | publicação | vigência/aplicação/prazo | impacto | materialidade | próxima ação`, seguidas da cobertura de fontes. Use o [registro de lacunas](../../templates/LACUNAS.md) se houver acompanhamento de ações.

Para agendamento solicitado, verifique se a sessão oferece tarefas agendadas (scheduled tasks) e as preferências do usuário antes de configurar. A criação só existe após retorno de sucesso. Não envie Slack, e-mail ou alerta a terceiros por inferência. Quando houver monitoramento autorizado, notifique mudanças materiais ou falhas que exijam ação; mantenha silêncio em rodadas sem novidade, salvo pedido de relatório periódico.

# Agente de Cotação

Projeto de automação desenvolvido em Python para monitorar mensagens de um grupo específico do WhatsApp, identificar novas mensagens e estruturar os dados recebidos para utilização em processos de cotação.

## Objetivo

O projeto surgiu a partir de uma necessidade real: organizar pedidos recebidos através de mensagens no WhatsApp, reduzindo o trabalho manual necessário para coletar, interpretar e estruturar essas informações.

A proposta é evoluir a automação para que o sistema seja capaz de monitorar continuamente o grupo, identificar novas mensagens, estruturar os pedidos e, posteriormente, utilizar Inteligência Artificial para interpretar informações mais complexas e gerar automaticamente uma planilha de cotação.

## Funcionamento atual

Atualmente, o projeto é capaz de:

- Abrir o WhatsApp Web utilizando Playwright;
- Manter a sessão do WhatsApp Web armazenada localmente, evitando a necessidade de realizar o login por QR Code a cada execução;
- Acessar um grupo específico;
- Monitorar alterações no conteúdo da conversa utilizando `MutationObserver`;
- Identificar quando novas mensagens são adicionadas;
- Acionar o processamento das novas mensagens automaticamente;
- Extrair e organizar informações das mensagens;
- Estruturar os dados processados em JSON.

## Arquitetura atual

O fluxo atual do projeto segue aproximadamente:

WhatsApp Web
→ Playwright
→ MutationObserver
→ Captura da nova mensagem
→ Processamento
→ Estruturação dos dados
→ JSON

A comunicação entre o JavaScript executado no navegador e o Python é realizada utilizando a funcionalidade `expose_function()` do Playwright.

## Tecnologias utilizadas

- Python
- Playwright
- JavaScript
- MutationObserver
- JSON
- Regex

## Próximos passos

- Refinar a identificação de mensagens novas;
- Melhorar a estrutura dos módulos e funções;
- Aprimorar o processamento e a estruturação dos pedidos;
- Desenvolver o interpretador dos pedidos;
- Integrar um modelo de Inteligência Artificial para interpretação das mensagens;
- Estruturar diferentes tipos de pedidos e ofertas;
- Gerar automaticamente planilhas com os pedidos processados;
- Implementar leitura e interpretação de informações presentes em imagens;
- Melhorar a persistência do estado da automação.

## Status

🚧 **Projeto em desenvolvimento**

O projeto está sendo desenvolvido de forma incremental, com cada etapa sendo testada antes da implementação da próxima funcionalidade.

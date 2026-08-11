# Agente de Cotação

Projeto de automação desenvolvido em Python para coletar e estruturar mensagens de um grupo específico do WhatsApp, com o objetivo de transformar pedidos recebidos em dados organizados para utilização em processos de cotação.

## Objetivo

O projeto surgiu a partir de uma necessidade real: organizar pedidos recebidos através de mensagens no WhatsApp, reduzindo o trabalho manual necessário para coletar e estruturar essas informações.

A proposta é evoluir a automação para que, além da coleta das mensagens, o sistema consiga interpretar os pedidos utilizando Inteligência Artificial e gerar automaticamente uma planilha estruturada.

## Funcionamento atual

Atualmente, o projeto é capaz de:

- Abrir o WhatsApp Web utilizando Playwright;
- Mantém a sessão do WhatsApp Web armazenada localmente, evitando a necessidade de realizar o login por QR Code a cada execução.
- Acessar um grupo específico;
- Coletar as mensagens disponíveis;
- Extrair e organizar as informações das mensagens;
- Armazenar os dados estruturados em JSON.

## Tecnologias utilizadas

- Python
- Playwright
- JSON
- Regex

## Próximos passos

- Refatorar o código em funções e módulos;
- Melhorar a organização e estrutura do projeto;
- Implementar a identificação de mensagens novas;
- Estruturar os pedidos recebidos;
- Integrar um modelo de Inteligência Artificial para interpretação das mensagens;
- Gerar automaticamente planilhas com os pedidos processados.

## Status

🚧 Projeto em desenvolvimento.

O projeto está sendo desenvolvido de forma incremental, com novas funcionalidades sendo adicionadas conforme a arquitetura é estruturada e testada.

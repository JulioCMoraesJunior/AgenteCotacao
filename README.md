# 🤖 Agente de Cotação

Projeto de automação desenvolvido em Python para monitorar mensagens de um grupo específico do WhatsApp, identificar novas mensagens e estruturar os dados recebidos para uso em processos de cotação.

---

## 🎯 Objetivo

O projeto surgiu de uma necessidade real: organizar pedidos recebidos por mensagens no WhatsApp, reduzindo o trabalho manual de coletar, interpretar e estruturar essas informações.

A proposta é evoluir a automação para que o sistema seja capaz de:

- Monitorar continuamente um grupo do WhatsApp;
- Identificar novas mensagens;
- Interpretar os pedidos recebidos;
- Estruturar os dados automaticamente;
- Gerar uma planilha de cotação;
- Utilizar Inteligência Artificial para interpretar mensagens em linguagem natural.

---

## ⚙️ Funcionamento

Atualmente, o sistema é capaz de:

- Abrir o WhatsApp Web utilizando **Playwright**;
- Manter a sessão do WhatsApp Web armazenada localmente;
- Acessar um grupo específico;
- Monitorar alterações no conteúdo da conversa utilizando **MutationObserver**;
- Identificar quando novas mensagens são adicionadas;
- Acionar automaticamente o processamento;
- Extrair informações das mensagens;
- Estruturar os dados capturados em **JSON**;
- Enviar as mensagens para um modelo de **Inteligência Artificial**;
- Interpretar produtos e quantidades solicitadas;
- Estruturar o resultado da IA em JSON;
- Utilizar **OpenPyXL** para inserir os pedidos em uma planilha Excel.

---

## 🏗️ Arquitetura

O fluxo atual do projeto segue a seguinte estrutura:

```
WhatsApp Web
     │
     ▼
  Playwright
     │
     ▼
MutationObserver
     │
     ▼
Captura das mensagens
     │
     ▼
     JSON
     │
     ▼
Inteligência Artificial
     │
     ▼
JSON estruturado
     │
     ▼
  OpenPyXL
     │
     ▼
Planilha Excel
```

A comunicação entre o JavaScript executado no navegador e o Python é realizada por meio da função `expose_function()` do Playwright.

---

## 🧠 Inteligência Artificial

A IA é utilizada para interpretar mensagens escritas de formas diferentes por cada cliente.

Por exemplo, mensagens como:

> "manda 10 tradicional 180"

ou:

> "preciso de 5 light 180 e 3 nata 300g"

são interpretadas e associadas aos produtos disponíveis na planilha.

O resultado é estruturado em JSON, contendo o cliente, os produtos e as respectivas quantidades.

### Exemplo

```json
{
    "usuario": "Carlos",
    "produtos": {
        "requeijao 180g tradicional": 10,
        "requeijao 180g light": 0,
        "requeijao 400g tradicional": 0,
        "cream cheese 150g": 0,
        "nata 300g": 0
    }
}
```

---

## 📦 Tecnologias utilizadas

- Python
- Playwright
- JavaScript
- MutationObserver
- Google Gemini API
- OpenPyXL
- JSON
- Regex

---

## 🚀 Próximos passos

- [ ] Refinar a identificação de mensagens novas
- [ ] Melhorar a estrutura dos módulos e funções
- [ ] Aprimorar o processamento e a estruturação dos pedidos
- [ ] Tratar múltiplas mensagens do mesmo cliente
- [ ] Implementar soma e atualização de pedidos existentes
- [ ] Melhorar a validação dos produtos retornados pela IA
- [ ] Estruturar diferentes tipos de pedidos e ofertas
- [ ] Aprimorar a geração e atualização das planilhas
- [ ] Implementar leitura e interpretação de informações presentes em imagens
- [ ] Melhorar a persistência do estado da automação
- [ ] Avaliar alternativas para execução local do modelo de IA
- [ ] Preparar o projeto para distribuição como aplicação executável

---

## 📌 Status

🚧 **Projeto em desenvolvimento**

O desenvolvimento é feito de forma incremental, com cada etapa testada antes da implementação da próxima funcionalidade.

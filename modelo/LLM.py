import json
from google import genai
from modelo.padrao_excel import PRODUTOS_OFICIAIS
with open("modelo/prompt.txt", "r", encoding = "utf-8") as arquivo:
    prompt = arquivo.read()
with open('chave.txt', 'r', encoding = 'utf-8') as arquivo:
    chave = arquivo.read()


def llm():
    with open("json/estado.json", "r", encoding="utf-8") as arquivo:
        mensagens = json.load(arquivo)

    client = genai.Client(api_key= chave)

    chat = client.chats.create(model='gemini-3.6-flash')

    resposta = chat.send_message(
        message=f'{prompt} + {PRODUTOS_OFICIAIS} + {mensagens}',
        config={"response_mime_type": "application/json"}
    )

    resposta_llm = json.loads(resposta.text)
    with open('json/resposta_llm.json', 'w', encoding='utf-8') as arquivo:
        json.dump(resposta_llm, arquivo, indent=4, ensure_ascii=False)
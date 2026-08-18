import re
import json

def inject_json(mensagens):
    cont = mensagens.count()
    mensagem_json = []
    for i in range(cont):
        padrao_json = {
            'hora': '',
            'data': '',
            'usuario': '',
            'mensagem': ''
        }
        titulo = mensagens.nth(i).get_attribute('data-pre-plain-text')
        mensagem = mensagens.nth(i).inner_text()
        hora = r'(\d{2}:\d{2})'
        data = r'(\d{2}/\d{2}/\d{4})'
        usuario = r'(.*?):'
        padrao = '\\[' + hora + ', ' + data + '\\] ' +  usuario

        resultadotitle = re.search(padrao, titulo)

        stringhora = resultadotitle.group(1)
        padrao_json['hora'] = stringhora

        stringdata = resultadotitle.group(2)
        padrao_json['data'] = stringdata

        stringuser = resultadotitle.group(3)
        padrao_json['usuario'] = stringuser

        padrao_json['mensagem'] = mensagem

        mensagem_json.append(padrao_json)


    print(mensagem_json)
    with open('json/estado.json', 'w', encoding='utf-8') as arquivo:
        json.dump(mensagem_json, arquivo, indent=4, ensure_ascii=False)
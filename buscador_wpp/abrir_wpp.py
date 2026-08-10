from playwright.sync_api import sync_playwright, expect
from time import sleep
import re
import json

with (sync_playwright() as pw):
    #abrir o navegador
    navegador = pw.chromium.launch_persistent_context(user_data_dir= './whatsapp.profile',
                                                      headless=False)
    #abrir uma janela
    pagina = navegador.new_page()

    #abrir wathsapp
    pagina.goto('https://web.whatsapp.com')
    pagina.wait_for_timeout(5000)

    #abrir grupo
    pagina.get_by_text('Teste agente cotação', exact=True).click()
    pagina.wait_for_timeout(5000)

    #ler mensagens do grupo
    mensagens = pagina.locator('[data-pre-plain-text]')
    cont = mensagens.count()

    #armazenar mensagens dentro de uma lista
    mensagem_json = []

    #loop para capturar todas as mensagens
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
    with open('estado.json', 'w', encoding='utf-8') as arquivo:
        json.dump(mensagem_json, arquivo, indent=4, ensure_ascii=False)

    sleep(10)


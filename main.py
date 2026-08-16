from buscador_wpp.abrir_wpp import abrir_navegador
from buscador_wpp.abrir_wpp import site
from buscador_wpp.abrir_wpp import conversa
from buscador_wpp.parser import inject_json
from buscador_wpp.observer import observer

from playwright.sync_api import sync_playwright

with (sync_playwright() as pw):
    abrir = abrir_navegador(pw)
    site(abrir)
    mensagens = conversa(abrir)
    estado = {"mudou": False}
    observer(abrir, estado)
    inject_json(mensagens)
    while True:
        if estado["mudou"]:
            inject_json(mensagens)
            estado["mudou"] = False
        abrir.wait_for_timeout(3000)
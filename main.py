from buscador_wpp.abrir_wpp import abrir_navegador
from buscador_wpp.abrir_wpp import site
from buscador_wpp.abrir_wpp import conversa
from buscador_wpp.parser import inject_json
from playwright.sync_api import sync_playwright

with (sync_playwright() as pw):
    abrir = abrir_navegador(pw)
    site(abrir)
    mensagens = conversa(abrir)
    inject_json(mensagens)

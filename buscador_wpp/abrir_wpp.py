def abrir_navegador(pw):
    navegador = pw.chromium.launch_persistent_context(user_data_dir= './whatsapp.profile', headless=False)
    pagina = navegador.new_page()
    return pagina

def site(pagina):
    pagina.goto('https://web.whatsapp.com')
    pagina.wait_for_timeout(5000)


def conversa(pagina):
    pagina.get_by_text('Teste agente cotação', exact=True).click()
    pagina.wait_for_timeout(5000)
    mensagens = pagina.locator('[data-pre-plain-text]')
    return mensagens

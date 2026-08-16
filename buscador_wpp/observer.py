from playwright.sync_api import Page

def observer(pagina: Page, estado):
    def olho():
        estado["mudou"] = True
        print(estado)

    pagina.expose_function("olho", olho)
    pagina.evaluate("""
                    const acao = function() {
                    console.log("MUTOU!");
                    console.log(typeof olho);
                    olho()
                        .then(() => console.log("PYTHON TERMINOU"))
                        .catch(erro => console.error("ERRO:", erro));
                    };
                    const conversa = document.querySelector('[data-tab="8"]');
                    const observer = new MutationObserver(acao);
                    observer.observe(conversa, {
                    childList: true
                    });
    """)

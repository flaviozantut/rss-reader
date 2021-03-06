# -*- coding: utf-8 -*-
"""
    Leitor RSS
    ~~~~~~~~~~~~~~

    Aplicativo para leitura de feeds rss
    Para mudar o endereço de leitura das noticias
    altere o  parametro RSS_URL
"""
# imports
import os, time, locale
from flask import Flask, render_template
from lib.feed import Feed
from locale import setlocale

# configurações
DEBUG = True
RSS_URL = 'http://nl.com.br/blog/?feed=rss2'
#Desabilitado devido ao heroku suportar somente localização
#em inglês
#locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')


# Criando a aplicação
app = Flask(__name__)


# definições de rotas
@app.route("/")
def all_items():
    f = Feed(RSS_URL)
    a = f.entries()
    return render_template('all_items.html', data=f.entries(), title=f.title(), debug=DEBUG, time=time)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG)

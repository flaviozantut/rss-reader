# -*- coding: utf-8 -*-
"""
    Leitor RSS
    ~~~~~~~~~~~~~~

    Aplicativo para leitura de feeds rss
    Para mudar o endereço de leitura das noticias
    altere o  parametro RSS_URL
"""
# imports
import os
from flask import Flask, render_template
from lib.feed import Feed

# configurações
DEBUG = False
RSS_URL = 'http://nl.com.br/blog/?feed=rss2'

# Criando a aplicação
app = Flask(__name__)
# app.config.from_object(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# definições de rotas
@app.route("/")
def all_items():
    f = Feed(RSS_URL)
    return render_template('all_items.html', data=f.entries(), title=f.title(), debug = DEBUG)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG)
# -*- coding: utf-8 -*-
"""
    Leitor RSS
    ~~~~~~~~~~~~~~

    Aplicativo para leitura de feeds rss
    Para mudar o endereço de leitura das noticias
    altere o  parametro RSS_URL
"""
# imports
from flask import Flask, render_template
from lib.feed import Feed

# configurações
DEBUG = True
RSS_URL = 'http://nl.com.br/blog/?feed=rss2'

# Criando a aplicação
app = Flask(__name__)
# app.config.from_object(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# definições de rotas
@app.route("/")
def all_items():
    f = Feed(RSS_URL)
    return render_template('all_items.html', data=f.entries(), title=f.title())

if __name__ == "__main__":
    app.run(debug=DEBUG)
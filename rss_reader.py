# -*- coding: utf-8 -*-
"""
    Leitor RSS
    ~~~~~~~~~~~~~~

    Aplicativo para leitura de feeds rss
    Para mudar o endereço de leitura das noticias
    altere o  parametro RSS_URL
"""
# imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# configurações
DEBUG = True
RSS_URL = 'http://nl.com.br/blog/?feed=rss2'

# Criando a aplicação
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# definições de rotas
@app.route("/")
def all_items():
    return render_template('all_items.html')

if __name__ == "__main__":
    app.run()
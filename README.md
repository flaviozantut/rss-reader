Requisitos
---
- ([Python](http://www.python.org/))
- ([PIP](http://www.pip-installer.org/en/latest/))
- ([VirtualEnv](http://www.virtualenv.org/en/latest/))
- ([virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper/))


Instruções
---
    $ mkvirtualenv rss-reader
    $ workon rss-reader
    (rss-reader)$ pip install -r requirements.txt
    (rss-reader)$ python rss_reader.py

minificar js e css
---
    slimit --mangle < static/js/main.js > static/js/main.min.js
    cssmin < static/css/main.css > static/css/main.min.css


Testes unitários
---
    python -m unittest discover -s tests/ -p '*_test.py'


Layout
---
O aplicativo foi desenvolvido visando a acessibilidade, portanto mesmo sedo acessado
por um dispositivo, sem suporte ou com o javascript desabilitado as noticias serão listadas
e poderão ser visualizadas.



TODO
---

- recuperar data de publicação da noticia

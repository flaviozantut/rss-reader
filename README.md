Requisitos
---
- ([Python](http://www.python.org/))
- ([node.js](http://nodejs.org/))
- ([npm](https://npmjs.org/))
- ([PIP](http://www.pip-installer.org/en/latest/))
- ([VirtualEnv](http://www.virtualenv.org/en/latest/))
- ([virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper/))


Instruções
---
    $ npm install bower -g
    $ bower install
    $ mkvirtualenv rss-reader
    $ workon rss-reader
    (rss-reader)$ pip install -r requirements.txt
    (rss-reader)$ python rss_reader.py


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

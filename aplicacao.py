from flask import *

aplicacao = Flask(__name__)
aplicacao.secret_key = '_-_-_'

from views import *

if __name__ == "__main__":
    aplicacao.run(debug=True)
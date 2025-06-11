from flask import Flask, jsonify, render_template_string

from flask_migrate import Migrate

from utils import db

from controllers.mensagem import bp_mensagens


app = Flask(__name__)

app.register_blueprint(bp_mensagens, url_prefix='/mensagens')


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

migrate = Migrate(app, db)


@app.errorhandler(400)

def conteudo_vazio(error):

    return jsonify({"mensagem":"Mensagem vazia."}), 400
'''
    a função conteudo_vazio (que pode ser chamada de decorada) retorna um dicionário Python convertido em JSON com a chave "mensagem" de valor "Mensagem vazia."
    e o código HTTP 400, que indica uma requisição mal-formada ou inválida; no caso, representa uma requisição feita com o conteúdo da mensagem vazio.
'''

@app.errorhandler(404)
#o erro 404 indica que o servidor não encontrou o recurso (dado) solicitado (requisitado); no caso, não encontrou a mensagem solicitada.
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404


@app.route('/')

def index():
    return render_template_string('''<a href="{{url_for('mensagens.read_all')}}">/mensagens</a>''')
   

if __name__ == '__main__':
    app.run()

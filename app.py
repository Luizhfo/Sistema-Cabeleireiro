from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Definindo a aplicação Flask
app = Flask(__name__)

# Configurando a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://@DIDICO\\SQLEXPRESS/cabeleireiro2?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy
db = SQLAlchemy(app)

# Rota inicial
@app.route('/')
def home():
    return 'Hello, Flask!'

# Rota para testar a conexão com o banco de dados
@app.route('/test_db')
def test_db():
    try:
        db.create_all()  # Cria as tabelas no banco, caso não existam
        return 'Conexão com o banco de dados bem-sucedida!'
    except Exception as e:
        return f'Erro na conexão: {str(e)}'

# Rodando a aplicação Flask
if __name__ == '_main_':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '_main_':
    app.run(debug=True)
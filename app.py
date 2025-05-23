from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    print(f'Cadastro: {nome}, {email}, {senha}')
    
    return f'Usuário {nome} cadastrado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)

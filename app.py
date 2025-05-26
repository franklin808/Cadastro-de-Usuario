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

    with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Nome: {nome} | Email: {email} | Senha: {senha}\n')
        return render_template('cadastrar.html', nome=nome)        
        

    return f'Usuário {nome} cadastrado com sucesso!'

@app.route('/login', methods=['POST'])
def login():
    email_digitado = request.form['email']
    senha_digitada = request.form['senha']

    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            usuarios = arquivo.readlines()
    except FileNotFoundError:
        return "Nenhum usuário cadastrado ainda."

    for linha in usuarios:
        if f'Email: {email_digitado} | Senha: {senha_digitada}' in linha:
            nome_inicio = linha.find('Nome: ') + 6
            nome_fim = linha.find(' | Email')
            nome_usuario = linha[nome_inicio:nome_fim]
            return render_template('login.html', nome_usuario=nome_usuario)
    
    return 'E-mail ou senha incorretos.'

if __name__ == '__main__':
    app.run(debug=True)

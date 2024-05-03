from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aqui, estamos passando algumas variáveis para o template
    # Estas variáveis serão acessíveis dentro do template HTML
    nome = "Usuário"
    idade = 30
    lista_de_compras = ['Maçã', 'Banana', 'Laranja']
    
    # Renderiza o template teste.html e passa as variáveis para ele
    return render_template('teste.html', nome=nome, idade=idade, lista_de_compras=lista_de_compras)

@app.route('/outra_pagina')
def outra_pagina():
    nome = "Usuário"
    idade = 30
    lista_de_compras = ['Amora', 'Banana', 'Limão']
    
    return render_template('teste2.html', nome=nome, idade=idade, lista_de_compras=lista_de_compras)
    
if __name__ == '__main__':
    app.run(debug=True)

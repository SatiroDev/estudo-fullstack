from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
import re

app = Flask(__name__)
app.secret_key = '12345'

# se conecta ao banco de dados
def conectar_db():
    conectar = sqlite3.connect('clientes.db')
    return conectar

# cria a tabela
def criar_tabela():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        create table if not exists clientes (
            id integer primary key autoincrement,
            nome text not null,
            email text not null
        )
    ''')
    conectar.commit()
    conectar.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Email inválido!', 'error')
            return redirect(url_for('index'))
        
        conectar = conectar_db()
        cursor = conectar.cursor()
        cursor.execute(
            'insert into clientes (nome, email) values (?, ?)', (nome, email)
        )
        conectar.commit()
        conectar.close()
        flash('Cliente adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    
@app.route('/clientes')
def listar_clientes():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute(
        'SELECT * FROM clientes'
    )
    clientes = cursor.fetchall()
    conectar.close()
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
        
from flask import Flask, render_template, redirect


# Criando a aplicação Flask
app = Flask(__name__)


# Executando o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5152)

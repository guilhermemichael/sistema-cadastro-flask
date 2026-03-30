# Sistema de Cadastro de Usuários (sem banco de dados)

from flask import Flask, render_template, request

app = Flask(__name__)

# "Banco de dados" temporário
usuarios = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        # salvando na lista
        usuarios.append({
            "nome": nome,
            "email": email
        })

        return render_template("cadastro.html")

    return render_template("cadastro.html")

@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from ramdom_data import pessoas
import funcoes

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API do RONALDO_SILVA_NOGUEIRA_BATISTA"})

@app.route("/aleatorios")
def aleatorios():
    import random
    a =random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/maior_de_50", methods=["GET"])
def maior_de_50():
    count = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "Pessoas com mais de 50 anos:": count})

@app.route("/mais_2000", methods=["GET"])
def mais_2000():
    count, x, total_registros = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "Total de pessoas registradas": total_registros, "Pessoas que ganham mais de 2000:": count, "Porcentagem de pessoas que ganham 2000:": x})

@app.route("/media_profissoes", methods=["GET"])
def media_profissoes():
    profissoes = funcoes.media_profissoes(pessoas)
    return jsonify({"status": 200, "informações das profissoes:": profissoes})

@app.route("/tres_salarios", methods=["GET"])
def tres_salarios():
    tres_salarios = funcoes.tres_salarios(pessoas)
    return jsonify({"status": 200, "3 maiores salários": tres_salarios})

@app.route("/sexo_intervalo_idades", methods=["GET"])
def sexo_intervalo_idades():
    count_feminino, count_masculino, intervalo_idades, sexo_maior_2000 = funcoes.sexo_intervalo_dade(pessoas)
    return jsonify({"status": 200, "Mulheres que ganham mais de 2000": count_feminino, "Homens que ganham mais de 2000": count_masculino, "intervalo da idade de quem ganha mais de 2000": intervalo_idades, "sexo que tem mais pessoas que ganham acima de 2000": sexo_maior_2000})

if __name__ == '_main_':
    app.run(debug=True)
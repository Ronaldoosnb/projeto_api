from flask import Flask, jsonify

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

if __name__ == '_main_':
    app.run(debug=True)
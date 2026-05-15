import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from core.prompt_mestre import PromptMestre
from services.ia_service import IAService

app = Flask(
    __name__,
    static_folder="frontend",
)

CORS(app)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/chat", methods=["POST"])
def chat():

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado encontrado"}), 400

    mensagem_usuario = dados.get("mensagem", "").strip()
    historico = dados.get("historico", [])

    if not mensagem_usuario:
        return jsonify({"erro": "A mensagem não pode estar vazia"}), 400

    historico.append({
        "role": "user",
        "content": mensagem_usuario
    })

    return jsonify({
        "resposta": "Mensagem recebida com sucesso",
        "historico": historico
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "online",
        "bot": "TutorBot"
    })


if __name__ == "__main__":
    print("=" * 55)
    print(" TutorBot rodando!")
    print(" API em: http://localhost:5000")
    print(" Status: http://localhost:5000/status")
    print("=" * 55)

    app.run(debug=True, port=5000)
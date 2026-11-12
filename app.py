from flask import Flask, request, jsonify, send_from_directory
import anthropic

app = Flask(__name__, static_folder=".", static_url_path="")
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment variable


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    history = request.json["messages"]
    try:
        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=500,
            system="You are a friendly, helpful assistant. Keep answers short and clear.",
            messages=history,
        )
        return jsonify({"reply": response.content[0].text})
    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

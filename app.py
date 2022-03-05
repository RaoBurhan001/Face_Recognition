from flask import Flask, jsonify, request
from Face import predictFace


app = Flask(__name__)

@app.route("/face", methods=["POST"])
def predict():
    predictions = predictFace(request)

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
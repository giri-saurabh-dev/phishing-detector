from flask import Flask, request, jsonify
from src.predict import predict_url

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get("url")
    result = predict_url(url)
    return jsonify({"url": url, "prediction": result})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello Sravan! Azure Web App is running successfully"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "app": "python-webapp",
        "message": "App is working fine!"
    })

@app.route("/about")
def about():
    return "This is a simple Python Flask app deployed on Azure"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

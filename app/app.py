from flask import Flask, render_template, jsonify
import socket
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        version=os.getenv("APP_VERSION", "v1.0.0")
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

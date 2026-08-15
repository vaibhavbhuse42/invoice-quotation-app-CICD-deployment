from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Invoice & Quotation Management App</h1>
    <p>Flask application is running successfully!</p>
    """


@app.route("/health")
def health():
    return "Application is Healthy!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
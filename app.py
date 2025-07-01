# from flask import Flask, request, render_template, jsonify
# import joblib

# app = Flask(__name__)

# # Load Model & Vectorizer
# model = joblib.load("waf_model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")

# # Store Scanned Requests
# scan_history = []

# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = None
#     if request.method == "POST":
#         user_input = request.form.get("query", "")
#         input_vector = vectorizer.transform([user_input])
#         prediction = model.predict(input_vector)[0]
#         result = "malicious" if prediction == "malicious" else "safe"

#         # Store Scan History
#         scan_history.append({"query": user_input, "result": result})

#     return render_template("index.html", result=result)

# @app.route("/stats")
# def stats():
#     safe_count = sum(1 for item in scan_history if item["result"] == "safe")
#     malicious_count = sum(1 for item in scan_history if item["result"] == "malicious")

#     return jsonify({
#         "safe": safe_count,
#         "malicious": malicious_count,
#         "scanned_urls": scan_history  # Sending full history
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
import joblib
import re
from urllib.parse import urlparse

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("waf_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Store stats and history
safe_count = 0
malicious_count = 0
scanned_urls = []

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

@app.route("/", methods=["GET", "POST"])
def index():
    global safe_count, malicious_count, scanned_urls
    result = ""
    message = ""

    if request.method == "POST":
        query = request.form["query"]
        transformed = vectorizer.transform([query])
        prediction = model.predict(transformed)[0]

        if prediction == "malicious":
            result = "malicious"
            malicious_count += 1
            message = "Access Denied"
        else:
            result = "safe"
            safe_count += 1
            if is_valid_url(query):
                return redirect(query)
            else:
                message = "Enter a valid URL"

        scanned_urls.append({"query": query, "result": result})

    return render_template("index.html", result=result, message=message)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/stats")
def stats():
    return jsonify({
        "safe": safe_count,
        "malicious": malicious_count,
        "scanned_urls": scanned_urls
    })

if __name__ == "__main__":
    app.run(debug=True)

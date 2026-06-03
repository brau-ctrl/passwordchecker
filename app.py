from flask import Flask, render_template, request, jsonify

from password_strength_checker import check_password_strength, calculate_entropy

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json(force=True)
    password = data.get("password", "").strip()
    if not password:
        return jsonify({"error": "Please enter a password."}), 400

    strength, suggestions = check_password_strength(password)
    entropy = calculate_entropy(password)
    return jsonify({
        "strength": strength,
        "entropy": round(entropy, 1),
        "suggestions": suggestions,
    })

if __name__ == "__main__":
    app.run(debug=True)

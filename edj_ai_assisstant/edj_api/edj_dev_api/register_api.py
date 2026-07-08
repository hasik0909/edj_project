from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return jsonify({
        "message": "Register API is Running"
    })

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    users.append({
        "username": data["username"],
        "password": data["password"],
        "email": data["email"]
    })

    return jsonify({
        "message": "Registration Successful",
        "user": data
    })

if __name__ == "__main__":
    app.run(debug=True)
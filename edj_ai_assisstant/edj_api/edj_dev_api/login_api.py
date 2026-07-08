from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"username": "admin", "password": "admin123"},
    {"username": "hasitha", "password": "welcome123"}
]

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({
                "status": "Success",
                "message": "Login Successful"
            })

    return jsonify({
        "status": "Failed",
        "message": "Invalid Credentials"
    }), 401

if __name__ == "__main__":
    app.run(debug=True)
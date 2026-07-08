from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/profile")
def profile():

    user = {
        "id": 1,
        "name": "Hasitha",
        "email": "hasitha@gmail.com",
        "role": "Developer"
    }

    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
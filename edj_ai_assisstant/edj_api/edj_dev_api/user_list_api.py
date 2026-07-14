from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Hasitha"
    },
    {
        "id": 2,
        "name": "Rahul"
    },
    {
        "id": 3,
        "name": "Kiran"
    }
]

@app.route("/users")
def users_list():

    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
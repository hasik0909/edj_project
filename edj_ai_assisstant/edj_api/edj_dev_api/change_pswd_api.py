from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/change-password", methods=["PUT"])
def change_password():

    data = request.get_json()

    return jsonify({
        "message": "Password Changed Successfully",
        "new_password": data["new_password"]
    })

if __name__ == "__main__":
    app.run(debug=True)
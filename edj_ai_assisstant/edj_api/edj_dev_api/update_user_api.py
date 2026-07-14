from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/update-user/<int:id>", methods=["PUT"])
def update_user(id):

    data = request.get_json()

    return jsonify({
        "message": "User Updated Successfully",
        "id": id,
        "updated_data": data
    })

if __name__ == "__main__":
    app.run(debug=True)
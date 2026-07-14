from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/delete-user/<int:id>", methods=["DELETE"])
def delete_user(id):

    return jsonify({
        "message": "User Deleted Successfully",
        "deleted_user_id": id
    })

if __name__ == "__main__":
    app.run(debug=True)
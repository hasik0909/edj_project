from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/logout", methods=["POST"])
def logout():

    return jsonify({
        "message": "Logout Successful"
    })

if __name__ == "__main__":
    app.run(debug=True)
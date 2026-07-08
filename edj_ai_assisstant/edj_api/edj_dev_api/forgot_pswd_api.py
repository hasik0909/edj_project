from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/forgot-password", methods=["POST"])
def forgot_password():

    data = request.get_json()

    return jsonify({
        "message": "Password Reset Link Sent",
        "email": data["email"]
    })

if __name__ == "__main__":
    app.run(debug=True)
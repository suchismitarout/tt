from flask import Flask, jsonify, request

app = Flask(__name__)

account = [{"name": "abc", "balance": 67000}, {"name": "xyz", "balance": 56000}]


@app.route("/account", methods=["GET"])
def get_account():
    return jsonify(account)


if __name__ == '__main__':
    app.run()

from flask import Flask,jsonify

app = Flask(__name__)

accounts = [
    {"name": "abc", "balance": 5400},
    {"name": "xyz", "balance": 7600}
]


@app.route("/account", methods=["GET"])
def get_account():
    return jsonify(accounts)

@app.route("/by_id/<id>", methods=["GET"])
def get_account_by_id(id):
    id = int(id)
    return jsonify(accounts)


if __name__ == '__main__':
    app.run()


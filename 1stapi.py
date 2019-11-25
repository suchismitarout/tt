from flask import Flask,jsonify

app = Flask(__name__)

info_list = [{
    "name": "abc",
    "id": 21237,
    "age": 28
},{
    "name": "xyz",
    "id": 21345,
    "age": 27
    }]


@app.route('/info', methods=['GET'])
def get_info():
    return jsonify(info_list)

if __name__ == '__main__':
    app.run()


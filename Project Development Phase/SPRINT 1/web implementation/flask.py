from flask import Flask, request

app = Flask(__name__)

items = {}


@app.route("/api")
def index():
    return "Hello form Flask API Server"


@app.route('/data', methods=['POST', 'GET'])
def api():
    if request.method == 'GET':
        return items

    if request.method == 'POST':
        data = request.json
        items.update(data)
        return "Data is inserted"


@app.route("/data/<id>", methods=["PUT"])
def update(id):
    data = request.form['item']
    items[str(id)] = data
    return "Data updated"


@app.route("/data/<id>", methods=["DELETE"])
def delete(id):
    items.pop(str(id))
    return "Data Deleted"

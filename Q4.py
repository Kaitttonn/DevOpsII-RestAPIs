from flask import Flask, request, jsonify

app = Flask(__name__)


items = [
    {"name": "Budweiser", "category": 1, "price": 20.5, "instock": 200},
    {"name": "Bud Light", "category": 2, "price": 15, "instock": 100},
    {"name": "Heineken", "category": 3, "price": 14.5, "instock": 45},
    {"name": "Corona", "category": 4, "price": 12, "instock": 250},
    {"name": "Sapporo", "category": 5, "price": 10.5, "instock": 500},
    {"name": "Brahma", "category": 6, "price": 10.5, "instock": 500},
    {"name": "Singha", "category": 7, "price": 10.5, "instock": 500},
]

def next(name):
    data = [x for x in items if x['name'] == name]
    return data

@app.route('/del_item/<name>', methods=["DELETE"])
def delete_item(name: str):

    data = next(name)
    if not data:
        return {"error": " not found"}, 404
    else:
        items.remove(data[0])
        return "deleted successful", 200


@app.route('/item', methods=["GET"])
def get_item():
    return jsonify(items)


@app.route('/item/<name>', methods=["GET"])
def get_items_name(name):
    data = next(name)
    return jsonify(data)

@app.route('/item_p', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (next(name) == name):
        return {"error": "can not Request"}, name
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/p_items/<name>', methods=["PUT"])
def update_item(name):
    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')


    for items in items:
        if name == items["name"]:
            items["category"] = int(category)
            items["price"] = int(price)
            items["instock"] = int(instock)
            return jsonify(items)

    else:
        return "Error", 404







        
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
from flask import Flask, redirect, render_template, request
import json
app = Flask(__name__)


@app.route('/')
def get():
    with open('db.txt') as f:
        items = json.load(f)
    return render_template(
        'index.html',
        items=items
    )


@app.route('/post', methods=["POST"])
def post():
    item = request.form['item']
    quantity = request.form['quantity']
    with open('db.txt') as f:
        items = json.load(f)
    items.update({item: quantity})
    with open('db.txt', 'w') as f:
        json.dump(items, f)
    return redirect('/')


@app.route('/items', methods=['GET', 'POST'])
def items():
    with open('db.txt') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            quantity = request.form['quantity']
            items.update({item: quantity})
            with open('db.txt', 'w') as f:
                json.dump(items, f)
        return render_template('items.html', items=items)


# @app.route('/remove_items', methods=['GET', 'POST'])
# def remove_items():
#     with open('db.txt', 'r') as f:
#         items = json.load(f)
#         if request.method == "POST":
#             item = request.form['item']
#             del items[item]
#             with open('db.txt', 'w') as f2:
#                 json.dump(items, f2)
#         return render_template('remove_items.html', items=items)


@app.route('/remove_items', methods=['GET', 'POST'])
def remove_items():
    '''
    Delete items and Quantity from db.txt
    '''
    with open('db.txt', 'r') as f:
        items = json.load(f)
        if request.method == 'POST':
            item = request.form['item']
            del items[item]
            with open('db.txt', 'w') as f2:
                json.dump(items, f2)
        return render_template('remove_items.html', items=items)

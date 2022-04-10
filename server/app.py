from flask import Flask, jsonify
from flask_cors import CORS
import json


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/shop', methods=['GET', 'POST'])
def all_shop_items():
    return jsonify({
        'status': 'success',
        'items': ITEMS
    })


ITEMS = []
with open("shopItems.json", 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    ITEMS = json_data['items']


if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return {"message": "List of orders"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

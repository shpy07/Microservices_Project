from flask import Flask

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return {"message": "List of products"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

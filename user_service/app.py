from flask import Flask

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return {"message": "List of users"}, 200  # You can replace this with actual user data.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)  # Changed to 0.0.0.0

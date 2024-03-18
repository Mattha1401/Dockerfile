from flask import Flask
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return "Hello World!"

@app.route('/god')
def god():
    return "Puhatai trainee"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


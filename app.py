# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask in Development!"

if __name__ == '__main__':
    app.run(debug=True)  # This will run the app in development mode
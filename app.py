import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is my first trading bot</h1>"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print(request.json)
    return 'success', 200

if __name__ == '__main__':
    app.run()
   

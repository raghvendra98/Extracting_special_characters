from flask import Flask, request, jsonify
#from test import get_font_characters
from test import get_all_font_characters

app = Flask(__name__)

@app.route('/', methods =['GET'])
def home():
    if request.method == 'GET':
        return jsonify({"data" : "Message is completed"})

@app.route('/emogi', methods =['POST'])
def emogi():
    if request.method == 'POST':
        input = request.files['file']
        output = (get_all_font_characters(input))
        return jsonify({"data": output})
    else:
        return jsonify({"Error": 404})

if __name__ == '__main__':
    app.run(debug=True)
#!petweb/bin/flask
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

times_fed = []

@app.route('/')
def index():
    return 'hello world'

@app.route('/feed', methods=['POST'])
def feed():
    new_date = datetime.datetime.now()
    times_fed.append(new_date)
    # print(times_fed)
    # return jsonify({'times_fed': times_fed})
    return 'Nom nom nom...'

@app.route('/lastfed', methods=['GET'])
def last_fed():
    return jsonify({'lastFed': times_fed[-1]})

if __name__ == '__main__':
    app.run(debug=True)
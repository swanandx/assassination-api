from flask import Flask,jsonify
from classroom import Assasination

app = Flask(__name__)
qoutes = Assasination()

@app.route('/', methods=['GET'])
def home():
	return '''<h4> Welcome to Assasination API <h4>\napi is at <strong> /api/ </strong>'''

@app.route('/api', methods=['GET'])
def api_req():
	return '''try <strong> /api/random </strong>'''

@app.route('/api/random', methods=['GET'])
def random_quote():
	return jsonify(qoutes.get_random_quote())

@app.route('/api/quotes', methods=['GET'])
def random_5_quotes():
	return jsonify(qoutes.get_5_quotes())

@app.route('/api/characters/<string:name>', methods=['GET'])
def quote_by_name(name):
	return jsonify(qoutes.get_quote_by_name(name))

@app.route('/api/characters', methods=['GET'])
def all_characters():
	return jsonify(qoutes.list_characters())

if __name__ == '__main__':
	app.run()
from flask import render_template, request, jsonify
from config import db, app
from models_logic import *
import json

@app.route('/log-in',methods=['GET'])
def verify_user():
	user = request.args.get('user')
	password = request.args.get('password')
	results = find_user(user, password)
	return jsonify(response=results)

@app.route('/stress', methods=['GET'])
def user_stress():
	user = request.args.get('user')
	results = show_stress(user)
	return jsonify(response=results)

@app.route('/diet', methods=['GET'])
def user_diet():
	user = request.args.get('user')
	results = show_diet(user)
	return jsonify(response=results)

@app.route('/sleep',methods=['GET'])
def user_sleep():
	user = request.args.get('user')
	results = show_sleep(user)
	return jsonify(response=results)



if __name__  ==	"__main__":
	app.run(debug=True, threaded=True, port= 3000)
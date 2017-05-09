from flask import render_template, request, jsonify
from config import db, app
from models_logic import *
import json

@app.route('/log-in',methods=['GET'])
def verify_user():
	user = request.args.get('user')
	password = request.args.get('password')
	user_info = find_user(user, password)
	return jsonify(response=user_info)	

@app.route('/stress', methods=['GET'])
def user_stress():
	user = request.args.get('user')
	results = show_stress(user)
	return jsonify(response=results)

@app.route('/outlets', methods=['GET'])
def user_outlets():
	user = request.args.get('user')
	results = show_outlets(user)
	return jsonify(response = results)

@app.route('/physical-activity',methods =['GET'])
def user_physical_activity():
	user=request.args.get('user')
	results=show_physical_activity(user)
	return jsonify(reponse= results)

@app.route('/indulgences', methods = ['GET'])
def user_indulgences():
	user = request.args.get('user')
	results= show_indulgences(user)
	return jsonify(resposne=results)

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

@app.route('/cog-cond', methods = ['GET'])
def user_cog_cond():
	user = request.args.get('user')
	results = show_cog_cond(user)
	return jsonify(response=results)

@app.route('/physical-cond', methods=['GET'])
def user_physical_cond():
	user = request.args.get('user')
	results = show_physical_cond(user)
	return jsonify(response= results)

@app.route('/sexual-activity', methods=['GET'])
def user_sexual_activity():
	user = request.args.get('user')
	results = show_sexual_activity(user)
	return jsonify(resposne = results)

@app.route('/goals', methods=['GET'])
def user_goals():
	user = request.args.get('user')
	results = show_goals(user)
	return jsonify( resposne= results)

@app.route('/tasks', methods=['GET'])
def user_tasks():
	user=request.args.get('user')
	results = show_user_tasks(user)
	return jsonify(response = results)

if __name__  ==	"__main__":
	app.run(debug=True, threaded=True, port= 3000)
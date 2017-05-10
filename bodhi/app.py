from flask import render_template, request, jsonify
from config import db, app
from models_logic import *
import json
import datetime

@app.route('/log-in',methods=['POST', 'GET'])
def verify_user():
	if request == 'GET':
		user = request.args.get('user')
		password = request.args.get('password')
		user_info = find_user(user, password)
		return jsonify(response=user_info)
	else:
		new_user={
		'first_name':request.json["first_name"],
		"last_name":request.json['last_name'],
		"email":request.json['email'],
		"password":request.json['password'],
		"gender":request.json['gender'],
		"join_date":datetime.date.today()
		}
		results = add_user(new_user)
		return results		

@app.route('/stress', methods=['GET','POST'])
def user_stress():
	user = request.args.get('user')	
	if request == 'GET':
		results = show_stress(user)
		return jsonify(response=results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'level':request.json['level'],
		'relationship':request.json['relationship'],
		'family':request.json['family'],
		'school':request.json['school'],
		'friends':request.json['friends'],
		'work':request.json['work'],
		'unclear':request.json['unclear'],
		'other':request.json['other'],
		'pms':request.json['pms'],
		'user':user
		}
		results = log_stress(new_entry)
		return results
			
@app.route('/outlets', methods=['GET', 'POST'])
def user_outlets():
	user = request.args.get('user')
	if request.method == 'GET':
		results = show_outlets(user)
		return jsonify(response = results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'journaled':request.json['journaled'],
		'meditated':request.json['meditated'],
		'other':request.json['other'],
		'user':user
		}
		results=log_outlets(new_entry)
		return results

@app.route('/physical-activity',methods =['GET', 'POST'])
def user_physical_activity():
	user=request.args.get('user')
	if request.method == 'GET':
		results=show_physical_activity(user)
		return jsonify(reponse= results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'yoga_pilates':request.json['yoga_pilates'],
		'cardio':request.json['cardio'],
		'toning':request.json['toning'],
		'other':request.json['other'],
		'user':user
		}
		results= log_physical_activity(new_entry)
		return results

@app.route('/indulgences', methods = ['GET', 'POST'])
def user_indulgences():
	user = request.args.get('user')
	if request.method == 'GET':
		results= show_indulgences(user)
		return jsonify(resposne=results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'alcohol':request.json['alcohol'],
		'tobacco':request.json['tobacco'],
		'sweets':request.json['sweets'],
		'coffee':request.json['coffee'],
		'other':request.json['other'],
		'user':user
		}
		results = log_indulgences(new_entry)
		return results

@app.route('/diet', methods=['GET', 'POST'])
def user_diet():
	user = request.args.get('user')
	if request.method == 'GET':
		results = show_diet(user)
		return jsonify(response=results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'fast':request.json['fast'],
		'dairy':request.json['dairy'],
		'gluten':request.json['gluten'],
		'meat':request.json['meat'],
		'user':user	
		}
		results = log_diet(new_entry)
		return results


@app.route('/sleep',methods=['GET', 'POST'])
def user_sleep():
	user = request.args.get('user')
	if request.method == 'GET':
		results = show_sleep(user)
		return jsonify(response=results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'hours':request.json['hours'],
		'quality':request.json['quality'],
		'user':user			
		}
		results = log_sleep(new_entry)
		return results

@app.route('/cog-cond', methods = ['GET','POST'])
def user_cog_cond():
	user = request.args.get('user')
	if request.method == 'GET':
		results = show_cog_cond(user)
		return jsonify(response=results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'energized':request.json['energized'],
		'calm':request.json['calm'],
		'irritable':request.json['irritable'],
		'confident':request.json['confident'],
		'anxious':request.json['anxious'],
		'distracted':request.json['distracted'],
		'focused':request.json['focused'],
		'creative':request.json['creative'],
		'apathetic':request.json['apathetic'],
		'mindful':request.json['mindful'],
		'user':user						
		}
		results=log_cog_cond(new_entry)
		return results	

@app.route('/physical-cond', methods=['GET', 'POST'])
def user_physical_cond():
	user = request.args.get('user')
	if request.method == 'GET':
		results = show_physical_cond(user)
		return jsonify(response= results)
	else:
		new_entry={
		'entry_date':datetime.date.today(),
		'sore':request.json['sore'],
		'fatigued':request.json['fatigued'],
		'bloated':request.json['bloated'],
		'constipated':request.json['constipated'],
		'nauseous':request.json['nauseous'],
		'acne_breakout':request.json['acne_breakout'],
		'hungry':request.json['hungry'],
		'sick':request.json['sick'],
		'headache':request.json['headache'],
		'stomach_ache':request.json['stomach_ache'],
		'user':user			
		}	
		results = log_physical_cond(new_entry)
		return results

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
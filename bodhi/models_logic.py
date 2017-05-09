from models import *

def find_user(user,password):
	user = User.query.filter_by(email=user).first()
	if user.password != password:
		return False
	return user.serialize()

def show_stress(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	stress = Stress.query.filter_by(user=user).all()
	for entry in stress:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def show_outlets(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	outlets = Outlets.query.filter_by(user=user).all()
	for entry in outlets:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def show_physical_activity(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	activity = Physical_Activity.query.filter_by(user=user).all()
	for entry in activity:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def show_indulgences(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	indulgences = Indulgences.query.filter_by(user=user).all()
	for entry in indulgences:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def show_diet(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	diet = Diet.query.filter_by(user=user).all()
	for entry in diet:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def show_sleep(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	sleep = Sleep.query.filter_by(user=user).all()
	for entry in sleep:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def show_cog_cond(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	cog = Cognitive_Condition.query.filter_by(user=user).all()
	for entry in cog:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def show_physical_cond(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	physical_condition = Physical_Condition.query.filter_by(user=user).all()
	for entry in physical_condition:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def show_sexual_activity(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	activity = Sexual_Activity.query.filter_by(user=user).all()
	for entry in activity:
		t = entry.serialize()
		occassions.append(t)
	return occassions		

def show_goals(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	goals = Goals.query.filter_by(user=user).all()
	for entry in goals:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def show_user_tasks(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	tasks = Tasks.query.filter_by(user=user).all()
	for entry in tasks:
		t = entry.serialize()
		occassions.append(t)
	return occassions				


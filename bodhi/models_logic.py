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

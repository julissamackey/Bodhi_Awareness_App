from models import *

def find_user(user,password):
	user = User.query.filter_by(email=user).first()
	if user.password != password or user == None:
		return False
	return user.serialize()

def add_user(new_user):
	first_name= new_user['first_name']
	last_name = new_user['last_name']
	email=new_user['email']
	password=new_user['password']
	gender=new_user['password']
	join_date = new_user['join_date']
	account_already_exists = find_user(email,password)
	if account_already_exists == False:
		new_account = User(first_name,last_name,email,password,gender,join_date)
		db.session.add(new_account)
		db.session.commit()
		return 'success'
	else:
		return 'user already has an account'

def show_stress(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	stress = Stress.query.filter_by(user=user).all()
	for entry in stress:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def log_stress(new_entry):
	entry_date = new_entry['entry_date']
	level = new_entry['level']
	relationship = new_entry['relationship']
	family = new_entry['family']
	school = new_entry['school']
	friends = new_entry['friends']
	work = new_entry['work']
	unclear = new_entry['unclear']
	other = new_entry['other']
	pms = new_entry['pms']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Stress(entry_date, level,relationship,family,school, friends, work, unclear, other, pms,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'

def show_outlets(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	outlets = Outlets.query.filter_by(user=user).all()
	for entry in outlets:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def log_outlets(new_entry):
	entry_date = new_entry['entry_date']
	journaled = new_entry['journaled']
	meditated = new_entry['meditated']
	other = new_entry['other']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Outlets(entry_date,journaled,meditated,other,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'

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


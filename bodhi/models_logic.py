from models import *

def find_user(user):
	current = User.query.filter_by(email=user['email']).first()
	if current == None:
		return False
	elif current.password != user['password']:
		return False 
	return current.serialize()


def add_user(new_user):
	first_name= new_user['first_name']
	last_name = new_user['last_name']
	email=new_user['email']
	password=new_user['password']
	gender=new_user['gender']
	if gender == '2':
		gender = 'M'
	elif gender == '1':
		gender = 'F'
	else:
		gender = 'N/A'
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

def log_physical_activity(new_entry):
	entry_date = new_entry['entry_date']
	yoga_pilates = new_entry['yoga_pilates']
	cardio = new_entry['cardio']
	toning = new_entry['toning']
	other = new_entry['other']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Physical_Activity(entry_date,yoga_pilates, cardio, toning,other,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'	

def show_indulgences(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	indulgences = Indulgences.query.filter_by(user=user).all()
	for entry in indulgences:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def log_indulgences(new_entry):
	entry_date = new_entry['entry_date']
	alcohol = new_entry['alcohol']
	tobacco = new_entry['tobacco']
	sweets = new_entry['sweets']
	coffee = new_entry['coffee']
	other = new_entry['other']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Indulgences(entry_date,alcohol,tobacco,sweets,coffee,other,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'

def show_diet(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	diet = Diet.query.filter_by(user=user).all()
	for entry in diet:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def log_diet(new_entry):
	entry_date = new_entry['entry_date']
	fast = new_entry['fast']
	dairy = new_entry['dairy']
	gluten = new_entry['gluten']
	meat = new_entry['meat']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Diet(entry_date,fast,dairy,gluten,meat,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'	

def show_sleep(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	sleep = Sleep.query.filter_by(user=user).all()
	for entry in sleep:
		t = entry.serialize()
		occassions.append(t)
	return occassions

def log_sleep(new_entry):
	entry_date = new_entry['entry_date']
	hours = int(new_entry['hours'])
	quality = new_entry['quality']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Sleep(entry_date,hours,quality,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'	


def show_cog_cond(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	cog = Cognitive_Condition.query.filter_by(user=user).all()
	for entry in cog:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def log_cog_cond(new_entry):
	entry_date = new_entry['entry_date']
	energized = new_entry['energized']
	calm = new_entry['calm']
	irritable = new_entry['irritable']
	confident = new_entry['confident']
	anxious = new_entry['anxious']
	distracted = new_entry['distracted']
	focused = new_entry['focused']
	creative = new_entry['creative']
	apathetic = new_entry['apathetic']
	mindful = new_entry['mindful']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Cognitive_Condition(entry_date,energized,calm,irritable,confident,anxious,distracted,focused,creative,apathetic,mindful,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'

def show_physical_cond(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	physical_condition = Physical_Condition.query.filter_by(user=user).all()
	for entry in physical_condition:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def log_physical_cond(new_entry):
	entry_date = new_entry['entry_date']
	sore = new_entry['sore']
	fatigued = new_entry['fatigued']
	bloated = new_entry['bloated']
	constipated = new_entry['constipated']
	nauseous = new_entry['nauseous']
	acne_breakout = new_entry['acne_breakout']
	hungry = new_entry['hungry']
	sick = new_entry['sick']
	headache = new_entry['headache']
	stomach_ache = new_entry['stomach_ache']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Physical_Condition(entry_date,sore, fatigued,bloated,constipated,nauseous,acne_breakout,hungry,sick,headache,stomach_ache,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'

def show_sexual_activity(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	activity = Sexual_Activity.query.filter_by(user=user).all()
	for entry in activity:
		t = entry.serialize()
		occassions.append(t)
	return occassions		

def log_sexual_activity(new_entry):
	entry_date = new_entry['entry_date']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Sexual_Activity(entry_date,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'	 	

def show_goals(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	goals = Goals.query.filter_by(user=user).all()
	for entry in goals:
		t = entry.serialize()
		occassions.append(t)
	return occassions	

def log_goals(new_entry):
	entry_date = new_entry['entry_date']
	goal = new_entry['goal']
	complete= new_entry['complete']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Goals(entry_date,goal,complete,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'		

def show_user_tasks(user):
	occassions = []
	user = User.query.filter_by(email=user).first()
	tasks = Tasks.query.filter_by(user=user).all()
	for entry in tasks:
		t = entry.serialize()
		occassions.append(t)
	return occassions				

def log_tasks(new_entry):
	entry_date = new_entry['entry_date']
	task = new_entry['task']
	complete = new_entry['complete']
	user = User.query.filter_by(email=new_entry['user']).first()
	data = Tasks(entry_date,task,complete,user)
	db.session.add(data)
	db.session.commit()	
	return 'success'	

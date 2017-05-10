from config import db
import datetime

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(25))
	last_name = db.Column(db.String(25))
	email = db.Column(db.String(35), unique = True)
	password = db.Column(db.String(20))
	gender = db.Column(db.String(3))
	join_date = db.Column(db.TIMESTAMP)
	stress_level = db.relationship('Stress', backref = 'user', lazy='dynamic')
	outlets = db.relationship('Outlets', backref = 'user', lazy = 'dynamic')
	physical_activity = db.relationship('Physical_Activity', backref ='user', lazy ='dynamic')
	indulgences = db.relationship('Indulgences', backref = 'user', lazy = "dynamic")
	diet = db.relationship('Diet', backref = 'user', lazy = 'dynamic')
	sleep = db.relationship('Sleep', backref='user', lazy = 'dynamic')
	cognitive_condition = db.relationship('Cognitive_Condition', backref='user',lazy = 'dynamic')
	physical_condition = db.relationship('Physical_Condition', backref='user', lazy='dynamic')
	sexual_activity = db.relationship('Sexual_Activity', backref='user', lazy='dynamic')
	goals = db.relationship('Goals', backref='user', lazy = 'dynamic')
	to_do= db.relationship('Tasks', backref ='user', lazy='dynamic')

	def __init__(self, first_name, last_name, email, password, gender, join_date):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.gender= gender
		self.join_date = join_date

	def serialize(self):
		return{
		'id' : self.id,
		'first_name':self.first_name,
		'last_name':self.last_name,
		'email':self.email,
		'password':self.password,
		'gender':self.gender,
		'join_date':self.join_date
		}

class Stress(db.Model):
	__tablename__='stress'
	id = db.Column(db.Integer,primary_key=True)
	entry_date = db.Column(db.TIMESTAMP)
	level= db.Column(db.Integer)
	relationship = db.Column(db.Boolean, default = False )
	family = db.Column(db.Boolean, default=False)
	school = db.Column(db.Boolean, default =False)
	friends = db.Column(db.Boolean, default=False)
	work = db.Column(db.Boolean, default=False)
	unclear = db.Column(db.Boolean, default=False)
	other = db.Column(db.Boolean, default=False)
	pms = db.Column(db.Boolean, default=False)  
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, entry_date, level, relationship, family, school, friends,work, unclear,other,pms,user):
		self.entry_date =entry_date
		self.level=level
		self.relationship = relationship
		self.family = family
		self.school = school
		self.friends = friends
		self.work = work
		self.unclear=unclear
		self.other = other
		self.pms = pms
		self.user=user

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'level':self.level,
		'relationship':self.relationship,
		'family':self.family,
		'school':self.school,
		'friends':self.friends,
		'work':self.work,
		'unclear':self.unclear,
		'other':self.other,
		'pms':self.pms,
		'user_id':self.user_id
		}

class Outlets(db.Model):
	__tablename__= 'outlets'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date=	db.Column(db.TIMESTAMP)
	journaled = db.Column(db.Boolean, default=False)
	meditated = db.Column(db.Boolean, default=False)
	other = db.Column(db.Boolean, default=False)
	user_id =  db.Column(db.Integer, db.ForeignKey('user.id')) 

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'journaled':self.journaled,
		'meditated':self.meditated,
		'other':self.other,
		'user_id':self.user_id
		}

class Physical_Activity(db.Model):
	__tablename__='physical_activity'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date = db.Column(db.TIMESTAMP)
	yoga_pilates = db.Column(db.Boolean, default=False)
	cardio = db.Column(db.Boolean, default=False)
	toning = db.Column(db.Boolean, default=False)
	other = db.Column(db.Boolean, default=False)
	user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'yoga_pilates':self.yoga_pilates,
		'cardio': self.cardio,
		'toning':self.toning,
		'other':self.other,
		'user_id':self.user_id
		}

class Indulgences(db.Model):
	__tablename__='indulgences'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date=db.Column(db.TIMESTAMP)
	alcohol = db.Column(db.Boolean, default=False)
	tobacco = db.Column(db.Boolean,default=False)
	sweets = db.Column(db.Boolean, default=False)
	other = db.Column(db.Boolean, default=False)
	coffee = db.Column(db.Boolean,default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'alcohol':self.alcohol,
		'tobacco':self.tobacco,
		'sweets':self.sweets,
		'other':self.other,
		'coffee':self.coffee,
		'user_id':self.user_id
	}

class Diet(db.Model):
	__tablename__='diet'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date = db.Column(db.TIMESTAMP)
	fast = db.Column(db.Boolean, default=False)
	dairy = db.Column(db.Boolean, default=False)
	gluten = db.Column(db.Boolean, default=False)
	meat = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'fast':self.fast,
		'dairy':self.dairy,
		'gluten':self.gluten,
		'meat':self.meat,
		'user_id':self.user_id
		}

class Sleep(db.Model):
	__tablename__='sleep'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date=db.Column(db.TIMESTAMP)
	hours = db.Column(db.Integer)
	quality = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'hours':self.hours,
		'quality':self.quality,
		'user_id':self.user_id
		}

class Cognitive_Condition(db.Model):
	__tablename__='cognitive_condition'
	id = db.Column(db.Integer, primary_key=True) 
	entry_date= db.Column(db.TIMESTAMP)
	energized = db.Column(db.Boolean,default=False)
	calm = db.Column(db.Boolean,default=False)
	irritable = db.Column(db.Boolean,default=False)
	confident = db.Column(db.Boolean,default=False)
	anxious = db.Column(db.Boolean,default=False)
	distracted = db.Column(db.Boolean,default=False)
	focused = db.Column(db.Boolean,default=False)
	creative = db.Column(db.Boolean,default=False)
	apathetic = db.Column(db.Boolean,default=False)
	mindful = db.Column(db.Boolean,default=False)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'energized':self.energized,
		'calm':self.calm,
		'irritable':self.irritable,
		'confident':self.confident,
		'anxious':self.anxious,
		'distracted':self.distracted,
		'focused':self.focused,
		'creative':self.creative,
		'apathetic':self.apathetic,
		'mindful':self.mindful,
		'user_id':self.user_id
		}

class Physical_Condition(db.Model):
	__tablename__='physical_condition'
	id = db.Column(db.Integer, primary_key=True)
	entry_date= db.Column(db.TIMESTAMP)
	sore = db.Column(db.Boolean,default=False)
	fatigued = db.Column(db.Boolean,default=False)
	bloated = db.Column(db.Boolean,default=False)
	constipated = db.Column(db.Boolean,default=False)
	nauseous = db.Column(db.Boolean,default=False)
	acne_breakout = db.Column(db.Boolean,default=False)
	hungry = db.Column(db.Boolean,default=False)
	sick = db.Column(db.Boolean,default=False)
	headache = db.Column(db.Boolean, default=False)
	stomach_ache =db.Column(db.Boolean,default=False) 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'sore':self.sore,
		'fatigued':self.fatigued,
		'bloated':self.bloated,
		'constipated':self.constipated,
		'nauseous':self.nauseous,
		'acne_breakout':self.acne_breakout,
		'hungry':self.hungry,
		'sick':self.sick,
		'headache':self.headache,
		'stomach_ache':self.stomach_ache,
		'user_id':self.user_id
		}

class Sexual_Activity(db.Model):
	__tablename__='sexual_activity'
	id = db.Column(db.Integer, primary_key=True)
	entry_date=db.Column(db.TIMESTAMP)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'user_id':self.user_id
		}

class Goals(db.Model):
	__tablename__='goals'
	id = db.Column(db.Integer,primary_key=True)
	entry_date= db.Column(db.TIMESTAMP)
	goal = db.Column(db.String(40))
	complete = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'goal':self.goal,
		'complete':self.complete,
		'user_id':self.user_id
		}

class Tasks(db.Model):
	__tablename__='to_do'
	id = db.Column(db.Integer, primary_key=True)
	entry_date=db.Column(db.TIMESTAMP)
	task = db.Column(db.String(40))
	complete = db.Column(db.Boolean, default=False)
	user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

	def serialize(self):
		return{
		'id':self.id,
		'entry_date':self.entry_date,
		'task':self.task,
		'complete':self.complete,
		'user_id':self.user_id
		}


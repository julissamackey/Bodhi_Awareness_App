
import config
from models import *
import datetime
from datetime import date, timedelta

yesterday = datetime.date.today() - timedelta(1)
current_date= datetime.date.today()
# config.db.drop_all()
# config.db.create_all()

# male_user= User(first_name="john",last_name="smith",email="jsmith@bodhi.com",password="password",gender="M",join_date=current_date)
male_user = User.query.filter_by(email="jsmith@bodhi.com").first()
male_stress= Stress(entry_date=current_date, level=6, relationship=False,family=True,school=False,friends=False,work=True,unclear=False,other=True,pms=False,user=male_user)
male_outlets= Outlets(entry_date=current_date,journaled=True,meditated=True,other=True,user=male_user)
male_phys_act= Physical_Activity(entry_date=current_date,yoga_pilates=False,cardio=False, toning=False,other=False, user= male_user)
male_indulgences= Indulgences(entry_date=current_date,alcohol=False, tobacco= False, sweets= True, coffee= True, other= False, user= male_user)
male_diet= Diet(entry_date=current_date,fast= False,dairy= True, gluten= False, meat= True, user= male_user)
male_sleep = Sleep(entry_date=current_date, hours= 8, quality= True, user= male_user)
male_cog_cond= Cognitive_Condition(entry_date=current_date, overall=7, energized= True, calm= True, irritable= False, confident= True, anxious= False,distracted= True, focused= True, creative= True, apathetic= False, mindful= False, user= male_user)
male_phys_cond= Physical_Condition(entry_date=current_date, overall= 10,sore= False, fatigued= False, bloated= False, constipated= False, nauseous= False, acne_breakout= False,hungry= False, sick= False,headache= False, stomach_ache= True, user= male_user)
male_sex_act= Sexual_Activity(entry_date=current_date, active= False, user= male_user)
# male_goals= Goals(entry_date=current_date, goal= "make 500k this year", complete= False, user= male_user)
male_goals= Goals(entry_date=current_date, goal="", complete=False, user=male_user)
male_tasks= Tasks(entry_date=current_date, task= "",complete= False, user = male_user)
# previous_task = Tasks.query.filter_by(id=1).first()
# previous_task.complete = True


# config.db.session.add(male_user)
config.db.session.add(male_stress)
config.db.session.add(male_outlets)
config.db.session.add(male_phys_act)
config.db.session.add(male_indulgences)
config.db.session.add(male_diet)
config.db.session.add(male_sleep)
config.db.session.add(male_cog_cond)
config.db.session.add(male_phys_cond)
config.db.session.add(male_sex_act)
config.db.session.add(male_goals)
config.db.session.add(male_tasks)

config.db.session.commit()

print('db created')

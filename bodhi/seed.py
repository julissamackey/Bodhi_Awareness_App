import config
from models import *
import datetime

current_date= datetime.date.today()
config.db.drop_all()
config.db.create_all()

first_male_user = User('John', 'Smith', 'jsmith@bodhi.com','password','M', current_date)
first_male_stress_level= Stress_Level(entry_date = current_date,level=1, user = first_male_user)
first_male_stress_causes = Male_Stress_Causes(entry_date=current_date,work = True)
first_male_outlets = Outlets(entry_date=current_date, meditated = True, journaled=True, user = first_male_user)
first_male_physical_activity = Physcial_Activity(entry_date=current_date, toning=True)
first_male_indulgences = Indulgences(entry_date=current_date, user = first_male_user, coffee = True)
first_male_diet = Diet(entry_date=current_date, user = first_male_user, dairy = True veg = True)
first_male_sleep= Sleep(entry_date=current_date, hours= 4, user=first_male_user)
first_male_cog = Cognitive_Condition(entry_date=current_date, distracted = True, irritable = True )
first_male_physical_condition = Physical_Condition(entry_date=current_date, fatigued = True)

first_female_user=User('Jane','Doe','janeD@bodhi.com','password','F',current_date)
first_female_stress_level = Stress_Level(entry_date=current_date, level=1, user=first_female_user)
first_female_stress_causes = Female_Stress_Causes(entry_date=current_date, school= True, pms= True)
first_female_outlets= Outlets(entry_date=current_date, user=first_female_user, other=True)
first_female_physcial_activity = Physcial_Activity(entry_date=current_date, user = first_female_user, yoga_pilates=True)
first_female_diet = Diet(entry_date=current_date, user=first_female_user, meat=True, gluten=True)
first_female_sleep  = Sleep(entry_date=current_date, hours=7,quality=True, user=first_female_user)
first_female_cog = Cognitive_Condition(entry_date=current_date, calm=True, creative=True, mindful=True)

config.db.session.add(first_male_user)
config.db.session.add(first_male_stress_level)
config.db.session.add(first_male_stress_causes)
config.db.session.add(first_male_outlets)
config.db.session.add(first_male_physical_activity)
config.db.session.add(first_male_indulgences)
config.db.session.add(first_male_diet)
config.db.session.add(first_male_sleep)
config.db.session.add(first_male_cog)

config.db.session.add(first_female_user)
config.db.session.add(first_female_stress_level)
config.db.session.add(first_female_stress_causes)
config.db.session.add(first_female_outlets)
config.db.session.add(first_female_physcial_activity)
config.db.session.add(first_female_diet)
config.db.session.add(first_female_sleep)
config.db.session.add(first_female_cog)

config.db.session.commit()

print('db created')
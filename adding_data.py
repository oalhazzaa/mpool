from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webdev import Base, requests, contacts
engine = create_engine('sqlite:///umtogo.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session  = DBsession()
f_request = requests(ID=1, From="Ann_Arbor", To="DTW", time_start = 4, time_end = 5, people_needed = 2)
f_contact = contacts(ID = 1, contact_info = "facebook", comment = "Hello")
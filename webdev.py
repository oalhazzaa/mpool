
from sqlalchemy import Column, ForeignKey, Integer, String, Float

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class requests(Base):
	__tablename__ = "requests_table"

	ID = Column(Integer, primary_key = True)
	From = Column(String(60), nullable = True)
	To = Column(String(60), nullable = False)
	time_start = Column(Float, nullable = False)
	time_end = Column(Float, nullable = False)
	time_period = Column(String(60), nullable = False)
	people_needed = Column(Integer, nullable = False)
	Rider_type = Column(String(60), nullable = False)
	payment = Column(String(60), nullable = False)
	amount = Column(Float, nullable = False)
	username = Column(String(220), nullable = False)

	@property
	def serialize(self):
		return {'ID': self.ID, 'From': self.From, 'To': self.To, 'time_start': self.time_start, 
		'time_end': self.time_end, 'people_needed': self.people_needed}

class contacts(Base):
	__tablename__ = "contacts_table"

	ID = Column(Integer, primary_key = True)
	contact_info = Column(String(300), nullable = False)
	comment = Column(String(300), nullable = True)



##

engine = create_engine('sqlite:///umto.db')
Base.metadata.create_all(engine)
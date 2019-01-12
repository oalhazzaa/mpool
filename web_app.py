from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webdev import Base, requests, contacts
app = Flask(__name__)





@app.route('/requests')
@app.route('/')

def main_web():
	engine = create_engine('sqlite:///umto.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind = engine)
	session  = DBsession()
	session.commit()
	requests_data = session.query(requests).all()
	contacts_data = session.query(contacts).all()
	output =""
	'''for request in requests_data:
		output = output + "{} ".format(request.ID) + request.From + " to " + request.To 
		output += '</br>'
	return output
	'''
	return render_template('index.html', items = requests_data)


@app.route('/requests/new', methods=['GET', 'POST'])	
def newMenuItem():
	engine = create_engine('sqlite:///umto.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind = engine)
	session  = DBsession()
	i = session.query(requests).count()
	if request.method == 'POST':
		newItem = requests(ID = i , From = request.form['from'], To = request.form['to'], 
			time_start = request.form['time_start'], time_end = request.form['time_end'],
			 time_period = request.form['time_period'],
			people_needed = request.form['people_needed'], Rider_type = request.form['Rider_type'], 
			payment = request.form['payment'],amount = request.form['amount'], username = request.form['username'])
		session.add(newItem)
		flash("New request added successfuly!")
		session.commit()
		return redirect(url_for('main_web'))
	else:
		return render_template('newrequest.html')
		'''request.form['request_id']'''

# Task 2: Create route for editMenuItem function here

@app.route('/requests/<int:request_id>/edit', methods=['GET', 'POST'])	

def editMenuItem(request_id):
	engine = create_engine('sqlite:///umto.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind = engine)
	session  = DBsession()
	EditedItem = session.query(requests).filter_by(ID = request_id).one()
	if request.method == 'POST':
		EditedItem.From = request.form['from']
		EditedItem.To = request.form['to']
		EditedItem.time_start = request.form['time_start']
		EditedItem.time_end = request.form['time_end']
		EditedItem.people_needed = request.form['people_needed']
		session.add(EditedItem)
		flash("Request edited successfuly!")
		session.commit()
		return redirect(url_for('main_web'))
	else:
		return render_template('editrequest.html', request_id= request_id)

# Task 3: Create a route for deleteMenuItem function here

@app.route('/requests/<int:request_id>/delete', methods=['GET', 'POST'])	

def deleteMenuItem(request_id):
	engine = create_engine('sqlite:///umto.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind = engine)
	session  = DBsession()
	DeletedItem = session.query(requests).filter_by(ID = request_id).one()
	if request.method == 'POST':
		session.delete(DeletedItem)
		flash("Request deleted successfuly!")
		session.commit()
		return redirect(url_for('main_web'))
	else:
		return render_template('deleterequest.html', request_id= request_id)

@app.route('/requests/<int:request_id>/JSON')	
def request_json(request_id):
	engine = create_engine('sqlite:///umto.db')
	Base.metadata.bind = engine
	DBsession = sessionmaker(bind = engine)
	session  = DBsession()
	request = session.query(requests).filter_by(ID = request_id).one()
	return jsonify(request.serialize) 

''', To="DTW", time_start = 4, time_end = 5, people_needed = 2'''
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)

import sqlite3 as sql
import sqlite3
from flask import Flask, request
import json

app = Flask(__name__)
def check_if_in(name, cur):
		cur.execute('SELECT * FROM students')
		for row in cur:
				print(row[0])
				if row[0] == name:
						return True
		return False
# update_status():
# PARAMETER: name, classNo
# First check if name exists in the db
# Then only change the status of classNo
@app.route('/update', methods = ['POST', 'GET'])
def update_status():
	if request.method == 'POST':
		name = request.form['name']
		classNo = request.form['classNo']

		with sql.connect("database.db") as con:
			cur = con.cursor()
			if (check_if_in(name, cur) == False):
				fail = {"FAILED": "NOT FOUND IN THE DATABASE"}
				return json.dumps(fail)
				
			cur.execute("UPDATE students SET {} = 'True' WHERE name = '{}'".format(str(classNo), name))

			con.commit()
			success = {"SUCCESS": "UPDATE SUCCESS"}
			return json.dumps(success)
			
# get_status()
# PARAMETER - classNo
# RETURN - json file contain all the students on class1
@app.route('/get', methods = ['POST', 'GET'])
def get_status():
	if request.method == 'POST':
		classNo = request.form['classNo']
		classint = int(classNo[5])
		with sql.connect("database.db") as con:
			cur = con.cursor()
			out_json = {}
			for row in cur:
				out_json[row[0]] = row[classint]
			con.commit()
			return json.dumps(out_json)
			
# reset_classNo()
@app.route('/reset', methods = ['POST', 'GET'])
def reset_classNo():
	if request.method == 'POST':
		classNo = request.form['classNo']
		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE students SET {} = 'False'".format(str(classNo), name))
			con.commit()
			out = {'SUCCESS': 'CHANGE SUCCESS'}
			return json.dumps(out)
			
@app.route('add', methods = ['POST', 'GET'])
def add_new():
	if request.method = 'POST':
		name = request.form['name']
		with sql.connect("database.db") as con:
			cur = con.cursor()
			find = check_if_in(name, cur)
			if find:
				out = {'FAILED': 'ALREADY IN DATABASE'}
				return json.dumps(out)
			cur.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', (str(name), 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
			con.commit()
			out = {'SUCCESS': 'CHANGE SUCCESS'}
			return json.dumps(out)

		
if __name__ == '__main__':
		app.run(host='0.0.0.0', port=80)
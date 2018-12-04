import sqlite3 as sql
import sqlite3
def init():
	conn = sqlite3.connect('database.db')
	print('Opened database successfully')

#	conn.execute('CREATE TABLE students (name TEXT, class1 TEXT, class2 TEXT, class3 TEXT, class4 TEXT, class5 TEXT, class6 TEXT )')

	conn.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', ('WangTianduo', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
	conn.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', ('LiYanzhang', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
	conn.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', ('TangXiaoyue', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
	conn.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', ('LuoYifan', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
	conn.execute('INSERT INTO students (name, class1, class2, class3, class4, class5, class6) VALUES (?,?,?,?,?,?,?)', ('ZhuBo', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE', 'FALSE'))

	print('Table created successfully')
	conn.commit()
	conn.close()
	return None
	
init()
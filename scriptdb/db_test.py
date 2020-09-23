import sqlite3 

db = sqlite3.connect('server_db') #create db
sql = db.cursor()

#create table with 3 columns
sql.execute("""CREATE TABLE IF NOT EXISTS USERS (
  login TEXT,
  password TEXT,
  cash BIGINT

)""")#create users

db.commit()

users_login = input("Login:")
users_password = input("Password:")

#condition : choose from login table users
sql.execute("SELECT login FROM users")
#main condition if we have no  this login 
if  sql.fetchone() is None:
	sql.execute(f"INSERT INTO users VALUES (?,?,?)",(users_login,users_password,0)) #write down information in users table
	db.commit()
else:
	print('This account is exists!')

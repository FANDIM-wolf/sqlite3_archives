import sqlite3 
from random import*

#we cant lose these variable 
global db
global sql



db = sqlite3.connect('server_db') #create db
sql = db.cursor()

#create table with 3 columns
sql.execute("""CREATE TABLE IF NOT EXISTS USERS (
  login TEXT,
  password TEXT,
  cash BIGINT

)""")#create users

db.commit()

def registration():

    users_login = input("Login:")
    users_password = input("Password:")

    #condition : choose  login from table users
    sql.execute(f"SELECT login FROM users WHERE login = '{users_login}'")
    #main condition if we have no  this login 
    if  sql.fetchone() is None:
	    sql.execute(f"INSERT INTO users VALUES (?,?,?)",(users_login,users_password,0)) #write down information in users table
	    db.commit()
	    print("Dutch account is registed.")
    else:
	    print('This account is exists!')
	    for value in sql.execute("SELECT * FROM users"):
	    	print("Users")
	    	print(value)
    
        #show  all users from table "users" 


#delete user function 
def delete_user():
	sql.execute(f"DELETE FROM users WHERE login = {'user_login'}")
	db.commit()
	print("User have been deleted.")    

#check name  and we  give  1000
def book():
	global user_login 
	user_enter = input("Enter your name:")
	number = randint(1,2)
    #get balance of user with loop
	for i in sql.execute(f"SELECT cash FROM  users WHERE login = '{user_login}'"):
		balance = i[0]

	sql.execute(f"SELECT login FROM users WHERE login ='{user_enter}'")
	if sql.fetchone() is None:
		print("Login does not exists. Check in")
		registration()
	else:
		if number == 1:
			#set for 1000 for  this  user
			sql.execute(f"UPDATE users SET cash={1000+balance} WHERE login='{user_login}' ")
			db.commit()
		else:
			print("You losed!")
			delete_db()
			
	
    
#show logins and cash of USERS    
def show():
	for i in sql.execute(f"SELECT login , cash FROM users"):
		print("USER DATA from table USERS:")
		print(i)

	

def main():
	book()
	show()

main()

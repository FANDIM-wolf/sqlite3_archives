import random
#cycles of model
cm = int(input("Enter a number of cycles:\n"))


#marks of year 
mark_1 = "*"
mark_2 = "**"
mark_3 = "***"
#minimum salary to live in another country
minimal_value_to_live = random.randint(100,134)
#year to start 
year = int(input("Enter your start year (2019 for example):"))
 
salary_of_man = int(input("Enter your salary:"))
if salary_of_man >= 100000:
	print("You are rich")
while (cm!=0):
    cm=cm-1
    year=year + 1
    object_1 = random.randint(100,234)
    object_2 = random.randint(100,450)
    object_3 = random.randint(100,560)
    object_4 = random.randint(100,1000)
    salary_of_man = salary_of_man-object_1-object_2-object_3-object_4
    
    if salary_of_man >= 1000:
        print(year)
        print(mark_3)
    elif salary_of_man <= 1000:
        print(year)
        print(mark_2)
    elif salary_of_man <= 500:
        print(year)
        print(mark_1)
      
    print("______________________________") 



		


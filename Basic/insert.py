import sqlite3

import random

conn = sqlite3.connect('my.db')
cursor = conn.cursor()

#teacher 

name = input("Enter the name : ")
email = input("Enter the email : ")

for i in range(0,100):
    mob = random.randint(100000,1000000)
    t_id  =1
    cursor.execute("INSERT INTO TEACHER (T_name,T_email,T_mobile) VALUES(?, ?,?)",( name,email,mob))  
    
conn.commit()
j = cursor.execute("SELECT * FROM TEACHER")  
print(j)
conn.close()
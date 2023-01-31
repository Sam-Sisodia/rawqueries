import sqlite3



conn = sqlite3.connect('my.db')
cursor = conn.cursor()
sql = ''' CREATE TABLE TEACHER(
        T_name VARCHAR(20),
        T_email VARCHAR(20),
        T_mobile VARCHAR(20)
    )'''
    
cursor.execute(sql)
conn.commit()
conn.close()
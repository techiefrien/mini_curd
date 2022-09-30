import sqlite3



con = sqlite3.connect("students.db")
cur = con.cursor()
cur.execute("select * from std")
datas = cur.fetchall()
 

for  data in datas:
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    
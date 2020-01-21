import mysql.connnector as mconn

conn = mconn.connect(host="localhost", user="root", database="test")
if not conn.is_connected():
    print("error: cant connect to mysql")
    conn.close()

cur  = conn.cursor()
cur.execute("select * from student")
data = cur.fetchmany(3)

for i in data:
    for j in i:
        print(i, end='\t')
    print()

conn.close()

import mysql.connector as mconn

conn = mconn.connect(host="localhost", user="root", database="test")
if not conn.is_connected():
    print("error: cant connect to mysql")
    conn.close()
cur = conn.cursor()
cur.execute("insert into student values('name', 'city', 15)")
conn.commit()
conn.close()

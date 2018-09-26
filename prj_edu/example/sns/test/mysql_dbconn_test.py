import MySQLdb as mysql

db = mysql.connect(host="localhost", user="devsns", passwd="devsns0!", db="db_sns")

cur = db.cursor()
cur.execute("SELECT * FROM message")
print(cur.fetchall())
print("-----------------------------------------")

db.close()

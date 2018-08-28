import MySQLdb as mysql

db = mysql.connect(host="localhost", user="devpythontest", passwd="Devpythontest0!", db="dev_pythontest_db")

cur = db.cursor()
cur.execute("SELECT * FROM users")
print(cur.fetchall())
print("-----------------------------------------")

db.close()

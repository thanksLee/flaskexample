import MySQLdb

def connection():
    conn = MySQLdb.connect(   host="localhost"
                            , user="devpythontest"
                            , passwd="Devpythontest0!"
                            , db="dev_pythontest_db"
                            )
    c = conn.cursor()
    return c, conn
import MySQLdb

def Connection():
    conn = MySQLdb.connect(   host="localhost"
                            , user="devpythontest"
                            , passwd="Devpythontest0!"
                            , db="dev_pythontest_db"
                            , charset='utf8'
                            )
    c = conn.cursor()
    return c, conn
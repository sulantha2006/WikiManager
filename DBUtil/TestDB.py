__author__ = 'sulantha'
import MySQLdb as mDB
import sys

try:
    con = mDB.connect('localhost', 'testuser', 'test321', 'testdb')

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Database version : %s " % ver

except mDB.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
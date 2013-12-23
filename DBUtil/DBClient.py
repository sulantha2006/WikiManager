__author__ = 'sulantha'
import MySQLdb as msqlDB
import Config.DBConfig as dbConfig


class DBClient:
    def __init__(self):
        pass

    def executeQuery(self, sqlQuery, **kwargs):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        if 'numOfResults' in kwargs:
            return cursor.fetchmany(kwargs['numOfResults'])
        else:
            return cursor.fetchall()

    def executeDictionaryQuery(self, sqlQuery, **kwargs):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor(msqlDB.cursors.DictCursor)
        cursor.execute(sqlQuery)
        if 'numOfResults' in kwargs:
            return cursor.fetchmany(kwargs['numOfResults'])
        else:
            return cursor.fetchall()
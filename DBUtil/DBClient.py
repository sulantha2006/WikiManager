__author__ = 'sulantha'
import MySQLdb as msqlDB
import Config.DBConfig as dbConfig


class DBClient:
    def __init__(self):
        pass

    def executeQuery(self, sqlQuery, numOfResults):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        return cursor.fetchmany(numOfResults)
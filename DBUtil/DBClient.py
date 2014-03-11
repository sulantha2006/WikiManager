__author__ = 'sulantha'
import MySQLdb as msqlDB
import Config.DBConfig as dbConfig


class DBClient:
    def __init__(self):
        pass

    @staticmethod
    def executeQuery(sqlQuery, **kwargs):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        if 'numOfResults' in kwargs:
            return cursor.fetchmany(kwargs['numOfResults'])
        else:
            return cursor.fetchall()

    @staticmethod
    def executeDictionaryQuery(sqlQuery, **kwargs):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor(msqlDB.cursors.DictCursor)
        cursor.execute(sqlQuery)
        if 'numOfResults' in kwargs:
            return cursor.fetchmany(kwargs['numOfResults'])
        else:
            return cursor.fetchall()

    @staticmethod
    def directExeQuery(sqlStr, *args):
        con = msqlDB.connect(dbConfig.DBParams['host'], dbConfig.DBParams['user'], dbConfig.DBParams['userPass'],
                             dbConfig.DBParams['dbName'])
        con.autocommit(True)
        cursor = con.cursor()
        cursor.execute(sqlStr, args)
        return cursor.fetchall()
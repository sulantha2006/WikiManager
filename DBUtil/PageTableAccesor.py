__author__ = 'sulantha'
from DBClient import DBClient
from Config import ManagerPageTableConfig


class PageTableAccessor:
    def __init__(self):
        pass

    @staticmethod
    def getNewIds():
        newIds = {}
        for entity in ManagerPageTableConfig.entityList:
            sqlStr = 'SELECT ' + ManagerPageTableConfig.managerPageTableColumns['pageTitle'] + \
                     ' FROM ' + ManagerPageTableConfig.managerPageTableName + ' WHERE ' + \
                     ManagerPageTableConfig.managerPageTableColumns['typeColumn'] + ' = \'' + entity + '\' AND ' + \
                     ManagerPageTableConfig.managerPageTableColumns['needsUpdate'] + ' = 1'
            newIds[entity] = [x[0] for x in DBClient.executeQuery(sqlStr)]
        return newIds
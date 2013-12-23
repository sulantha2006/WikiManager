__author__ = 'sulantha'
from DBClient import DBClient
from Config import ManagerPageTableConfig


class PageTableAccessor:
    dbClient = None

    def __init__(self):
        self.dbClient = DBClient()

    def getNewWells(self):
        sqlStr = 'SELECT PAGE_NAME FROM ' + ManagerPageTableConfig.managerPageTableName + ' WHERE TYPE = \'wells\' AND NEEDS_UPDATE = 1'
        return self.dbClient.executeQuery(sqlStr)

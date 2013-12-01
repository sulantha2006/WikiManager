__author__ = 'sulantha'
import Config.ManagerPageTableConfig as mPTConfig
from DBUtil.DBClient import DBClient


class PageTableUpdater:
    dbClient = DBClient()

    def __init__(self):
        pass

    def updateEntity(self, entityName, entityTable, entityColumnName):
        sqlStr = ('INSERT IGNORE INTO ' + mPTConfig.managerPageTableName +
                  ' (' + mPTConfig.managerPageTableColumns['pageTitle'] +
                  ', ' + mPTConfig.managerPageTableColumns['typeColumn'] + ')' +
                  ' (SELECT DISTINCT ' + entityColumnName + ' AS ' + mPTConfig.managerPageTableColumns['pageTitle'] +
                  ', \'' + entityName + '\' AS ' + mPTConfig.managerPageTableColumns['typeColumn'] +
                  ' FROM ' + entityTable + ')')
        print self.dbClient.executeQuery(sqlStr, 1)
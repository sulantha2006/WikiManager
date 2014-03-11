__author__ = 'sulantha'
import Config.ManagerPageTableConfig as mPTConfig
from DBUtil.DBClient import DBClient


class PageTableUpdater:

    def __init__(self):
        pass

    @staticmethod
    def updateEntity(entityName, entityTable, entityColumnName):
        sqlStr = ('INSERT IGNORE INTO ' + mPTConfig.managerPageTableName +
                  ' (' + mPTConfig.managerPageTableColumns['pageTitle'] +
                  ', ' + mPTConfig.managerPageTableColumns['typeColumn'] + ')' +
                  ' (SELECT DISTINCT ' + entityColumnName + ' AS ' + mPTConfig.managerPageTableColumns['pageTitle'] +
                  ', \'' + entityName + '\' AS ' + mPTConfig.managerPageTableColumns['typeColumn'] +
                  ' FROM ' + entityTable + ' WHERE ' + entityColumnName + ' IS NOT NULL )')
        print DBClient.executeQuery(sqlStr, numOfResults=1)

    @staticmethod
    def setUpdateSuccess(entityId):
        sqlStr = ('UPDATE ' + mPTConfig.managerPageTableName + ' SET ' +
                  mPTConfig.managerPageTableColumns['needsUpdate'] + ' = 0 WHERE ' +
                  mPTConfig.managerPageTableColumns['pageTitle'] + ' = %s')

        print DBClient.directExeQuery(sqlStr, entityId)
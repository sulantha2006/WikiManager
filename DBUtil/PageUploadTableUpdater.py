__author__ = 'sulantha'
from DBClient import DBClient
from Config import WikiPageUploadConfig


class PageUploadTableUpdater():
    def __init__(self):
        pass

    @staticmethod
    def addEntry(entityId, filePath):
        sqlStr = ('INSERT INTO ' + WikiPageUploadConfig.wikiPageUploadTableName +
                  ' ( ' + WikiPageUploadConfig.wikiPageUploadTableColumns['pageId'] +
                  ', ' + WikiPageUploadConfig.wikiPageUploadTableColumns['filePath'] + ' )' +
                  ' VALUES ( \'' + entityId + '\', \'' + filePath + '\' )')

        print DBClient.executeQuery(sqlStr, numOfResults=1)

    @staticmethod
    def setUploadSuccess(tableId):
        sqlStr = ('UPDATE ' + WikiPageUploadConfig.wikiPageUploadTableName + ' SET ' +
                  WikiPageUploadConfig.wikiPageUploadTableColumns['needsUpload'] + ' = 0 WHERE ' +
                  WikiPageUploadConfig.wikiPageUploadTableColumns['tableId'] + ' = \'' + str(tableId) + '\'')

        print DBClient.executeQuery(sqlStr, numOfResults=1)

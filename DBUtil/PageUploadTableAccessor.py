__author__ = 'sulantha'
from Config import WikiPageUploadConfig
from DBClient import DBClient


class PageUploadTableAccessor():
    def __init__(self):
        pass

    @staticmethod
    def getUploadFiles():
        sqlStr = 'SELECT ' + WikiPageUploadConfig.wikiPageUploadTableColumns['tableId'] + ', ' + \
                 WikiPageUploadConfig.wikiPageUploadTableColumns['filePath'] + \
                 ' FROM ' + WikiPageUploadConfig.wikiPageUploadTableName + ' WHERE ' + \
                 WikiPageUploadConfig.wikiPageUploadTableColumns['needsUpload'] + ' = 1'
        return [(x[0], x[1]) for x in DBClient.executeQuery(sqlStr)]
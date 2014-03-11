__author__ = 'sulantha'
from DBClient import DBClient
from Config import WikiPageUploadConfig


class PageUploadTableUpdater():
    def __init__(self):
        pass

    @staticmethod
    def addEntry(entityId, filePath):
        # if '\'' in entityId:
        #     entityId = str.replace(entityId, '\'', '\\\'')
        # if '\'' in filePath:
        #     filePath = str.replace(filePath, '\'', '\\\'')
        # sqlStr = ("""INSERT INTO """ + WikiPageUploadConfig.wikiPageUploadTableName +
        #           """ ( """ + WikiPageUploadConfig.wikiPageUploadTableColumns['pageId'] +
        #           """, """ + WikiPageUploadConfig.wikiPageUploadTableColumns['filePath'] + """ )""" +
        #           """ VALUES ( \'""" + entityId + """\', \'""" + filePath + """\' )""")
        sqlStr = """INSERT INTO """ + WikiPageUploadConfig.wikiPageUploadTableName + """ ( """ + WikiPageUploadConfig.wikiPageUploadTableColumns['pageId'] + """, """ + WikiPageUploadConfig.wikiPageUploadTableColumns['filePath'] + """ ) VALUES ( %s, %s )"""
        print DBClient.directExeQuery(sqlStr, entityId, filePath)

    @staticmethod
    def setUploadSuccess(tableId):
        sqlStr = ('UPDATE ' + WikiPageUploadConfig.wikiPageUploadTableName + ' SET ' +
                  WikiPageUploadConfig.wikiPageUploadTableColumns['needsUpload'] + ' = 0 WHERE ' +
                  WikiPageUploadConfig.wikiPageUploadTableColumns['tableId'] + ' = \'' + str(tableId) + '\'')

        print DBClient.executeQuery(sqlStr, numOfResults=1)

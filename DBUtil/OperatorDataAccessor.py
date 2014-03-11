__author__ = 'sulantha'
from DBClient import DBClient
from WellDataAccessor import WellDataAccessor
from Config import OperatorDataConfig as odc


class OperatorDataAccessor:
    dbClient = None
    operatorID = None

    def __init__(self, operatorID):
        self.dbClient = DBClient()
        self.operatorID = operatorID

    def getAllWellsFromOperator(self, operatorName):
        sqlStr = 'SELECT WELL_API_COUNTY_ID FROM well_complete WHERE OPERATOR_NAME = %s'
        return self.dbClient.directExeQuery(sqlStr, operatorName)

    def getInfoForWell(self, wellId):
        wellDataAcc = WellDataAccessor(wellId)
        return wellDataAcc.getWellPrimaryData()

    def getOperatorSecondaryData(self):
        finalDataDict = {}
        for dataType in odc.operatorDataDBTables:
            if dataType == 'wells':
                dataDict = {}
                wellsInCounty = self.getAllWellsFromOperator(self.operatorID)
                for well in wellsInCounty:
                    dataDict[well[0]] = self.getInfoForWell(well[0])
                    finalDataDict[dataType] = dataDict
            else:
                sqlStr = 'SELECT ' + odc.operatorDataSelectedColumnsFromTables[odc.operatorDataDBTables[dataType]] + ' FROM ' + \
                         odc.operatorDataDBTables[dataType] + \
                         ' WHERE ' + odc.operatorDataDBTableIDs[odc.operatorDataDBTables[dataType]] + ' = \'' + self.operatorID + '\''
                finalDataDict[dataType] = self.dbClient.executeQuery(sqlStr)
        return finalDataDict

    def getOperatorPrimaryData(self):
        dataDict = {}
        for table in odc.operatorDetailsTables:
            try:
                sqlStr = 'SELECT ' + odc.operatorDetailsTablesSelectionColumns[table] + ' FROM ' + table + ' WHERE ' + \
                         odc.operatorDataDBTableIDs[table] + ' = \'' + self.operatorID + '\''
            except KeyError:
                pass
            try:
                data = self.dbClient.executeDictionaryQuery(sqlStr)[0]
            except IndexError:
                data = {x.strip(): 'NULL' for x in str.split(odc.operatorDetailsTablesSelectionColumns[table], ',')}
            dataDict.update(data)
        return dataDict
__author__ = 'sulantha'
from DBClient import DBClient
from WellDataAccessor import WellDataAccessor
from Config import CountyDataConfig as cdc


class CountyDataAccessor:
    dbClient = None
    conId = None

    def __init__(self, conId):
        self.dbClient = DBClient()
        self.conId = conId

    def getAllWellsInCounty(self, conName, stateName):
        sqlStr = 'SELECT WELL_API_COUNTY_ID FROM well_complete WHERE WELL_COUNTY = %s'
        return self.dbClient.directExeQuery(sqlStr, conName)

    def getInfoForWell(self, wellId):
        wellDataAcc = WellDataAccessor(wellId)
        return wellDataAcc.getWellPrimaryData()

    def getConSecondaryData(self):
        finalDataDict = {}
        conName = str.split(self.conId, ',')[0].strip()
        stateName = str.split(self.conId, ',')[1].strip()
        for dataType in cdc.conDataDBTables:
            dataDict = {}
            if dataType == 'wells':
                wellsInCounty = self.getAllWellsInCounty(conName, stateName)
                for well in wellsInCounty:
                    dataDict[well[0]] = self.getInfoForWell(well[0])
            finalDataDict[dataType] = dataDict
        return finalDataDict

    def getConPrimaryData(self):
        pass

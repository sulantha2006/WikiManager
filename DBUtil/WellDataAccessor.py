__author__ = 'sulantha'
from DBClient import DBClient
from Config import WellDataConfig as wdc


class WellDataAccessor:
    dbClient = None
    wellID = None

    def __init__(self, wellID):
        self.dbClient = DBClient()
        self.wellID = wellID

    def getWellSecondaryData(self):
        finalDataDict = {}
        for dataType in wdc.wellDataDBTables:
            sqlStr = 'SELECT ' + wdc.wellDataSelectedColumnsFromTables[wdc.wellDataDBTables[dataType]] + ' FROM ' + \
                     wdc.wellDataDBTables[dataType] + \
                     ' WHERE ' + wdc.wellDataDBTableIDs[wdc.wellDataDBTables[dataType]] + ' = \'' + self.wellID + '\''
            finalDataDict[dataType] = self.dbClient.executeQuery(sqlStr)
        return finalDataDict

    def getWellPrimaryData(self):
        dataDict = {}
        for table in wdc.wellDetailsTables:
            try:
                sqlStr = 'SELECT ' + wdc.wellDetailsTablesSelectionColumns[table] + ' FROM ' + table + ' WHERE ' + \
                         wdc.wellDataDBTableIDs[table] + ' = \'' + self.wellID + '\''
            except KeyError:
                ### Error by municipality or county
                pass
            ##### Municipality need to be handled seperately as the name of each need to be unique.
            if table == 'municipality':
                sqlStr = 'SELECT CONCAT(municipality_name_long, \', \', county_name, \', \', state_code) AS \'MUNICIPALITY_FULL_NAME\' FROM municipality WHERE (COUNTY_NAME, MUNICIPALITY_NAME_LSAD) = (SELECT WELL_COUNTY, WELL_MUNICIPALITY FROM unconventional WHERE WELL_API_COUNTY_ID = \'' + self.wellID + '\')'
            if table == 'county':
                sqlStr = 'SELECT CONCAT(county_name, \', \', state_code) AS \'COUNTY_FULL_NAME\' FROM municipality WHERE (COUNTY_NAME, MUNICIPALITY_NAME_LSAD) = (SELECT WELL_COUNTY, WELL_MUNICIPALITY FROM unconventional WHERE WELL_API_COUNTY_ID = \'' + self.wellID + '\')'

            try:
                data = self.dbClient.executeDictionaryQuery(sqlStr)[0]
            except IndexError:
                data = {x.strip(): 'NULL' for x in str.split(wdc.wellDetailsTablesSelectionColumns[table], ',')}
            dataDict.update(data)
        return dataDict
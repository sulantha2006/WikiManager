__author__ = 'sulantha'
from DBClient import DBClient
from Config import MunicipalityDataConfig as mdc


class MunicipalityDataAccessor:
    dbClient = None
    munId = None

    def __init__(self, munId):
        self.dbClient = DBClient()
        self.munId = munId

    def getMunSecondaryData(self):
        finalDataDict = {}
        munName = str.split(self.munId, ',')[0].strip()
        countyName = str.split(self.munId, ',')[1].strip()
        for dataType in mdc.munDataDBTables:
            if dataType == 'wells':
                sqlStr = 'SELECT well_api_county_id, operator_name, first_permit_issued_date, spud_date, unconventional, horizontal_well, well_status, violation_count FROM (SELECT well_complete.well_api_county_id, permit.operator_name, well_complete.first_permit_issued_date, well_complete.spud_date, well_complete.unconventional, well_complete.horizontal_well, unconventional.well_status, well_complete.violation_count, county_name, municipality_name_long  FROM well_complete join unconventional on well_complete.well_api_county_id = unconventional.well_api_county_id join permit on unconventional.well_api_county_id = permit.well_api_county_id join municipality on unconventional.well_county = municipality.county_name and unconventional.well_municipality = municipality.municipality_name_lsad) AS temp WHERE county_name= %s AND municipality_name_long = %s'
            finalDataDict[dataType] = self.dbClient.directExeQuery(sqlStr, countyName, munName)
        return finalDataDict

    def getMunPrimaryData(self):
        pass

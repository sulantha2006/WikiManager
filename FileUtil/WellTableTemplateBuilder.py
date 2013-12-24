__author__ = 'sulantha'
from DBUtil.WellDataAccessor import WellDataAccessor
from Config import WellDataConfig, FileConfig
from FileHandler import FileHandler


class WellTableTemplateBuilder:
    wellDataAccessor = None
    fileHandler = None
    wellID = None

    def __init__(self, wellID):
        self.wellDataAccessor = WellDataAccessor(wellID)
        self.fileHandler = FileHandler()
        self.wellID = wellID

    def buildSecondaryTemplates(self):
        def addUnsortColumn(dataType, columnName):
            if columnName in WellDataConfig.wellDataSortableColumns[dataType]:
                return ''
            else:
                return 'class="unsortable"'

        wellSecondaryData = self.wellDataAccessor.getWellSecondaryData()
        for dataType in wellSecondaryData:
            wikiText = '{| class="wikitable sortable" width="95%"\n'
            numberOfColumns = len(wellSecondaryData[dataType][0])
            wikiText += '!colspan="' + str(numberOfColumns) + '"|' + WellDataConfig.wellDataProperFinalTableTopics[dataType] + '\n|-\n'
            for column in WellDataConfig.wellDataProperColumnNames[dataType]:
                wikiText += '!scope="col" ' + addUnsortColumn(dataType, column) + '| '+column + '\n'

            for row in wellSecondaryData[dataType]:
                wikiText += '|-\n'
                for item in row:
                    wikiText += '| ' + str(item) + '\n'
                wikiText += '|-\n'
            wikiText += '|}'
            self.fileHandler.writeFile(FileConfig.templateFilePath, self.wellID+'_'+dataType+'_Template.txt', 'Template:'+self.wellID+'-'+dataType, wikiText)

    def buildPrimaryTemplates(self):
        wellPrimaryData = self.wellDataAccessor.getWellPrimaryData()
        numberOfRows = len(wellPrimaryData)
        wikiText = '{| class="wikitable" width="95%"\n'
        wikiText += '!colspan="2"| Well Details \n'
        wikiText += '|-\n'
        wikiText += '| Well ID: ' + self.wellID + '\n'
        wikiText += '| style="width: 30%" rowspan="' + str(numberOfRows+1) + '" | {{#display_map: ' + str(wellPrimaryData['LATITUDE_DECIMAL'])+', ' + str(wellPrimaryData['LONGITUDE_DECIMAL']) + ' | width=500px }} \n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_COUNTY'] + ': ' + wellPrimaryData['WELL_COUNTY'] + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_MUNICIPALITY'] + ': ' + wellPrimaryData['WELL_MUNICIPALITY'] + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['OPERATOR_NAME'] + ': ' + wellPrimaryData['OPERATOR_NAME'] + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['OPERATOR_OGO'] + ': ' + wellPrimaryData['OPERATOR_OGO'] + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['FARM_NAME'] + ': ' + wellPrimaryData['FARM_NAME'] + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['FIRST_PERMIT_ISSUED_DATE'] + ': ' + str(wellPrimaryData['FIRST_PERMIT_ISSUED_DATE']) + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LAST_PERMIT_ISSUED_DATE'] + ': ' + str(wellPrimaryData['LAST_PERMIT_ISSUED_DATE']) + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['SPUD_DATE'] + ': ' + str(wellPrimaryData['SPUD_DATE']) + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['UNCONVENTIONAL'] + ': ' + ('Yes' if wellPrimaryData['UNCONVENTIONAL'] is 'Y' else 'No') + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['HORIZONTAL_WELL'] + ': ' + ('Yes' if wellPrimaryData['HORIZONTAL_WELL'] is 'Y' else 'No') + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_STATUS'] + ': ' + ('Yes' if wellPrimaryData['WELL_STATUS'] is 'Active' else 'No') + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['VIOLATION_COUNT'] + ': ' + str(wellPrimaryData['VIOLATION_COUNT']) + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LATITUDE_DECIMAL'] + ': ' + str(wellPrimaryData['LATITUDE_DECIMAL']) + '\n'
        wikiText += '|-\n'
        wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LONGITUDE_DECIMAL'] + ': ' + str(wellPrimaryData['LONGITUDE_DECIMAL']) + '\n'
        wikiText += '|-\n'
        wikiText += '|}'

        self.fileHandler.writeFile(FileConfig.templateFilePath, self.wellID+'_Details_Template.txt', 'Template:'+self.wellID+'-Details', wikiText)

    def buildTableTemplates(self):
        self.buildSecondaryTemplates()
        self.buildPrimaryTemplates()
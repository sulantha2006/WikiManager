__author__ = 'sulantha'
from DBUtil.WellDataAccessor import WellDataAccessor
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater
from Config import WellDataConfig, FileConfig
from FileUtil.FileHandler import FileHandler


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
            if WellDataConfig.wellDataSelectiveSortingEnabled:
                if columnName in WellDataConfig.wellDataSortableColumns[dataType]:
                    return ''
                else:
                    return 'class="unsortable"'
            else:
                return ''

        wellSecondaryData = self.wellDataAccessor.getWellSecondaryData()
        for dataType in wellSecondaryData:
            wikiText = '{| class="wikitable sortable" width="95%"\n'
            try:
                numberOfColumns = len(wellSecondaryData[dataType][0])
            except IndexError:
                numberOfColumns = 0
            wikiText += '!colspan="' + str(numberOfColumns) + '"|' + WellDataConfig.wellDataProperFinalTableTopics[dataType] + '\n|-\n'
            for column in WellDataConfig.wellDataProperColumnNames[dataType]:
                wikiText += '!scope="col" ' + addUnsortColumn(dataType, column) + '| '+column + '\n'

            for row in wellSecondaryData[dataType]:
                wikiText += '|-\n'
                for item in row:
                    wikiText += '| ' + str(item) + '\n'
                wikiText += '|-\n'
            wikiText += '|}'
            templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.wellID+'_'+dataType+'_Template.txt', 'Template:'+self.wellID+'-'+dataType, wikiText)
            PageUploadTableUpdater.addEntry(self.wellID, templateFile)

    def buildPrimaryTemplates(self):
        wellPrimaryData = self.wellDataAccessor.getWellPrimaryData()
        numberOfRows = len(wellPrimaryData)
        wikiText = '{| class="wikitable" width="95%"\n'
        wikiText += '!colspan="2"| Well Details \n'
        wikiText += '|-\n'
        wikiText += '| Well ID: ' + self.wellID + '\n'
        if wellPrimaryData['LATITUDE_DECIMAL'] is not None and wellPrimaryData['LONGITUDE_DECIMAL'] is not None:
            wikiText += '| style="width: 50%; height=100%; align=center" rowspan="' + str(numberOfRows+1) + '" | {{#display_map: ' + str(wellPrimaryData['LATITUDE_DECIMAL'])+', ' + str(wellPrimaryData['LONGITUDE_DECIMAL']) + ' | width=100% | height=100% }} \n'
            wikiText += '|-\n'
        else:
            wikiText += '|-\n'
        if wellPrimaryData['WELL_COUNTY'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_COUNTY'] + ': [[' + wellPrimaryData['COUNTY_FULL_NAME'] + ']]\n'
            wikiText += '|-\n'
        if wellPrimaryData['WELL_MUNICIPALITY'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_MUNICIPALITY'] + ': [[' + wellPrimaryData['MUNICIPALITY_FULL_NAME'] + ']]\n'
            wikiText += '|-\n'
        if wellPrimaryData['OPERATOR_NAME'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['OPERATOR_NAME'] + ': [[' + wellPrimaryData['OPERATOR_NAME'] + ']]\n'
            wikiText += '|-\n'
        if wellPrimaryData['OPERATOR_OGO'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['OPERATOR_OGO'] + ': [[' + wellPrimaryData['OPERATOR_OGO'] + ']]\n'
            wikiText += '|-\n'
        if wellPrimaryData['FARM_NAME'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['FARM_NAME'] + ': ' + wellPrimaryData['FARM_NAME'] + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['FIRST_PERMIT_ISSUED_DATE'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['FIRST_PERMIT_ISSUED_DATE'] + ': ' + str(wellPrimaryData['FIRST_PERMIT_ISSUED_DATE']) + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['LAST_PERMIT_ISSUED_DATE'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LAST_PERMIT_ISSUED_DATE'] + ': ' + str(wellPrimaryData['LAST_PERMIT_ISSUED_DATE']) + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['SPUD_DATE'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['SPUD_DATE'] + ': ' + str(wellPrimaryData['SPUD_DATE']) + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['UNCONVENTIONAL'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['UNCONVENTIONAL'] + ': ' + ('Yes' if wellPrimaryData['UNCONVENTIONAL'] is 'Y' else 'No') + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['HORIZONTAL_WELL'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['HORIZONTAL_WELL'] + ': ' + ('Yes' if wellPrimaryData['HORIZONTAL_WELL'] is 'Y' else 'No') + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['WELL_STATUS'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['WELL_STATUS'] + ': ' + ('Yes' if wellPrimaryData['WELL_STATUS'] == 'Active' else 'No') + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['VIOLATION_COUNT'] != 'NULL':
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['VIOLATION_COUNT'] + ': ' + str(wellPrimaryData['VIOLATION_COUNT']) + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['LATITUDE_DECIMAL'] is not None:
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LATITUDE_DECIMAL'] + ': ' + str(wellPrimaryData['LATITUDE_DECIMAL']) + '\n'
            wikiText += '|-\n'
        if wellPrimaryData['LONGITUDE_DECIMAL'] is not None:
            wikiText += '| ' + WellDataConfig.wellDetailsDataProperColumnNames['LONGITUDE_DECIMAL'] + ': ' + str(wellPrimaryData['LONGITUDE_DECIMAL']) + '\n'
            wikiText += '|-\n'
        wikiText += '|}'

        templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.wellID+'_Details_Template.txt', 'Template:'+self.wellID+'-Details', wikiText)
        PageUploadTableUpdater.addEntry(self.wellID, templateFile)

    def buildTableTemplates(self):
        self.buildSecondaryTemplates()
        self.buildPrimaryTemplates()
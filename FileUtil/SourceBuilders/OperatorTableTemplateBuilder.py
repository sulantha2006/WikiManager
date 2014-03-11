__author__ = 'sulantha'
from DBUtil.OperatorDataAccessor import OperatorDataAccessor
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater
from Config import OperatorDataConfig, FileConfig
from FileUtil.FileHandler import FileHandler


class OperatorTableTemplateBuilder:
    operatorDataAccessor = None
    fileHandler = None
    operatorID = None

    def __init__(self, operatorID):
        self.operatorDataAccessor = OperatorDataAccessor(operatorID)
        self.fileHandler = FileHandler()
        self.operatorID = operatorID

    def buildSecondaryTemplates(self):
        def addUnsortColumn(dataType, columnName):
            if OperatorDataConfig.operatorDataSelectiveSortingEnabled:
                if columnName in OperatorDataConfig.operatorDataSortableColumns[dataType]:
                    return ''
                else:
                    return 'class="unsortable"'
            else:
                return ''

        operatorSecondaryData = self.operatorDataAccessor.getOperatorSecondaryData()
        for dataType in operatorSecondaryData:
            wikiText = '{| class="wikitable sortable" width="95%"\n'
            try:
                numberOfColumns = len(OperatorDataConfig.operatorDataProperColumnNames[dataType])
            except IndexError:
                numberOfColumns = 0
            wikiText += '!colspan="' + str(numberOfColumns) + '"|' + OperatorDataConfig.operatorDataProperFinalTableTopics[dataType] + '\n|-\n'
            for column in OperatorDataConfig.operatorDataProperColumnNames[dataType]:
                wikiText += '!scope="col" ' + addUnsortColumn(dataType, column) + '| '+column + '\n'

            if dataType == 'wells':
                for row in operatorSecondaryData[dataType]:
                    wikiText += '|-\n'

                    wikiText += '| ' + str('[[' + row + ']]') + '\n'

                    if operatorSecondaryData[dataType][row]['WELL_COUNTY'] != 'NULL':
                        wikiText += '| ' + str('[[' + operatorSecondaryData[dataType][row]['COUNTY_FULL_NAME'] + ']]') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['WELL_MUNICIPALITY'] != 'NULL':
                        wikiText += '| ' + str('[[' + operatorSecondaryData[dataType][row]['MUNICIPALITY_FULL_NAME'] + ']]') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['FIRST_PERMIT_ISSUED_DATE'] != 'NULL':
                        wikiText += '| ' + str(operatorSecondaryData[dataType][row]['FIRST_PERMIT_ISSUED_DATE']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['SPUD_DATE'] != 'NULL':
                        wikiText += '| ' + str(operatorSecondaryData[dataType][row]['SPUD_DATE']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['UNCONVENTIONAL'] != 'NULL':
                        wikiText += '| ' + ('Yes' if operatorSecondaryData[dataType][row]['UNCONVENTIONAL'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['HORIZONTAL_WELL'] != 'NULL':
                        wikiText += '| ' + ('Yes' if operatorSecondaryData[dataType][row]['HORIZONTAL_WELL'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['WELL_STATUS'] != 'NULL':
                        wikiText += '| ' + ('Yes' if operatorSecondaryData[dataType][row]['WELL_STATUS'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if operatorSecondaryData[dataType][row]['VIOLATION_COUNT'] != 'NULL':
                        wikiText += '| ' + str(operatorSecondaryData[dataType][row]['VIOLATION_COUNT']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    wikiText += '|-\n'
            else:
                for row in operatorSecondaryData[dataType]:
                    wikiText += '|-\n'
                    for item in row:
                        wikiText += '| ' + str(item) + '\n'
                    wikiText += '|-\n'
            wikiText += '|}'
            templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.operatorID+'_'+dataType+'_Template.txt', 'Template:'+self.operatorID+'-'+dataType, wikiText)
            PageUploadTableUpdater.addEntry(self.operatorID, templateFile)

    def buildPrimaryTemplates(self):
        operatorPrimaryData = self.operatorDataAccessor.getOperatorPrimaryData()
        numberOfRows = len(operatorPrimaryData)
        wikiText = '{| class="wikitable" width="95%"\n'
        wikiText += '!colspan="2"| Operator Details \n'
        wikiText += '|-\n'
        wikiText += '| Operator Name: ' + self.operatorID + '\n'
        if operatorPrimaryData['OPERATOR_ADDRESS'] is not None and operatorPrimaryData['OPERATOR_CITY'] is not None and operatorPrimaryData['OPERATOR_STATE'] is not None and operatorPrimaryData['OPERATOR_ZIP'] is not None:
            wikiText += '| style="width: 50%; height=100%; align=center" rowspan="' + str(numberOfRows+1) + '" | {{#display_map: ' + str(operatorPrimaryData['OPERATOR_ADDRESS'])+', ' + str(operatorPrimaryData['OPERATOR_CITY'])+', ' + str(operatorPrimaryData['OPERATOR_STATE'])+', ' + str(operatorPrimaryData['OPERATOR_ZIP']) + ' | width=100% | height=100% }} \n'
            wikiText += '|-\n'
        else:
            wikiText += '|-\n'
        if operatorPrimaryData['OPERATOR_OGO'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['OPERATOR_OGO'] + ': ' + operatorPrimaryData['OPERATOR_OGO'] + '\n'
            wikiText += '|-\n'
        if operatorPrimaryData['OPERATOR_ADDRESS'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['OPERATOR_ADDRESS'] + ': ' + operatorPrimaryData['OPERATOR_ADDRESS'] + '\n'
            wikiText += '|-\n'
        if operatorPrimaryData['OPERATOR_CITY'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['OPERATOR_CITY'] + ': ' + operatorPrimaryData['OPERATOR_CITY'] + '\n'
            wikiText += '|-\n'
        if operatorPrimaryData['OPERATOR_STATE'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['OPERATOR_STATE'] + ': ' + operatorPrimaryData['OPERATOR_STATE'] + '\n'
            wikiText += '|-\n'
        if operatorPrimaryData['OPERATOR_ZIP'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['OPERATOR_ZIP'] + ': ' + operatorPrimaryData['OPERATOR_ZIP'] + '\n'
            wikiText += '|-\n'
        if operatorPrimaryData['UNCONVENTIONAL'] != 'NULL':
            wikiText += '| ' + OperatorDataConfig.operatorDetailsDataProperColumnNames['UNCONVENTIONAL'] + ': ' + ('Yes' if operatorPrimaryData['UNCONVENTIONAL'] is 'Y' else 'No') + '\n'
            wikiText += '|-\n'
        wikiText += '|}'

        templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.operatorID+'_Details_Template.txt', 'Template:'+self.operatorID+'-Details', wikiText)
        PageUploadTableUpdater.addEntry(self.operatorID, templateFile)

    def buildTableTemplates(self):
        self.buildSecondaryTemplates()
        self.buildPrimaryTemplates()
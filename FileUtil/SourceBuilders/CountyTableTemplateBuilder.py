__author__ = 'sulantha'

from FileUtil.FileHandler import FileHandler
from DBUtil.CountyDataAccessor import CountyDataAccessor
from Config import CountyDataConfig, FileConfig
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class CountyTableTemplateBuilder:
    CountyDataAccessor = None
    fileHandler = None
    conID = None

    def __init__(self, conID):
        self.CountyDataAccessor = CountyDataAccessor(conID)
        self.fileHandler = FileHandler()
        self.conID = conID

    def buildSecondaryTemplates(self):
        def addUnsortColumn(dataType, columnName):
            if CountyDataConfig.countyDataSelectiveSortingEnabled:
                if columnName in CountyDataConfig.countyDataSortableColumns[dataType]:
                    return ''
                else:
                    return 'class="unsortable"'
            else:
                return ''

        CountySecondaryData = self.CountyDataAccessor.getConSecondaryData()
        for dataType in CountySecondaryData:
            wikiText = '{| class="wikitable sortable" width="95%"\n'
            try:
                numberOfColumns = len(CountyDataConfig.conDataProperColumnNames)
            except IndexError:
                numberOfColumns = 0
            wikiText += '!colspan="' + str(numberOfColumns) + '"|' + CountyDataConfig.conDataProperFinalTableTopics[dataType] + '\n|-\n'
            for column in CountyDataConfig.conDataProperColumnNames[dataType]:
                wikiText += '!scope="col" ' + addUnsortColumn(dataType, column) + '| '+column + '\n'

            if dataType == 'wells':
                for row in CountySecondaryData[dataType]:
                    wikiText += '|-\n'

                    wikiText += '| ' + str('[[' + row + ']]') + '\n'

                    if CountySecondaryData[dataType][row]['WELL_MUNICIPALITY'] != 'NULL':
                        wikiText += '| ' + str('[[' + CountySecondaryData[dataType][row]['MUNICIPALITY_FULL_NAME'] + ']]') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['OPERATOR_NAME'] != 'NULL':
                        wikiText += '| ' + str('[[' + CountySecondaryData[dataType][row]['OPERATOR_NAME'] + ']]') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['FIRST_PERMIT_ISSUED_DATE'] != 'NULL':
                        wikiText += '| ' + str(CountySecondaryData[dataType][row]['FIRST_PERMIT_ISSUED_DATE']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['SPUD_DATE'] != 'NULL':
                        wikiText += '| ' + str(CountySecondaryData[dataType][row]['SPUD_DATE']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['UNCONVENTIONAL'] != 'NULL':
                        wikiText += '| ' + ('Yes' if CountySecondaryData[dataType][row]['UNCONVENTIONAL'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['HORIZONTAL_WELL'] != 'NULL':
                        wikiText += '| ' + ('Yes' if CountySecondaryData[dataType][row]['HORIZONTAL_WELL'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['WELL_STATUS'] != 'NULL':
                        wikiText += '| ' + ('Yes' if CountySecondaryData[dataType][row]['WELL_STATUS'] is 'Y' else 'No') + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    if CountySecondaryData[dataType][row]['VIOLATION_COUNT'] != 'NULL':
                        wikiText += '| ' + str(CountySecondaryData[dataType][row]['VIOLATION_COUNT']) + '\n'
                    else:
                        wikiText += '| ' + '\n'

                    wikiText += '|-\n'
            wikiText += '|}'
            templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.conID+'_'+dataType+'_Template.txt', 'Template:'+self.conID+'-'+dataType, wikiText)
            PageUploadTableUpdater.addEntry(self.conID, templateFile)

    def buildPrimaryTemplates(self):
        pass

    def buildTableTemplates(self):
        self.buildSecondaryTemplates()
        self.buildPrimaryTemplates()
__author__ = 'sulantha'

from FileUtil.FileHandler import FileHandler
from DBUtil.MunicipalityDataAccessor import MunicipalityDataAccessor
from Config import MunicipalityDataConfig, FileConfig
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class MunicipalityTableTemplateBuilder:
    municipalityDataAccessor = None
    fileHandler = None
    munID = None

    def __init__(self, munID):
        self.municipalityDataAccessor = MunicipalityDataAccessor(munID)
        self.fileHandler = FileHandler()
        self.munID = munID

    def buildSecondaryTemplates(self):
        def addUnsortColumn(dataType, columnName):
            if MunicipalityDataConfig.municipalityDataSelectiveSortingEnabled:
                if columnName in MunicipalityDataConfig.municipalityDataSortableColumns[dataType]:
                    return ''
                else:
                    return 'class="unsortable"'
            else:
                return ''

        municipalitySecondaryData = self.municipalityDataAccessor.getMunSecondaryData()
        for dataType in municipalitySecondaryData:
            wikiText = '{| class="wikitable sortable" width="95%"\n'
            try:
                numberOfColumns = len(municipalitySecondaryData[dataType][0])
            except IndexError:
                numberOfColumns = 0
            wikiText += '!colspan="' + str(numberOfColumns) + '"|' + MunicipalityDataConfig.munDataProperFinalTableTopics[dataType] + '\n|-\n'
            for column in MunicipalityDataConfig.munDataProperColumnNames[dataType]:
                wikiText += '!scope="col" ' + addUnsortColumn(dataType, column) + '| '+column + '\n'

            for row in municipalitySecondaryData[dataType]:
                wikiText += '|-\n'
                item_count = 0
                for item in row:
                    if item =='NULL':
                        item = ''
                    if item_count == 0:
                        item = '[[' + str(item) + ']]'
                    wikiText += '| ' + str(item) + '\n'
                    item_count += 1
                wikiText += '|-\n'
            wikiText += '|}'
            templateFile = self.fileHandler.writeWikiSourceFile(FileConfig.templateFilePath, self.munID+'_'+dataType+'_Template.txt', 'Template:'+self.munID+'-'+dataType, wikiText)
            PageUploadTableUpdater.addEntry(self.munID, templateFile)

    def buildPrimaryTemplates(self):
        pass

    def buildTableTemplates(self):
        self.buildSecondaryTemplates()
        self.buildPrimaryTemplates()
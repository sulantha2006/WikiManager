__author__ = 'sulantha'
from Config import FileConfig
from FileUtil.FileHandler import FileHandler
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class WellSourceBuilder:
    wellID = None
    fileHandler = None

    def __init__(self, wellID):
        self.wellID = wellID
        self.fileHandler = FileHandler()

    def buildMainSource(self):
        source = '== Well Details ==\n'
        source += '{{' + self.wellID + '-Details}}\n'
        source += '__TOC__\n'
        source += '== Well Inspection Data ==\n'
        source += '{{' + self.wellID + '-inspection}}\n'
        source += '== Production Data ==\n'
        source += '{{' + self.wellID + '-production}}\n'
        source += '== Waste Data ==\n'
        source += '{{' + self.wellID + '-waste}}\n'
        source += '__NOEDITSECTION__\n'
        sourceFile = self.fileHandler.writeWikiSourceFile(FileConfig.mainSourcePath, self.wellID+'_main.txt', self.wellID, source)
        PageUploadTableUpdater.addEntry(self.wellID, sourceFile)
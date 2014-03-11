__author__ = 'sulantha'
from Config import FileConfig
from FileUtil.FileHandler import FileHandler
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class CountySourceBuilder:
    munID = None
    fileHandler = None

    def __init__(self, munID):
        self.munID = munID
        self.fileHandler = FileHandler()

    def buildMainSource(self):
        source = '== Municipality Details ==\n'
        #source += '{{' + self.munID + '-Details}}\n'
        source += '__TOC__\n'
        source += '== Oil and Gas Activity ==\n'
        source += '{{' + self.munID + '-wells}}\n'
        source += '__NOEDITSECTION__\n'
        sourceFile = self.fileHandler.writeWikiSourceFile(FileConfig.mainSourcePath, self.munID+'_main.txt', self.munID, source)
        PageUploadTableUpdater.addEntry(self.munID, sourceFile)

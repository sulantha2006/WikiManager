__author__ = 'sulantha'
from Config import FileConfig
from FileUtil.FileHandler import FileHandler
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class CountySourceBuilder:
    conID = None
    fileHandler = None

    def __init__(self, conID):
        self.conID = conID
        self.fileHandler = FileHandler()

    def buildMainSource(self):
        source = '== County Details ==\n'
        #source += '{{' + self.conID + '-Details}}\n'
        source += '__TOC__\n'
        source += '== Oil and Gas Activity ==\n'
        source += '{{' + self.conID + '-wells}}\n'
        source += '__NOEDITSECTION__\n'
        sourceFile = self.fileHandler.writeWikiSourceFile(FileConfig.mainSourcePath, self.conID+'_main.txt', self.conID, source)
        PageUploadTableUpdater.addEntry(self.conID, sourceFile)

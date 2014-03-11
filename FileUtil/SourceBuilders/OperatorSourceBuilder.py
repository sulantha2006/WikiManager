__author__ = 'sulantha'
from Config import FileConfig
from FileUtil.FileHandler import FileHandler
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater


class OperatorSourceBuilder:
    operatorID = None
    fileHandler = None

    def __init__(self, operatorID):
        self.operatorID = operatorID
        self.fileHandler = FileHandler()

    def buildMainSource(self):
        source = '== Operator Details ==\n'
        source += '{{' + self.operatorID + '-Details}}\n'
        source += '__TOC__\n'
        source += '== Operator Well Data ==\n'
        source += '{{' + self.operatorID + '-wells}}\n'
        source += '__NOEDITSECTION__\n'
        sourceFile = self.fileHandler.writeWikiSourceFile(FileConfig.mainSourcePath, self.operatorID+'_main.txt', self.operatorID, source)
        PageUploadTableUpdater.addEntry(self.operatorID, sourceFile)
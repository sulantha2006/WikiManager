__author__ = 'sulantha'


class FileHandler:
    file = 0

    def __init__(self):
        self.file = 0

    def getFileContent(self, filePath):
        self.file = open(filePath, 'r').read()
        fileContents = self.file.split('--ENDTITLE--')
        return [str.strip(x) for x in fileContents]
__author__ = 'sulantha'


class FileHandler:
    file = 0

    def __init__(self):
        self.file = 0

    def getWikiSourceFileContent(self, filePath):
        self.file = open(filePath, 'r').read()
        fileContents = self.file.split('--ENDTITLE--')
        return [str.strip(x) for x in fileContents]

    def writeWikiSourceFile(self, filePath, fileName, contentTitle, content):
        f = open(filePath+fileName, 'w')
        f.write(contentTitle)
        f.write('\n--ENDTITLE--\n')
        f.write(content)
        f.close()
        return filePath+fileName
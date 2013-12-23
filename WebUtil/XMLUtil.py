__author__ = 'sulantha'
import xml.etree.ElementTree as ET


class XMLUtil:
    root = 0

    def __init__(self, xmlResponse):
        self.root = ET.parse(xmlResponse).getroot()

    def getLoginToken(self):
        return self.root.find('login').attrib['token']

    def getSessionID(self):
        return self.root.find('login').attrib['sessionid']

    def getEditToken(self):
        try:
            return self.root.find('query')[1][0].attrib['edittoken']
        except IndexError:
            return self.root.find('query')[0][0].attrib['edittoken']


    def getActionSuccess(self):
        if (self.root[0].attrib['result']) == 'Success':
            return True
        else:
            return self.root[0].attrib['info'], self.root[0].attrib['code']

    def printResponse(self):
        try:
            return self.root.find('query')[1][0].attrib['edittoken']
        except IndexError:
            return self.root.find('query')[0][0].attrib['edittoken']

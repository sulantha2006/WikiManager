__author__ = 'sulantha'
from Config import ManagerConfig
from WebUtil.Client import Client
from FileUtil.FileHandler import FileHandler

fileHandler = FileHandler()
[pageTitle, pageBody] = fileHandler.getFileContent('/home/sulantha/PycharmProjects/WikiManager/TestSources/InfoBoxTest.txt')

loginSuccess = False
editSuccess = False

webBot = Client()
loginSuccess = webBot.login()

if loginSuccess:
    editSuccess = webBot.editPage(pageTitle, pageBody)
    if editSuccess:
        print 'Edit/Create Page Successful. New Page can be found at : '+pageTitle
    else:
        print 'Edit operation failed. Status : '+editSuccess
else:
    print 'Login Error. Status : '+loginSuccess



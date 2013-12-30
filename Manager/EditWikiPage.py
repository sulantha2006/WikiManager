__author__ = 'sulantha'
from Config import ManagerConfig
from WebUtil.Client import Client
from FileUtil.FileHandler import FileHandler

fileHandler = FileHandler()
[pageTitle, pageBody] = fileHandler.getWikiSourceFileContent('/home/sulantha/PycharmProjects/WikiManager/TestSources/125-23023_waste_Template.txt')

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



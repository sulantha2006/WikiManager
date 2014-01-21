__author__ = 'sulantha'
from WebUtil.Client import Client
from FileUtil.FileHandler import FileHandler
from DBUtil.PageUploadTableAccessor import PageUploadTableAccessor
from DBUtil.PageUploadTableUpdater import PageUploadTableUpdater

fileHandler = FileHandler()
loginSuccess = False
editSuccess = False
webBot = Client()
loginSuccess = webBot.login()

if loginSuccess:
    filesToBeUploaded = PageUploadTableAccessor.getUploadFiles()
    count = 1
    total = len(filesToBeUploaded)
    for (fileId, textFile) in filesToBeUploaded:
        print 'Processing ' + str(count) + '/' + str(total) + ':'
        [pageTitle, pageBody] = fileHandler.getWikiSourceFileContent(textFile)
        editSuccess = webBot.editPage(pageTitle, pageBody)
        if editSuccess:
            PageUploadTableUpdater.setUploadSuccess(fileId)
            print 'Edit/Create Page Successful. New Page can be found at : '+pageTitle
        else:
            print 'Edit operation failed. Status : '+editSuccess
        count += 1
else:
    print 'Login Error. Status : '+loginSuccess



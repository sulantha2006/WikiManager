__author__ = 'sulantha'
import urllib
import urllib2
from XMLUtil import XMLUtil
import Config.WebConfig as webConfig


class Client:
    sessionID = 0

    def __init__(self):
        self.sessionID = 0

    def login(self):
        loginVars = {'action': 'login', 'lgname': webConfig.editorRobotUser, 'lgpassword': webConfig.editorRobotPass,
                     'format': 'xml'}
        data = urllib.urlencode(loginVars)
        req = urllib2.Request(webConfig.wikiapi, data)
        response = urllib2.urlopen(req)
        xmlUtil = XMLUtil(response)
        loginVars['lgtoken'] = xmlUtil.getLoginToken()
        data = urllib.urlencode(loginVars)
        req = urllib2.Request(webConfig.wikiapi, data)
        self.sessionID = xmlUtil.getSessionID()
        req.add_header('Cookie', webConfig.sessionName + '=' + self.sessionID)
        response = urllib2.urlopen(req)
        xmlUtil = XMLUtil(response)
        return xmlUtil.getActionSuccess()

    def editPage(self, pageTitle, pageBody):
        safePageTitle = str.replace(pageTitle, ' ', '_')
        editVars = {'action': 'query', 'prop': 'info', 'intoken': 'edit', 'titles': safePageTitle, 'format': 'xml'}
        data = urllib.urlencode(editVars)
        req = urllib2.Request(webConfig.wikiapi, data)
        req.add_header('Cookie', webConfig.sessionName + '=' + self.sessionID)
        response = urllib2.urlopen(req)
        xmlUtil = XMLUtil(response)
        editToken = xmlUtil.getEditToken()

        submitVars = {'action': 'edit', 'title': safePageTitle, 'text': pageBody, 'contentformat': 'text/x-wiki',
                      'contentmodel': 'wikitext', 'bot': '1', 'token': editToken, 'format': 'xml'}
        data = urllib.urlencode(submitVars)
        req = urllib2.Request(webConfig.wikiapi, data)
        req.add_header('Cookie', webConfig.sessionName + '=' + self.sessionID)
        response = urllib2.urlopen(req)
        xmlUtil = XMLUtil(response)
        return xmlUtil.getActionSuccess()



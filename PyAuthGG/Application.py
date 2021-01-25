import PyAuthGG

import requests
import json
import bs4

import subprocess
import getpass

class Application():
    def __init__(self, API, AID, SECRET):
        self.API = API
        self.AID = AID
        self.SECRET = SECRET
        self.URL = "https://api.auth.gg/v1/"
        self.HEADERS = PyAuthGG.HEADERS

    def Status(self):
        r = requests.get("https://authgg.statuspage.io/")
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        SpanElements = soup.find_all("span", class_="component-status")
        StatusList = []
        for x in SpanElements:
            StatusList.append(x.text.replace("\n", "").replace(" ", ""))

        return {"Backend/API" : StatusList[0], "Frontend" : StatusList[1], "S3 Storage" : StatusList[2]}

    def GetHWID(self):
        return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

    def Info(self):
        DATA = {"type" : "info", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET}
        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def Login(self, USER : str, PASS : str):
        HWID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        DATA = {"type" : "login", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "username" : USER, "password" : PASS, "hwid" : HWID}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def Register(self, LICENSE : str, USER : str, EMAIL : str, PASS : str):
        HWID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        DATA = {"type" : "register", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "license" : LICENSE, "username" : USER, "email" : EMAIL, "password" : PASS, "hwid" : HWID}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def Extend(self, LICENSE : str, USER : str, PASS : str):
        DATA = {"type" : "extend", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "username" : USER, "password" : PASS, "license" : LICENSE}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def ForgotPassword(self, USER : str):
        DATA = {"type" : "forgotpw", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "username" : USER}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def ChangePassword(self, USER : str, PASS : str, NEWPASS : str):
        DATA = {"type" : "changepw", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "username" : USER, "password" : PASS, "newpassword" : NEWPASS}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

    def Log(self, USER : str, ACTION : str):
        DATA = {"type" : "log", "aid" : self.AID, "apikey" : self.API, "secret" : self.SECRET, "pcuser" : getpass.getuser(), "username" : USER, "action" : ACTION}

        r = requests.post(self.URL, data=DATA, headers=self.HEADERS).json()
        return r

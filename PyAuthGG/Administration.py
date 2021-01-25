import PyAuthGG

import requests
import json
import bs4

class Administration():
    def __init__(self, API):
        self.API = API
        self.URL = "https://developers.auth.gg/"
        self.HEADERS = PyAuthGG.HEADERS

        r = requests.post(self.URL + f"USERS?type=count&authorization={self.API}").json()

        if r['status'] == "failed":
            if ['info'] == "No application found":
                raise PyAuthGG.Exceptions.ApplicationNotFound

    def Status(self):
        r = requests.get("https://authgg.statuspage.io/")
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        SpanElements = soup.find_all("span", class_="component-status")
        StatusList = []
        for x in SpanElements:
            StatusList.append(x.text.replace("\n", "").replace(" ", ""))

        return {"Backend/API" : StatusList[0], "Frontend" : StatusList[1], "S3 Storage" : StatusList[2]}

    def FetchUser(self, USER : str):
        r = requests.get(self.URL + f"USERS?type=fetch&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

    def FetchUsedLicenses(self, USER : str):
        r = requests.get(self.URL + f"LICENSES?type=fetchall&authorization={self.API}", headers=self.HEADERS).json()

        UsedLicenses = {"Licenses" : []}

        for License in r.items():
            if License[1]['used'] == "1" and License[1]['used_by'] == USER:
                UsedLicenses['Licenses'].append(License[1])

        return UsedLicenses

    def FetchUsers(self):
        r = requests.get(self.URL + f"USERS?type=fetchall&authorization={self.API}", headers=self.HEADERS).json()
        return r

    def FetchUserCount(self):
        r = requests.get(self.URL + f"USERS?type=count&authorization={self.API}", headers=self.HEADERS).json()
        return r #int(r['value'])

    def DeleteUser(self, USER : str):
        r = requests.get(self.URL + f"USERS?type=delete&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

    def ChangeVariable(self, USER : str, VARIABLE : str):
        r = requests.get(self.URL + f"USERS?type=editvar&authorization={self.API}&user={USER}&value={VARIABLE}", headers=self.HEADERS).json()
        return r

    def ChangeRank(self, USER : str, RANK : int):
        r = requests.get(self.URL + f"USERS?type=editrank&authorization={self.API}&user={USER}&rank={str(RANK)}", headers=self.HEADERS).json()
        return r

    def ChangePassword(self, USER : str, PASSWORD : str):
        r = requests.get(self.URL + f"USERS?type=changepw&authorization={self.API}&user={USER}&password={PASSWORD}", headers=self.HEADERS).json()
        return r

    def FetchLicense(self, LICENSE : str):
        r = requests.get(self.URL + f"LICENSES?type=fetch&authorization={self.API}&license={LICENSE}", headers=self.HEADERS).json()
        return r

    def FetchLicenses(self):
        r = requests.get(self.URL + f"LICENSES?type=fetchall&authorization={self.API}", headers=self.HEADERS).json()
        return r

    def FetchLicenseCount(self):
        r = requests.get(self.URL + f"LICENSES?type=count&authorization={self.API}", headers=self.HEADERS).json()
        return r #int(r['value'])

    def DeleteLicense(self, LICENSE : str):
        r = requests.get(self.URL + f"LICENSES?type=delete&authorization={self.API}&license={LICENSE}", headers=self.HEADERS).json()
        return r

    def UseLicense(self, LICENSE : str):
        r = requests.get(self.URL + f"LICENSES?type=use&authorization={self.API}&license={LICENSE}", headers=self.HEADERS).json()
        return r

    def UnuseLicense(self, LICENSE : str):
        r = requests.get(self.URL + f"LICENSES?type=unuse&authorization={self.API}&license={LICENSE}", headers=self.HEADERS).json()
        return r

    # 9998 days is max
    def GenerateLicense(self, AMOUNT : int, DAYS : int, LEVEL : int, FORMAT : int, PREFIX : str = "", LENGTH : int = 0):
        r = requests.get(self.URL + f"LICENSES?type=generate&authorization={self.API}&amount={str(AMOUNT)}&days={str(DAYS)}&level={str(LEVEL)}&format={str(FORMAT)}&prefix={str(PREFIX)}&length={str(LENGTH)}", headers=self.HEADERS).json()
        return r #[x for x in r.items()]

    def FetchHWID(self, USER : str):
        r = requests.get(self.URL + f"HWID?type=fetch&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

    def ResetHWID(self, USER : str):
        r = requests.get(self.URL + f"HWID?type=reset&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

    def SetHWID(self, USER : str, HWID : str):
        r = requests.get(self.URL + f"HWID?type=set&authorization={self.API}&user={USER}&hwid={HWID}", headers=self.HEADERS).json()
        return r

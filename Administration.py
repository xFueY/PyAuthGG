import PyAuthGG

import requests
import json

class Administration():
    def __init__(self, API):
        self.API = API
        self.URL = "https://developers.auth.gg/"
        self.HEADERS = PyAuthGG.HEADERS

        r = requests.post(self.URL + f"USERS?type=count&authorization={self.API}").json()

        if r['status'] == "failed":
            if ['info'] == "No application found":
                raise PyAuthGG.Exceptions.ApplicationNotFound

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

    def UnuseLicense(self, LICENSE : str):
        r = requests.get(self.URL + f"LICENSES?type=unuse&authorization={self.API}&license={LICENSE}", headers=self.HEADERS).json()
        return r

    # 9998 days is max
    def GenerateLicense(self, AMOUNT : int, DAYS : int, LEVEL : int, FORMAT : int, PREFIX : str):
        r = requests.get(self.URL + f"LICENSES?type=generate&authorization={self.API}&amount={str(AMOUNT)}&days={str(DAYS)}&level={str(LEVEL)}&format={str(FORMAT)}&prefix={str(PREFIX)}", headers=self.HEADERS).json()
        return r #[x for x in r.items()]

    def FetchHWID(self, USER : str):
        r = requests.get(self.URL + f"HWID?type=fetch&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

    def ResetHWID(self, USER : str):
        r = requests.get(self.URL + f"HWID?type=reset&authorization={self.API}&user={USER}", headers=self.HEADERS).json()
        return r

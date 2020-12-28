Simple Python Auth.GG Package

* Simple
* Lightweight
* User Friendly
<br>
All functions will return the response directly from https://auth.gg/ without modifying them.
This allows you to do just what you want with the information instead of being restricted to what this package does and can do.
<br><br>
Donate: 15EAMkhNpxa6m2AYemfiZcjmx6TFaJzUGb
<br><br>

Application API Example:
```python
import PyAuthGG

App = PyAuthGG.Application("API Key", "AID", "Application Secret")
print(App.Info())
```

Admin API Example:
```python
import PyAuthGG

Admin = PyAuthGG.Administration.Administration("Admin API Key")
print(Admin.FetchUser("xFueY"))
```

<br>

To Do:
- [x] Application API Support
- [x] Admin API Support
- [ ] In Depth Documentation


Application API Functions Available:<br>
In Depth Documentation: SoonTM
```python

App = PyAuthGG.Application("API", "AID", "SECRET")

App.Info()

App.Login(Username, Password)

App.Register(License, Username, Email, Password)

App.Extend(License, Username, Password)

App.ForgotPassword(Username)

App.ChangePassword(Username, Password, NewPassword)

App.Log(Username, Action)
```

Admin API Functions Available:<br>
In Depth Documentation: SoonTM
```python
Admin = PyAuthGG.Administration("API")

Admin.FetchUser(Username)

Admin.FetchUsedLicenses(Username) # Custom Function That Returns All Licenses Used By A User

Admin.FetchUsers()

Admin.FetchUserCount()

Admin.DeleteUser(Username)

Admin.ChangeVariable(Username, Variable)

Admin.ChangePassword(Username, Password)

Admin.FetchLicense(License)

Admin.FetchLicenses()

Admin.FetchLicenseCount()

Admin.DeleteLicense()

Admin.UnuseLicense()

Admin.GenerateLicense(Amount, Days, Level, Format, Prefix)

Admin.FetchHWID(Username)

Admin.ResetHWID(Username)
```

Simple Python Auth.GG Package

* Simple
* Lightweight
* User Friendly
<br>
All functions will return the response directly from https://auth.gg/ without modifying them.
This allows you to do just what you want with the information instead of being restricted to what this package does and can do.

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


To Do:
- [x] Application API Support
- [x] Admin API Support
- [ ] In Depth Documentation


Application API Functions Available:<br>
In Depth Documentation: SoonTM
```python

Info()

Login(Username, Password)

Register(License, Username, Email, Password)

Extend(License, Username, Password)

ForgotPassword(Username)

ChangePassword(Username, Password, NewPassword)

Log(Username, Action)
```

Admin API Functions Available:<br>
In Depth Documentation: SoonTM
```python
FetchUser(Username)

FetchUsedLicenses(Username) # Custom Function That Returns All Licenses Used By A User

FetchUsers()

FetchUserCount()

DeleteUser(Username)

ChangeVariable(Username, Variable)

ChangePassword(Username, Password)

FetchLicense(License)

FetchLicenses()

FetchLicenseCount()

DeleteLicense()

UnuseLicense()

GenerateLicense(Amount, Days, Level, Format, Prefix)

FetchHWID(Username)

ResetHWID(Username)
```

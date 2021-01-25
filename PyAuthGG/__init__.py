from .Administration import *
from .Application import *
from .Exceptions import *

Version = "1.0.6"
Author = "xFueY"
Source = "https://github.com/xFueY/PyAuthGG"
Changelog = """Version 1.0.6 - 30th December 2020
- Added Application.Status()
- Added Administration.Status()
- Added Administration.UseLicense()
- Added Support For License Format 4 {PREFIX}-{LENGTH}"""

HEADERS = {"Content-Type" : "application/x-www-form-urlencoded", "User-Agent" : f"PyAuthGG {Version}"}

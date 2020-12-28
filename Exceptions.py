class ApplicationNotFound(Exception):
    def __init__(self):
        raise Exception("Application Not Found")

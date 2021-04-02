from .errCode import codeDict


class HiKException(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return codeDict.get(self.code)

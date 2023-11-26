from src.utils.general.time import timeStamp
from src.exception.default_exception import DefaultException

class DefaultException(Exception):
    def __init__(self, data, msn, status):
        self.data = data
        self.statusMessage = msn
        self.statusCode = status
        self.time = timeStamp()
        super().__init__(self.statusMessage)
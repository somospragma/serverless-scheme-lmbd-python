from src.patterns.strategy.bodyRequest.strategyManager.strategy import Strategy
import json
import base64

class Get(Strategy):

    __name = "get"

    def __init__(self, data):
        self.__data = data

    def getName(self):
        return self.__name

    def getBody(self):
        return self.__data.get('queryStringParameters', None)
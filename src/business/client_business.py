from src.patterns.strategy.bodyRequest.context.context import Context
from src.validators.json_schema_validator import ValidateRequest
from src.exception.default_exception import DefaultException
import requests
import os

class Clients:

    def __init__(self, event) -> None:
        self.__typeRequest = os.getenv('typeRequest')
        self.__event = event
        self.__context = Context(self.__typeRequest, self.__event)
        self.setContextPetition()

    def setContextPetition(self) -> None:
        self.__context.setStrategy()

    def geBody(self):
        self.__context.chooseStrategy()
        return self.__context.getAction()

    def validateBodyRequest(self, data, schema) -> None:
        validetor = ValidateRequest()
        validetor.json_schema_validator(data, schema)

    def getCountries(self):
        try:
            url = "https://restcountries.com/v3.1/all"

            response = requests.get(url)
            response.raise_for_status()  # Lanzará una excepción si la solicitud no fue exitosa

            result_list = [
                {"name": obj["name"], "region": obj["region"]}
                for obj in response.json()
            ]

            return result_list

        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 404:
                raise DefaultException(None, "NOT_FOUND_REQUEST", 404)
            else:
                raise DefaultException(None, "INTERNAL_ERROR_REQUEST", 501)

        except requests.exceptions.RequestException as req_err:
            raise DefaultException(None, "INTERNAL_ERROR_REQUEST", 500)

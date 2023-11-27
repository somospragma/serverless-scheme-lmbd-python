from src.business.response_business import ResponseBusiness
from src.business.client_business import Clients
from src.validators.json_schema.example_validator import TestRequest
from src.utils.general.time import timeStamp

def app(event, context):
    try:
        client = Clients(event)
        getBody = client.getBody()

        client.validateBodyRequest(getBody, TestRequest().get_schema())

        countries = client.getCountries()

        response = ResponseBusiness(200, "OK", countries).getResponse()

        return response
    except Exception as error:
        error_data = {
            'data': error.data if hasattr(error, 'data') else None,
            'statusCode': error.statusCode if hasattr(error, 'statusCode') else 500,
            'statusMessage': error.statusMessage if hasattr(error, 'statusMessage') else "Internal server error",
            'time': error.time if hasattr(error, 'time') else timeStamp()
        }

        response = ResponseBusiness(error_data['statusCode'], error_data['statusMessage'], error_data['data']).getResponse()

        return response




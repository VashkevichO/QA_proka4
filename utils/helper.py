import json
import allure
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    def attach_response_code(self, response):
        response = json.dumps(response)
        allure.attach(body=str(response), name="API Response", attachment_type=AttachmentType.TEXT)

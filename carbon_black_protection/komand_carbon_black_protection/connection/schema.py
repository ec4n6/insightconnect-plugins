# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API key",
      "order": 2
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "True for Certificate Validation",
      "default": true,
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Root Host URL",
      "order": 1
    }
  },
  "required": [
    "api_key",
    "ssl_verify",
    "url"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

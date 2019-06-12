# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    USERNAME = "username"
    

class Output:
    FOUND = "found"
    FULL_MESSAGE = "full_message"
    

class UserStatusInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "username": {
      "type": "string",
      "title": "Username",
      "description": "The UID of the user to return status of",
      "order": 1
    }
  },
  "required": [
    "username"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UserStatusOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Boolean showing the status of the request",
      "order": 1
    },
    "full_message": {
      "$ref": "#/definitions/user_status_output",
      "title": "Full Message",
      "description": "All data returned by the request",
      "order": 2
    }
  },
  "definitions": {
    "user_status_output": {
      "type": "object",
      "title": "user_status_output",
      "properties": {
        "dn": {
          "type": "string",
          "title": "DN",
          "description": "DN",
          "order": 1
        },
        "krblastfailedauth": {
          "type": "array",
          "title": "Krb Last Failed Auth",
          "description": "Krb last failed auth",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "krblastsuccessfulauth": {
          "type": "array",
          "title": "Krb Last Successful Auth",
          "description": "Krb last successful auth",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "krbloginfailedcount": {
          "type": "array",
          "title": "Krb Login Failed Count",
          "description": "Krb login failed count",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "now": {
          "type": "string",
          "title": "Now",
          "description": "Now",
          "order": 5
        },
        "server": {
          "type": "string",
          "title": "Server",
          "description": "Server",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
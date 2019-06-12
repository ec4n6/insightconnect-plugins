# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    IP = "ip"
    

class Output:
    RESULT = "result"
    

class SearchByIpInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip": {
      "type": "string",
      "title": "IP",
      "description": "IP address",
      "order": 1
    }
  },
  "required": [
    "ip"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchByIpOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "array",
      "title": "Result",
      "description": "Object References of all objects with given IP address",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "result"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
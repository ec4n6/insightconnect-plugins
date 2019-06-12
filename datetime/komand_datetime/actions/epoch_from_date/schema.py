# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DATETIME = "datetime"
    

class Output:
    EPOCH = "epoch"
    

class EpochFromDateInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "datetime": {
      "type": "string",
      "title": "Datetime",
      "displayType": "date",
      "description": "Date in RFC3339 format",
      "format": "date-time",
      "order": 1
    }
  },
  "required": [
    "datetime"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EpochFromDateOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "epoch": {
      "type": "integer",
      "title": "Epoch",
      "description": "Epoch after conversion",
      "order": 1
    }
  },
  "required": [
    "epoch"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
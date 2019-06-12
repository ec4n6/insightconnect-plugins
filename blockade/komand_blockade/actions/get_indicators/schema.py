# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DB_ROUTE = "db_route"
    

class Output:
    INDICATORCOUNT = "indicatorCount"
    INDICATORS = "indicators"
    SUCCESS = "success"
    

class GetIndicatorsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "db_route": {
      "type": "string",
      "title": "DB Route",
      "description": "Database name, leave empty if only a single database is used",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIndicatorsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicatorCount": {
      "type": "integer",
      "title": "Indicator Count",
      "description": "Indicator count",
      "order": 2
    },
    "indicators": {
      "type": "array",
      "title": "Indicators",
      "description": "List of indicators",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 3
    }
  },
  "required": [
    "indicators",
    "indicatorCount",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
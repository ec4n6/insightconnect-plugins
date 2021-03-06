# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Expands metrics with matching paths"


class Input:
    LEAVES_ONLY = "leaves_only"
    QUERY = "query"
    

class Output:
    METRICS = "metrics"
    

class MetricsExpandInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "leaves_only": {
      "type": "boolean",
      "title": "Leaves Only",
      "description": "Display only leaves",
      "default": false,
      "order": 2
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Search query",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MetricsExpandOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "metrics": {
      "type": "array",
      "title": "Metrics",
      "description": "List of matching metrics' names",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

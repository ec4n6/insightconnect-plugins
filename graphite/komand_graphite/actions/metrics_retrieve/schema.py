# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    FROM = "from"
    TARGET = "target"
    TEMPLATES = "templates"
    UNTIL = "until"
    

class Output:
    METRICS = "metrics"
    

class MetricsRetrieveInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "from": {
      "type": "string",
      "title": "From",
      "description": "Beginning of required range (can be relative or absolute)",
      "order": 2
    },
    "target": {
      "type": "string",
      "title": "Target",
      "description": "A path identifying one or several metrics, optionally with functions acting on those metrics",
      "order": 1
    },
    "templates": {
      "type": "object",
      "title": "Template Variables",
      "description": "Values for template variables used in target",
      "order": 4
    },
    "until": {
      "type": "string",
      "title": "Until",
      "description": "End of required range (can be relative or absolute)",
      "order": 3
    }
  },
  "required": [
    "target"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MetricsRetrieveOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "metrics": {
      "type": "array",
      "title": "Metrics",
      "description": "Target metrics in JSON format",
      "items": {
        "$ref": "#/definitions/metric_raw"
      },
      "order": 1
    }
  },
  "definitions": {
    "metric_raw": {
      "type": "object",
      "title": "metric_raw",
      "properties": {
        "datapoints": {
          "type": "array",
          "title": "Datapoints",
          "items": {
            "type": "array"
          },
          "order": 2
        },
        "target": {
          "type": "string",
          "title": "Target",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
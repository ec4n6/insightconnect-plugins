# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ID = "id"
    INSTANCE = "instance"
    

class Output:
    REPORT = "report"
    

class DownloadReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Report ID",
      "description": "Identifier of the report to download e.g. 265",
      "order": 1
    },
    "instance": {
      "type": "string",
      "title": "Instance",
      "description": "The identifier of the report instance, 'latest' or ID e.g. 100",
      "order": 2
    }
  },
  "required": [
    "instance",
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "type": "string",
      "title": "Report",
      "displayType": "bytes",
      "description": "Base64 encoded report",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
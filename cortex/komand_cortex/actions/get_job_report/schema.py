# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    JOB_ID = "job_id"
    

class Output:
    REPORT = "report"
    

class GetJobReportInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_id": {
      "type": "string",
      "title": "Job ID",
      "description": "Job ID e.g. c9uZDbHBf32DdIVJ",
      "order": 1
    }
  },
  "required": [
    "job_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetJobReportOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "report": {
      "type": "object",
      "title": "Report",
      "description": "Report",
      "order": 1
    }
  },
  "required": [
    "report"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    HOSTNAME = "hostname"
    

class Output:
    SUCCESS = "success"
    

class IsolateSensorInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "Hostname of the sensor to isolate",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IsolateSensorOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the isolation was successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
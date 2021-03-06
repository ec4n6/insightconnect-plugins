# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Apply a mitigation action to a threat"


class Input:
    ACTION = "action"
    THREAT_ID = "threat_id"
    

class Output:
    AFFECTED = "affected"
    

class MitigateThreatInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Mitigation action",
      "enum": [
        "rollback-remediation",
        "quarantine",
        "kill",
        "remediate",
        "un-quarantine"
      ],
      "order": 2
    },
    "threat_id": {
      "type": "string",
      "title": "Threat ID",
      "description": "ID of a threat",
      "order": 1
    }
  },
  "required": [
    "action",
    "threat_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MitigateThreatOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

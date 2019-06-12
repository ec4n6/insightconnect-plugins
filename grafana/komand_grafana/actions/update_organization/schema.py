# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    NAME = "name"
    ORGANIZATION_ID = "organization_id"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    

class UpdateOrganizationInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "New Organization Name",
      "description": "New name for organization",
      "order": 2
    },
    "organization_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Unique ID of the organization eg. 123 (-1 implies current)",
      "default": -1,
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateOrganizationOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Grafana API response, if any",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True, if organization name was updated",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
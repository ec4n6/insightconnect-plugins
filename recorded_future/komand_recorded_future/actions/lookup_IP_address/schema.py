# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    IP_ADDRESS = "IP_address"
    

class Output:
    ENTITY = "entity"
    TIMESTAMPS = "timestamps"
    

class LookupIPAddressInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "IP_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address",
      "order": 1
    }
  },
  "required": [
    "IP_address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupIPAddressOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "entity": {
      "$ref": "#/definitions/entity",
      "title": "Entity",
      "description": "Timestamps",
      "order": 1
    },
    "timestamps": {
      "$ref": "#/definitions/timestamps",
      "title": "Timestamps",
      "description": "Timestamps",
      "order": 2
    }
  },
  "definitions": {
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
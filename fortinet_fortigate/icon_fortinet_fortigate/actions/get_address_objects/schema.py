# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get address objects"


class Input:
    NAME_FILTER = "name_filter"
    

class Output:
    ADDRESS_OBJECTS = "address_objects"
    

class GetAddressObjectsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name_filter": {
      "type": "string",
      "title": "Name Filter",
      "description": "Optional name to filter on",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAddressObjectsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_objects": {
      "type": "array",
      "title": "Address Objects",
      "description": "A list of address objects",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "address_objects"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

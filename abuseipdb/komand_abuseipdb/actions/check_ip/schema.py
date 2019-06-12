# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Look up an IP address in the database"


class Input:
    ADDRESS = "address"
    DAYS = "days"
    VERBOSE = "verbose"
    

class Output:
    FOUND = "found"
    LIST = "list"
    

class CheckIpInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IPv4 or IPv6 address e.g. 8.8.8.8, ::1",
      "order": 1
    },
    "days": {
      "type": "string",
      "title": "Days",
      "description": "Check for IP reports in the last x days",
      "default": "30",
      "order": 2
    },
    "verbose": {
      "type": "boolean",
      "title": "Verbose",
      "description": "When set, reports will include the comment (if any) and the reporter's user id number (0 if reported anonymously)",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "address",
    "days",
    "verbose"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIpOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether an IP address was found in the database",
      "order": 2
    },
    "list": {
      "type": "array",
      "title": "Reports",
      "description": "List of IP reports",
      "items": {
        "$ref": "#/definitions/ip"
      },
      "order": 1
    }
  },
  "required": [
    "found"
  ],
  "definitions": {
    "ip": {
      "type": "object",
      "title": "ip",
      "properties": {
        "category": {
          "type": "array",
          "title": "Category",
          "items": {
            "type": "integer"
          },
          "order": 1
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "order": 7
        },
        "country": {
          "type": "string",
          "title": "Country",
          "order": 5
        },
        "created": {
          "type": "string",
          "title": "Created",
          "order": 2
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "order": 3
        },
        "isWhitelisted": {
          "type": "boolean",
          "title": "Is Whitelisted",
          "order": 4
        },
        "isoCode": {
          "type": "string",
          "title": "ISO Code",
          "order": 6
        },
        "userId": {
          "type": "integer",
          "title": "User ID",
          "description": "Reporter's user id number (0 if reported anonymously)",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
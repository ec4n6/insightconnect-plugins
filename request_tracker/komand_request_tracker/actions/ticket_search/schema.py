# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    KEYWORDS = "keywords"
    ORDER = "order"
    QUEUE = "queue"
    RAW_QUERY = "raw_query"
    

class Output:
    TICKETS = "Tickets"
    

class TicketSearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "keywords": {
      "type": "object",
      "title": "Keywords",
      "description": "Key-Value pair map of other arguments possible to set if not passing raw_query. See the plugin docs for more on this",
      "order": 4
    },
    "order": {
      "type": "string",
      "title": "Order",
      "description": "By this parameter you can change the sort field and order of the search result. To sort a list ascending just put a '+'  before the fieldname, otherwise a '-'",
      "order": 3
    },
    "queue": {
      "type": "string",
      "title": "Queue",
      "description": "Queue",
      "order": 2
    },
    "raw_query": {
      "type": "string",
      "title": "Raw Query",
      "description": "Raw query E.g. id=1",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketSearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Tickets": {
      "type": "array",
      "title": "Tickets",
      "description": "Tickets",
      "items": {
        "$ref": "#/definitions/Ticket"
      },
      "order": 1
    }
  },
  "definitions": {
    "Ticket": {
      "type": "object",
      "title": "Ticket",
      "properties": {
        "AdminCc": {
          "type": "string",
          "title": "AdminCc",
          "order": 10
        },
        "Cc": {
          "type": "string",
          "title": "Cc",
          "order": 9
        },
        "Created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "format": "date-time",
          "order": 11
        },
        "Creator": {
          "type": "string",
          "title": "Creator",
          "order": 3
        },
        "Due": {
          "type": "string",
          "title": "Due",
          "order": 14
        },
        "FinalPriority": {
          "type": "string",
          "title": "FinalPriority",
          "order": 7
        },
        "InitialPriority": {
          "type": "string",
          "title": "InitialPriority",
          "order": 6
        },
        "Owner": {
          "type": "string",
          "title": "Owner",
          "order": 2
        },
        "Priority": {
          "type": "string",
          "title": "Priority",
          "order": 5
        },
        "Queue": {
          "type": "string",
          "title": "Queue",
          "order": 1
        },
        "Requestors": {
          "type": "array",
          "title": "Requestors",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "Resolved": {
          "type": "string",
          "title": "Resolved",
          "order": 15
        },
        "Started": {
          "type": "string",
          "title": "Started",
          "displayType": "date",
          "format": "date-time",
          "order": 13
        },
        "Starts": {
          "type": "string",
          "title": "Starts",
          "displayType": "date",
          "format": "date-time",
          "order": 12
        },
        "Subject": {
          "type": "string",
          "title": "Subject",
          "order": 4
        },
        "TimeEstimated": {
          "type": "string",
          "title": "TimeEstimated",
          "order": 17
        },
        "TimeLeft": {
          "type": "string",
          "title": "TimeLeft",
          "order": 19
        },
        "TimeWorked": {
          "type": "string",
          "title": "TimeWorked",
          "order": 18
        },
        "Told": {
          "type": "string",
          "title": "Told",
          "order": 16
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
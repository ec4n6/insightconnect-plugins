# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ATTACHMENT_ID = "attachment_id"
    TICKET_ID = "ticket_id"
    

class Output:
    CONTENT = "Content"
    

class TicketAttachmentContentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment_id": {
      "type": "integer",
      "title": "Attachment ID",
      "description": "Attachment ID e.g. 2",
      "order": 2
    },
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID e.g. 3",
      "order": 1
    }
  },
  "required": [
    "ticket_id",
    "attachment_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketAttachmentContentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Content": {
      "type": "string",
      "title": "Content",
      "description": "Content",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
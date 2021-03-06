# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Update OTRS ticket"


class Input:
    ARTICLE = "Article"
    ATTACHMENTS = "Attachments"
    CUSTOMERUSER = "CustomerUser"
    DYNAMICFIELDS = "DynamicFields"
    LOCK = "Lock"
    NOARTICLE = "NoArticle"
    PENDINGTIME = "PendingTime"
    PRIORITY = "Priority"
    QUEUE = "Queue"
    RESPONSIBLE = "Responsible"
    SLA = "SLA"
    SERVICE = "Service"
    TICKETID = "TicketID"
    TITLE = "Title"
    TYPE = "Type"
    

class Output:
    TICKET_ID = "ticket_id"
    TICKET_NUMBER = "ticket_number"
    

class UpdateInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Article": {
      "$ref": "#/definitions/new_article",
      "title": "Article",
      "description": "New article (gets appended)",
      "order": 13
    },
    "Attachments": {
      "type": "array",
      "title": "Attachments",
      "description": "New attachments as array of objects e.g. [{\\"filename\\":\\"notes.txt\\",\\"content\\":\\"VGhpcyBpcyBhIHRlc3QK\\"}]",
      "items": {
        "$ref": "#/definitions/attachment"
      },
      "order": 15
    },
    "CustomerUser": {
      "type": "string",
      "title": "Customer User",
      "description": "Updated customer user",
      "order": 10
    },
    "DynamicFields": {
      "type": "array",
      "title": "Dynamic Fields",
      "description": "Updated dynamic fields e.g. [{\\"name\\":\\"TestName1\\",\\"value\\":\\"TestValue1\\"},{\\"name\\":\\"TestName2\\",\\"value\\":\\"TestValue2\\"}]",
      "items": {
        "$ref": "#/definitions/dynamic_field"
      },
      "order": 14
    },
    "Lock": {
      "type": "string",
      "title": "Lock",
      "description": "Lock",
      "order": 4
    },
    "NoArticle": {
      "type": "boolean",
      "title": "No Article",
      "description": "Will not add article to ticket",
      "order": 12
    },
    "PendingTime": {
      "type": "string",
      "title": "Pending Time",
      "displayType": "date",
      "description": "Pending time",
      "format": "date-time",
      "order": 3
    },
    "Priority": {
      "type": "string",
      "title": "Priority",
      "description": "Updated ticket priority e.g. 1 very low, 2 low, 3 normal, 4 high, 5 very high and so on",
      "order": 2
    },
    "Queue": {
      "type": "string",
      "title": "Queue",
      "description": "Updated queue",
      "order": 7
    },
    "Responsible": {
      "type": "string",
      "title": "Responsible",
      "description": "Responsible",
      "order": 8
    },
    "SLA": {
      "type": "string",
      "title": "SLA",
      "description": "SLA",
      "order": 6
    },
    "Service": {
      "type": "string",
      "title": "Service",
      "description": "Service",
      "order": 5
    },
    "TicketID": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID",
      "order": 1
    },
    "Title": {
      "type": "string",
      "title": "Title",
      "description": "Updated title",
      "order": 9
    },
    "Type": {
      "type": "string",
      "title": "Type",
      "description": "Updated type e.g. Incident",
      "order": 11
    }
  },
  "required": [
    "NoArticle"
  ],
  "definitions": {
    "attachment": {
      "type": "object",
      "title": "attachment",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "displayType": "bytes",
          "description": "Attachment Content",
          "format": "bytes",
          "order": 2
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Attachment filename",
          "order": 1
        }
      }
    },
    "dynamic_field": {
      "type": "object",
      "title": "dynamic_field",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Dynamic field name",
          "order": 1
        },
        "operator": {
          "type": "string",
          "title": "Operator",
          "description": "Dynamic field operator",
          "order": 3
        },
        "pattern": {
          "type": "array",
          "title": "Pattern",
          "description": "Search pattern",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Dynamic field value",
          "order": 2
        }
      },
      "required": [
        "name",
        "value"
      ]
    },
    "new_article": {
      "type": "object",
      "title": "new_article",
      "properties": {
        "AutoResponseType": {
          "type": "string",
          "title": "Auto Response Type",
          "description": "Auto response type",
          "order": 6
        },
        "Body": {
          "type": "string",
          "title": "Body",
          "description": "Ticket body",
          "order": 9
        },
        "Charset": {
          "type": "string",
          "title": "Charset",
          "description": "Character set e.g. UTF-8",
          "default": "UTF-8",
          "order": 12
        },
        "CommunicationChannel": {
          "type": "string",
          "title": "Communication Channel",
          "description": "Communication channel",
          "order": 2
        },
        "CommunicationChannelID": {
          "type": "integer",
          "title": "Communication Channel ID",
          "description": "Communication channel ID",
          "order": 1
        },
        "ContentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type",
          "order": 10
        },
        "ExcludeMuteNotificationToUserID": {
          "type": "array",
          "title": "Exclude Mute Notification",
          "description": "Exclude mute notification to user ID ",
          "items": {
            "type": "integer"
          },
          "order": 19
        },
        "ExcludeNotificationToUserID": {
          "type": "array",
          "title": "Exclude Notification",
          "description": "Exclude notification to user ID",
          "items": {
            "type": "integer"
          },
          "order": 18
        },
        "ForceNotificationToUserID": {
          "type": "array",
          "title": "Force Notification",
          "description": "Force notification to user ID",
          "items": {
            "type": "integer"
          },
          "order": 17
        },
        "From": {
          "type": "string",
          "title": "From",
          "description": "From",
          "order": 7
        },
        "HistoryComment": {
          "type": "string",
          "title": "History Comment",
          "description": "History comment",
          "order": 14
        },
        "HistoryType": {
          "type": "string",
          "title": "History Type",
          "description": "History type",
          "order": 13
        },
        "IsVisibleForCustomer": {
          "type": "integer",
          "title": "Is Visible For Customer",
          "description": "Is visible for customer",
          "order": 3
        },
        "MimeType": {
          "type": "string",
          "title": "MIME Type",
          "description": "MIME type e.g. plain/text",
          "order": 11
        },
        "NoAgentNotify": {
          "type": "integer",
          "title": "No Agent Notify",
          "description": "No agent notify",
          "order": 16
        },
        "SenderType": {
          "type": "string",
          "title": "Sender Type",
          "description": "Sender type",
          "order": 4
        },
        "SenderTypeID": {
          "type": "integer",
          "title": "Sender Type ID",
          "description": "Sender type ID",
          "order": 5
        },
        "Subject": {
          "type": "string",
          "title": "Subject",
          "description": "Ticket subject",
          "order": 8
        },
        "TimeUnit": {
          "type": "number",
          "title": "Time Unit",
          "description": "Time Unit",
          "order": 15
        }
      },
      "required": [
        "Charset"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID",
      "order": 1
    },
    "ticket_number": {
      "type": "integer",
      "title": "Ticket Number",
      "description": "Ticket number",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

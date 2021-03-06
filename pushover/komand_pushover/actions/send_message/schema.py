# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Send a Pushover notification to a user or group"


class Input:
    EXPIRE = "expire"
    MESSAGE = "message"
    PRIORITY = "priority"
    RETRY = "retry"
    SOUND = "sound"
    TIMESTAMP = "timestamp"
    TITLE = "title"
    URL = "url"
    URL_TITLE = "url_title"
    USER = "user"
    

class Output:
    RECEIPT = "receipt"
    REQUEST = "request"
    STATUS = "status"
    

class SendMessageInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "expire": {
      "type": "integer",
      "title": "Expirey of retry on emergency",
      "description": "Expirey of retry on emergency notifications - in seconds",
      "order": 8
    },
    "message": {
      "type": "string",
      "title": "The message to send",
      "description": "The message to send",
      "order": 2
    },
    "priority": {
      "type": "string",
      "title": "Priority of the message to send",
      "description": "Priority of the message to send",
      "default": "Normal",
      "enum": [
        "Lowest",
        "Low",
        "Normal",
        "High",
        "Emergency"
      ],
      "order": 6
    },
    "retry": {
      "type": "integer",
      "title": "Frequency of retry for emergency",
      "description": "Frequency of retry on emergency notifications - in seconds",
      "order": 7
    },
    "sound": {
      "type": "string",
      "title": "Sound to play",
      "description": "Sound to play - names at https://pushover.net/api#sounds",
      "order": 9
    },
    "timestamp": {
      "type": "string",
      "title": "Timestamp to send",
      "displayType": "date",
      "description": "Timestamp to send instead of timestamp message was sent",
      "format": "date-time",
      "order": 10
    },
    "title": {
      "type": "string",
      "title": "The message title to send",
      "description": "The message title to send - defaults to app name linked to API key",
      "order": 3
    },
    "url": {
      "type": "string",
      "title": "Supplemental URL",
      "description": "Supplemental URL to provide with the message",
      "order": 4
    },
    "url_title": {
      "type": "string",
      "title": "Title for supplemental URL",
      "description": "Title for supplemental URL",
      "order": 5
    },
    "user": {
      "type": "string",
      "title": "User/group key to send message to",
      "description": "User/group key to send message to",
      "order": 1
    }
  },
  "required": [
    "message",
    "priority",
    "user"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendMessageOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "receipt": {
      "type": "string",
      "title": "Receipt",
      "description": "Receipt",
      "order": 3
    },
    "request": {
      "type": "string",
      "title": "Request ID",
      "description": "Request ID",
      "order": 2
    },
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  },
  "required": [
    "request",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

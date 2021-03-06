# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DISCARD_OTHER_SESSIONS = "discard_other_sessions"
    PORT = "port"
    SERVER = "server"
    SSL_VERIFY = "ssl_verify"
    USERNAME_PASSWORD = "username_password"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "discard_other_sessions": {
      "type": "boolean",
      "title": "Force Changes",
      "description": "Force changes made by any plugin actions. Currently logged in users will be logged out of their sessions to allow the plugin to commit changes. Users of Check Point R80+ may not need to enable this option",
      "default": false,
      "order": 5
    },
    "port": {
      "type": "integer",
      "title": "Check Point Server Port",
      "description": "Check Point server port",
      "default": 443,
      "order": 3
    },
    "server": {
      "type": "string",
      "title": "Check Point Server IP Address",
      "description": "Check Point server IP address",
      "order": 2
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Use SSL verification",
      "default": true,
      "order": 4
    },
    "username_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Credentials",
      "description": "Username and password",
      "order": 1
    }
  },
  "required": [
    "discard_other_sessions",
    "port",
    "server",
    "ssl_verify",
    "username_password"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

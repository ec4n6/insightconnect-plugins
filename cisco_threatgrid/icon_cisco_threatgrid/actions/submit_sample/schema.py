# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Submits a sample to Threat Grid for analysis"


class Input:
    CALLBACK_URL = "callback_url"
    EMAIL_NOTIFICATION = "email_notification"
    NETWORK_EXIT = "network_exit"
    PLAYBOOK = "playbook"
    PRIVATE = "private"
    SAMPLE = "sample"
    SAMPLE_FILENAME = "sample_filename"
    SAMPLE_PASSWORD = "sample_password"
    TAGS = "tags"
    VM = "vm"
    

class Output:
    RESULTS = "results"
    

class SubmitSampleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "callback_url": {
      "type": "string",
      "title": "Callback URL",
      "description": "A URL where the results will `POST` to, upon completion of analysis",
      "order": 2
    },
    "email_notification": {
      "type": "boolean",
      "title": "Email Notification",
      "description": "If true, sends an email to the email address of the user that submitted the sample, upon completion of the sample analysis",
      "order": 3
    },
    "network_exit": {
      "type": "string",
      "title": "Network Exit",
      "description": "Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location",
      "order": 4
    },
    "playbook": {
      "type": "string",
      "title": "Playbook",
      "description": "Name of a playbook to apply to this sample run",
      "order": 5
    },
    "private": {
      "type": "string",
      "title": "Private",
      "description": "If present, and set to any value but `false` the sample will be marked private",
      "order": 6
    },
    "sample": {
      "$ref": "#/definitions/file",
      "title": "Sample",
      "description": "The sample file",
      "order": 1
    },
    "sample_filename": {
      "type": "string",
      "title": "Sample Filename",
      "description": "Filename to use to override the default filename",
      "order": 7
    },
    "sample_password": {
      "type": "string",
      "title": "Sample Password",
      "description": "Password used to open the submitted archive or document",
      "order": 8
    },
    "tags": {
      "type": "string",
      "title": "Tags",
      "description": "A comma-separated list of tags applied to this sample",
      "order": 9
    },
    "vm": {
      "type": "string",
      "title": "VM",
      "description": "A string identifying a specific VM to use. See the linked configuration endpoint",
      "order": 10
    }
  },
  "required": [
    "sample"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitSampleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/submit_sample_results",
      "title": "Results",
      "description": "Results from submit sample",
      "order": 1
    }
  },
  "definitions": {
    "submit_sample_data": {
      "type": "object",
      "title": "submit_sample_data",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Filename",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "login": {
          "type": "string",
          "title": "Login",
          "description": "Login",
          "order": 3
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5",
          "order": 4
        },
        "os": {
          "type": "string",
          "title": "OS",
          "description": "OS",
          "order": 5
        },
        "sha1": {
          "type": "string",
          "title": "SHA1",
          "description": "SHA1",
          "order": 6
        },
        "sha256": {
          "type": "string",
          "title": "SHA256",
          "description": "SHA256",
          "order": 7
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 8
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 9
        },
        "submission_id": {
          "type": "integer",
          "title": "Submission ID",
          "description": "Submission ID",
          "order": 10
        },
        "submitted_at": {
          "type": "string",
          "title": "Submitted At",
          "description": "Submitted at",
          "order": 11
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "object"
          },
          "order": 12
        },
        "vm": {
          "type": "string",
          "title": "VM",
          "description": "VM",
          "order": 13
        }
      }
    },
    "submit_sample_results": {
      "type": "object",
      "title": "submit_sample_results",
      "properties": {
        "api_version": {
          "type": "integer",
          "title": "API Version",
          "description": "API version",
          "order": 1
        },
        "data": {
          "$ref": "#/definitions/submit_sample_data",
          "title": "Data",
          "description": "Data",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 3
        }
      },
      "definitions": {
        "submit_sample_data": {
          "type": "object",
          "title": "submit_sample_data",
          "properties": {
            "filename": {
              "type": "string",
              "title": "Filename",
              "description": "Filename",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 2
            },
            "login": {
              "type": "string",
              "title": "Login",
              "description": "Login",
              "order": 3
            },
            "md5": {
              "type": "string",
              "title": "MD5",
              "description": "MD5",
              "order": 4
            },
            "os": {
              "type": "string",
              "title": "OS",
              "description": "OS",
              "order": 5
            },
            "sha1": {
              "type": "string",
              "title": "SHA1",
              "description": "SHA1",
              "order": 6
            },
            "sha256": {
              "type": "string",
              "title": "SHA256",
              "description": "SHA256",
              "order": 7
            },
            "state": {
              "type": "string",
              "title": "State",
              "description": "State",
              "order": 8
            },
            "status": {
              "type": "string",
              "title": "Status",
              "description": "Status",
              "order": 9
            },
            "submission_id": {
              "type": "integer",
              "title": "Submission ID",
              "description": "Submission ID",
              "order": 10
            },
            "submitted_at": {
              "type": "string",
              "title": "Submitted At",
              "description": "Submitted at",
              "order": 11
            },
            "tags": {
              "type": "array",
              "title": "Tags",
              "description": "Tags",
              "items": {
                "type": "object"
              },
              "order": 12
            },
            "vm": {
              "type": "string",
              "title": "VM",
              "description": "VM",
              "order": 13
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
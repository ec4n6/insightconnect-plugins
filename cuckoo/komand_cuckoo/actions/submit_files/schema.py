# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Adds one or more files and/or files embedded in archives to the list of pending tasks"


class Input:
    FILES = "files"
    

class Output:
    ERRORS = "errors"
    SUBMIT_ID = "submit_id"
    TASK_ID = "task_id"
    

class SubmitFilesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "files": {
      "type": "array",
      "title": "Files",
      "description": "List of files of the format: {'filename': 'blah.exe', 'contents': '\\u003cb64-encoded-bytes\\u003e'}",
      "items": {
        "$ref": "#/definitions/file"
      },
      "order": 1
    }
  },
  "required": [
    "files"
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


class SubmitFilesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "errors": {
      "type": "array",
      "title": "Errors",
      "description": "Errors if any",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "submit_id": {
      "type": "integer",
      "title": "Submit ID",
      "description": "Submission ID",
      "order": 2
    },
    "task_id": {
      "type": "integer",
      "title": "Task ID",
      "description": "Task ID",
      "order": 1
    }
  },
  "required": [
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

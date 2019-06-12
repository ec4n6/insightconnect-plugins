# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    DOMAIN = "domain"
    

class Output:
    DOMAIN_RECORD = "domain_record"
    FOUND = "found"
    

class LookupDomainInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain, e.g. 4.2.2.2",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupDomainOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain_record": {
      "$ref": "#/definitions/domain_record",
      "title": "Domain Record",
      "description": "Domain Record",
      "order": 1
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "True if found",
      "order": 2
    }
  },
  "definitions": {
    "domain_record": {
      "type": "object",
      "title": "domain_record",
      "properties": {
        "dynamic_dns": {
          "type": "boolean",
          "title": "Dynamic Dns",
          "description": "True if Dynamic DNS",
          "order": 5
        },
        "ever_compromised": {
          "type": "boolean",
          "title": "Ever Compromised",
          "description": "True if ever compromised",
          "order": 1
        },
        "primary_domain": {
          "type": "string",
          "title": "Primary Domain",
          "description": "True if primary Domain",
          "order": 2
        },
        "subdomains": {
          "type": "array",
          "title": "Subdomains",
          "description": "Subdomains",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "tld": {
          "type": "string",
          "title": "Tld",
          "description": "TLD",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
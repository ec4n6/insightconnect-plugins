# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ADDRESS = "address"
    AVS_RESULT = "avs_result"
    BANK_PHONE_COUNTRY_CODE = "bank_phone_country_code"
    BANK_PHONE_NUMBER = "bank_phone_number"
    CARD_BANK_NAME = "card_bank_name"
    CARD_ISSUER_ID_NUMBER = "card_issuer_id_number"
    CARD_LAST_4_DIGITS = "card_last_4_digits"
    CARD_TOKEN = "card_token"
    CVV_RESULT = "cvv_result"
    

class Output:
    CREDIT_CARD_RESULT = "credit_card_result"
    RISK_SCORE = "risk_score"
    

class CardLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "avs_result": {
      "type": "string",
      "title": "AVS Result",
      "description": "Address Verification System result",
      "order": 8
    },
    "bank_phone_country_code": {
      "type": "string",
      "title": "Bank Phone Country Code",
      "description": "Phone country code for bank",
      "order": 6
    },
    "bank_phone_number": {
      "type": "string",
      "title": "Bank Phone Number",
      "description": "Phone number for bank",
      "order": 7
    },
    "card_bank_name": {
      "type": "string",
      "title": "Issuing Bank",
      "description": "Issuing bank of the credit card",
      "order": 5
    },
    "card_issuer_id_number": {
      "type": "string",
      "title": "Card Issuer ID Number",
      "description": "Issuer ID number for the credit card",
      "order": 2
    },
    "card_last_4_digits": {
      "type": "string",
      "title": "Card Last 4 Digits",
      "description": "Last 4 digits of credit card",
      "order": 3
    },
    "card_token": {
      "type": "string",
      "title": "Credit Card Token",
      "description": "Token representing the credit card",
      "order": 4
    },
    "cvv_result": {
      "type": "string",
      "title": "CVV Result",
      "description": "Card Verification Value code",
      "order": 9
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CardLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credit_card_result": {
      "$ref": "#/definitions/credit_card",
      "title": "Credit Card Result",
      "description": "Result for credit card",
      "order": 1
    },
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 2
    }
  },
  "definitions": {
    "credit_card": {
      "type": "object",
      "title": "credit_card",
      "properties": {
        "brand": {
          "type": "string",
          "title": "Brand",
          "description": "Card brand",
          "order": 2
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "Country of credit card",
          "order": 3
        },
        "is_issued_in_billing_address_country": {
          "type": "boolean",
          "title": "Is Issued In Billing Address Country",
          "description": "Is card issued in billing address country",
          "order": 4
        },
        "is_prepaid": {
          "type": "boolean",
          "title": "Is Prepaid",
          "description": "Is card prepaid",
          "order": 5
        },
        "issuer": {
          "$ref": "#/definitions/issuer",
          "title": "Issuer",
          "description": "Issuer data",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Card type",
          "order": 6
        }
      },
      "definitions": {
        "issuer": {
          "type": "object",
          "title": "issuer",
          "properties": {
            "matches_provided_name": {
              "type": "boolean",
              "title": "Matches Provided Name",
              "description": "Issuer name matches name provided",
              "order": 2
            },
            "matches_provided_phone_number": {
              "type": "boolean",
              "title": "Matches Provided Phone Number",
              "description": "Issuer phone number matches number provided",
              "order": 4
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Card issuer name",
              "order": 1
            },
            "phone_number": {
              "type": "string",
              "title": "Phone Number",
              "description": "Issuer phone number",
              "order": 3
            }
          }
        }
      }
    },
    "issuer": {
      "type": "object",
      "title": "issuer",
      "properties": {
        "matches_provided_name": {
          "type": "boolean",
          "title": "Matches Provided Name",
          "description": "Issuer name matches name provided",
          "order": 2
        },
        "matches_provided_phone_number": {
          "type": "boolean",
          "title": "Matches Provided Phone Number",
          "description": "Issuer phone number matches number provided",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Card issuer name",
          "order": 1
        },
        "phone_number": {
          "type": "string",
          "title": "Phone Number",
          "description": "Issuer phone number",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)

# TenableIO

## About

[TenableIO](http://www.tenable.com/products/tenable-io) is a cloud-based vulnerability management platform
This plugin utilizes the [TenableIO API](https://cloud.tenable.com/api#/overview).

## Actions

### Launch Scan

This action is used to scan external assets. Options for template include 'basic' and 'discovery'.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Scan name|None|
|template|string|None|True|Scan template|None|
|targets|[]string|None|True|Array of domain names and/or IP addresses to scan|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_name|string|True|Name of the recently launched scan|

Example Output:

```

{
  "scan_name": "My Scan"
}

```

### Download Report

This action is used to download the base64-encoded report generated by a completed scan.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|The name of the scan to download. In case of conflicts, the most recent scan of this name will be used|None|
|report_type|string|None|False|The class of report to generate|['Vulnerabilities by Host', 'Vulnerabilities by Plugin', 'Executive Summary']|
|file_format|string|None|False|File format to download the report in|['CSV', 'HTML', 'NESSUS', 'PDF']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_report|file|False|The Base64 encoded report|

Example Output:

```

{
  "scan_report": {
      "filename": "report",
      "content": "VGhpcyBpcyBhIHRlc3QgbWVzc2FnZQo="
    }
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_key|credential_secret_key|None|True|Access Key|None|
|secret_key|credential_secret_key|None|True|Secret Key|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Example goes here

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [Tenable.io SDK](https://github.com/tenable/Tenable.io-SDK-for-Python)
* [Tenable.io API Documentation](https://cloud.tenable.com/api#/overview)
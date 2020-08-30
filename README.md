# WAFv2 - AWS managed rules CloudFormation stack (Cloudfront scope)
This repository provides you with scripts needed to generate stack with all AWS managed wafv2 rule groups.

## Prerequisites
To run `./list-available-rules.sh` you should run `aws configure` first!
Jq is needed so: `pip install jq==1.0.2`
Install troposphere: `pip install troposphere==2.6.2`

## Files
`list-available-rules.sh` - lists all available rules
`wafv2-template.py` - troposphere powered cloudformation generation for wafv2 managed rules

## Usage
- Run: `./list-available-rules.sh`
- Edit wafv2-template.py file to make sure you have all the *managed_rules* listed.
- Run `python wafv2-template.py > template.json`
- Go to your cloudformation console - Make sure you use **us-east-1** region, since only there wafv2 cloudfront scoped webacl can be created.
- Click **Create Stack** and upload this **template.json**, watch your WebACL get up and running.

## Notes
Be sure you choose only rules that you need, since if you include them all you will get an error:

```Error reason: You exceeded the capacity limit for a rule group or web ACL., field: WEB_ACL, parameter: 1975 (Service: Wafv2, Status Code: 400, Request ID: bcce2981-bfeb-4e29-b4c0-50cd386b75df, Extended Request ID: null)```

This is due to limit of 1500 WCUs per WebACL. If you run into this error, choose fewer number of managed rules.

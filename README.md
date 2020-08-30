# WAFv2 - AWS managed rules CloudFormation stack (Cloudfront scope)
This repository provides you with scripts needed to generate stack with all AWS managed wafv2 rule groups.

## Prerequisites
To run `./list-available-rules.sh` you should run `aws configure` first!
Install troposphere: `pip install troposphere==2.6.2`

## Files
`list-available-rules.sh` - lists all available rules
`wafv2-template.py` - troposphere powered cloudformation generation for wafv2 managed rules

## Usage
- Run: `./list-available-rules.sh`
- Edit wafv2-template.py file to make sure you have all the *managed_rules* listed.
- Run `python wafv2-template.py > template.json`
- Go to your cloudformation console - Make sure you use us-east-1 region, since only there wafv2 cloudfront scoped webacl can be created.

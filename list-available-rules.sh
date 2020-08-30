#!/bin/bash
echo "List of available managed rule groups:"
aws --region us-east-1 wafv2 list-available-managed-rule-groups --scope "CLOUDFRONT" | jq -r '.ManagedRuleGroups[].Name'

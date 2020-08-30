
import troposphere
from troposphere import Parameter, Template, Output, Export, GetAtt
from troposphere.cloudformation import Stack
from troposphere.wafv2 import WebACL, DefaultAction, AllowAction, BlockAction, RuleAction, OverrideAction, CountAction, NoneAction
from troposphere.wafv2 import StatementOne, ManagedRuleGroupStatement, WebACLRule, VisibilityConfig, IPSet, IPSetReferenceStatement

#
# You can edit these to your liking
#

managed_rules=[
  "AWSManagedRulesCommonRuleSet",
  "AWSManagedRulesAdminProtectionRuleSet",
  "AWSManagedRulesKnownBadInputsRuleSet",
  "AWSManagedRulesSQLiRuleSet",
  "AWSManagedRulesLinuxRuleSet",
  "AWSManagedRulesUnixRuleSet",
  # "AWSManagedRulesWindowsRuleSet",
  # "AWSManagedRulesPHPRuleSet",
  # "AWSManagedRulesWordPressRuleSet",
  "AWSManagedRulesAmazonIpReputationList",
  "AWSManagedRulesAnonymousIpList"
]

def generate_managed_rules():
  rules=[]
  priority=10
  for managed_rule in managed_rules:
    rules.append(
      WebACLRule(
        OverrideAction=OverrideAction(**{'None': NoneAction()}),
        Name=managed_rule,
        Priority=priority,
        Statement=StatementOne(
          ManagedRuleGroupStatement=ManagedRuleGroupStatement(
            Name=managed_rule,
            VendorName="AWS"
          )
        ),
        VisibilityConfig=VisibilityConfig(
            CloudWatchMetricsEnabled=True,
            MetricName=managed_rule,
            SampledRequestsEnabled=False
        )
      )
    )
    priority=(priority+1)
  return rules


t = Template()
t.add_version("2010-09-09")

t.add_description("WAFv2 AWS managed rules stack")

"""
Cloudformation
Resources
"""

cdnwaf = t.add_resource(WebACL(
    "WebACL",
    Name="AWSBasicWAF",
    Scope="CLOUDFRONT",
    Description="WAFv2 AWS managed rules WebACL",
    DefaultAction=DefaultAction(
        Block=BlockAction()
    ),
    VisibilityConfig=VisibilityConfig(
        CloudWatchMetricsEnabled=True,
        MetricName="AWSBasicWAF",
        SampledRequestsEnabled=False
    ),
    Rules=generate_managed_rules()
))

"""
Cloudformation
Outputs
"""
t.add_output(
    Output(
        "wafarn",
        Description="WAFv2 WebACL ARN.",
        Value=GetAtt("WebACL", "Arn"),
        Export=Export("wafarn"),
    ))

print(t.to_json())

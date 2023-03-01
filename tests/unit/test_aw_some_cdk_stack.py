import aws_cdk as core
import aws_cdk.assertions as assertions

from aw_some_cdk.aw_some_cdk_stack import AwSomeCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aw_some_cdk/aw_some_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwSomeCdkStack(app, "aw-some-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

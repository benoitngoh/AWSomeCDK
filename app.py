#!/usr/bin/env python3
import os

# import aws_cdk as cdk
from aws_cdk import(
    App
)

from aw_some_cdk.aw_some_cdk_stack import GithubActionSetupRole


app = App()
env={'region':'us-east-1','account':'771500531194'}
stack_env='Staging'

GithubAction=GithubActionSetupRole(app, "GithubActionSetupRole",env=env,stack_env=stack_env
    )


app.synth()

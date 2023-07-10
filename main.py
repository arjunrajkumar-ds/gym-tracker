import boto3
from botocore.exceptions import ClientError

# Instantiate the AWS Cognito Client with AWS credentials
client = boto3.client('cognito-idp', region_name = 'ap-southeast-2')
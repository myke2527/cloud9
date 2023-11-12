import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SGfrom boto3',
    GroupName='boto3 SG',
    VpcId='vpc-08f0457b82d0e69e6',
)

print(response["GroupId"])
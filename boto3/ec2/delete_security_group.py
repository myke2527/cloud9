import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-01acd874a90b915e9',
)

print(response)
import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-067a10a93742762e9',
    )
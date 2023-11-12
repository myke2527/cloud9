import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-01f6f0b7641f33282',
    Name='Ubuntu EC2 Server'
    )

print(response["ImageId"])
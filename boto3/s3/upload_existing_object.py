import boto3

s3 = boto3.client('s3')

with open("/home/ec2-user/environment/cloud9/boto3/newtest.txt", 'rb') as f:
    s3.put_object(Bucket="mvsboto30926", Key="newtest.txt", Body=f)

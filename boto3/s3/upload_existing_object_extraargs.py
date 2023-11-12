import boto3

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/clou9/boto3/test_text.txt', 'mvsboto30926', ExtraArgs ={'ContentType' : 'text/plain'})

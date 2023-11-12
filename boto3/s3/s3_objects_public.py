import boto3

s3 = boto3.client('s3')

bucket = "mvsboto30926"
key = "newfile.txt"

response = s3.put_public_access_block(
    Bucket=bucket,
    
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    },
)
                                
print(response)
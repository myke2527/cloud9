import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Generate a presigned URL for the 'get_object' operation
response = s3.generate_presigned_url('get_object', Params={'Bucket': "mvsboto30926", 'Key': "fruits"}, ExpiresIn=300)

# Print the generated presigned URL
print(response)
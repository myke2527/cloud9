def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_group_id
        ],
        UserData=user_data
    )
    
    print(response["Instances"][0]["InstanceId"])

ami_id = "ami-0fc5d935ebf8bc3bc"
key_pair_name = "Key from boto3"
security_group_id = "sg-01acd874a90b915e9"

user_data='''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')
create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)
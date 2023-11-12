import boto3


def stop_instance(client, instance_id):
    response = ec2.stop_instance(
        InstanceIds=[
            instance_id
        ],
        
    )
    
    print(instance_id, "stopped")
    
def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id
    ],
)

    print(instance_id, "started")

if __name__ == '__main__':
    instance_id = "i-01ab529e74c33b3dc"	


ec2 = boto3.client('ec2')
start_instance(ec2, instance_id)

from flask import Flask, request
import json
import boto3


app = Flask(__name__)


@app.route("/AllInstances")
def hello():
    client = boto3.client('ec2')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        conn = boto3.resource('ec2', region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.instance_lifecycle is None:
                k = "On-Demand"
            elif instance.instance_lifecycle is 'spot':
                k = "Spot"
            else:
                k = "Scheduled"
            output = {
                'Id': instance.id,
                'Instance_Type': instance.instance_type,
                'Public Ip Address': instance.public_ip_address,
                'Private Ip Address': instance.private_ip_address,
                'Instance State': instance.state['Name'],
                'Instance Tags': instance.tags,
                'Instance Cost': k,
                'Availability Zone': instance.placement['AvailabilityZone'],
                'Launch Time': instance.launch_time,
                'Region': region
            }
            return json.dumps(output, indent=4, sort_keys=True, default=str)
if __name__ == "__main__":
    app.run(host='localhost', port=5000)

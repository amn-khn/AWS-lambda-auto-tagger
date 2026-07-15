import boto3

ec2 = boto3.client("ec2")


def lambda_handler(event, context):

    try:

        instance_ids = []

        items = event["detail"]["responseElements"]["instancesSet"]["items"]

        for item in items:
            instance_ids.append(item["instanceId"])

        response = ec2.describe_instances(
            InstanceIds=instance_ids
        )

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:

                tags = instance.get("Tags", [])

                if len(tags) == 0:

                    print(f"Stopping {instance['InstanceId']}")

                    ec2.stop_instances(
                        InstanceIds=[instance["InstanceId"]]
                    )

                else:
                    print(f"{instance['InstanceId']} has tags.")

    except Exception as e:
        print(e)

    return {
        "statusCode":200
    }
import boto3

s3 = boto3.client("s3")

OWNER_NAME = "Mohammed Amankhan"

def lambda_handler(event, context):

    print(event)

    bucket_name = event["detail"]["requestParameters"]["bucketName"]

    s3.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            "TagSet": [
                {
                    "Key": "Owner",
                    "Value": OWNER_NAME
                }
            ]
        }
    )

    return {
        "statusCode": 200,
        "body": f"Tag added to {bucket_name}"
    }
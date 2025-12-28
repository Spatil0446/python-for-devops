import boto3
from botocore.exceptions import ClientError

REGION = "ap-south-1"   # change if needed
BUCKET_NAME = "shubham-demo-s3-bucket-12345"  # must be globally unique

def create_s3_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)

    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        print(f"✅ Bucket created: {bucket_name}")

    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"ℹ Bucket already exists and owned by you: {bucket_name}")
        else:
            print(f"❌ Error creating bucket: {e}")


def list_s3_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()

    print("\n📦 S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")


def main():
    create_s3_bucket(BUCKET_NAME, REGION)
    list_s3_buckets()


if __name__ == "__main__":
    main()

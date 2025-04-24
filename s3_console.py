from __future__ import annotations

import os
import boto3
from botocore.client import Config
import argparse
import sys


class S3Manager:
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket_name: str | None = None):
        if not all([access_key, secret_key, endpoint_url]):
            raise ValueError("ACCESS_KEY, SECRET_KEY, and ENDPOINT_URL must be provided.")

        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint_url,
            config=Config(signature_version='s3v4'),
            region_name='minsk',
            verify=False
        )
        self.s3_bucket = bucket_name

    def set_s3_bucket_name(self, bucket_name):
        self.s3_bucket = bucket_name
        return f"✅ Bucket name set to: {bucket_name}"

    def list_of_bucket(self):
        try:
            response = self.s3_client.list_buckets()
            print("\n🪣 Buckets:")
            for bucket in response['Buckets']:
                print(f" - {bucket['Name']} | Created on: {bucket['CreationDate']}")
        except Exception as e:
            print(f"❌ Error listing buckets:\n{e}")

    def _bucket_exists(self, bucket_name):
        try:
            buckets = self.s3_client.list_buckets().get('Buckets', [])
            return any(bucket['Name'] == bucket_name for bucket in buckets)
        except Exception as e:
            print(f"❌ Cannot check if bucket exists:\n{e}")
            return False

    def create_bucket(self, new_bucket_name: str):
        try:
            if not self._bucket_exists(new_bucket_name):
                self.s3_client.create_bucket(Bucket=new_bucket_name)
                print(f"✅ Bucket '{new_bucket_name}' created.")
            else:
                print(f"⚠️ Bucket '{new_bucket_name}' already exists.")
        except Exception as e:
            print(f"❌ Cannot create bucket:\n{e}")

    def list_objects_in_bucket(self, prefix=""):
        if not self.s3_bucket:
            print("⚠️ No bucket selected. Use option 3 to set a bucket.")
            return
        try:
            print(f"\n📂 Contents of bucket '{self.s3_bucket}':")
            response = self.s3_client.list_objects_v2(Bucket=self.s3_bucket, Prefix=prefix, Delimiter='/')
            if 'CommonPrefixes' in response:
                for cp in response['CommonPrefixes']:
                    print(f"📁 {cp['Prefix']}")
            if 'Contents' in response:
                for obj in response['Contents']:
                    if obj['Key'] != prefix:
                        print(f"📄 {obj['Key']} ({obj['Size']} bytes)")
            if 'Contents' not in response and 'CommonPrefixes' not in response:
                print("ℹ️ Bucket is empty or path not found.")
        except Exception as e:
            print(f"❌ Cannot list objects:\n{e}")

    def download_file(self, object_key: str, local_path: str):
        if not self.s3_bucket:
            print("⚠️ No bucket selected.")
            return
        try:
            self.s3_client.download_file(self.s3_bucket, object_key, local_path)
            print(f"✅ File '{object_key}' downloaded to '{local_path}'")
        except Exception as e:
            print(f"❌ Failed to download file:\n{e}")

    def upload_file(self, local_path: str, s3_path: str):
        if not self.s3_bucket:
            print("⚠️ No bucket selected.")
            return
        if not os.path.isfile(local_path):
            print(f"❌ Local file '{local_path}' does not exist.")
            return
        try:
            s3_key = s3_path.lstrip("/")
            self.s3_client.upload_file(local_path, self.s3_bucket, s3_key)
            print(f"✅ File '{local_path}' uploaded to '{self.s3_bucket}/{s3_key}'")
        except Exception as e:
            print(f"❌ Failed to upload file:\n{e}")


def main():
    parser = argparse.ArgumentParser(description="S3 Cloudian Interactive Console")
    parser.add_argument("--access-key", help="Your S3 access key")
    parser.add_argument("--secret-key", help="Your S3 secret key")
    parser.add_argument("--endpoint-url", help="Your S3 endpoint URL")
    args = parser.parse_args()

    access_key = args.access_key or input("Enter ACCESS_KEY: ").strip()
    secret_key = args.secret_key or input("Enter SECRET_KEY: ").strip()
    endpoint_url = args.endpoint_url or input("Enter ENDPOINT_URL: ").strip()

    if not access_key or not secret_key or not endpoint_url:
        print("❌ All credentials are required. Exiting.")
        sys.exit(1)

    s3 = S3Manager(access_key, secret_key, endpoint_url)

    while True:
        print("\n=== S3 Cloudian Manager ===")
        if s3.s3_bucket:
            print(f"=== Current bucket: {s3.s3_bucket} ===")
        print("1. List all buckets")
        print("2. Create new bucket")
        print("3. Set bucket name for action")
        print("4. List contents of current bucket")
        print("5. Download file from bucket")
        print("6. Upload file to bucket")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            s3.list_of_bucket()
        elif choice == '2':
            name = input("Enter new bucket name: ")
            s3.create_bucket(name)
        elif choice == '3':
            name = input("Enter bucket name to set: ")
            result = s3.set_s3_bucket_name(name)
            print(result)
        elif choice == '4':
            prefix = input("Enter prefix (or leave empty for root): ").strip()
            s3.list_objects_in_bucket(prefix)
        elif choice == '5':
            key = input("Enter the object key to download: ").strip()
            local = input("Enter local path to save the file: ").strip()
            s3.download_file(key, local)
        elif choice == '6':
            local_path = input("Enter local file path to upload: ").strip()
            s3_path = input("Enter target path in bucket (e.g. /folder/file.txt): ").strip()
            s3.upload_file(local_path, s3_path)
        elif choice == '7':
            print("👋 Exiting.")
            break
        else:
            print("❗ Invalid option, try again.")


if __name__ == "__main__":
    main()

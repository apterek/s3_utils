# 🪣 S3 Cloudian Manager

An interactive Python script for managing S3-compatible storage (e.g., Cloudian). It allows you to list buckets, create new buckets, explore bucket contents, and download files.

## 📦 Features

- List all available buckets
- Create a new bucket
- Set the active bucket for operations
- Browse contents of the active bucket (pseudo-directories and files)
- Download files from a bucket to your local machine

## ⚙️ Requirements

- Python 3.9+
- Python packages:
  - `boto3`
  - `botocore`

Install the required packages using pip:

```bash
pip install boto3
```

## 🚀 Usage
Run the script with optional command-line arguments:

```bash
python s3_console.py --access-key YOUR_ACCESS_KEY --secret-key YOUR_SECRET_KEY --endpoint-url https://your-cloudian-endpoint
```

If you don’t provide these arguments, the script will prompt you for them interactively.


## 🧭 Menu Options
Once started, you will see a menu like this:

```
=== S3 Cloudian Manager ===
1. List all buckets
2. Create new bucket
3. Set bucket name for action
4. List contents of current bucket
5. Download file from bucket
6. Exit
```

### Example Usage

#### List all buckets
Select option `1` to list all available buckets.

#### Create a new bucket
Choose option `2` and enter a unique name for the new bucket.

#### Set the current bucket
Use option `3` to set an existing bucket for file operations.

#### List contents of the current bucket
Choose option `4`. You can enter a prefix (e.g., folder/) or leave it empty to list the root.

#### Download a file
Select option `5`, provide the object key (e.g., `folder/file.txt`) and the local path where the file should be saved.


## 🔐 Notes
- SSL verification is disabled (verify=False) in the script. This is helpful for development and local environments but not recommended for production.

- Works with any S3-compatible API, not just AWS S3.

## 📜 License
MIT License.

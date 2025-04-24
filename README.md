# 🪣 S3 Cloudian Manager

This Python script provides an interactive command-line interface to manage an S3-compatible object storage service (such as Cloudian). It allows you to list, create, and select buckets, browse files and folders, and upload/download files using a simple terminal interface.

## 📦 Features

- 🔐 Authenticate with access key, secret key, and endpoint URL
- 🪣 List all available buckets
- 🧰 Create new buckets
- 📁 Set active bucket
- 📂 View contents of a selected bucket (folders and files)
- ⬇️ Download files from a bucket
- ⬆️ Upload files to a bucket (with folder support via paths)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- `boto3` and `botocore`

Install dependencies:

```bash
pip install boto3 botocore
```

## 🚀 Usage
Run the script with optional command-line arguments:

```bash
python s3_console.py --access-key YOUR_ACCESS_KEY --secret-key YOUR_SECRET_KEY --endpoint-url https://your-cloudian-endpoint
```

You can also run it interactively without arguments, and it will prompt for credentials:

```bash
python s3_console.py
```

## 🧭 Menu Options
After launching the script, you'll see the following menu:

```
=== S3 Cloudian Manager ===
1. List all buckets
2. Create new bucket
3. Set bucket name for action
4. List contents of current bucket
5. Download file from bucket
6. Upload file to bucket
7. Exit
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


#### ⬇️ Download File Example
Select option `5`, provide the object key (e.g., `folder/file.txt`) and the local path where the file should be saved.
```
Enter the object key to download: logs/2025/example.log
Enter local path to save the file: ./downloaded_example.log
```

#### 🔼 Upload File Example
When uploading, you can specify a path to simulate folders in the bucket:

```
Enter local file path to upload: ./example.log
Enter target path in bucket (e.g. /logs/2025/example.log): /logs/2025/example.log
```
This will upload `example.log` into a logical folder `logs/2025/` inside the selected bucket.


## 🔐 Notes
- SSL verification is disabled (verify=False) in the script. This is helpful for development and local environments but not recommended for production.

- Works with any S3-compatible API, not just AWS S3.

## 🧑‍💻 Author
Built with ❤️ to simplify working with Cloudian S3.

## 📜 License
MIT License.


from flask import Flask, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os

app = Flask(__name__)

# Ensure AWS credentials are set as environment variables or in the default credentials file
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")  # Default to us-east-1 if not specified
BUCKET_NAME = os.getenv("BUCKET_NAME", "your-bucket-name")

if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
    raise EnvironmentError("AWS credentials are not properly configured.")

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the S3 Bucket Content Service!"})

@app.route('/list-bucket-content', defaults={'path': ''})
@app.route('/list-bucket-content/<path:path>')
def list_bucket_content(path):
    try:
        if not BUCKET_NAME:
            return jsonify({"error": "Bucket name is not configured."}), 500

        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path, Delimiter='/')

        if 'Contents' not in response and 'CommonPrefixes' not in response:
            return jsonify({"content": []})

        contents = []

        if 'CommonPrefixes' in response:
            contents.extend([prefix['Prefix'] for prefix in response['CommonPrefixes']])

        if 'Contents' in response:
            contents.extend([obj['Key'] for obj in response['Contents'] if obj['Key'] != path])

        return jsonify({"content": contents})

    except NoCredentialsError:
        return jsonify({"error": "AWS credentials not found."}), 403

    except PartialCredentialsError:
        return jsonify({"error": "Incomplete AWS credentials."}), 403

    except s3_client.exceptions.NoSuchBucket:
        return jsonify({"error": "Bucket does not exist."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


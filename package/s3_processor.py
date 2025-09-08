cat > package/s3_processor.py <<'PY'
import os
import boto3
import urllib.parse
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
TABLE = os.environ.get('DDB_TABLE')

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE)
    for rec in event.get('Records', []):
        s3_bucket = rec['s3']['bucket']['name']
        s3_key = urllib.parse.unquote_plus(rec['s3']['object']['key'])
        size = rec['s3']['object'].get('size', 0)
        uploaded_at = datetime.utcnow().isoformat()
        table.put_item(Item={
            "pk": f"S3#{s3_bucket}#{s3_key}",
            "uploaded_at": uploaded_at,
            "bucket": s3_bucket,
            "key": s3_key,
            "size": str(size)
        })
    return {"statusCode": 200, "body": "processed"}
PY

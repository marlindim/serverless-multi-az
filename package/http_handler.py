cat > package/http_handler.py <<'PY'
import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
TABLE = os.environ.get('DDB_TABLE')

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE)
    try:
        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)
    except Exception:
        body = {}
    pk = body.get('pk') or f"HTTP#{datetime.utcnow().isoformat()}"
    payload = {
        "pk": pk,
        "uploaded_at": datetime.utcnow().isoformat(),
        "payload": json.dumps(body)
    }
    table.put_item(Item=payload)
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "saved", "pk": pk})
    }
PY

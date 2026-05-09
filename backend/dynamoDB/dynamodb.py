# Access file for DynamoDB through AWS SDK for Python (Boto3)
# For use in AWS Lambda to handle API requests for fastener lookups
# NOT INTENDED FOR LOCAL DEVELOPMENT
import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["fastener-db"])


def lambda_handler(event, context):
    try:
        # Get code from query string: /search?code=ABC
        params = event.get("queryStringParameters") or {}
        code = params.get("code", "").strip().upper()

        # Validate that code is provided
        if not code:
            return response(400, {
                "error": "Missing fastener code"
            })

        # Query DynamoDB for the fastener with the given code
        result = table.get_item(
            Key={
                "code": code
            }
        )

        # Check if item exists in the result
        item = result.get("Item")

        # If no item is found, return a 404 response
        if not item:
            return response(404, {
                "error": "Fastener not found"
            })

        # Return the fastener details in the response
        return response(200, {
            "code": item.get("code"),
            "material": item.get("material"),
            "size": item.get("size"),
            "length": item.get("length"),
            "name": item.get("name")
        })

    # Catch any exceptions that occur during the process and return a 500 response with error details
    except Exception as e:
        return response(500, {
            "error": "Server error",
            "details": str(e)
        })


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps(body)
    }
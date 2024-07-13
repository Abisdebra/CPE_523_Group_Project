import boto3
import os
import json
from product_details import ProductDetails
import boto3

def handler(event, context):
    print(event["body"])
    event_body = json.loads(event["body"])

    dynamodb = boto3.resource("dynamodb")
    product = ProductDetails(dynamodb)  
    product.add_product(event_body["name"], event_body["price"], event_body["expiry_date"])
    

    return {
        "statusCode": 200,
        "body": json.dumps("Hello World!")
    }
from helper_funcs.downloadSCfile import get_chart
from helper_funcs.createImageGrid import createImage
import json

def lambda_handler(event, context):
    event_body = json.loads(event['body'])
    email_body = event_body['email_body']

    ticker = email_body.split(" ")[8] # ticker is the 9th word in the string
    
    data_1h = get_chart(ticker, '1h')
    data_4h = get_chart(ticker, '4h')
    data_1d = get_chart(ticker, '1d')
    data_1w = get_chart(ticker, '1w')

    createImage(
        data_1h,
        data_4h,
        data_1d,
        data_1w,
        ticker
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello chartstamp"
        }),
    }


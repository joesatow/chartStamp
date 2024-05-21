from helper_funcs.downloadSCfile import get_chart
from helper_funcs.createImageGrid import createImage
import json

def lambda_handler(event, context):
    ticker = event['queryStringParameters'].get('ticker', '')
    
    data_1h = get_chart(ticker, '1h')
    data_4h = get_chart(ticker, '4h')
    data_1d = get_chart(ticker, '1d')
    data_1w = get_chart(ticker, '1w')

    info = createImage(
        data_1h,
        data_4h,
        data_1d,
        data_1w,
        ticker
    )

    presigned_image_download_url = info['presigned_image_download_url']
    object_name = info['object_name']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello chartstamp",
            "url": presigned_image_download_url,
            "object_name": object_name
        }),
    }


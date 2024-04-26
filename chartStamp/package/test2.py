import json

# This should be the exact JSON string response from Lambda
lambda_response = '''
{
    "message": "hello chartstamp",
    "event": {
        "version": "2.0",
        "routeKey": "POST /stamp",
        "rawPath": "/stamp",
        "rawQueryString": "",
        "headers": {
            "accept-encoding": "gzip, deflate, br",
            "content-length": "190",
            "content-type": "application/json",
            "host": "3g9c0nk0124.execute-api.us-east-2.amazonaws.com",
            "user-agent": "Mozilla/5.0 (compatible; Google-Apps-Script; beanserver; +https://script.google.com; id: UAEmdDd-3dtqVxidl_f5aRbok2xuM5FdbIqg)",
            "x-amzn-trace-id": "Root=1-662afe5b-193915a479cc3e37720df8b7",
            "x-forwarded-for": "2600:1700:37a0:806f:7e12:4d1e:7ad5:197e, 107.178.203.230",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "requestContext": {
            "accountId": "728866571318",
            "apiId": "3g9c0nk0124",
            "domainName": "3g9c0nk0124.execute-api.us-east-2.amazonaws.com",
            "domainPrefix": "3g9c0nk0124",
            "http": {
                "method": "POST",
                "path": "/stamp",
                "protocol": "HTTP/1.1",
                "sourceIp": "107.178.203.230",
                "userAgent": "Mozilla/5.0 (compatible; Google-Apps-Script; beanserver; +https://script.google.com; id: UAEmdDd-3dtqVxidl_f5aRbok2xuM5FdbIqg)"
            },
            "requestId": "WzyuTibwCyCEJIw=",
            "routeKey": "POST /stamp",
            "stage": "$default",
            "time": "26/Apr/2024:01:07:39 +0000",
            "timeEpoch": 1714093659249
        }
    },
    "body": "{\"email_body\":\"Your limit order to buy 200 contracts of UPS $149.00 Call 4/26 in your brokerage account executed at an average price of $23.00 per contract on April 25, 2024 at 3:32 PM ET.\"}",
    "isBase64Encoded": false
}
'''

# Parse the response string into a Python dictionary
parsed_response = json.loads(lambda_response)

# Now extract the body which is also a JSON string
body_string = parsed_response['body']
parsed_body = json.loads(body_string)

# Now extract 'email_body' from the parsed body dictionary
email_body = parsed_body['email_body']

print(email_body)

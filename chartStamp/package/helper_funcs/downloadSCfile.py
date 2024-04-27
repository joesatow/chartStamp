import requests
import time
from requests import Response
from urllib.parse import urlencode
from user_agent import generate_user_agent
from aws_jserver import GetSecret

sc_cookie = GetSecret("SC-Cookie")

#sc_cookie = "test"
user_agent = generate_user_agent()

# [0] = Daily, [1] = 4h, [2] = 1h, [3] = 1w
iValues = ['p55738127392', 'p57289512688', 'p23851798625', 'p57719994331']

def get_chart(symbol, tf):
    if tf == '1d':
        selector = 0
    if tf == '4h':
        selector = 1
    if tf == '1h':
        selector = 2
    if tf == '1w':
        selector = 3

    millisecondsEpoch = str(int(time.time()*1000))

    # [0] = Daily, [1] = 4h, [2] = 1h, [3] = 1w
    payloadObjects = [
        {"s": symbol, "p": "D", 'i': iValues[selector], 'r': millisecondsEpoch},
        {"s": symbol, "p": "195", "i": iValues[selector], 'r': millisecondsEpoch},
        {"s": symbol, "p": "60", "i": iValues[selector], 'r': millisecondsEpoch},
        {"s": symbol, "p": "W", "i": iValues[selector], 'r': millisecondsEpoch}
    ]

    encoded_payload = urlencode(
            payloadObjects[selector]
        )
    
    url = f"https://stockcharts.com/c-sc/sc?{encoded_payload}"
    response = stockCharts_request(url, user_agent)
    # fileName = download_chart_image(response, url, tf)
    return response.content

def stockCharts_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={
        "cookie": sc_cookie, 
        "User-Agent": user_agent
    })
    return response

import requests
import json
import os
import pprint
pp = pprint.PrettyPrinter(indent=4)

API_KEY = os.environ['APIKEY']


def get_weather_data(lat, lng):
    """makes API call to return weather data"""
    lat = str(lat)
    lng = str(lng)

    request_url = "https://api.forecast.io/forecast/%s/%s,%s" % (API_KEY, lat, lng)

    r = requests.get(request_url)
    resp = json.loads(r.text)

    pp.pprint(resp)

    results = []
    for item in resp['currently']:
        results.append({'temp': item['apparentTemperature'],
                        'humidity': item['humidity']})

    return results

get_weather_data(37.7749, 122.4194)

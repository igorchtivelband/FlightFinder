__author__ = 'igorchtivelband'
import ConfigLoader
import PriceMailer
import urllib2
import json


def sendRequest():
    request_url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='+conf_loader.qpx__express_api_key
    f = open('./config/flight_details.json', 'rb')
    json_data = json.load(f)
    jsonreq = json.dumps(json_data)
    req = urllib2.Request(request_url, jsonreq, {'Content-Type': 'application/json'})
    flight = urllib2.urlopen(req)
    response = flight.read()
    flight.close()
    return response

def analyzeResults(json_response):
    json_data = json.loads(json_response)
    lowest_price_with_currency = json_data["trips"]["tripOption"][0]["saleTotal"]
    if (lowest_price_with_currency[:3]=='EUR'):
        lowest_price = lowest_price_with_currency[3:]
        if ( float(lowest_price) < float(conf_loader.price_threshold)):
            print (lowest_price)
            PriceMailer.sendPriceEmail(lowest_price,conf_loader.target_email, conf_loader.SMTP_SERVER, conf_loader.SMTP_PORT, conf_loader.SMTP_USERNAME, conf_loader.SMTP_PASSWORD)


if __name__ == '__main__':
    conf_loader = ConfigLoader.ConfigLoader()
    response = sendRequest()
    analyzeResults(response)


import http.client
import urllib.parse
import time

key = "AT68QYQ94MQEWXL3"  # Put your API Key here


def lab4task():
    while True:
        # Calculate CPU temperature of Raspberry Pi in Degrees C
        group = "L3-T-3"
        email = "thomaspoetting@cmail.carleton.ca"
        ident = "c"

        params = urllib.parse.urlencode(
            {'field1': group, 'field2': email, 'field3': ident, 'key': key})  # thingspeak fields

        headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}

        conn = http.client.HTTPConnection("api.thingspeak.com:80")

        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()

            # print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break


if __name__ == "__main__":
    while True:
        lab4task()
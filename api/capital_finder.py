from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        s = self.path
        url = parse.urlsplit(s)
        query_str =parse.parse_qsl(url.query)
        dic = dict(query_str)
        country = dic.get("country")
        capital = dic.get("capital")
        # print(country)

     
        if country:
            url="https://restcountries.com/v3.1/name/"
            res = requests.get(url+country)
            data = res.json()
            result = data[0]["capital"][0]
            # print(url)

            Result = "The capital of "+country+" is "+result+"."

        if capital:
            url="https://restcountries.com/v3.1/capital/"
            res = requests.get(url+capital)
            data = res.json()
            result = data[0]["name"]["common"]
            # print(url)

            Result = capital+" is the capital of "+result+"."



        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(Result.encode('utf-8'))
        return
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
        print(country)

        capital=""
        if country:
            url="https://restcountries.com/v3.1/all"
            res = requests.get(url)
            data = res.json()
            # for i in data:
            #     if i[0]["common"] == country:
            #         capital = i[11][0]
            #         return 


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
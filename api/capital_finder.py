from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        s = self.path
        url = parse.urlsplit(s)
        query_str =parse.parse_qsl(url.query)
        dic = dict(query_str)
        country = dic.get("country")
        print(country)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(country.encode('utf-8'))
        return
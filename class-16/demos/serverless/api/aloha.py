"""
Python files within the api directory, containing an handler variable that inherits from the BaseHTTPRequestHandler
"""
from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # parse the query
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get("name")


        # response code
        self.send_response(200)

        # headers
        self.headers.add_header("Content-type", "text/plain")
        self.end_headers()

        # create message
        message = f"Aloha to {name}"

        # respond with the formatted current time?
        self.wfile.write(message.encode())

        return

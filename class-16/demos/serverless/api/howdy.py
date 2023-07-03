"""
Python files within the api directory, containing an handler variable that inherits from the BaseHTTPRequestHandler
"""
from datetime import datetime
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # response code
        self.send_response(200)

        # headers
        self.headers.add_header("Content-type", "text/plain")
        self.end_headers()

        # create message
        message = "Howdy"

        # respond with the formatted current time?
        self.wfile.write(message.encode())

        return

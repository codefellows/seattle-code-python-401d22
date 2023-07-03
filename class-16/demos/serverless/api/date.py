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

        # format time
        formatted_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # respond with the formatted current time?
        self.wfile.write(formatted_time.encode())

        return

# character by char while looking at other screen
from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

# https://serverless-fawn-iota.vercel.app/api/aloha?name=Roger
# Hello Roger.  How are you?
# Hello Stranger.  Stranger Danger!
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        given_dictionary = dict(query_string_list)
        name = given_dictionary.get('name')

        if name:
            message = f"Hello {name}.  How are you?"
        else:
            message = "Hello Stranger.  Stranger Danger!"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message += " " + platform.python_version()
        self.wfile.write(message.encode())
        return
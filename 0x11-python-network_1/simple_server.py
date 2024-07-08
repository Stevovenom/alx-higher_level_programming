#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        email = post_data.get('email', [None])[0]
        response = f"Your email is: {email}"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Starting server at http://0.0.0.0:5000")
    httpd.serve_forever()


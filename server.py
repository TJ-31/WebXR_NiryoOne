import http.server
import socketserver
import os

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

port = 8000
directory = os.path.join(os.getcwd(), 'webXR')  # Update the directory path accordingly

with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
    print("Serving at port", port)
    httpd.serve_forever()

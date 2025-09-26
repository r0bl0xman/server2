# -*- coding: UTF-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "話し合いの場"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>my web server</title></head>", "utf-8"))
        self.wfile.write(bytes("<h1>Request: %s</h1>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h2>This is my web server.</h2>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))




print('Create server...')

webServer = HTTPServer((hostName, serverPort), MyServer)

print('Open safari...')
# open safari
import webbrowser
webbrowser.open("http://localhost:8080/path")


try:
    webServer.serve_forever()

except:
    pass

webServer.server_close()
print("Server stopped.")

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

PORT = 65432

class CORSRequestHandler (SimpleHTTPRequestHandler):
  def end_headers (self):
    self.send_my_headers()
    self.send_header('Access-Control-Allow-Origin', '*')
    SimpleHTTPRequestHandler.end_headers(self)

  def send_my_headers(self):
    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
    self.send_header("Pragma", "no-cache")
    self.send_header("Expires", "0")

httpd = HTTPServer(('localhost', PORT), CORSRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="key.pem", certfile='cert.pem', server_side=True)
print("Server running in port {}".format(PORT))
httpd.serve_forever()

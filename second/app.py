from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

def run(server_class=HTTPServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, SimpleHandler)
    print(f'Serving on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

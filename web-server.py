from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

class DateHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        now = datetime.datetime.now()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Current Date</title>
        </head>
        <body>
            <h1>Current Date and Time</h1>
            <p>{now}</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, DateHandler)
    print(f"Server listening on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()
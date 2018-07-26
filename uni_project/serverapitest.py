#!/usr/bin/env python3
"""

Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from pymongo import *

client = MongoClient()
db = client.test
mycollection = db["auth_user"]


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        
        if self.path[:11] == "/subscribe/":
            self._set_response()
            test = self.path[17:]
            print(test)
            test2 = test.split("&")
            print(test2)
            print(test2[0])
            email = test2[0]
            band = test2[1][5:]
            print(band)
            collections = (db.collection_names())
            if band in collections and "auth_user" in collections:
                mycollection.find_and_modify(query={'email': email}, update={"$set": {'following_artists': band}}, upsert=False, full_response=True)
                self.wfile.write("You have followed Rise Against".format(self.path).encode('utf-8'))
                self.wfile.write('<br><a href="http://127.0.0.1:8000/webscraper/show/">Return</a>'.format(self.path).encode('utf-8'))
            else:
                print("None is not an email")
        else:
            self._set_response()
            self.wfile.write("You are not signed in, please sign in to follow an artist{}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
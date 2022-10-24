#!/usr/bin/env python

# -*- coding:utf-8 -*-
import BaseHTTPServer
# import logging
import random
import sys
import time


# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG)


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    Page = '200 OK'

    def do_GET(self):
        path = self.path
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)
        cost_time = random.randint(150, 300)
        status = random.choice([200, 201, 302, 301, 400, 404, 403, 405, 500])
        if status <= 405:
            sys.stdout.write("%s INFO: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))
        else:
            sys.stdout.write("%s ERROR: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import BaseHTTPServer
import random
import time
import sys
import logging
from logging import handlers


# logger = logging.getLogger()
# # logger.setLevel(logging.INFO)
# # handler = logging.StreamHandler(sys.stdout)
# # logger.addHandler(handler)
# logging.basicConfig(level=logging.DEBUG,
#                     filename='./log/api.log',
#                     filemode='a',
#                     format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     )


def _get_logger(filename):
    # 创建日志对象
    log = logging.getLogger(filename)
    # 设置日志级别
    log.setLevel(logging.DEBUG)
    # 日志输出格式
    fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 输出到控制台
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(fmt)
    # 输出到文件
    # 日志文件按天进行保存，每天一个日志文件
    file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')
    # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
    file_handler.setFormatter(fmt)

    log.addHandler(console_handler)
    log.addHandler(file_handler)
    return log


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
            # sys.stdout.write("%s INFO: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))
            logger.info("%s INFO: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))
        else:
            logger.error("%s ERROR: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))
            # sys.stdout.write("%s ERROR: path=%s status=%s cost_time=%s " % (time.time(), path, status, cost_time / 10))


if __name__ == '__main__':
    logger = _get_logger('./log/api.log')
    serverAddress = ('', 80)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

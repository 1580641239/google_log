# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
"""
Authors:     huozhirui(huozhirui@baidu.com)
Date:        2022/11/29 14:40
File:        app
Software:    PyCharm
"""
import os
from loguru import logger
import random
import time
import uuid
from flask import Flask

app = Flask(__name__)  # 记住这里的变量名app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(BASE_DIR, 'log/access.log')
err_log_file_path = os.path.join(BASE_DIR, 'log/err.log')
logger.remove(handler_id=None)

sufix_file_path = os.path.join(BASE_DIR, 'log/isis.log.{time:YYYYMMDDHH}')
logger.add(err_log_file_path, format="{message}", rotation="1 H", level="CRITICAL",
           enqueue=True, encoding='utf-8',
           retention=2)

logger.add(log_file_path, format="{message}", rotation="1 H", level="INFO",
           enqueue=True, encoding='utf-8',
           retention=2)

logger.add(sufix_file_path, format="{time} {message}", rotation="1 H", encoding='utf-8', retention=2, level='ERROR')

from_service = ["za-%s" % (i) for i in range(5)]
to_module = ["nz-az-%s" % (i) for i in range(4, 9)]


@app.route('/')
def index():
    line = f"[ISIS] [{time.strftime('%d/%b/%Y:%H:%M:%S +0800', time.localtime(time.time()))}] logid={uuid.uuid5(uuid.NAMESPACE_URL, str(random.randint(0, 1000))).hex} " \
           "callid=cdmdqm00rjlds35qglfg local_hostname=ax01-xaxax-axa-.ax01 " \
           "remote_addr=127.0.0.1 server_addr=- host=127.0.0.1 client_costtime=0.18 " \
           f"http_code={random.randint(200, 599)} req_time=0.000 client_timeout=- timeout_quantile=- " \
           f"fault=- sdk_version=GO-1.0.0.6 request_from=local ufc_time={random.randint(1, 9) / 10} " \
           f"to_module={random.choice(to_module)} ufc_backup=- from_service={random.choice(from_service)} " \
           "update_lantency=10 ori_to_service=q-table " \
           "api=/pwds method=get from_idc=abx " \
           "interact=[[callid=cdmdqm00rjlds35qglfg cost_time=0.000 to_module=sa-table " \
           "to_bns=netsa-proxy.TABLE.yq01 to_ip=10.123.725.124:000 to_idc=- upstream_status=200]]"

    logger.info(line)
    logger.critical(line)
    try:
        1 / 0
    except Exception:
        err = """
Traceback (most recent call last):
File "/threading.py", line 890, in _bootstrap
self._bootstrap_inner()
│    └ <function Thread._bootstrap_inner at 0x1008f75e0>
└ <Thread(Thread-4, started daemon 6235107328)>
File "/python3.8/threading.py", line 932, in _bootstrap_inner
self.run()
│    └ <function Thread.run at 0x1008f7310>
└ <Thread(Thread-4, started daemon 6235107328)>
        """
        logger.error(err)
    return line


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 clowwindy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the right to use
# , copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to premit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substatial portinos of the software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, NICLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILTY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTTIN WITH THE SOFTWARE OR THE USE OF OTHER DEALINGS IN THE SOFTWARE.

from __future__ import absolute_import, division, print_function, with_statement

import sys
import os
import logging
import signal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from shadowsocks import utils, daemon, encrypt, eventloop, tcprelay, udprelay, \
asyncdns


def main():
	utils.check_python()

	config = utils.get_config(False)

	daemon.daemon_exec(config)

	utils.print_shadowsocks()

	if config['port_password']:
		if config['password']:
			logging.warning('warning: port_password should not be used with '
				            'server_port and password. server_port and password '
				            'will be ignored')
		else:
			
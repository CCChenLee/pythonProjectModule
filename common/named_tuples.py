#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#
#定义必须的名称元组

import collections

#用于MySQL的服务信息

MySQL=collections.namedtuple('MySQL',['host','user','password','port','charset','schema'])

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DataHandler.py
@Time    :   2019/11/20 16:51:18
@Author  :   sui mingyang 
@Version :   0.0.1
@Contact :   suimingyang123@gmail.com
@License :   (C)Copyright 2018-2019, weidian
@Desc    :   None
'''
from Helper.DataHelper import DataHelper
from Config.base import conf,variable
# 数据处理
class DataHandler(object):
    def __init__(self,host,username,password):
        #host=conf.get('neo4j','server'),username=conf.get('neo4j','user'),password=conf.get('neo4j','pwd')
        self.helper=DataHelper(host=host,username=username,password=password)
    
    def update_by_day(self):
        pass

    def update_intime(self):
        pass

    def co_recommend_by_product(self):
        pass

    def co_recommend_by_user(self):
        pass

    def recommend_by_graph(self,top):
        pass


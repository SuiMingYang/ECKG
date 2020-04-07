#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DataHelper.py
@Time    :   2019/11/20 16:50:51
@Author  :   sui mingyang 
@Version :   0.0.1
@Contact :   suimingyang123@gmail.com
@License :   (C)Copyright 2018-2019, weidian
@Desc    :   None
'''

from py2neo import Graph,Node,Relationship,Subgraph


### 数据交互层,封装orm
# 聊天数据解析成可录入的信息，增量更新：用户偏好，商品。

class DataHelper(object):
    def __init__(self,host,username,password):
        self.cursor = Graph(host=host,username=username,password=password)
    
    def truncate(self):
        self.cursor.run('match (n) detach delete n;')

    def match_to_node(self,entity,condition):
        return self.cursor.run("MATCH (p:{entity} {{{where}}}) RETURN p limit 1".format(entity=entity,where=condition)).evaluate()
        
    def update_or_insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

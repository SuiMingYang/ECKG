from aliyun.log import LogClient
from aliyun.log import GetLogsRequest
import pymysql
from py2neo import Graph,Node,Relationship,Subgraph,NodeMatcher

class ossdataserver:
    def __init__(self,endpoint,accessKeyId,accessKey,basename,tablename):
        
        self.endpoint = endpoint #http://oss-cn-hangzhou.aliyuncs.com
        # 用户访问秘钥对中的 AccessKeyId。
        self.accessKeyId = accessKeyId
        # 用户访问秘钥对中的 AccessKeySecret。
        self.accessKey = accessKey
        self.basename = basename
        self.tablename = tablename
        self.client = LogClient(self.endpoint, self.accessKeyId, self.accessKey)
    def close(self):
        #self.client.shutdown()
        pass
    # def database(self,basename,tablename):
    #     self.basename=basename
    #     self.tablename=tablename

class mysqlserver:
    def __init__(self,host,port,user,passwd,db):
        #pymysql.connect('rm-bp171b759ha99x5wfso.mysql.rds.aliyuncs.com',port=3306,user='root',passwd='HPGQEhutFBUCi8ZE8JYgWDwZVhAHXWJx',db='businessdata')
        self.host=host
        self.port=port 
        self.user=user
        self.passwd=passwd
        self.db=db
        self.conn = pymysql.connect(self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)
    def close(self):
        self.conn.close()

class neo4jserver:
    """
    封装neo4j的orm
    """
    def __init__(self,url,name,pwd):
        #pymysql.connect('rm-bp171b759ha99x5wfso.mysql.rds.aliyuncs.com',port=3306,user='root',passwd='HPGQEhutFBUCi8ZE8JYgWDwZVhAHXWJx',db='businessdata')
        self.graph = Graph(url,username=name,password=pwd)
        self.start = self.graph.begin()
        
    def close(self):
        #self.start.close()
        pass

    def insert_entity(self,data):
        self.start.create(data)
        self.start.commit()

    def insert_relation(self,data=[],relation=[]):
        data=Subgraph(data,relationships=relation)
        self.start.create(data)
        self.start.commit()

    def select_entity_sql(self,sql):
        self.graph.run(sql).data()  # list型
        self.graph.run(sql).to_data_frame()  # dataframe型
        self.graph.run(sql).to_table()  # table
    
    def select_entity_cond(self,obj,condition):
        self.matcher = NodeMatcher(self.graph)
        self.matcher.match("Person", name="Kevin").first()
        self.matcher.match("Person", name__not="Rick Astley").first()

    '''
    描述	后缀	示例
    表达相等	__exact	matcher.match(“Person”, name__exact="Kevin Bacon")
    表达不相等	__not	matcher.match(“Person”, name__not="Rick Astley")
    表达大于	__gt	matcher.match(“Person”, born__gt=1985)
    表达大于等于	__gte	matcher.match(“Person”, born__gte=1965)
    表达小于	__lt	matcher.match(“Person”, born__lt=1965)
    表达小于等于	__lte	matcher.match(“Person”, born__lte=1965)
    以XX开头	__startswith	matcher.match(“Person”, name__startswith="Kevin")
    以XX结尾	__endswith	matcher.match(“Person”, name__endswith="Smith")
    包含关系	__contains	matcher.match(“Person”, name__contains="James")
    '''
from py2neo import Graph,Node,Relationship,Subgraph
from Config.base import conf,variable
graph = Graph('http://localhost:7474',username='neo4j',password='smy769')
import inspect

p1=graph.nodes.match("product", pid="227071").first()
print(p1)

gql="MATCH (p1:product)-[k:KNOWS]->(p2:Person) RETURN *"
cursor=graph.run(gql)

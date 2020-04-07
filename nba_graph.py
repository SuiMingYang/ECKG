from py2neo import Graph,Node,Relationship,Subgraph

graph = Graph('http://localhost:7474',username='neo4j',password='123456')

tx = graph.begin()

# ### 增加
# # 可以一个一个创建
# a = Node('Person',name='bubu')
# graph.create(a)
# b = Node('Person',name='kaka')
# graph.create(b)
# r = Relationship(a,'KNOWS',b)
# graph.create(r)

# # 也可以一次性创建
# s = a | b | r
# graph.create(s)
opera=[]
data={
    'person':[
        {'id':'0','name':u'恩比德','height':'2.13','age':'23','team':'76人'},
        {'id':'1','name':u'科比','height':'1.96','age':'42','team':'湖人'},
        {'id':'2','name':u'詹姆斯','height':'2.03','age':'35','team':'湖人'},
        {'id':'3','name':u'韦德','height':'1.93','age':'38','team':'热火'},
        {'id':'4','name':u'安东尼','height':'2.03','age':'36','team':'尼克斯'},
        {'id':'5','name':u'欧文','height':'1.91','age':'29','team':'篮网'},
        {'id':'6','name':u'杜兰特','height':'2.11','age':'32','team':'篮网'},
        {'id':'7','name':u'戴维斯','height':'2.10','age':'28','team':'湖人'},
        {'id':'8','name':u'乔治','height':'2.06','age':'31','team':'快船'},
        {'id':'9','name':u'保罗','height':'1.85','age':'34','team':'雷霆'},
        {'id':'10','name':u'伦纳德','height':'2.03','age':'33','team':'快船'},
        {'id':'11','name':u'哈登','height':'1.98','age':'33','team':'火箭'},
        {'id':'12','name':u'库里','height':'1.91','age':'33','team':'勇士'},
        {'id':'13','name':u'汤普森','height':'2.03','age':'32','team':'勇士'},
        {'id':'14','name':u'格林','height':'1.98','age':'31','team':'勇士'},
        {'id':'15','name':u'维斯布鲁克','height':'1.91','age':'30','team':'火箭'}
    ],
    'team':[
        {'id':'0','name':'湖人','location':'洛杉矶'},
        {'id':'1','name':'热火','location':'迈阿密'},
        {'id':'2','name':'快船','location':'洛杉矶'},
        {'id':'3','name':'勇士','location':'金州'},
        {'id':'4','name':'火箭','location':'休斯顿'},
        {'id':'5','name':'尼克斯','location':'纽约'},
        {'id':'6','name':'雷霆','location':'俄克拉马荷'},
        {'id':'7','name':'篮网','location':'新泽西'},
        {'id':'8','name':'76人','location':'费城'},
    ],
    'mvp':[
        {'id':'0','year':'2010'},
        {'id':'2','year':'2012'},
        {'id':'3','year':'2013'},
        {'id':'4','year':'2014'},
        {'id':'5','year':'2015'},
        {'id':'6','year':'2016'},
        {'id':'7','year':'2017'},
        {'id':'8','year':'2018'}
    ],
    'fmvp':[
        {'id':'0','year':'2010'},
        {'id':'2','year':'2012'},
        {'id':'3','year':'2013'},
        {'id':'4','year':'2014'},
        {'id':'5','year':'2015'},
        {'id':'6','year':'2016'},
        {'id':'7','year':'2017'},
        {'id':'8','year':'2018'}
    ],
    'relation':[
        ['p3','brother','p4'],
        ['p2','brother','p4'],
        ['p2','brother','p3'],
        ['p9','brother','p2'],
        ['p9','brother','p3'],
        ['p9','brother','p4'],
        ['p15','brother','p6'],

        ['p2','sameboth','p12'],
        ['p1','teacher','p11'],

        ['p2','teammate','p7'],
        ['p1','teammate','p2'],
        ['p5','teammate','p6'],

        ['p15','work','t4'],
        ['p14','work','t3'],
        ['p13','work','t3'],
        ['p12','work','t3'],
        ['p11','work','t4'],
        ['p10','work','t2'],
        ['p9','work','t6'],
        ['p8','work','t2'],
        ['p7','work','t0'],
        ['p6','work','t7'],
        ['p5','work','t7'],
        ['p4','work','t5'],
        ['p3','work','t1'],
        ['p2','work','t0'],
        ['p1','work','t0'],
        ['p0','work','t8'],

        ['m0','grant','p2'],
        ['m2','grant','p2'],
        ['m3','grant','p2'],
        ['m4','grant','p6'],
        ['m5','grant','p12'],
        ['m6','grant','p12'],
        ['m7','grant','p15'],
        ['m8','grant','p11'],

        ['f0','grant','p1'],
        ['f2','grant','p2'],
        ['f3','grant','p2'],
        ['f4','grant','p10'],
        ['f5','grant','p12'],
        ['f6','grant','p2'],
        ['f7','grant','p6'],
        ['f8','grant','p6'],

    ]
}
person='person'
for i,item in enumerate(data[person]):
    locals()["p"+item['id']] = Node(person,name='{}'.format(item['name']),height='{}'.format(item['height']),age='{}'.format(item['age']),team='{}'.format(item['team']))
    #locals()["p"+item['id']] = Node(person,name='{}'.format(item['name']))
    #graph.create(locals()["p"+item['id']])
    opera.append(locals()["p"+item['id']])

team='team'
for i,item in enumerate(data[team]):
    locals()["t"+item['id']] = Node(team,name='{}'.format(item['name']),location='{}'.format(item['location']))
    #r = Node(person,name='{}'.format(item['name']))
    #graph.create(locals()["t"+item['id']])
    opera.append(locals()["t"+item['id']])

mvp='mvp'
for i,item in enumerate(data[mvp]):
    locals()["m"+item['id']] = Node(mvp,name='{}'.format(item['year']))
    #r = Node(person,name='{}'.format(item['name']))
    #graph.create(locals()["t"+item['id']])
    opera.append(locals()["m"+item['id']])

fmvp='fmvp'
for i,item in enumerate(data[fmvp]):
    locals()["f"+item['id']] = Node(fmvp,name='{}'.format(item['year']))
    #r = Node(person,name='{}'.format(item['name']))
    #graph.create(locals()["t"+item['id']])
    opera.append(locals()["f"+item['id']])

rela=[]
relation='relation'
for i,item in enumerate(data[relation]):
    r = Relationship(locals()[item[0]],item[1],locals()[item[2]])
    #r = Node(person,name='{}'.format(item['name']))
    #graph.create(r)
    rela.append(r)

### 事务
opera=Subgraph(opera,relationships=rela)
tx.create(opera)
tx.commit()






from py2neo import Graph,Node,Relationship,Subgraph
from Config.base import conf,variable
graph = Graph(host=conf.get('neo4j','server'),username=conf.get('neo4j','user'),password=conf.get('neo4j','pwd'))
import inspect

graph.run('match (n) detach delete n;')

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

data={
    'product':[
        {'id':'0','name':'重磅真丝衬衫纯色女长袖名媛优雅桑蚕丝弹力绸缎上衣','pid':'221725','price':129,'main_pic':'FsHngvAP3aoUeeJbqrcCzR6qBh5V','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'1','name':'新式改良版旗袍优雅花鸟民国风修身旗袍','pid':'314256','price':319,'main_pic':'FtOthj3HT-HmYve17MWuRKQhyyOW','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'2','name':'夏季新款韩版百搭网面厚底增高休闲女鞋透气运动鞋潮','pid':'123567','price':220,'main_pic':'FmKyMBnERw2yY8AS8CcLoc5aL9pD','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'3','name':'2019夏季新款拖鞋女时尚粗跟一字凉拖鞋女鞋hh2','pid':'928716','price':79,'main_pic':'Fi2bTm24Bt3Do2sd3Cyjn32oF4dN','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'4','name':'妈妈鞋浅口单鞋坡跟软底女士皮鞋休闲中老年平底','pid':'276365','price':88,'main_pic':'Fm19tlUsBHijnf9JO0fiF7ClfXgn','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'5','name':'复古印花连体裤女春款女装洋气时尚显瘦收腰长袖雪纺两件套长裤','pid':'273612','price':139,'main_pic':'Fh2nXeeHLasOjE4PNWY712WNoq6h','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'6','name':'连衣裙2018新款夏装韩版显瘦宽松大码女装短袖碎花气质长裙子','pid':'383271','price':146,'main_pic':'dfe5eaac833d4c3a9a42d8e7106bae17','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'7','name':'秋冬新款加厚中长款毛衣套头针织打底衫线衣','pid':'283721','price':160,'main_pic':'FtHloKAkrloIPLkuDHf8BDwpE4nd','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'8','name':'毛衣女秋冬韩版新款弹力纯色修身长袖套头花边领毛针织衫打底衫女','pid':'127361','price':260,'main_pic':'Fj1dvXTi0GuacO0EPCGTOKajLRkV','details':'4aeaa9de11c34759b1da99daa4cb5361'},
        {'id':'9','name':'收口袖潮流拼接气质休闲时尚纯色拼色2018年秋季圆领','pid':'326139','price':218,'main_pic':'FgfMbfLxtMsAHUUa5J6rQd4rvuVw','details':'4aeaa9de11c34759b1da99daa4cb5361'}
    ],
    'user':[
        {'id':'0','name':'张三','uid':'12345678','age':48,},
        {'id':'1','name':'李四','uid':'27362812','age':26,},
        {'id':'2','name':'王五','uid':'28172831','age':24,},
        {'id':'3','name':'赵六','uid':'12738173','age':22,},
        {'id':'4','name':'田七','uid':'47162718','age':34,},
        {'id':'5','name':'周八','uid':'18271783','age':36,}
    ],
    'mp_alies':[
        {'id':'0','name':'女王新款'},
        {'id':'1','name':'女王轻奢'},
        {'id':'2','name':'女王新款+'}
    ],
    'style':[
        {'id':'0','name':'少女'},
        {'id':'1','name':'休闲'},
        {'id':'2','name':'淑女'},
        {'id':'3','name':'大气'},
        {'id':'4','name':'通勤'},
        {'id':'5','name':'职业'},
        {'id':'6','name':'运动'},
        {'id':'7','name':'家居'},
        {'id':'8','name':'商务'},
        {'id':'9','name':'百搭'},
        {'id':'10','name':'简约'},
        {'id':'11','name':'奢华'}
    ],
    'category':[
        {'id':'0','name':'连衣裙'},
        {'id':'1','name':'裤子'},
        {'id':'2','name':'上衣'},
        {'id':'3','name':'套装'},
        {'id':'4','name':'鞋子'},
        {'id':'5','name':'箱包'},
        {'id':'6','name':'配饰'}
    ],
    'material':[
        {'id':'0','name':'真丝'},
        {'id':'1','name':'棉麻'},
        {'id':'2','name':'纯棉'},
        {'id':'3','name':'聚酯纤维'}
    ],
    'effect':[
        {'id':'0','name':'保暖'},
        {'id':'1','name':'耐磨'},
        {'id':'2','name':'显瘦'},
        {'id':'3','name':'显白'},
        {'id':'4','name':'显腿长'},
        {'id':'5','name':'塑型'}
    ],
    'size':[
        {'id':'0','name':'S','zh':'小码'},
        {'id':'1','name':'M','zh':'中码'},
        {'id':'2','name':'L','zh':'大码'},
        {'id':'3','name':'XL','zh':'超大码'},
        {'id':'4','name':'XXL','zh':'特大码'},
        {'id':'5','name':'XXXL','zh':'最大码'}
    ],
    'store':[
        {'sid':'0','name':'杰克琼斯'},
        {'sid':'1','name':'波司登'},
        {'sid':'2','name':'海澜之家'},
        {'sid':'3','name':'优衣库'},
        {'sid':'4','name':'美特斯邦威'},
        {'sid':'5','name':'花花公子'},
        {'sid':'6','name':'纺织厂'}
    ],
    'stereo':[
        {'id':'0','name':'修身'},
        {'id':'1','name':'宽松'},
        {'id':'2','name':'大码'},
        {'id':'3','name':'紧身'}
    ],
    'sale':[
        {'sid':'123','name':'萧峰'},
        {'sid':'234','name':'虚竹'},
        {'sid':'345','name':'段誉'},
        {'sid':'456','name':'令狐冲'},
        {'sid':'567','name':'岳不群'},
        {'sid':'678','name':'狄云'},
        {'sid':'789','name':'郭靖'},
        {'sid':'890','name':'黄蓉'},
        {'sid':'901','name':'欧阳锋'}
    ],
    'team':[
        {'tid':'0','name':'缥缈峰'},
        {'tid':'1','name':'光明顶'},
        {'tid':'2','name':'唐门'},
        {'tid':'3','name':'逍遥派'},
        {'tid':'4','name':'侠客岛'},
        {'tid':'5','name':'聚贤庄'},
        {'tid':'6','name':'丐帮'}
        
    ],
    'transport':[
        {'id':'0','name':'顺丰','speed':'一天内'},
        {'id':'1','name':'申通','speed':'三天内'},
        {'id':'2','name':'圆通','speed':'三天内'},
        {'id':'3','name':'中通','speed':'三天内'},
        {'id':'4','name':'韵达','speed':'三天内'},
        {'id':'5','name':'百世','speed':'五天内'},
        {'id':'6','name':'菜鸟','speed':'二天内'},
        {'id':'7','name':'自营','speed':'联系客服'}
    ],
    'bodyfeature':[
        {'id':'0','name':'苹果型','abstract':'腰粗+臀小+腿相对长细','introduct':'苹果型是比较好判断的一种体型，判断的关键就是腰围。体重120+，腰围超过80cm，臀围相对比较小，腿比较长，不算太粗（和腰比），一般都属于苹果型身材。','suit':['宽松上衣','铅笔裤','直筒裤']},
        {'id':'1','name':'H型','abstract':'瘦+腰短腿长','introduct':'H型身材必须要瘦一点，其次是腰胸臀围差不太多，胸臀不大，腰也不细，腰围一般65-70cm之间，肩胯也不能太宽，腿要长（粗点倒没事）。','suit':['铅笔裤','直筒裤']},
        {'id':'2','name':'梨型','abstract':'微胖+臀大+腰不太细','introduct':'梨形身材有时候是会和翘臀的沙漏型搞混。沙漏的腰一定是比较细的，腰围一般应该小于70cm，而且胸围比较大，而梨形的腰不会太细，胸围也不太大。','suit':[]},
        {'id':'3','name':'细沙漏型','abstract':'细腰+有胸+翘臀','introduct':'细沙漏型，对身材要求非常高，一般腰围小于65cm，胸臀都有小小的挺起，就算细沙漏型。比如舒淇，就是典型的亚洲细沙漏型身材。','suit':[]},
        {'id':'4','name':'长方形','abstract':'肩宽胯大+没胸没屁股','introduct':'有的妹纸，肉肉并不多，没胸没屁股，但肩宽胯大，这就属于长方形身材，也是俗称的大骨架。长方体型重点是人要比较瘦，如果你虽然是长方体型，但本身就有胸有屁股，那还是沙漏型。','suit':[]},
        {'id':'5','name':'V型','abstract':'肩宽','introduct':'V型又叫倒三角型，这个一般很少搞错，因为特点特别明显，就是肩宽胯窄的体型,而且腰也不会特别细。就是整个人看起来很壮，有点像运动员的赶脚。如果背厚，那是V型里面的分支草莓型。小个子女生+V型，会有点困扰。','suit':[]},
        {'id':'6','name':'圆型','abstract':'腰粗+臀大+腿相对长细','introduct':'圆形体型腿比较粗，臀部比较大，而苹果型腿应该不是特别粗，臀部也不是很大。总之，无论苹果和圆型身材，肚子都很大，但圆型的屁股也很大。一般又矮又胖的体型，属于圆形体型。','suit':[]},
        {'id':'7','name':'胖沙漏型','abstract':'细腰+有胸+翘臀+胖','introduct':'胖沙漏型和圆形的区别是，胖沙漏型腰臀比一般都比较好，胸也比较大。全身呈现一种均匀的胖。胖沙漏型的女生一定首先是胖人。','suit':[]},
        {'id':'8','name':'五五分型','abstract':'腰长+腿短','introduct':'五五型就是腿特别短，腰特别长。','suit':['连衣裙']},
        {'id':'9','name':'瘦小型','abstract':'个矮+瘦','introduct':'一般身高<155,又非常瘦，就算瘦小型。','suit':[]},
        {'id':'10','name':'超高型','abstract':'个高','introduct':'超高型的目标也很独特，为了显矮。所以也单独列出来了。不管怎么说，高个子都是很好的优势。','suit':[]},
        {'id':'11','name':'I型','abstract':'个头中等+非常瘦','introduct':'I型是指个子不矮，一般160以上，但人非常消瘦，80斤出头，如果你已经因瘦而非常烦恼了，一般就属于I型，一般I型都有肩窄或者胯小的问题。','suit':[]}
    ]
}

relation={
    '品类':[
        [{'pid':'221725'},{'name':'上衣'}],
        [{'pid':'314256'},{'name':'裤子'}],
        [{'pid':'123567'},{'name':'裤子'}],
        [{'pid':'928716'},{'name':'上衣'}],
        [{'pid':'276365'},{'name':'套装'}],
        [{'pid':'273612'},{'name':'鞋子'}],
        [{'pid':'383271'},{'name':'连衣裙'}],
        [{'pid':'283721'},{'name':'箱包'}],
        [{'pid':'127361'},{'name':'鞋子'}],
        [{'pid':'326139'},{'name':'套装'}]
    ],
    '购买':[
        [{'uid':'12345678'},{'pid':'221725'},{'date':'2019-07-10'}],
        [{'uid':'12345678'},{'pid':'221725'},{'date':'2019-08-11'}],
        [{'uid':'27362812'},{'pid':'314256'},{'date':'2019-06-09'}],
        [{'uid':'28172831'},{'pid':'123567'},{'date':'2019-08-23'}],
        [{'uid':'12738173'},{'pid':'928716'},{'date':'2019-11-16'}],
        [{'uid':'47162718'},{'pid':'276365'},{'date':'2020-02-01'}],
        [{'uid':'18271783'},{'pid':'273612'},{'date':'2019-06-09'}],
        [{'uid':'12345678'},{'pid':'383271'},{'date':'2019-07-10'}],
        [{'uid':'27362812'},{'pid':'283721'},{'date':'2019-09-10'}],
        [{'uid':'28172831'},{'pid':'127361'},{'date':'2019-08-10'}],
        [{'uid':'12738173'},{'pid':'326139'},{'date':'2019-04-10'}],
        [{'uid':'47162718'},{'pid':'221725'},{'date':'2019-05-10'}],
        [{'uid':'18271783'},{'pid':'314256'},{'date':'2019-01-10'}],
        [{'uid':'12345678'},{'pid':'123567'},{'date':'2019-07-13'}],
        [{'uid':'27362812'},{'pid':'928716'},{'date':'2019-07-24'}],
        [{'uid':'28172831'},{'pid':'276365'},{'date':'2019-07-26'}],
        [{'uid':'12738173'},{'pid':'273612'},{'date':'2019-07-30'}],
        [{'uid':'47162718'},{'pid':'383271'},{'date':'2019-07-11'}],
        [{'uid':'18271783'},{'pid':'283721'},{'date':'2019-06-12'}],
        [{'uid':'12345678'},{'pid':'127361'},{'date':'2019-06-16'}],
        [{'uid':'27362812'},{'pid':'326139'},{'date':'2019-05-18'}]
    ],
    '咨询':[
        [{'uid':'12345678'},{'sid':'123'},{'count':'12'}],
        [{'uid':'27362812'},{'sid':'234'},{'count':'34'}],
        [{'uid':'28172831'},{'sid':'345'},{'count':'45'}],
        [{'uid':'12738173'},{'sid':'456'},{'count':'56'}],
        [{'uid':'47162718'},{'sid':'567'},{'count':'13'}],
        [{'uid':'18271783'},{'sid':'678'},{'count':'45'}],
        [{'uid':'12345678'},{'sid':'123'},{'count':'65'}],
        [{'uid':'27362812'},{'sid':'234'},{'count':'37'}],
        [{'uid':'28172831'},{'sid':'345'},{'count':'18'}],
        [{'uid':'12738173'},{'sid':'456'},{'count':'67'}],
        [{'uid':'47162718'},{'sid':'567'},{'count':'35'}],
        [{'uid':'18271783'},{'sid':'678'},{'count':'32'}],
        [{'uid':'12345678'},{'sid':'123'},{'count':'67'}],
        [{'uid':'27362812'},{'sid':'234'},{'count':'89'}],
        [{'uid':'28172831'},{'sid':'345'},{'count':'241'}],
        [{'uid':'12738173'},{'sid':'456'},{'count':'24'}],
        [{'uid':'47162718'},{'sid':'567'},{'count':'64'}],
        [{'uid':'18271783'},{'sid':'678'},{'count':'46'}],
        [{'uid':'12345678'},{'sid':'789'},{'count':'25'}],
        [{'uid':'27362812'},{'sid':'789'},{'count':'71'}]
    ],
    '风格':[
        [{'pid':'221725'},{'name':'职业'}],
        [{'pid':'314256'},{'name':'休闲'}],
        [{'pid':'123567'},{'name':'休闲'}],
        [{'pid':'928716'},{'name':'通勤'}],
        [{'pid':'276365'},{'name':'家居'}],
        [{'pid':'273612'},{'name':'运动'}],
        [{'pid':'383271'},{'name':'少女'}],
        [{'pid':'283721'},{'name':'淑女'}],
        [{'pid':'127361'},{'name':'通勤'}],
        [{'pid':'326139'},{'name':'大气'}]
    ],
    '材质':[
        [{'pid':'221725'},{'name':'聚酯纤维'}],
        [{'pid':'314256'},{'name':'真丝'}],
        [{'pid':'123567'},{'name':'真丝'}],
        [{'pid':'928716'},{'name':'棉麻'}],
        [{'pid':'276365'},{'name':'棉麻'}],
        [{'pid':'273612'},{'name':'纯棉'}],
        [{'pid':'383271'},{'name':'真丝'}],
        [{'pid':'283721'},{'name':'棉麻'}],
        [{'pid':'127361'},{'name':'纯棉'}],
        [{'pid':'326139'},{'name':'聚酯纤维'}]
    ],
    '功效':[
        [{'pid':'221725'},{'name':'保暖'}],
        [{'pid':'314256'},{'name':'耐磨'}],
        [{'pid':'123567'},{'name':'显瘦'}],
        [{'pid':'123567'},{'name':'显白'}],
        [{'pid':'928716'},{'name':'显白'}],
        [{'pid':'276365'},{'name':'显腿长'}],
        [{'pid':'273612'},{'name':'塑型'}],
        [{'pid':'383271'},{'name':'塑型'}],
        [{'pid':'283721'},{'name':'保暖'}],
        [{'pid':'127361'},{'name':'耐磨'}],
        [{'pid':'326139'},{'name':'显瘦'}]
    ],
    '尺码':[
        [{'pid':'221725'},{'name':'S'}],
        [{'pid':'314256'},{'name':'M'}],
        [{'pid':'123567'},{'name':'L'}],
        [{'pid':'928716'},{'name':'XL'}],
        [{'pid':'276365'},{'name':'XXL'}],
        [{'pid':'273612'},{'name':'XXXL'}],
        [{'pid':'383271'},{'name':'S'}],
        [{'pid':'283721'},{'name':'M'}],
        [{'pid':'127361'},{'name':'L'}],
        [{'pid':'326139'},{'name':'XL'}],
        [{'pid':'221725'},{'name':'XXXL'}],
        [{'pid':'314256'},{'name':'S'}],
        [{'pid':'123567'},{'name':'M'}],
        [{'pid':'928716'},{'name':'L'}],
        [{'pid':'276365'},{'name':'XL'}],
        [{'pid':'273612'},{'name':'XXL'}],
        [{'pid':'383271'},{'name':'XXXL'}],
        [{'pid':'283721'},{'name':'S'}],
        [{'pid':'127361'},{'name':'M'}],
        [{'pid':'326139'},{'name':'L'}]
    ],
    '商家':[
        [{'pid':'221725'},{'sid':'0'}],
        [{'pid':'314256'},{'sid':'1'}],
        [{'pid':'123567'},{'sid':'2'}],
        [{'pid':'928716'},{'sid':'3'}],
        [{'pid':'276365'},{'sid':'4'}],
        [{'pid':'273612'},{'sid':'5'}],
        [{'pid':'383271'},{'sid':'6'}],
        [{'pid':'283721'},{'sid':'0'}],
        [{'pid':'127361'},{'sid':'1'}],
        [{'pid':'326139'},{'sid':'2'}]
    ],
    '配送':[
        [{'pid':'221725'},{'name':'顺丰'}],
        [{'pid':'314256'},{'name':'申通'}],
        [{'pid':'123567'},{'name':'圆通'}],
        [{'pid':'928716'},{'name':'中通'}],
        [{'pid':'276365'},{'name':'韵达'}],
        [{'pid':'273612'},{'name':'百世'}],
        [{'pid':'383271'},{'name':'菜鸟'}],
        [{'pid':'283721'},{'name':'顺丰'}],
        [{'pid':'127361'},{'name':'申通'}],
        [{'pid':'326139'},{'name':'圆通'}]
    ],
    '版型':[
        [{'pid':'221725'},{'name':'修身'}],
        [{'pid':'314256'},{'name':'宽松'}],
        [{'pid':'123567'},{'name':'大码'}],
        [{'pid':'928716'},{'name':'紧身'}],
        [{'pid':'276365'},{'name':'修身'}],
        [{'pid':'273612'},{'name':'大码'}],
        [{'pid':'383271'},{'name':'宽松'}],
        [{'pid':'283721'},{'name':'紧身'}],
        [{'pid':'127361'},{'name':'修身'}],
        [{'pid':'326139'},{'name':'宽松'}]
    ],
    '身材类型':[
        [{'pid':'221725'},{'name':'苹果型'}],
        [{'pid':'314256'},{'name':'H型'}],
        [{'pid':'123567'},{'name':'梨型'}],
        [{'pid':'928716'},{'name':'细沙漏型'}],
        [{'pid':'276365'},{'name':'苹果型'}],
        [{'pid':'273612'},{'name':'H型'}],
        [{'pid':'383271'},{'name':'梨型'}],
        [{'pid':'283721'},{'name':'细沙漏型'}],
        [{'pid':'127361'},{'name':'苹果型'}],
        [{'pid':'326139'},{'name':'梨型'}]
    ],
    '团队':[
        [{'sid':'123'},{'tid':'0'}],
        [{'sid':'234'},{'tid':'1'}],
        [{'sid':'345'},{'tid':'2'}],
        [{'sid':'456'},{'tid':'3'}],
        [{'sid':'567'},{'tid':'4'}],
        [{'sid':'678'},{'tid':'5'}],
        [{'sid':'789'},{'tid':'2'}],
        [{'sid':'890'},{'tid':'1'}],
        [{'sid':'901'},{'tid':'0'}]
    ]
}

opera=[]
for item in data.keys():
    for i,arr in enumerate(data[item]):
        obj=Node(item)
        for k,v in arr.items():
            if k!='id':
                obj[k]=v
            # name='{}'.format(item['name']),main_pic='{}'.format(item['main_pic']),price='{}'.format(item['price']),pid='{}'.format(item['pid']),_buy_num='{}'.format(item['_buy_num'])
        #locals()[item] = obj #Node(item,name='{}'.format(item['name']),main_pic='{}'.format(item['main_pic']),price='{}'.format(item['price']),pid='{}'.format(item['pid']),_buy_num='{}'.format(item['_buy_num']))
        opera.append(obj)

opera=Subgraph(opera)
tx.create(opera)
tx.commit()

rela=[]

def concat_where(item):
    where1=[]
    for k in item.keys():
        temp="'"+item[k]+"'" if type(item[k])==str  else str(item[k])
        where1.append(k+':'+ temp)
    return ','.join(where1)

for rel in relation.keys():
    en1,en2=variable.get('relation',rel).split(',')
    
    for itt in relation[rel]:
        item1={}
        item2={}
        if len(relation[rel][0])==2:
            item3={}
            
        for i in range(len(relation[rel][0])):
            locals()['item'+str(i+1)]=itt[i]
        
        l1=graph.run("MATCH (p:{entity} {{{where}}}) RETURN p limit 1".format(entity=en1,where=concat_where(item1))).evaluate()
        l2=graph.run("MATCH (p:{entity} {{{where}}}) RETURN p limit 1".format(entity=en2,where=concat_where(item2))).evaluate()
        r = Relationship(l1,rel,l2,**item3)#locals()[item[1]]
        #r = Node(person,name='{}'.format(item['name']))
        graph.create(r)
        rela.append(r)


### 事务

# opera=Subgraph(relationships=rela)
# tx.create(opera)
# tx.commit()

### 查询数据

### 根据订单表、日志表、咨询表，更新数据

### 根据商品表更新库存

### 图推荐



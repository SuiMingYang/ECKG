

# 商品品类
    select aa.* ,bb.tag_name from
    (
    SELECT product_id,mp_alias,tag_id FROM weidian_operator.t_product_tag where (data_status='001' or data_status='101') and mp_alias in ('gh1b14f7568197','gh212565199e78')  #group by product_id having num >1
    ) aa
    inner join
    (
    select id,tag_name,data_status from weidian_operator.t_tag where data_status in ('001','101')
    ) bb
    on aa.tag_id=bb.id;

# 获取品类均价
    select tag_id,tag_name,mp_alias,avg(mem_sale) from (

    select x.*,y.tag_id,y.tag_name,y.data_status from
    (
    select a.sort,b.* from (
    SELECT product_id,mp_alias,sort FROM weidian_operator.t_product_mp where state='0' and data_status='001')a
    join
    (
    SELECT main_pic,mp_alias,product_alias,cost_price,channel_id,channel_name,category_id,mem_sale,product_title,id as product_id,product_buy_num,product_collect_num FROM weidian_operator.t_product
    where data_status='001'
    ) b
    on a.mp_alias=b.mp_alias and a.product_id=b.product_id
    )x
    inner join (

    # 商品品类
    select aa.* ,bb.tag_name,bb.data_status from
    (
    SELECT product_id,mp_alias,tag_id FROM weidian_operator.t_product_tag where (data_status='001' or data_status='101') and mp_alias in ('gh1b14f7568197','gh212565199e78')  #group by product_id having num >1
    ) aa
    inner join
    (
    select id,tag_name,data_status from weidian_operator.t_tag where data_status in ('001','101')
    ) bb
    on aa.tag_id=bb.id) y
    on x.product_id=y.product_id and x.mp_alias=y.mp_alias

    ) p
    group by tag_id,mp_alias

结果

    '265', '特价99', '99.000000'
    '358', '上衣', '443.919101'
    '359', '连衣裙', '602.221003'
    '360', '套装', '581.217290'
    '361', '裤子', '414.513793'
    '459', '大码合集', '131.003469'
    '485', '上衣衬衫', '111.938243'
    '486', '优雅美裙', '157.353836'
    '552', '时尚套装', '162.215372'
    '557', '裤鞋搭配', '111.145932'
    '558', '女士内衣', '66.667458'
    '586', '品质棉麻', '464.589404'
    '587', '优选真丝', '877.823164'
    '588', '每日新款', '519.137881'
    '591', '外套', '557.755981'
    '592', '其他面料', '653.790123'
    '593', '半身裙', '422.571429'
    '595', '国风旗袍', '521.096296'
    '607', '包包配饰', '392.000000'
    '611', '女王专柜', '202.835232'
    '613', '上衣【新】', '110.575616'
    '614', '裙子【新】', '161.989426'
    '615', '套装【新】', '167.318903'
    '616', '裤子', '106.952931'
    '618', '外套', '162.412760'
    '619', '内衣睡衣', '66.071749'
    '620', '包包', '81.774436'
    '621', '鞋子', '106.912794'
    '622', '家居用品', '174.221519'
    '623', '配饰', '51.343750'
    '624', '男装', '129.809295'
    '625', '夏末清仓', '580.250000'
    '626', '清仓特价', '94.894495'
    '627', '初秋风衣', '188.944559'

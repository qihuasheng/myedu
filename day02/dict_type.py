# # 调用 import
# import json
# # 全局变量通用
# # 字典
# # adict = {"2":"yansl","pa":"123456"}
# # bdict = {5:"yansl","pa":[2,5]}
# # cdict ='{"2":"yansl","pa":"123456"}'
# def dict_sel():
#  # 查询字典中的元素
#     print(adict['2'])
#     print(bdict[5])
# def dict_del():
#     # 删除字典中的元素 .pop
#     adict.pop('pa')
#     print(adict)
#     bdict.pop(5)
#     print(bdict)
# def dict_update():
#     # 更新字典中的元素
#     adict['2'] = '9'
#     print(adict)
# def dict_add():
#     #合并字典中的元素 去重 如果有相同的字段只显示括号里的
#     adict.update(bdict)
#     print(adict)
#     bdict.update(adict)
#     print(bdict)
# def dict_add1():
#     # 添加 如果['name']是字典里没有的key 就是添加，如果是有的key就是更新
#     adict['name'] ='qihs'
#     print(adict)
# def dict2str():
#     print(type(adict))
#     #字典转换成字符串用json.dumps
#     dict2str = json.dumps(adict)
#     print(dict2str)
#     print(type(dict2str))
# def str2dict():
#     print(type(cdict))
#     #字符串转换成字典用json.loads
#     str2dict=json.loads(cdict)
#     print(str2dict)
#     print(type(str2dict))


a= {"2": "yansl", "pa": "123456"}
b = {5: "yansl", "pa": [2, 5]}
def dict_():
    print(a['2'])
    a.pop('2')
    print(a)
    a['5']='我的'
    print(a)
    a["pa"] =12
    print(a)
    a.update(b)
    print(a)
    c= dict(a, **b)
    print(c)
if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_update()
    # dict_add()
    # dict_add1()
    # dict2str()
    # str2dict()
    # alist=[2,5,7,9,7,6]
    # print(len(alist))
    dict_()



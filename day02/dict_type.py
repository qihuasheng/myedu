import json
adict = {"2":"yansl","pa":"123456"}
bdict = {5:"yansl","pa":[2,5]}
cdict ='{"2":"yansl","pa":"123456"}'
def dict_sel():
    print(adict['2'])
    print(bdict[5])
def dict_del():
    adict.pop('pa')
    print(adict)
    bdict.pop(5)
    print(bdict)
def dict_update():
    adict['2'] = '9'
    print(adict)
def dict_add():
    adict.update(bdict)
    print(adict)
    bdict.update(adict)
    print(bdict)
def dict_add1():
    adict['name'] ='qihs'
    print(adict)
def dict2str():
    print(type(adict))
    #字典转换成字符串用json.dumps
    dict2str = json.dumps(adict)
    print(dict2str)
    print(type(dict2str))
def str2dict():
    print(type(cdict))
    #字符串转换成字典用json.loads
    str2dict=json.loads(cdict)
    print(str2dict)
    print(type(str2dict))

if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_update()
    # dict_add()
    # dict_add1()
    # dict2str()
    # str2dict()
    alist=[2,5,7,9,7,6]
    print(len(alist))



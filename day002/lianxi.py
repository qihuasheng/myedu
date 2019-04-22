#import 导入
import json
alist ={5:3,'s':2}
blist ={3:'r','q':'d'}
clist =' {"username":"yansl","password":"1254"}'
def di_ww():
    #查看
    print(alist[5])
    print(blist['q'])
def di_cc():
    #删除.pop
    alist.pop('s')
    print(alist)
def di_xx():
    #更新 不用调用方法
    alist[5] ='什么'
    print(alist)
    #增加 不用调用方法
    alist['这是'] ='真的'
    print(alist)
def di_ss():
    # print(type(clist))
    # ccd = json.loads(clist)
    # print(ccd)
    # print(type(ccd))
    # print(type(clist))
    # di_ss=json.dumps(clist)
    # print(type(di_ss))
    # clist["password"]="中华"
    # print(clist)
    #字典转换成str用json.dumps
    # cc=json.dumps(blist)
    # print(type)
    # print(type(cc))
    #str转换成字典用json.loads
    bb=json.loads(clist)
    print(type)
    print(type(bb))
def di_jj():
    #字典中合并
    blist.update(alist)
    print(blist)
def add_jiafa():
    a=['有的','是的',2,5]
    b=[3,5,'dd']
    print(a+b)
    print(type(a))
def add_jianfa():
    a = ['有的', '是的', 2, 5]
    b = [3, 5, 'dd']
    a[0]=1
    a[1]=3
    b[2]=4
    print(a)











if __name__ == '__main__':
      # di_ww()
      # di_cc()
      # di_xx()
      # di_ss
      # di_jj
      # add_jiafa()
      add_jianfa()

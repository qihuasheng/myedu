def list_sel(a):
    #list查找集合中的元素
    print(a[1])
    print(a[3])
    #list查找集合中的切片
    print(a[1:5])
    print(a[0:3])
    print(a)
    print(a[-3:-1])
def list_sel(b):
    print(b[0:4])
def list_del():
    alist =[1,2,4,5,7,9,'qi']
    #list删除用 .pop
    alist.pop()
    print(alist)
    alist.pop(2)
    print(alist)
    alist.pop(0)
    print(alist)
    alist.pop(-1)
    print(alist)
def list_add():
    #list增加用 .append 括号里('abc')面填写要增加的元素
    alist=[1,2,3,4,5]
    alist.append('abc')

    print(alist)
    blist=[3,4,5]
    #添加一个集合blist
    alist.append(blist)
    print(alist)
def list_updtae():
    #更新集合中的元数
    alist=[5,6,7,9]
    alist[2]=11
    print(alist)
# def list_a():
#     a=[1,2,3,4,5,6,7]
#     print(a[1])
#     print(a[0,5])
#     a.pop(2)
#     print(a)
#     a.append(10,11)
#     print(a)
#     a[0] ='5'
#     print()
#     len(a)
#     print(len(a))
def list_b():
    b =[5,4,3,2,1]
    print(b[2])
    print(b[1:4])
    b.pop(3)
    print(b)
    b.append(10)
    print(b)
    b.append(12)
    print(b)
    b[5] ='5'
    print(b)
    len(b)
    print(len(b))










if __name__ == '__main__':
    # alist=[5,'shide',3,6,'啊','5.8','ss','我的','123']
    # blist=[4,8,5,9,6,'hh','gg']
    # list_sel(alist)
    # list_sel(blist)\
    # list_del()
    # list_add()
    # list_updtae()
    # list_a()
    list_b()

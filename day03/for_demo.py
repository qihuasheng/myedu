list=[2,3,4,'wo','de','ha']
def for_demo():
    # for (关键字) i(变量名,代表循环次数)  in(关键字)  range( 迭代器函数 )
    for i in range(5):
        print(i)
        print('nihao')
def for_demo1():
    for i in range(5,10):
        print(i)
    for k in range(7,15):
        print(k)
def for_list():

    for i in list:
        print(i)
def for_list2():
    a =len(list)
    for i in range(a):
        print(list[i])
def for_break():
    #停止
    for i in range(7):
        print(i)
        if i==3:
            break
def for_continue():
    # 停止当前
    for i in range(11):
        print(i)
        if i == 5:
            continue
        print('hao%s'%i)
        print('')
def for_nine():
    # 九九乘法表
    for i in range(1,10):
        for k in range(1,i+1):
            print('%s*%s=%s '%(k,i,k*i),end=' ')
        print('')

def for_sum():
    # 计算1到50之间的奇数和
    sum=0
    for i in range(1,51):
        if i%2 ==1:
            sum =sum+i
    print(sum)
def for_sun():
    sum =0
    for i in range(1,51):
        if i%2 ==0:
            sum =sum+i
def for_ww():
    clist=[]
    alist=[['admin', '123456', '成功', '登录成功'], ['admin1', '123456', '错误', '用户名错误'], ['admin', '123456a', '错误', '密码错误'], ['admin', '123456', '成功', '登录成功1'], ['admin1', '123456', '错误', '用户名错误1'], ['admin', '123456a', '错误', '密码错误1']]
    b=len(alist)
    for i in range(b):
        b=alist[i].pop(-1)
        clist.append(b)
    print(alist)
    print(clist)









if __name__ == '__main__':
    # for_demo1()
    # for_list()
    # for_list2()
    # for_break()
    # for_continue()
    # for_nine()
    # for_sum()
    for_ww()
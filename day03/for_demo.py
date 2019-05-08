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
    # 50之计算1到间的奇数和
    sum=0
    for i in range(1,51):
        if i%2 ==1:
            sum =sum+i
    print(sum)
    #50之计算1到间的偶数和
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

def jiu_jiu():
    for i in  range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end=' ')
        print()










if __name__ == '__main__':
    # for_demo1()
    # for_list()
    # for_list2()
    # for_break()
    # for_continue()
    # for_nine()
    # for_sum()
    # for_ww()
    jiu_jiu()
    # 因为乘法表里面有两个数,所以写两个for 循环
    # 乘法表 从1到 9  所以外循环是 range(1,10)
    # 内循环 写i+1 因为 每次每一行 数字 j 最大的都是i
    # 内循环打印 就是字符串拼接,以 ' '结尾 防止每次打印换行,并 分隔开每次打印内容
    # 外循环的print 主要是为了 每次内循环结束 需要换行
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end=' ')

        print(' ')


    alist=[3,2,1,5,4,9,6,7,8]

    # 外循环 len - 1 :  因为 两两比较 ,比如有10个数 我需要比较 9轮
    # 内循环: len - i -1 : 因为 两两比较 ,比如有10个数 我需要比较 9次, 第二遍的时候 只需要比较 8次,
    # 每一遍都少一次,因为每遍 都会放一个数在后面

    #             if alist[j] <= alist[j+1]:
    #                 continue                    判断相邻两个数 要不要换位置

    #             temp = alist[j]
    #             alist[j] = alist[j+1]     将相邻两个数 换位置
    #             alist[j+1] = temp
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] <= alist[j+1]:
                continue
            temp = alist[j]
            alist[j] = alist[j+1]
            alist[j+1] = temp
    print(alist)

    # list去重
    alist = [3, 2, 1, 5, 4, 4,5]
    blist= []
    for i in alist:
        if i not in blist:
            blist.append(i)
    print(blist)

    # 去重方式 2
    s = set(alist)
    print(s)





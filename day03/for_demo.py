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
    for i in range(11):
        print(i)
        if i == 5:
            continue
        print('hao%s'%i)
        print('')
def for_nine():
    for i in range(1,10):
        for k in range(1,i+1):
            print('%s*%s=%s '%(k,i,k*i),end=' ')
        print('')

def for_sum():
    sum=0
    for i in range(1,51):
        if i%2 ==1:
            sum =sum+i
    print(sum)



if __name__ == '__main__':
    # for_demo1()
    # for_list()
    # for_list2()
    # for_break()
    # for_continue()
    # for_nine()
    for_sum()
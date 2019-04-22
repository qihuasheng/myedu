
def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')
def int_demo():
    aint=6
    print(aint)
    print(type(aint))
def str_demo():
     astr='7'
     print(astr)
     print(type(astr))
def float_demo():
     float=7.5
     print(float)
     print(type(float))
def add_demo(a,b):
    #加法
    print(a+b)
def type_zhuanhuan():
    #转换类型
     aint=7
    #转换int类型
     print(type(aint))
    #转换str类型
     print(type( str(aint) ))
def str_join():
     a=5
     b=5.8
     c='什么'
     #合并多个元素
     # 方法一
     print('%s %s %s'%(a,b,c))
     #方法二
     print(str(a)+str(b)+c)
def str_abc():
    ab='这是什么'
    b=55.5
    cd='hhh'
    print(ab+str(b)+cd)

def jianfa_demo(a,b):
    #减法
     c=a-b
    # return c
     return c
if __name__ == '__main__':
    # test3()
    # test1()
    # test2()
    # int_demo()
    # str_demo()
    # float_demo()
    # add_demo(8,5)
    # type_zhuanhuan()
    # str_join()
    # c=jianfa_demo(10,6)
    # e=add_demo(1,7)
    # print(e)
    # print(c)
    str_abc()


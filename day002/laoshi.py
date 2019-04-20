
# 查询或者获取list 里面的值(元素)
# a[索引]: 或者叫下标值  元素从0开始数
def list_sel(a):
    # 顺序取值: 从0开始数
    print( a[2] )
    # 倒序取值: 从 -1 开始数
    print(a[-1])
    # 切片取值 语法: 前索引值 : 后索引值  取的时候取到后索引值的前一位
    print(a[2:5])
    print(a[0:2])
    # 不填值的话  从第一个开始取值
    print(a[:4])
    # 不填值的话  取到最后一位
    print(a[3:])

def list_del():
    # 定义一个list
    alist = ['a', 4, 'nihao', '8', '就是', '哈']
    # 调用删除方法 不填参数 默认删除最后一位
    alist.pop()
    print(alist)
    # 调用删除方法, 填写参数: 索引值   就可以删除指定元素
    alist.pop(0)
    print(alist)

    # 将切片获取的 元素 重新定义一个list 保存起来
    blist = alist[:-3]
    print(blist)

def list_add():
    alist = ['a', 4, 4, 4, 'nihao', '8', '就是', '哈']
    # 增加元素 ,增加在末尾
    alist.append('哈哈哈哈')
    print(alist)

    blist = [1,2,3]
    # 将一个list 作为元素,添加到 list里面
    alist.append(blist)
    print(alist)

    # 元素更换位置

# 更改list中的元素
def list_update():
    alist = ['a', 4, 'nihao', '8', '就是', '哈', '哈哈哈哈', [1, 2, 3]]
    alist[0] = 5
    print(alist)



if __name__ == '__main__':
    alist = ['a',4,'nihao','8','就是','哈']
    # 获取list中元素的总数
    print( len(alist) )
    # list_sel(alist)
    # print(alist)
    # list_del()
    # list_add()
    # list_update()

    import json

    # 全局变量
    adict = {"username": "yansl", "password": "123456"}
    bdict = {'5': "yansl", "password": [2, 5]}

    cdict_str = '{"username":"yansl","password":"123456"}'


    # 查询字典中的元素
    def dict_sel():
        # 通过key来访问,key可以是 str 类型 ,也可是int类型
        print(adict['username'])
        print(bdict[5])
        # 将访问到的值 可以重新赋值 给 新的变量
        b = bdict['password']
        print(b)


    # 删除字典中的元素
    def dict_del():
        adict.pop('password')
        print(adict)


    # 更改字典中的值
    def dict_update():
        adict['username'] = '闫松林'
        print(adict)


    # 合并字典
    def dict_add():
        # 方式一
        # 字典中的key 不能重复 , 相同key 保存value时 取 括号里面的值
        adict.update(bdict)
        print(adict)

        # 方式二
        # 使用 dict() 方法时 ,两个字典中的key 必须都是字符串格式
        cdict = dict(adict, **bdict)
        print(cdict)


    # 增加字典中的元素
    def dict_add1():
        adict['sex'] = '男'
        print(adict)


    # 字典转换字符串  json.dumps()
    def dict2str():
        print(type(adict))
        # 将 adict 转换成 字符串类型  再重新赋值 给 adict_str
        adict_str = json.dumps(adict)
        print(adict_str)
        print(type(adict_str))


    # 字符串转换字典 json.loads()
    def str2dict():
        print(type(cdict_str))
        # 将 cdict_str 转换成 字典类型  再重新赋值 给 cdict
        cdict = json.loads(cdict_str)
        print(cdict)
        print(type(cdict))


    if __name__ == '__main__':
        # dict_sel()
        # dict_del()
        # dict_update()
        # dict_add()
        # dict_add1()
        # dict2str()
        str2dict()
        # 元组类型  tuple
        # 与list的区别 : 只能被访问,不能更改

        if __name__ == '__main__':
            atuple = (1, 5, 6, 'ha', 6)
            print(atuple[2])
            print(atuple[2:4])
            atuple[2] = 7

            if __name__ == '__main__':
                # 布尔 类型
                abool = True
                bbool = False
                print(type(abool))

                # 复数 类型
                acomplex = 1 + 2j
                print(acomplex)
                print(type(acomplex))
                # 调用其他模块的方法

                # 先导入模块  语法 : from 包名 import 模块名
                from day01 import base_type

                if __name__ == '__main__':
                    # 使用 :  模块名.方法名(参数1,参数2)
                    base_type.add_demo(5, 10)
                    value = base_type.jianfa_demo(3, 6)
                    print(value)


                    # def声明一个方法
                    # first_demo 这是方法名
                    # ():

                    def text1():
                        print('text1')


                    def text2():
                        print('text2')


                    def text3():
                        print('text3')


                    def first_demo():
                        print('xxx')
                        print('jjj')


                    # 整数类型的演示
                    def int_demo():
                        # 声明一个变量  = 前面的就是变量名   , =后面的就是变量值
                        aint = 5
                        # 打印 aint变量
                        print(aint)
                        # type(aint) : 获取aint的变量类型
                        # print(type(aint)) : 打印 aint的变量类型
                        print(type(aint))


                    # 字符串类型的演示
                    def str_demo():
                        astr = '5'
                        print(astr)
                        print(type(astr))


                    # 小数类型的演示
                    def float_demo():
                        afloat = 5.5
                        print(afloat)
                        print(type(afloat))


                    def type_zhuanhuan():
                        aint = 7
                        # 获取 aint 的类型
                        print(type(aint))
                        # 将aint 转换为 str 类型 , 在打印出它的类型
                        print(type(str(aint)))
                        # 将aint 再转换回来:  int 类型 , 在打印出它的类型
                        print(type(int(aint)))

                        # 被转换的字符 必须是满足 数字的格式
                        # print(type( int('xxx') ))


                    # 字符串拼接
                    def str_join():
                        a = 123
                        b = '你好'
                        c = 5.88
                        # 方式一 : 将变量转换为str  然后用 + 连接起来
                        print(str(a) + b + str(c))
                        # 方式二 %s: 占位符
                        print('a是%s b是%s c是%s' % (a, b, c))


                    # 加法方法演示  (a,b) :  () 里面的东西 叫参数,多个参数用 , 分隔开 ; 参数等同于变量 , 只不过没有赋值
                    def add_demo(a, b):
                        print(a + b)


                    def jianfa_demo(a, b):
                        c = a - b
                        # return : 返回的意思  后面是什么  方法执行后就返回什么
                        return c
                        # return 后面不能继续写代码,因为方法执行到 return 就会结束
                        # print(c)


                    if __name__ == '__main__':
                        # text1()
                        # print('hell')
                        # first_demo()
                        # int_demo()
                        # str_demo()
                        # float_demo()

                        # 调用方法, 并传参
                        # add_demo(3000,5832784)
                        # 加法如果传字符串 ,会把两个字符串拼接到一起
                        # add_demo('你好',' 世界')
                        # type_zhuanhuan()
                        # str_join()
                        # 将减法执行完 返回的值 赋值 给 c   所以c是8
                        c = jianfa_demo(6, 2)
                        # d = 加法执行完返回的值, 但是 加法没有返回值   所以d 是 None
                        d = add_demo(6, 2)
                        print(c)
                        print(d)
                        print(type(d))
# if __name__ == '__main__':
#     # w+覆盖
#     # text_io =open('test.text','w+')
#     # text_io.write('hhhhh')
#     # a+追加
#     text_io =open('test.text','a+')
    # text_io.write('dddddd')
    # text_io =open('test.text','r')
    # # a=text_io.readline()
    # # print(a)
    # b= text_io.readlines()
    # print(b)
def for_demo():
    for i in range(9):
        i+=1
        for k in range(i):
            k+=1
            print('%s*%s=%2s   '%(i,k,i*k),end='')
        print('')








def for_demo1():
    for i in range(9):
        i+=1
        for j in range(i):
            j+=1
            print('%s*%s=%2s'%(i,j,i*j),end='  ')
        print('')

def for_demo2():
    alist =[5,3,2,11]
    len(alist)
    for i in range(len(alist)):
        for j in range(i):

            n=alist[j]
            m=alist[j+1]
            if n <= m:
                continue
            en=alist[j]
            alist[j] = alist[j + 1]
            alist[j+1]=en
    print(alist)














if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    for_demo2()

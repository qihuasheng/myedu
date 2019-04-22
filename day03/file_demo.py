if __name__ == '__main__':
    # w+覆盖
    # text_io =open('test.text','w+')
    # text_io.write('hhhhh')
    # a+追加
    text_io =open('test.text','a+')
    text_io.write('dddddd')
    text_io =open('test.text','r')
    # a=text_io.readline()
    # print(a)
    b= text_io.readlines()
    print(b)



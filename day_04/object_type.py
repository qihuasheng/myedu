class wode (object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def shijiao(self):
        print('%s睡觉'%self.age)
    def chifan(self):
        print('%s吃饭'%self.name)
class tester(wode):
    def work(self):
        print('%s在测试'%self.name)
        self.shijiao()
class hum (object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def
if __name__ == '__main__':
    awode = wode('hh',25,'男')
    awode.shijiao()
    awode.chifan()
    # tester =tester('hh',25,'男')
    # tester.work()
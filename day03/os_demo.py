import os

if __name__ == '__main__':
   pwd= os.getcwd()
   print(pwd)
   a=os.path.abspath('..')
   print(a)


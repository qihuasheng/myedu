#冒泡用例
alist=[1,4,3,5,6,7,9,12]
for i in range(len(alist)-1):
    for j in range(len(alist)-i-1):
        if alist[j]<=alist[j+1]:
            continue
            a=alist[j]
            alist[j]=alist[j+1]
            alist[j+1]=a
    print(alist)

alist=[1,4,7,5,20,25,9,12]
for i in range(len(alist)-1):
    for j in range(len(alist)-i-1):
        if alist[j]>alist[j+1]:
            a=alist[j]
            alist[j]=alist[j+1]
            alist[j+1]=a
print(alist)



#list去重
listb=[5,2,6,8,9,12,6,8,5]
listc=[]
for i in listb:
    if i not in listc:
        listc.append(i)
print(listc)

#第二种方法
listb=[5,2,6,8,9,12,6,8,5]
s=set(listb)
print(s)
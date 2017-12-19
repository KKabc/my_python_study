'''

s1 = (1,1.3,'love',5.6,12,False)
s2 = (True,5,'smile')
s3 = []
s4 = [1,(3,4,5)]
s5 = 'abcdefghijklmnopqrstuvwxyz'
print(s1,type(s1),s1[0],s1[4],"；")
print(s2,type(s2),s3,type(s3),"；")
print(s4[1][2],"；")
print(s1[0:-1],s1[2:5:2],"；")
print(s5[-1],s5[20:2:-1],"；")

s3.append(3)
print(s3)
s3.insert(0,[1])
print(s3)
s3.pop(1)
print(s3)

a = "hello"
print(a)
print(type (a))

a = '%1.1f%%' % (0.5*100)
print(a)

print(abs(-3)) #返回绝对值

# 2017-12-15
'''
'''
print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(20%3)
print(2**2,2**3)

print(5==6)
print(8!=8.0)
print(3<3,3<=3)
print(4>1,4>=1)
print(5 in [1,2,3,4]) #5是list列表中的一员

print(True and True,True and False) #和运算，全真才真
print(True or False) #或运算，有真则真
print(not False) #费运算，取反
print(1>2 and 2<3)

#2017-12-18

'''
'''
i = -1
x = 1
if i > 0 :
    x = x + 1
    print("1",x)
else :
    print("负数")
print("2",x)
'''
'''
i = 1
if i > 1 :
    print('positive i')
    i = i + 1
elif i ==0 :
    print('i is 0')
    i = i - 1
else:
    print('negative i')
    if i == 1 :
        print('i原来是1')
    i = i - 1
print('new i =',i)
'''
'''
aaa = range(5)
for a in [3,4,4,'life',[1,2,3]]:
    print(a)
idx = range(5)
print(idx)
for b in  range(4):
    print(b)

i=19
while i < 20 :
    print(i)
    i = i + 1
'''
'''
for i in range(5):
    if i ==2:
        continue #跳过当前循环
    print(i)

for i in range(5):
    if i ==2:
        break #中断当前循环
    print(i)
'''
'''
def sqquare_sum(a,b):
    c = a**2 + b**2
    return a,b,c
print(sqquare_sum(2,3))

a = 1
def change_integer(a):
    a = a + 1
    return a
print(change_integer(a))
print(a)   #a原值不变化

b = [1,2,3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print(change_list(b))
print(b)  #b原值变化
#1、对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，
#从而不影响原来的变量。我们称之为值传递
#2、对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中
#对表的操作将再原有内存中进行，从而影响原有变量。我们称之为指针传递
2017-12-18
'''

print(1986%100)



































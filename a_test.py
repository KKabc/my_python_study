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
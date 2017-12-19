#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Filename : test.py
'''
print ("hello word!")
print("hello word!")

year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))

'''
#函数判断

y =int(input("请输入： "))
def year_judge1(y):
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                return True # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True # 非整百年能被4整除的为闰年
    else:
        return False
print('year_judge1',year_judge1(y))

def year_judge2(y):
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False
print ( 'year_judge2',year_judge2 ( y ) )

def year_judge3(y):
    if ((y % 4 ==0 and y % 100 !=0) or y % 400 == 0):
        return True
    else:
        return False
print('year_judge3',year_judge3(y))

def year_judge4(y):#这个是个错误例子
    if y % 400 == 0 and y % 4 ==0 or y % 100 !=0:
        return True
    else:
        return False
print('year_judge4',year_judge4(y),'这是个错误例子')

def year_judge5(y):
    if y % 100 == 0:
        return y % 400 ==0
    else:
        return y % 4 == 0
print('year_judge5',year_judge5(y))

def year_judge6(y):
    if y % 100 == 0:
        if y % 400 ==0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False
print('year_judge6',year_judge6(y))


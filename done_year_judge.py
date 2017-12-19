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

def year_judge(y):
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
print(year_judge(1900))


def year_judge2(y):
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False
y =int(input("请输入"))
print ( year_judge2 ( y ) )


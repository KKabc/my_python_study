import matplotlib.pyplot as  plt

labels='forgs','hogs','dogs','logs'
sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0
# autopct : [ None | format string | format function ] ，
# 用于标记它们的值(大小为x/sum(x)*100）；，可以为一个format string，或function。如format string, %d（整数）,
# %1.1f（保留一位的小数）等
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()



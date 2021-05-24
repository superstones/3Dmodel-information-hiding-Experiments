import numpy as np
import matplotlib.pyplot as plt
#定义一个函数
def func(x):
    return x+ 85
#定义另一个函数
def func1(x):
    return x*x*x+85
def func2(x):
    return x*x+85
#np.linspace()取x的值
x = np.linspace(0, 10)
y = func(x)
y1 = func1(x)
y2 = func2(x)

# 画线
fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.plot(x, y1, 'g', linewidth=2)
plt.plot(x, y2, 'b', linewidth=2)
plt.ylim(ymin=0)

# 画阴影区域
a, b = 0, 10  # integral limits
xf = x[np.where((x>a)&(x<b))]
#plt.fill_between(xf),在xf范围内
#曲线1：np.zeros(len(xf))与曲线2：func(xf)之间的区域
#np.zeros()从零开始，np.ones()从1开始，np.ones()*20从20开始
#plt.fill_between(xf, np.zeros(len(xf)), func(xf), color='blue', alpha=.25)
#两条曲线之间的区域
plt.fill_between(xf,func1(xf),func(xf),color='blue',alpha=0.25)

plt.show()
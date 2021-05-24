import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# 构建 时间序列数据 从2000-1-31开始，以月份为间隔，构建100条记录
SNR=pd.read_csv('SNR.csv')
SNR.head()
fmri=pd.read_csv('../Example/fmri.csv')


"""
案例7：绘制时间序列数据
"""

#markers 给折线图是否标点\
print(SNR)

sns.relplot(data=SNR, x="k(Embedding Capacity Index $2^{k}$)/b", y="SNR/dB", dashes=False, markers=True,
            kind="line",hue="Method",style="Method")
plt.legend(title='Method', bbox_to_anchor=(1.05, 1))
plt.xlim(-0.08,20.08)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.ylim(40,100.08)
#sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event",markers=True)

plt.show()


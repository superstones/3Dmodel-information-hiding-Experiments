import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
import matplotlib
from matplotlib import ticker, font_manager




matplotlib.rcParams['font.sans-serif'] = ['SimHei']
sns.set(style="darkgrid")
Hausdoff=pd.read_csv('Hausdoff.csv')
Hausdoff.head()


#markers 给折线图是否标点\
print(Hausdoff)

g=sns.relplot(data=Hausdoff, x="k(Embedding Capacity Index $2^{k}$)/b", y="Hausdorff Distance/$10^{-3}$)", dashes=False, markers=True,
            kind="line",hue="Method",style="Method",legend="full")
leg =g.legend
leg.set_bbox_to_anchor([0.4, 0.8])#修改图例位置避免重叠

# plt.legend(title="Method",loc="upper left")
# plt.legend(title='Method', bbox_to_anchor=(1.05, 1))
plt.xlim(-0.05,20.05)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.yticks([0,5,10,15,20])
plt.ylim(-0.15,20.05)
#sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event",markers=True)

plt.show()


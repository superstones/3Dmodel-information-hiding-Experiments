import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
import matplotlib
from matplotlib import ticker, font_manager




matplotlib.rcParams['font.sans-serif'] = ['SimHei']
sns.set(style="darkgrid")
Cut=pd.read_csv('Cut.csv')
Cut.head()


#markers 给折线图是否标点\
print(Cut)

g=sns.relplot(data=Cut, x="Cut Ratio/%", y="Correkatuib(Corr)", dashes=False, markers=True,
            kind="line",hue="Method",style="Method",legend="full")
leg =g.legend
leg.set_bbox_to_anchor([0.9, 0.8])#修改图例位置避免重叠

# plt.legend(title="Method",loc="upper left")
# plt.legend(title='Method', bbox_to_anchor=(1.05, 1))
plt.xlim(-0.05,40.05)
plt.xticks([0,5,10,15,20,25,30,35,40])
plt.yticks([0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.ylim(0.3995,1.0005)
#sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event",markers=True)

plt.show()


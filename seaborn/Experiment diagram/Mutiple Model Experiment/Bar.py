import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
import matplotlib
from matplotlib import ticker, font_manager
Bar=pd.read_csv('Bar.csv')

g = sns.catplot(data=Bar,x="Databse", y="Correkatuib(Corr)",
                hue="Attack Method",
                kind="bar",
                height=4, aspect=.8,saturation=1);
leg =g.legend
leg.set_bbox_to_anchor([0.85, 0.88])#修改图例位置避免重叠

# plt.legend(title="Method",loc="upper left")
# plt.legend(title='Method', bbox_to_anchor=(1.05, 1))

plt.yticks([0,0.2,0.4,0.6,0.8,1.0])
plt.ylim(0,1.2)
plt.show()
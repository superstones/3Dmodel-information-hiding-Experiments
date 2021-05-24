import numpy as np
import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns

# 构建 时间序列数据 从2000-1-31开始，以月份为间隔，构建100条记录
index = pd.date_range("1 1 2000", periods=100,freq="m", name="date")
data = np.random.randn(100, 4).cumsum(axis=0)

# 构建5列数据，列名分别为data a b c d
wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])
"""
案例7：绘制时间序列数据
"""
sns.lineplot(data=wide_df)
plt.show()

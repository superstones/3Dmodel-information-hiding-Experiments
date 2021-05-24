import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.ensemble import RandomForestRegressor

datafile = u'D:\OneDrive文件\OneDrive\桌面\附件一：325个样本数据.xlsx'
data = pd.read_excel(datafile)
data_fea = data.iloc[:, 1:367]  # 取数据中指标所在的列
data_y = data.iloc[:, 0]
model = RandomForestRegressor(random_state=None, max_depth=None)
data_fea = data_fea.fillna(0)  # 随机森林只接受数字输入，不接受空值、逻辑值、文字等类型
data_fea = pd.get_dummies(data_fea)
print(data_fea)
model.fit(data_fea, data_y)
# 根据特征的重要性绘制柱状图
features = data_fea.columns
importances = model.feature_importances_
indices = np.argsort(-importances[0:367])
plot.figure(figsize=(8, 8))
plot.title('Index selection')
nm = np.argsort(-importances[indices])
nm = nm[340:]
# plot.barh(range(len(indices)), np.argsort(-importances[indices]), color='pink', align='center')
plot.barh(range(len(nm)), nm, color='pink', align='center')
plot.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plot.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
print(indices + 1)
plot.yticks(range(len(nm)), [features[i] for i in indices[340:]])
plot.xlabel('Relative importance of indicators')
plot.show()

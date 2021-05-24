# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as ds
import matplotlib.colors
from sklearn.cluster import MeanShift
from sklearn.metrics import euclidean_distances

# MeanShift 均值漂移算法  原理见：http://blog.csdn.net/google19890102/article/details/51030884

if __name__ == '__main__':
    N = 1000
    centers = [[1, 2], [-1, -1], [1, -1], [-1, 1]]
    # scikit中的make_blobs方法常被用来生成聚类算法的测试数据，直观地说，make_blobs会根据用户指定的特征数量、
    # 中心点数量、范围等来生成几类数据，这些数据可用于测试聚类算法的效果。
    # 函数原型：sklearn.datasets.make_blobs(n_samples=100, n_features=2,
    # centers=3, cluster_std=1.0, center_box=(-10.0, 10.0), shuffle=True, random_state=None)[source]
    # 参数解析：
    # n_samples是待生成的样本的总数。
    #
    # n_features是每个样本的特征数。
    #
    # centers表示类别数。
    #
    # cluster_std表示每个类别的方差，例如我们希望生成2类数据，其中一类比另一类具有更大的方差，可以将cluster_std设置为[1.0, 3.0]。
    data, y = ds.make_blobs(N, n_features=2, centers=centers, cluster_std=[0.5, 0.25, 0.7, 0.5], random_state=0)

    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 9), facecolor='w')
    # 计算向量之间的距离
    m = euclidean_distances(data, squared=True)
    print('m=', m)
    bw = np.median(m)
    print('bw=', bw)
    for i, mul in enumerate(np.linspace(0.1, 0.4, 4)):
        band_width = mul * bw
        model = MeanShift(bin_seeding=True, bandwidth=band_width)
        ms = model.fit(data)
        centers = ms.cluster_centers_
        y_hat = ms.labels_
        n_clusters = np.unique(y_hat).size
        print('带宽：', mul, band_width, '聚类簇的个数为:', n_clusters)

        plt.subplot(2, 2, i + 1)
        plt.title(u'带宽:%.2f,聚类簇的个数为:%d' % (band_width, n_clusters))
        clrs = []
        for c in np.linspace(16711680, 255, n_clusters):
            clrs.append('#%06x' % c)
        print
        clrs
        for k, clr in enumerate(clrs):
            cur = (y_hat == k)
            # 绘制散点图
            plt.scatter(data[cur, 0], data[cur, 1], c=clr, edgecolors='none')
        plt.scatter(centers[:, 0], centers[:, 1], s=150, c=clrs, marker='*', edgecolors='k')
        plt.grid(True)
    plt.tight_layout(2)
    plt.suptitle(u'MeanShift聚类', fontsize=20)
    plt.subplots_adjust(top=0.92)
    plt.show()
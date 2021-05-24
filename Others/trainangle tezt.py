from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['font.sans-serif'] = ['SimHei']


def plot_linear_cube(ax, x, y, z, dx, dy, dz, color='green'):
    xx = [1, 1, 3, 3, 1]
    yy = [0, 2, 2, 0, 0]  # 这里xx,yy是二维平面上的坐标，如第一个点坐标就是[1，0]。第二个点依次类推，最后多的[1,0]是指图形形成一个闭环。
    kwargs = {'alpha': 1, 'color': 'green'}
    ax.plot3D(xx, yy, [6] * 5, **kwargs)
    ax.plot3D(xx, yy, [9] * 5, **kwargs)
    ax.plot3D([1, 1], [0, 0], [6, 9], **kwargs)
    ax.plot3D([1, 1], [2, 2], [6, 9], **kwargs)
    ax.plot3D([3, 3], [2, 2], [6, 9], **kwargs)
    ax.plot3D([3, 3], [0, 0], [6, 9], **kwargs)
    plt.title('Cube')
    plt.show()


def plot_lineara_cube(ax, x, y, z, dx, dy, dz, dm, dn):
    xx = [1, 1, 3, 3, 1]
    yy = [0, 2, 2, 0, 0]
    kwargs = {'alpha': 1, 'color': 'green'}
    ax.plot3D(xx, yy, [6] * 5, **kwargs)
    ax.plot3D(xx, yy, [9] * 5, **kwargs)
    ax.plot3D([1, 1], [0, 0], [6, 9], **kwargs)
    ax.plot3D([1, 1], [2, 2], [6, 9], **kwargs)
    ax.plot3D([3, 3], [2, 2], [6, 9], **kwargs)
    ax.plot3D([3, 3], [0, 0], [6, 9], **kwargs)

    xx3 = [0.3, 0.3, 3, 0.3]
    yy3 = [1, 2, 1, 1]
    kwargs = {'alpha': 1, 'color': 'yellow'}
    ax.plot3D(xx3, yy3, [4] * 4, **kwargs)
    ax.plot3D(xx3, yy3, [2] * 4, **kwargs)
    ax.plot3D([0.3, 0.3], [1, 1], [4, 2], **kwargs)
    ax.plot3D([0.3, 0.3], [2, 2], [4, 2], **kwargs)
    ax.plot3D([3, 3], [1, 1], [4, 2], **kwargs)

    xx1 = [x, x, x + dm, x + dx, x + dx, x + dm, x]
    yy1 = [y, y + dy, y + 3 * dn, y + dy, y, y - dn, y]
    kwargs = {'alpha': 1, 'color': 'red'}
    ax.plot3D(xx1, yy1, [z] * 7, **kwargs)
    ax.plot3D(xx1, yy1, [z + dz] * 7, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z + dz], **kwargs)
    ax.plot3D([x, x], [y + dy, y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y + dy, y + dy], [z, z + dz], **kwargs)
    ax.plot3D([x + dx, x + dx], [y, y], [z, z + dz], **kwargs)
    ax.plot3D([x + dm, x + dm], [y - dn, y - dn], [z, z + dz], **kwargs)
    ax.plot3D([x + dm, x + dm], [y + 3 * dn, y + 3 * dn], [z, z + dz], **kwargs)
    plt.title('Cube')
    plt.show()


if __name__ == "__main__":
    fig = plt.figure()
    ax = Axes3D(fig)
    plot_linear_cube(ax, 1, 0, 6, 2, 2, 3)
    fig = plt.figure()
    ax = Axes3D(fig)
    plot_lineara_cube(ax, 2, 1, 5, 2, 2, 3, 1, 2)
    # plot_opaque_cube()

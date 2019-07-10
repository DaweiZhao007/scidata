#!/usr/bin/env python
# -*- coding:utf-8 -*-

import seaborn as sns
import matplotlib as mpl

# 读取数据
df = pd.read_csv('curry.csv', header=None, names=['width', 'height', 'type'])


def colormap():
    """
    颜色转换
    """
    return mpl.colors.LinearSegmentedColormap.from_list('cmap', ['#C5C5C5', '#9F9F9F', '#706A7C', '#675678', '#713A71','#9D3E5E', '#BC5245',  '#C86138', '#C96239', '#D37636', '#D67F39', '#DA8C3E', '#E1A352'], 256)


# 绘制球员投篮热力图
shot_heatmap = sns.jointplot(df['width'], df['height'], stat_func=None, kind='kde', space=0, color='w', cmap=colormap())
# 设置图像大小
shot_heatmap.fig.set_size_inches(6, 6)
# 图像反向
ax = shot_heatmap.ax_joint
# 绘制投篮散点图
ax.scatter(x=df['width'], y=df['height'], s=0.1, marker='o', color="w", alpha=1)
# 添加篮球场
draw_ball_field(color='w', lw=2)
# 将坐标轴颜色更改为白色
lines = plt.gca()
lines.spines['top'].set_color('none')
lines.spines['left'].set_color('none')
# 去除坐标轴标签
ax.axis('off')

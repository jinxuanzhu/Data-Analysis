# coding:utf-8
import pandas as pd
from matplotlib import pyplot as plt
import re

class ReadTop10():

 if __name__ == '__main__':

    df = pd.read_csv('E:\project\Data Analysis\\rrcp.csv')

    # 数据清洗
    dom = []
    for i in df['read']:
        if i.isdigit():
            dom.append(int(i.replace('万', '0000')))
        else:
            dom.append(int(re.sub('[.]','',i).replace('万', '000')))
    df['read'] = dom

    # 数据排序  从大到小
    names = df.sort_values(by='read', ascending=False)['title'][:10]
    read = df.sort_values(by='read', ascending=False)['read'][:10]
    # 设置显示数据
    names = [i for i in names]
    # reverse() 反向排序 改为从小到大
    names.reverse()
    read = [i for i in read]
    read.reverse()
    # Series (collections names) 配对排序，不改变顺序，只进行配对
    data = pd.Series(read, index=names)
    # 设置图片显示属性,字体及大小
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    # 设置图片显示属性
    fig = plt.figure(figsize=(16, 8), dpi=80)
    ax = plt.subplot(1, 1, 1)
    ax.patch.set_color('white')
    # 设置坐标轴属性
    lines = plt.gca()
    # 设置坐标轴颜色
    lines.spines['right'].set_color('none')
    lines.spines['top'].set_color('none')
    lines.spines['left'].set_color((64 / 255, 64 / 255, 64 / 255))
    lines.spines['bottom'].set_color((64 / 255, 64 / 255, 64 / 255))
    # 设置坐标轴刻度
    lines.xaxis.set_ticks_position('none')
    lines.yaxis.set_ticks_position('none')
    # 绘制柱状图,设置柱状图颜色 barh 柱子横向，bar 柱子竖向
    data.plot.barh(ax=ax, width=0.7, alpha=0.7, color=(8 / 255, 88 / 255, 121 / 255), title='1月份人人都是产品经理文章阅读 TOP10')
    # 添加阅读数量文本
    for x, y in enumerate(data.values):
        num = str(y / 10000)
        plt.text(y + 2700, x - 0.08, '%s' % (num + '万'), ha='center')
    # 显示图片
    plt.show()

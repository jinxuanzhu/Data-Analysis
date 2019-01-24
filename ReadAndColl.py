# coding:utf-8
import pandas as pd
from matplotlib import pyplot as plt
import re


class ReadTop10():

 if __name__ == '__main__':

    df = pd.read_csv('E:\project\Data Analysis\\rrcp.csv')
    # 指定默认字体 可显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'

    # 数据清洗
    dom = []
    for i in df['read']:
        if i.isdigit():
            dom.append(int(i.replace('万', '0000')))
        else:
            dom.append(int(re.sub('[.]','',i).replace('万', '000')))
    df['read'] = dom

    # 散点图
    re = df[df['collection']>100].plot.scatter(x='read', y='collection')
    re.set_title('阅读量和收藏量关系图', fontsize=12)
    plt.show(block=True)
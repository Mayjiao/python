#!/usr/bin/python
# -*- coding: UTF-8 -*-

#导入matplotlib的所有内容
from pylab import *

#创建一个8*6点图，并设置分辨率为80
figure(figsize=(8,6), dpi=80)

#创建一个新的1*1子图，接下来的图样绘制在其中的第1块
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

#绘制余弦曲线，使用蓝色的、连续的、宽度为1像素的线条
plot(X,C,color="blue", linewidth=1.0, linestyle="-")

#绘制正弦曲线，使用绿色的、连续的、宽度为1像素的线条
plot(X,S,color="green", linewidth=1.0, linestyle="-")

#设置横轴的上下限
xlim(-4.0,4.0)

#设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

#设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

#在屏幕上显示
show()

#plotting a histogram graph (has Quantitative values) graph


from matplotlib import  pyplot as plt
from matplotlib import style
x1=[1, 2, 3, 6, 7]
y1=[5, 5, 7, 3, 8 ]
x2=[1,2,3,4,5]
y2=[1,4,5,7,3]
plt.plot(x1,y1,color='k',label='line1',linewidth=4)
plt.plot(x2,y2,color='g',label='line1',linewidth=8)
plt.xlabel('x side')
plt.ylabel('y crd')
plt.title('plot')
plt.legend()

style.use('ggplot')
plt.grid(True)
plt.show()
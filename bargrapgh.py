#printing/plotting a bar grapg with a different command plt.bar()  instead of plt.plot()
#bar graph is used for catogorised values
from matplotlib import  pyplot as plt
from matplotlib import style
x1=[1, 2, 3, 6, 7]
y1=[5, 5, 7, 3, 8 ]
x2=[1,2,3,4,5]
y2=[1,4,5,7,3]
plt.bar(x1,y1,color='k',label='line1') #plt.bar() only difference


#grid is removed as not good with bar graph
plt.xlabel('x side')
plt.ylabel('y crd')
plt.title('plot')
plt.legend()




plt.show()
import matplotlib.pyplot as plt
import numpy as np


p=[1,2,4,5]
q=[45,64,34,12]
plt.plot(p,q)
plt.xlabel("time")
plt.ylabel("I")
plt.title('Mi')
plt.show()

#For subplot creation
x=[i for i in range(10)]
y=[i*i for i in range(10,20)]
z=[i*2 for i in range(10,20)]
plt.subplot(2,1,1)
plt.plot(x,y)
plt.subplot(2,1,2)
plt.plot(x,z)
plt.show()

x=np.arange(-10,10,0.1)
print(len(x))
#Graph for quadratic formula/cos value
i=np.arange(-10,10,0.1)
j=i*i +2*j +5
plt.plot(i,j)
plt.show()
#Bar Graph the format is plt.bar(x,y,color,width,label)
x=[i for i in range(10)]
y=[4,1,2,34,4,5,6,7,1,2]
x2=[i+0.2 for i in range(10)]#use to shift the bars away from one another
z=[4,1,2,34,4,5,2,1,1,2]
plt.bar(x,y,color="Blue",width=0.2,label="2017")
plt.bar(x2,z,color="Red",width=0.3,label="2018")
plt.legend()#Important to show labels
plt.title("Bar Graph")
plt.show()

#plt.pie(sizes,colors,labels,shadow,explode) Format for pie graph
#Example is day distribution

hours=[2,3,4,5,6,7,8]
activities=["Youtbe","Chill","Fun","play","tv","rest","sleep"]
explodes=[0,0.2,0,0,0,0,0.2]
plt.pie(hours,labels=activities,explode=explodes)
#Shadow is boolean value and explode is assigned to a list
plt.show()

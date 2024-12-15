#Bar graph
import numpy as np
import matplotlib.pyplot as plt
#creating a dataset
data={'SS':20,'NT':15,'EDC':30,'Python':35}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
#creating the barplot
plt.bar(courses,values,color='maroon',width=0.4)
plt.xlabel('Courses offered')
plt.ylabel('No of students enrolled')
plt.title('Students enrolled in different courses')
plt.show()

#scatter plor
import matplotlib.pyplot as plt
#dataset-1
x1=[89,43,36,36,95,10,66,34,38,20]
y1=[21,46,3,35,67,95,53,72,58,10]
#dataset-2
x2=[26,29,48,64,6,5,36,66,72,40]
y2=[26,34,90,33,38,20,56,2,47,15]
plt.scatter(x1,y1,c='pink',linewidths=2,marker='s',edgecolor='green',s=50)
plt.scatter(x2,y2,c='cyan',linewidths=2,marker='^',edgecolor='red',s=200)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


#boxplot
import matplotlib.pyplot as plt
value1=[1,10,20,30,40,50]
value2=[1,3,5,7,9]
value3=[2,4,6,8,10]
box_plot_data=[value1,value2,value3]
plt.boxplot(box_plot_data)
plt.show()

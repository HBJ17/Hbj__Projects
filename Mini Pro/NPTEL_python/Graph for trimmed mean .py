import matplotlib.pyplot as plt
import statistics
x = [472, 134, 298, 419, 255, 382, 97, 311, 451, 168,
284, 392, 276, 149, 356, 213, 489, 341, 192, 425,
277, 361, 146, 329, 493, 234, 287, 174, 421, 306,
255, 385, 114, 267, 498, 202, 332, 184, 476, 294,
361, 154, 443, 318, 209, 275, 398, 265, 489, 176]

x.sort()
tv=int(len(x)*0.1)
x = x[tv:]
x= x[:len(x)-tv]

y=[]
for i in range(len(x)):
    y.append(5)
#this is done so that we get constant value 5 in y-axis
#for loop make sure that the y list have same number of "5" as the number of data in x list.

plt.plot(x,y,'r--')
plt.plot([320],[5],'g^')  #this is the actual number
plt.plot(statistics.mean(x),[5],'ro') #this is the trimmed mean
plt.plot(statistics.median(x),[5],'r^')
plt.show()


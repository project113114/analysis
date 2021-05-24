import matplotlib.pyplot as plt
import psutil 
from itertools import count
from matplotlib.animation import FuncAnimation
#listing all data for axies
x = list()
y1 = list()
y2 = list()
y3 = list()

   
#indexing
index = count()
#function for live graph
def animate(i):
    #counting
    j = next(index)
    #appending data in list
    x.append(j)
    y1.append(psutil.cpu_freq()[0])
    y2.append(psutil.cpu_freq()[1])
    y3.append(psutil.cpu_freq()[2])
    #cla()
    plt.cla()
    #limiting x-axies
    plt.xlim(j-20,j+5)
    #ploting graph and label
    plt.plot(x,y1,label="current freq")
    plt.plot(x,y2,label="min freq")
    plt.plot(x,y3,label="max freq")
    plt.legend(loc = "upper left")
    #title and label
    plt.title("CPU Frequncey Status")
    plt.xlabel("interval = 0.1 sec")
    plt.ylabel("Freq in MHz")
 
    #removing past unusal data for ram management 
    #and smooth folw of graph and smooth operation
    if (j>21) :
        x.pop(0)
        y1.pop(0)
        y2.pop(0)
        y3.pop(0)
       
#funAnimation in use interval 0.1sec
ani = FuncAnimation(plt.gcf(), animate, interval=50)
plt.tight_layout()
#showing graph
plt.show()
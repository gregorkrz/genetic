import matplotlib.pyplot as plt

from time import sleep
import numpy as np
import math

pt1 = [[50, 0], [2, 10], [25, 20], [11, 30], [92, 40], [22, 50], [5, 60], [0, 70]]
path1 = [1 ,8 ,7 ,2 ,4 ,3 ,6, 5]


path1 = [1, 4, 6, 5, 2, 7, 3, 8]





def plotmap(path,pt=[[50, 0], [2, 10], [25, 20], [11, 30], [92, 40], [22, 50], [5, 60], [0, 70]]):
	for i in range(len(path)):
		path[i] = path[i]-1
	plt.figure()
	for i in pt:
		plt.plot(i[0],i[1],".",color="blue")
		
	for i in range(len(path)-1):
		plt.plot([pt[path[i]][0],pt[path[i+1]][0]],[pt[path[i]][1],pt[path[i+1]][1]],"-",color="red")
	k = len(path)-1
	plt.plot([pt[path[0]][0],pt[path[k]][0]],[pt[path[0]][1],pt[path[k]][1]],"-",color="red")
	plt.show()
	
plotmap(path1)


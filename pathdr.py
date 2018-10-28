import matplotlib.pyplot as plt

from time import sleep
import numpy as np
import math


path1 =  [[1, 11], [12, 5], [8, 13], [2, 10], [10, 14], [6, 9], [16, 2], [12, 14, 1, 4, 1, 11]


def plotmap(path):
	plt.figure()
	for i in range(len(path)-1):
		plt.plot([pt[path[i]][0],pt[path[i+1]][0]],[pt[path[i]][1],pt[path[i+1]][1]],"-",color="red")
	k = len(path)-1
	plt.plot([pt[path[0]][0],pt[path[k]][0]],[pt[path[0]][1],pt[path[k]][1]],"-",color="red")
	plt.show()
	
plotmap(path1)


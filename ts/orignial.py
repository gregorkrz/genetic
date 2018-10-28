import matplotlib.pyplot as plt

from time import sleep
import numpy as np
import math
chrlen = 8
num = 10
best = 0.2
gen = 0


########################
percent_breeded = 0.20
percent_mutated = 0.45
mutation_chance = 0.9
#######################



stddevs = []
avgs = []
geners = []


def initPop(chrlen1,num1):
	b = []
	
	for i in range(num1):
		b.append([])
		t = np.arange(8)+1
		np.random.shuffle(t)
		b[i] = t
	return np.array(b)
	
pop = initPop(chrlen,num)



def breed(mum,dad):
	return [mum,dad]
	# crossover
	
	pt = np.random.randint(0,chrlen-1)
	mum = mum.tolist()
	dad = dad.tolist()
	
	return [ mum[:pt]+dad[pt:] , dad[:pt]+mum[pt:] ]




def generatePoint(NoOfTrait=8):
    happendx = []
    happendy = []
    point = [2 * [0] for i in range(NoOfTrait)]#range confused!!!
    #for i in range(0,NoOfTrait):
    '''rndx = random.randint(0,100)
        rndy = random.randint(0,100)
        check(happendx, rndx,101)#can be better
        check(happendy, rndy,101)#can be better
        happendx.append(rndx)
        happendy.append(rndy)
        point[i][0] = rndx
        point[i][1] = rndy'''
    #city1
    point[0][0] = 50
    point[0][1] = 0
    #city2
    point[1][0] = 2
    point[1][1] = 10
    #city3
    point[2][0] = 25
    point[2][1] = 20
    #city4
    point[3][0] = 11
    point[3][1] = 30
    #city5
    point[4][0] = 92
    point[4][1] = 40
    #city6
    point[5][0] = 22
    point[5][1] = 50
    #city7
    point[6][0] = 5
    point[6][1] = 60
    #city8
    point[7][0] = 0
    point[7][1] = 70
      
    return point;

def fitness(hr):
	point = generatePoint()
	ptList = []
	for i in range(len(hr)):
		ptList.append(0)
		for a in range(1,len(hr[i])):       
			x = point[hr[i][a-1]-1][0]-point[hr[i][a]-1][0]
			y = point[hr[i][a-1]-1][1]-point[hr[i][a]-1][1]
			x1 = math.pow(x,2)
			y1 = math.pow(y,2)
			z = x1 + y1
			z = math.sqrt(z)
			#ptList.append(z)
			ptList[i] += z
		x = point[hr[i][len(hr[i])-1]-1][0]-point[hr[i][0]-1][0]
		y = point[hr[i][len(hr[i])-1]-1][1]-point[hr[i][0]-1][1]
		x1 = math.pow(x,2)
		y1 = math.pow(y,2)
		z = x1 + y1
		z = math.sqrt(z)
		ptList[i] += z
	return ptList


def plotff(population):
	global gen
	b = fitness(population)
	m = np.amin(b)
	x = np.amax(b)
	stddevs.append(np.std(b))
	avgs.append(np.median(b))
	geners.append(gen)

	ffs = {}
	k = (x-m)/100

	for i in range(len(b)):
		#if(b[i] > 1): print("ugh")
		#print("iter",i)
		#if(x-m == 0): print("err", x,m,b[i])
		tmp = round((b[i]-m)/(x-m) * 99) # the number 1-100
		#print("i=",i,"b[i]=",b[i],"x,m=",x,m)
		#print("tmp",tmp)
		#tmp = tmp * (x-m) + m
		if(tmp in ffs):
			ffs[tmp] += 1
		else:
			ffs[tmp]=1
		#print(ffs)
	ffs2 = {}	
	for key in ffs:
		ffs2[key/100*(x-m)+m]=ffs[key]
	if(gen%5 == 0): 
		plt.figure()
		plt.title("Generation " + str(gen))
		plt.xlabel("fitness function")
		plt.axis([0,5,0,40])
		plt.ylabel("number of chromosomes")
		plt.plot(*zip(*sorted(ffs2.items())))
		
		plt.savefig("gen"+str(gen)+".png")
	
	

def best(population): # returns an array of best chromosomes in the population
	ret = []
	f = fitness(population)
	avg = np.median(f)
	print("avg",avg,"FF len",len(f))
	#print(f)
	for i in range(len(f)):
		if(f[i] >= avg):
			ret.append(population[i])
			if(f[i] >= avg + 1.5*np.std(f)):
				print("wow!",population[i])
				
				for a in range(15):
					ret.append(population[i])
	return np.array(ret)


def rn(inp):
	#returns random index of the input array
	if(len(inp)<=0): print("ERR",len(inp),"INP",inp)
	a = np.random.randint(0,len(inp)-1)

	
	return a


def mutate(gene):
	# swaps 2 random genes (90% chance)
	if(np.random.rand() <= 0.9):
		rnd1 = rn(gene)
		rnd2 = rn(gene)
		t = gene[rnd2]
		gene[rnd2] = gene[rnd1]
		gene[rnd1] = t
	
	if(np.random.rand() <= 0.9):
		rnd1 = rn(gene)
		rnd2 = rn(gene)
		t = gene[rnd2]
		gene[rnd2] = gene[rnd1]
		gene[rnd1] = t
	if(np.random.rand() <= 0.9):
		rnd1 = rn(gene)
		rnd2 = rn(gene)
		t = gene[rnd2]
		gene[rnd2] = gene[rnd1]
		gene[rnd1] = t
	return gene

def newGen(population):
	global gen
	ret = []
	gen = gen + 1
	
	# returns a new generation
	
	b = best(population)
	#print("B.LENGTH",len(b))

	for i in range(round(len(b)*percent_breeded/2)):
		#print(i)
		rnd1 = b[rn(b)]
		rnd2 = b[rn(b)]
		#print("parents",rnd1,rnd2)
		children = breed(rnd1,rnd2)
		#print("children",children)
		#print("CHILDREN",children[0],children[1])
		for c in children:
			ret.append(c)
		#	print("RET",ret)
	for i in range(round(len(population)*percent_mutated)):
		if(np.random.rand() < mutation_chance):
			mut = mutate(b[rn(b)])
			ret.append(mut)
	while(len(ret) < len(population)):
		ret.append(b[rn(b)])
	return np.array(ret)

av1=0

bestfitness = 0

bestfitness = 100000
bestchr = "<empty chromosome>"
		
bestgens = []
if(1):
	for i in range(10):
		print("generation",i)
		if(i==0): firstone=pop
		plotff(pop)
		pop_temp = newGen(pop)
		fit = (fitness(pop_temp))
		if(0 and np.median(fit) < av1):
			# this is not a good decision; try again?
			# print("ignoring")
			i = i - 1
		else:
			av1 = np.median(fit)
			bestgens.append(np.amin(fit))
			if(np.amin(fit)<bestfitness):
				bestfitness = np.amin(fit)
				bestchr = pop[np.argmin(fit)]
			pop = pop_temp
			if(i==99): print(pop[0])
			print("Best one so far:",bestfitness)
			print(bestchr)
		
plt.figure()
plt.plot(geners,avgs,label="avg")
plt.plot(geners,stddevs,label="stddev")
plt.legend()
plt.savefig('stats.png')

def plotmap(pt,path):
	for i in range(len(path)):
		path[i] = path[i]-1
	plt.figure()
	for i in pt:
		plt.plot(i[0],i[1],".",color="blue")
		
	for i in range(len(path)-1):
		plt.plot([pt[path[i]][0],pt[path[i+1]][0]],[pt[path[i]][1],pt[path[i+1]][1]],"-",color="red")
	k = len(path)-1
	plt.plot([pt[path[0]][0],pt[path[k]][0]],[pt[path[0]][1],pt[path[k]][1]],"-",color="red")
	plt.savefig("a123a.png")
	
plotmap(generatePoint(),bestchr.tolist())


'''
def bestFromGen(population): #WIP
	# returns best chromosomes and some randomly selected ones
	f = np.array([fitness(population)])
	t = []
	for i in range(population.size):
		t.append([[population[i]],[f[i]]])
	t = np.array(t)
	t.view('i8,i8,i8').sort(order=['f1'], axis=0)
	
'''	

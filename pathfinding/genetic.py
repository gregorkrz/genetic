import matplotlib.pyplot as plt

from time import sleep
import numpy as np

chrlen = 20
num = 100

gen = 0


########################
percent_breeded = 0.20
percent_mutated = 0.45

#######################



stddevs = []
avgs = []
geners = []


def initPop(chrlen1,num1):
	x = []
	for i in range(20):
		x.append(np.random.randint(1,20))
	return np.array(x)
	
pop = initPop(chrlen,num)



def breed(mum,dad):
	
	# crossover
	
	pt = np.random.randint(0,chrlen-1)
	mum = mum.tolist()
	dad = dad.tolist()
	
	return [ mum[:pt]+dad[pt:] , dad[:pt]+mum[pt:] ]






def fitness(population):
	#  A fitness function (fitness = distance of the path)
	r = np.array(num*[0.0])

	for i in range(num):
		pts = [[0],[0]]
		
		for x in range(20):
			if(x%2):
				# 1,3,5...

				pts[1].append(population[i][x])

			else:
				print(population[i][x])
				pts[0].append(population[i][x])
		pts[0].append(20)
		pts[1].append(20)
		for y in range(len(pts[0])-1):
			r[i] += np.sqrt((pts[0][y]-pts[0][y+1])**2+(pts[1][y]-pts[1][y+1])**2)
			
			
	return r


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
		if(f[i] < avg):
			ret.append(population[i])
			#if(f[i] >= avg + 1.5*np.std(f)):
			#	print("wow!",population[i])
				
			#	for a in range(15):
			#		ret.append(population[i])
	return np.array(ret)

def rn(inp):
	#returns random index of the input array
	if(len(inp)<=0): print("ERR",len(inp),"INP",inp)
	a = np.random.randint(0,len(inp)-1)

	
	return a


def mutate(gene):
	# swaps 2 random genes (50% chance)
	if(np.random.rand() <= 0.5):
		rnd1 = rn(gene)
		rnd2 = rn(gene)
		t = gene[rnd2]
		gene[rnd2] = gene[rnd1]
		gene[rnd1] = t
	# variate the inputs by up to +-2
	for i in range(len(gene)):
		rr = np.random.randint(-2,2)/100
		rr2 = rn(gene)
		gene[rr2] = gene[rr2] + rr
		
	
	
	
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
		mut = mutate(b[rn(b)])
		ret.append(mut)
	while(len(ret) < len(population)):
		ret.append(b[rn(b)])
	return np.array(ret)

av1=0

bestfitness = 0


for i in range(100):
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
		if(np.amax(fit)>bestfitness): bestfitness = np.amax(fit)
		pop = pop_temp
		if(i==99): print(pop[0])
		print("Best one so far:",bestfitness)
		print(pop[np.argmax(fit)])
plt.figure()
plt.plot(geners,avgs,label="avg")
plt.plot(geners,stddevs,label="stddev")
plt.legend()
plt.savefig('stats.png')


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




import numpy as np

chrlen = 20
num = 300



gen = 0


########################
percent_breeded = 0.2
rand_mut = 0.3
#######################


bestgens = []
stddevs = []
avgs = []
geners = []
first40 = 0
first40chr = []
def initPop(chrlen1,num1):
	x = []
	for i in range(num1):
		x.append([])
		for j in range(chrlen):
			x[i].append(np.random.randint(1,20))
	return np.array(x)
	
pop = initPop(chrlen,num)



def breed(mum,dad):
	
	# crossover
	
	pt = np.random.randint(0,chrlen-1)
	mum = mum.tolist()
	dad = dad.tolist()
	
	return [ mum[:pt]+dad[pt:] , dad[:pt]+mum[pt:] ]






def fitness(population):
	#  the fitness function (fitness = distance of the path)
	r = np.array(num*[0.0])

	for i in range(num):
		pts = [[0],[0]]
		
		for x in range(20):
			if(x%2):
				# 1,3,5...
				pts[1].append(population[i][x])

			else:
				pts[0].append(population[i][x])
		pts[0].append(20)
		pts[1].append(20)
		for y in range(len(pts[0])-1):
			#r[i] += np.sqrt((pts[0][y]-pts[0][y+1])**2+(pts[1][y]-pts[1][y+1])**2)
			r[i] += abs(pts[0][y]-pts[0][y+1])+abs(pts[1][y]-pts[1][y+1])
			
	return r


def best(population,sensitivity=0): # returns an array of the best chromosomes in the population
	ret = []
	f = fitness(population)
	avg = np.median(f)
	print("avg",avg,"FF len",len(f))
	#print(f)
	for i in range(len(f)):
		if(0 and f[i] < avg and not sensitivity):
			ret.append(population[i])
			#if(f[i] >= avg + 1.5*np.std(f)):
			#	print("wow!",population[i])
				
			#	for a in range(15):
			#		ret.append(population[i])
	if(sensitivity):
			c = np.argsort(f)
			# now choose the best/lowest 30%
			for y in range(round(len(f)*0.3)):
				ret.append(population[c[y]])
			for y in range(round(len(f)*0.05)):
				for č in range(5):
					ret.append(population[c[y]])

	return np.array(ret)
	
def rn(inp):
	#returns random index of the input array
	if(len(inp)<=0): print("ERR",len(inp),"INP",inp)
	a = np.random.randint(0,len(inp)-1)
	
	
	return a


def mutate(gene):
	# swaps 2 random genes (20% chance)
	if(np.random.rand() <= 0.2):
		rnd1 = rn(gene)
		rnd2 = rn(gene)
		t = gene[rnd2]
		gene[rnd2] = gene[rnd1]
		gene[rnd1] = t
	# variate the inputs by up to +-2
	for i in range(len(gene)):
		if(np.random.rand()<rand_mut):
			a = np.random.randint(-2,2)
			if(not (gene[i]+a > 20 or gene[i]+a < 1)):
				gene[i] = gene[i]+a
	return gene

def newGen(population):
	global gen
	ret = []
	gen = gen + 1
	
	# returns a new generation
	
	b = best(population)
	if(1):
	#print("B.LENGTH",len(b))
		if(len(b)==0): b = best(population,1)
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
		for i in range(round(len(population))):
			mut = mutate(b[rn(b)])
			ret.append(mut)
		while(len(ret) < len(population)):
			ret.append(b[rn(b)])
		return np.array(ret)

	
		
av1=0

bestfitness = 100000
bestchr = "<empty chromosome>"

if(1):
	for i in range(100):
		print("generation",i)
		if(i==0): firstone=pop

		pop_temp = newGen(pop)
		fit = (fitness(pop_temp))
		if(0 and np.median(fit) < av1):
			# this is not a good decision; try again?
			# print("ignoring")
			i = i - 1
		else:
			if(np.amin(fit)==40 and first40 == 0):
				first40 = i
				first40chr = pop_temp[np.argmin(fit)]
			av1 = np.median(fit)
			bestgens.append(np.amin(fit))
			if(np.amin(fit)<bestfitness):
				bestfitness = np.amin(fit)
				bestchr = pop[np.argmin(fit)]
			pop = pop_temp
			if(i==99): print(pop[0])
			print("Best one so far:",bestfitness)
			print(bestchr)
			


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

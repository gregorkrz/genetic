import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps as integrate
from scipy.stats import linregress as regression
def Boundary(percent,sigma):
	a=1
	b=0
	c=sigma

	def f(x):
		return a*np.exp(-(x-b)*(x-b)/(2*c*c))
	
	x = np.arange(-100,100,0.01)
	y = f(x)
	whole = integrate(y,x,dx=0.01)



	#print(whole)
	fint  = percent/2 * whole
	i=0
	s=[0,0.01]
	## dx = 0.01
	while(i <= fint):
		#print("s0",s[0],"s1",s[1])
		i += 0.01*((f(s[0])-f(s[1]))/2+f(s[1]))
		n=s[1]
		s[0] = s[1]
		s[1]=n+0.01
	#print("boundary:",s[0])
	t=np.arange(-s[0],s[0],0.01)
	#print(integrate(f(t),t,dx=0.01)/whole)
	return s[0]
	
Xs = np.arange(0.5,20,0.5)
Ys = []
#print("xy",Boundary(0.95,1))
#print("bnd",Boundary(0.95,0.5))

for a in range(Xs.size):
	Ys.append(Boundary(0.80,Xs[a]))


Ys = np.array(Ys)

# BOUNDARY VS SIGMA GRAPH

plt.figure()
plt.plot(Xs,Ys,"-")
plt.show()


# linear regression
slope, intercept, r_value, p_value, std_err = regression(Xs,Ys)
print("slope",slope,"intercept",intercept)


from numpy import loadtxt, zeros 
from pylab import plot ,show
i 
h=loadtxt("sunspots.txt",float)
plot(h[:,0],h[:,1])
show() 

plot(h[:,0],h[:,1])
xlim(0.1001)
show()
r=5
y1=zeros(1000,float)

for k in  range(0,1001):
	for m in range(-r,r):
		y[k]+=[km,1]
        y1[k]/=2*r+1

plot(a[0:1000,0],y)
show()		

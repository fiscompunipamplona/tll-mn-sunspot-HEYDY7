from pylab import plot,show

#x=[] 
#y=[]

#for  i in range(10):

#	y.append(i*i)
#	x.append(2*i)
#plot(x,y)
#show()
#2
from numpy import  linspace,sin,loadtxt,cos

x = linspace(0,10,100)
y = sin(x)
z = cos(x)
#plot(x,y)
#show()
#3
h = open("prueba.dat","w")
for i in range(len(x)):
	h.write("%.2f %.2f %.2f\n" % (x[i], y[i],z[i]))
h.close()
#$
z = loadtxt("prueba.dat",float)
#plot(x,y)
plot(z[:,0],z[:,1],"go")
plot(z[:,0],z[:,2])
show()
#5


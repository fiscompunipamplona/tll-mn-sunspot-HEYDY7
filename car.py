import math as mt


r=float( input("ingrese el valor de r:"))
theta =float( input("ingrese el valor de theta:"))
x=r*mt.cos(theta)
y=r*mt.sin(theta)
print("x:",x)
print("y:",y)


#2
x= float(input("ingrese el valor de la distancia en años luz:"))
v= float(input("ingrese el valor de la velocidad de la nave en fraccion de c(m/s):"))
x1=x*9.461e+15
t=x1/v
print("tiempo desde la tierra en segundos t:",t ) # s
c=3e8 # m/s
gamma= mt.sqrt(1-v**2)
print("el valor de gamma es..",gamma)
t1= gamma*(t-(v*x)/c)
print("el valor del tiempo desde la nave es..",t1)
#3

f1=1
f2=1
print (f1)
print(f2)
f3=f1+f2
print(f3)
while f3<1000:
     f1=f2
     f2=f3
     f3=f1+f2
     if f3>1000:
             break  
     print(f3) 
 


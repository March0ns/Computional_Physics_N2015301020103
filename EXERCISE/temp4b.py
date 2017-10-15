from pylab import *
from math import *

x1=[0.]
y1=[0.]
x2=[0.]
y2=[0.]

vx1=[20.]
vy1=[100.]
vx2=[20.]
vy2=[100.]
g=9.8
b2m=4e-5
a=6.5e-3
t=10000
dt=0.1
for i in range(int(t/dt)):
	v=sqrt(vx1[i]**2+vy1[i]**2)
	f=b2m*(1-a*y1[i]/293.15)**2.5
	f_x=f*v*vx1[i]/v
	f_y=f*v*y1[i]/v
	v_x1=vx1[i]-f_x*dt
	v_y1=vy1[i]-f_y*dt-g*dt
	vx1.append(v_x1)
	vy1.append(v_y1)
	temp_x1=x1[i]+vx1[i]*dt
	temp_y1=y1[i]+vy1[i]*dt
	if y1[i]>=0.:
		x1.append(temp_x1)
		y1.append(temp_y1)
	else:
		break
plot(x1,y1,color='c',label="Air drag with density correction")
for i in range(int(t/dt)):
	v=sqrt(vx2[i]**2+vy2[i]**2)
	f=b2m*(v**2)
	f_x=f*v*vx2[i]/v
	f_y=f*v*vy2[i]/v
	v_x2=vx2[i]-f_x*dt
	v_y2=vy2[i]-f_y*dt-g*dt
	vx2.append(v_x2)
	vy2.append(v_y2)
	temp_x2=x2[i]+vx2[i]*dt
	temp_y2=y2[i]+vy2[i]*dt
	if y2[i]>=0.:
		x2.append(temp_x2)
		y2.append(temp_y2)
	else:
		break
plot(x2,y2,color='r',label="Air drag without density correction")
legend(loc='upper left')
title('density')
show()

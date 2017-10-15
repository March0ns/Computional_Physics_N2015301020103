from math import *
from pylab import *
g=9.8
dt=0.1
t=1000
a=6.5e-3
b2m=4e-5 
x30=[0]
y30=[0]
vx30=[300*cos(radians(30))]
vy30=[300*sin(radians(30))]
for i in range(int(t/dt)):
		v=sqrt(vx30[i]**2+vy30[i]**2)
		f=b2m*(1-a*y30[i]/253.16)**2.5
		f_x=f*v*vx30[i]/v
		f_y=f*v*vy30[i]/v
		v_x=vx30[i]-f_x*dt
		v_y=vy30[i]-g*dt-f_y*dt
		vx30.append(v_x)
		vy30.append(v_y)
		x_temp=x30[i]+vx30[i]*dt
		y_temp=y30[i]+vy30[i]*dt
		print (vx30[i],vy30[i],x30[i],y30[i])
		if y30[i]>=0:
			x30.append(x_temp)
			y30.append(y_temp)
		else:
			break
plot(x30,y30,color='g',label="30")
x35=[0]
y35=[0]
vx35=[300*cos(radians(35))]
vy35=[300*sin(radians(35))]
for i in range(int(t/dt)):
		v=sqrt(vx35[i]**2+vy35[i]**2)
		f=b2m*(1-a*y35[i]/253.16)**2.5
		f_x=f*v*vx35[i]/v
		f_y=f*v*vy35[i]/v
		v_x=vx35[i]-f_x*dt
		v_y=vy35[i]-g*dt-f_y*dt
		vx35.append(v_x)
		vy35.append(v_y)
		x_temp=x35[i]+vx35[i]*dt
		y_temp=y35[i]+vy35[i]*dt
		print (vx35[i],vy35[i],x35[i],y35[i])
		if y35[i]>=0.:
			x35.append(x_temp)
			y35.append(y_temp)
		else:
			break
plot(x35,y35,color='r',label="35")
x40=[0]
y40=[0]
vx40=[300*cos(radians(40))]
vy40=[300*sin(radians(40))]
for i in range(int(t/dt)):
		v=sqrt(vx40[i]**2+vy40[i]**2)
		f=b2m*(1-a*y40[i]/253.16)**2.5
		f_x=f*v*vx40[i]/v
		f_y=f*v*vy40[i]/v
		v_x=vx40[i]-f_x*dt
		v_y=vy40[i]-g*dt-f_y*dt
		vx40.append(v_x)
		vy40.append(v_y)
		x_temp=x40[i]+vx40[i]*dt
		y_temp=y40[i]+vy40[i]*dt
		print (vx40[i],vy40[i],x40[i],y40[i])
		if y40[i]>=0:
			x40.append(x_temp)
			y40.append(y_temp)
		else:
			break
plot(x40,y40,color='b',label="40")
x45=[0.]
y45=[0.]
vx45=[300*cos(radians(45))]
vy45=[300*sin(radians(45))]
for i in range(int(t/dt)):
		v=sqrt(vx45[i]**2+vy45[i]**2)
		f=b2m*(1-a*y45[i]/253.16)**2.5
		f_x=f*v*vx45[i]/v
		f_y=f*v*vy45[i]/v
		v_x=vx45[i]-f_x*dt
		v_y=vy45[i]-g*dt-f_y*dt
		vx45.append(v_x)
		vy45.append(v_y)
		x_temp=x45[i]+vx45[i]*dt
		y_temp=y45[i]+vy45[i]*dt
		print (vx45[i],vy45[i],x45[i],y45[i])
		if y45[i]>=0:
			x45.append(x_temp)
			y45.append(y_temp)
		else:
			break
plot(x45,y45,color='c',label="45")
x50=[0]
y50=[0]
vx50=[300*cos(radians(50))]
vy50=[300*sin(radians(50))]
for i in range(int(t/dt)):
		v=sqrt(vx50[i]**2+vy50[i]**2)
		f=b2m*(1-a*y50[i]/253.16)**2.5
		f_x=f*v*vx50[i]/v
		f_y=f*v*vy50[i]/v
		v_x=vx50[i]-f_x*dt
		v_y=vy50[i]-g*dt-f_y*dt
		vx50.append(v_x)
		vy50.append(v_y)
		x_temp=x50[i]+vx50[i]*dt
		y_temp=y50[i]+vy50[i]*dt
		print (vx50[i],vy50[i],x50[i],y50[i])
		if y50[i]>=0.:
			x50.append(x_temp)
			y50.append(y_temp)
		else:
			break
plot(x50,y50,color='m',label="50")
x55=[0]
y55=[0]
vx55=[300*cos(radians(55))]
vy55=[300*sin(radians(55))]
for i in range(int(t/dt)):
		v=sqrt(vx55[i]**2+vy55[i]**2)
		f=b2m*(1-a*y55[i]/253.16)**2.5
		f_x=f*v*vx55[i]/v
		f_y=f*v*vy55[i]/v
		v_x=vx55[i]-f_x*dt
		v_y=vy55[i]-g*dt-f_y*dt
		vx55.append(v_x)
		vy55.append(v_y)
		x_temp=x55[i]+vx55[i]*dt
		y_temp=y55[i]+vy55[i]*dt
		print (vx55[i],vy55[i],x55[i],y55[i])
		if y55[i]>=0:
			x55.append(x_temp)
			y55.append(y_temp)
		else:
			break
plot(x55,y55,color='y',label="55")
x60=[0]
y60=[0]
vx60=[300*cos(radians(60))]
vy60=[300*sin(radians(60))]
for i in range(int(t/dt)):
		v=sqrt(vx60[i]**2+vy60[i]**2)
		f=b2m*(1-a*y60[i]/253.16)**2.5
		f_x=f*v*vx60[i]/v
		f_y=f*v*vy60[i]/v
		v_x=vx60[i]-f_x*dt
		v_y=vy60[i]-g*dt-f_y*dt
		vx60.append(v_x)
		vy60.append(v_y)
		x_temp=x60[i]+vx60[i]*dt
		y_temp=y60[i]+vy60[i]*dt
		print (vx60[i],vy60[i],x60[i],y60[i])
		if y60[i]>=0:
			x60.append(x_temp)
			y60.append(y_temp)
		else:
			break
plot(x60,y60,color='k',label="60")
legend(loc='best')
title('different firing angles')
show()
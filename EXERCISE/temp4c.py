from math import *
from pylab import *
x=[]
y=[]
v_x=[]
v_y=[]


thetarange=[]
shootrange=[]
dt=0.01
g=-9.8
c=700
a=6.5e-3
b2m=4e-5

for theta in range(30,61):
    
    v_x.append(c*cos(radians(theta)))
    v_y.append(c*sin(radians(theta)))
    x.append(0.0)
    y.append(0.0)
    
    while y[-1]>=0.0:
        c=sqrt(v_x[-1]**2+v_y[-1]**2)
        f=b2m*(1-a*y[-1]/293.16)**2.5
        f_x=f*c*v_x[-1]/c
        f_y=f*c*v_y[-1]/c
        v_x_tmp=v_x[-1]-f_x*dt
        v_x.append(v_x_tmp)
        v_y_tmp=v_y[-1]+dt*g-f_y*dt
        v_y.append(v_y_tmp)
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
    thetarange.append(theta)
    shootrange.append(x[-1])
print("the value of the angle that gives the maximum range:",thetarange[shootrange.index(max(shootrange))])

plot(thetarange,shootrange,'or' , label="(theta,shoot range)",color = "r")
xlabel("theta")
ylabel("shoot range")
title('the relationship bewteen Theta and shoot range \n of a cannon shell with air drag and density correction')
legend()
show()

from pylab import *
import numpy as np
l=9.8
g=9.8
dt=0.04
q=0.5
F=1.2
D=2.0/3.0
w=[0]
w1=[0]
x=[0.2]
x1=[0.201]
t=[0]
delt_x=[0.001]
while t[-1]<=200:    
       current_w=w[-1]
       current_x=x[-1]
       current_t=t[-1]
       next_w=current_w-(g/l*np.sin(current_x)+q*current_w-F*sin(D*current_t))*dt
       next_x=current_x+next_w*dt
       next_t=current_t+dt
       current_w1=w1[-1]
       current_x1=x1[-1]
       next_w1=current_w1-(g/l*np.sin(current_x1)+q*current_w1-F*sin(D*current_t))*dt
       next_x1=current_x1+next_w1*dt
 
       w.append(next_w)
       x.append(next_x)
       w1.append(next_w1)
       x1.append(next_x1)       
       t.append(next_t)
       
       delt_x.append(abs(x[-1]-x1[-1]))
       
        
       
plot(t,log(delt_x))

show()
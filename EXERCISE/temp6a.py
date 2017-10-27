from pylab import *
import numpy as np
l=9.8
g=9.8
dt=0.04
q=0.5
F=1.2
D=2.0/3.0
w=[0]
x=[0.2]
t=[0]
n=0

while t[-1]<=5000:    
       current_w=w[-1]
       current_x=x[-1]
       current_t=t[-1]
       next_w=current_w-(g/l*np.sin(current_x)+q*current_w-F*sin(D*current_t))*dt
       next_x=current_x+next_w*dt
       next_t=current_t+dt
       if next_x>np.pi:
              next_x+=-2*np.pi
       else:
              if next_x<-np.pi:
                   next_x+=2*np.pi
              else:next_x=next_x
       w.append(next_w)
       x.append(next_x)
       t.append(next_t)
'''plot(t,x)
xlim(0,150)
plot(x,w,',')'''

while 2*n*pi/D<=t[-1]:
        scatter(x[int(2*n*pi/D/dt)],w[int(2*n*pi/D/dt)],c="b",Alpha=0.3)
        n=n+1

show()
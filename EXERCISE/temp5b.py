# -*from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from math import *
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure(figsize=(9,6))

ax = fig.gca(projection='3d')
g=9.8
dt=0.1
t=1000
s0m=4.1e-4
w=4000*pi/60



x3=[0]
y3=[0]
z3=[0]
vx3=[30]
vy3=[10]
vz3=[20]
for i in range(int(t/dt)):
       v=sqrt(vx3[i]**2+vy3[i]**2+vz3[i]**2)
       b2m=0.0039+0.0058/(1+exp((v-35)/5))
       f_x=b2m*v*vx3[i]+s0m*w*vz3[i]
       f_z=b2m*v*vz3[i]+g*dt-s0m*w*vx3[i]
       f_y=b2m*v*vy3[i]
       v_x=vx3[i]-f_x*dt
       v_y=vy3[i]-f_y*dt
       v_z=vz3[i]-f_z*dt
       vx3.append(v_x)
       vz3.append(v_z)
       vy3.append(v_y)
       x_temp=x3[i]+vx3[i]*dt
       y_temp=y3[i]+vy3[i]*dt
       z_temp=z3[i]+vz3[i]*dt
       print (vx3[i],vy3[i],vz3[i],x3[i],y3[i],z3[i])
       if z3[i]>=0:
          x3.append(x_temp)
          y3.append(y_temp)
          z3.append(z_temp)
       else:
          break
ax.plot(x3,y3,z3,color='r',label='no wind')      
x1=[0]
y1=[0]
z1=[0]
vx1=[30]
vy1=[10]
vz1=[20]
for i in range(int(t/dt)):
       v=sqrt(vx1[i]**2+vy1[i]**2+vz1[i]**2)
       b2m=0.0039+0.0058/(1+exp((v-35)/5))
       f_x=b2m*v*(vx1[i]+3)+s0m*w*vz1[i]
       f_z=b2m*v*vz1[i]+g*dt-s0m*w*vx1[i]
       f_y=b2m*v*vy1[i]
       v_x=vx1[i]-f_x*dt
       v_y=vy1[i]-f_y*dt
       v_z=vz1[i]-f_z*dt
       vx1.append(v_x)
       vy1.append(v_y)
       vz1.append(v_z)
       x_temp=x1[i]+vx1[i]*dt
       y_temp=y1[i]+vy1[i]*dt
       z_temp=z1[i]+vz1[i]*dt
       print (vx1[i],vy1[i],vz1[i],x1[i],y1[i],z1[i])
       if z1[i]>=0:
          x1.append(x_temp)
          y1.append(y_temp)
          z1.append(z_temp)
       else:
          break
ax.plot(x1,y1,z1,color='g',label='against the wind')      
x2=[0]
y2=[0]
z2=[0]
vx2=[30]
vy2=[10]
vz2=[20]
for i in range(int(t/dt)):
       v=sqrt(vx2[i]**2+vy2[i]**2+vz2[i]**2)
       b2m=0.0039+0.0058/(1+exp((v-35)/5))
       f_x=b2m*v*(vx2[i]-3)+s0m*w*vz2[i]
       f_z=b2m*v*vz2[i]+g*dt-s0m*w*vx2[i]
       f_y=b2m*v*vy2[i]
       v_x=vx2[i]-f_x*dt
       v_y=vy2[i]-f_y*dt
       v_z=vz2[i]-f_z*dt
       vx2.append(v_x)
       vy2.append(v_y)
       vz2.append(v_z)
       x_temp=x2[i]+vx2[i]*dt
       y_temp=y2[i]+vy2[i]*dt
       z_temp=z2[i]+vz2[i]*dt
       print (vx2[i],vy2[i],vz2[i],x2[i],y2[i],z2[i])
       if z2[i]>=0:
          x2.append(x_temp)
          y2.append(y_temp)
          z2.append(z_temp)
       else:
          break
ax.plot(x2,y2,z2,color='k',label='following the wind') 
      
ax.legend()                        
plt.xlabel("x(m)")
plt.ylabel("y(m)")
ax.set_zlabel("z(m)")       
        
        
        
plt.title("trajectory of battedball in the wind")
plt.show()

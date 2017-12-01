
import matplotlib.pyplot as plt
G=6.67e-11
m1=1.989e30
m2=5.98e24
m3=318*m2*10
dt=3600*24/10
end_t=20*365*3600*24
t=[0]

x_1=[0.]
v_x_1=[0]
y_1=[0.]
v_y_1=[0]

x_2=[1.5e11]
v_x_2=[0]
y_2=[0.]
v_y_2=[3e4]

x_3=[778.6e9]
v_x_3=[0]
y_3=[0.]
v_y_3=[13.1e3]


for i in range(int(end_t/dt)):

      v_x_1.append(v_x_1[i]+(G*m2*(x_2[i]-x_1[i])/((x_1[i]-x_2[i])**2+(y_1[i]-y_2[i])**2)**(1.5)+G*m3*(x_3[i]-x_1[i])/((x_1[i]-x_3[i])**2+(y_1[i]-y_3[i])**2)**(1.5))*dt)
      v_x_2.append(v_x_2[i]+(G*m1*(x_1[i]-x_2[i])/((x_1[i]-x_2[i])**2+(y_1[i]-y_2[i])**2)**(1.5)+G*m3*(x_3[i]-x_2[i])/((x_2[i]-x_3[i])**2+(y_2[i]-y_3[i])**2)**(1.5))*dt)
      v_x_3.append(v_x_3[i]+(G*m1*(x_1[i]-x_3[i])/((x_1[i]-x_3[i])**2+(y_1[i]-y_3[i])**2)**(1.5)+G*m2*(x_2[i]-x_3[i])/((x_2[i]-x_3[i])**2+(y_2[i]-y_3[i])**2)**(1.5))*dt)
      v_y_1.append(v_y_1[i]+(G*m2*(y_2[i]-y_1[i])/((x_1[i]-x_2[i])**2+(y_1[i]-y_2[i])**2)**(1.5)+G*m3*(y_3[i]-y_1[i])/((x_1[i]-x_3[i])**2+(y_1[i]-y_3[i])**2)**(1.5))*dt)
      v_y_2.append(v_y_2[i]+(G*m1*(y_1[i]-y_2[i])/((x_1[i]-x_2[i])**2+(y_1[i]-y_2[i])**2)**(1.5)+G*m3*(y_3[i]-y_2[i])/((x_2[i]-x_3[i])**2+(y_2[i]-y_3[i])**2)**(1.5))*dt)
      v_y_3.append(v_y_3[i]+(G*m1*(y_1[i]-y_3[i])/((x_1[i]-x_3[i])**2+(y_1[i]-y_3[i])**2)**(1.5)+G*m2*(y_2[i]-y_3[i])/((x_2[i]-x_3[i])**2+(y_2[i]-y_3[i])**2)**(1.5))*dt)
      x_1.append(x_1[i]+v_x_1[i+1]*dt)
      x_2.append(x_2[i]+v_x_2[i+1]*dt)
      x_3.append(x_3[i]+v_x_3[i+1]*dt)
      y_1.append(y_1[i]+v_y_1[i+1]*dt)
      y_2.append(y_2[i]+v_y_2[i+1]*dt)
      y_3.append(y_3[i]+v_y_3[i+1]*dt)




plt.plot(x_1,y_1,'-' ,label='sun,$r_1=1,m_1=1$')
plt.plot(x_2,y_2,'-',label='earth,$r_2=1,m_2=1$')
plt.plot(x_3,y_3,'-',label='jupiter,$r_3=1,m_3=1$')
plt.title(u'the orbit of star',fontsize=14)
plt.xlabel(u'x/AU',fontsize=14)
plt.ylabel(u'y/AU',fontsize=14)
plt.legend(fontsize=8,loc='best')
plt.show()


from pylab import*
v=[]
t=[]
a=10
b=1
dt=0.1

v.append(0)
t.append(0)
for i in range(1000):
    v.append(v[i]+(a-b*v[i])*dt)
    t.append(t[i]+dt)

plot(t,v,'ko-')
title('the velocity of a parachutist')
xlabel('t')
ylabel('v')
show()



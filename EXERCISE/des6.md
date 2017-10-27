## EXEXCISE 3.12    
* 姓名：王硕
* 学号：2015301020103
* 班级：物基二班    
#### 1.摘要：
* 混沌现象：指发生在确定性系统中的貌似随机的不规则运动，一个确定性理论描述的系统，其行为却表现为不确定性一不可重复、不可预测，这就是混沌现象
* 用Euler-Cromer方法模拟计算混沌现象    
####2.正文：    
用Euler-Cromer方法模拟计算如下驱动力下的混沌现象：
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d} \theta ^{2}}{\mathrm{d} t^2}=-\frac{g}{l}sin\theta -q\frac{\mathrm{d} \theta }{\mathrm{d} t}+F_{D}sin(\Omega _{D}t)">    
即：    
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d} \omega}{\mathrm{d} t}=-\frac{g}{l}sin\theta -q\frac{\mathrm{d} \theta }{\mathrm{d} t}+F_{D}sin(\Omega _{D}t)">     
运用Euler-Cromer方法：    
<img src="http://latex.codecogs.com/gif.latex?\omega_{i+1}=\omega_{i}-[(\frac{g}{l})sin\theta_{i}-q\omega_{i}+F_{D}sin(\Omega_{D})]\Delta t">   
<img src="http://latex.codecogs.com/gif.latex?\theta_{i+1}=\theta_{i}+\omega_{i+1}\Delta t">
<img src="http://latex.codecogs.com/gif.latex?t_{i+1}=t_{i}+\Delta t">


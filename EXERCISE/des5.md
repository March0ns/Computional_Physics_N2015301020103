
## EXERCISE 2.9    
* 姓名：王硕
* 学号：2015301020103
* 班级：物基二    
#### 1 摘要：    
* 旋转对棒球射距的影响，Magus力
* 风速
* 3d图
#### 2 题目     
Modle the effect of backspin on the range of a batted ball.Assume an angular velocity of 2000 rpm    
#### 3 正文     
考虑旋转与空气阻力，棒球的运动方程：    
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,x}{\mathrm{d}\,t}=v_{x}\,"> 
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,v_{x}}{\mathrm{d}\,t}=-\frac{B_{2}}{m}vv_{x}+\frac{F_{Magnus}}{m}">          
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,y}{\mathrm{d}\,t}=v_{y}\,">     
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,v_{y}}{\mathrm{d}\,t}=-\frac{B_{2}}{m}vv_{y}\,">      
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,z}{\mathrm{d}\,t}=v_{z}">
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,v_{z}}{\mathrm{d}\,t}=-\frac{B_{2}}{m}vv_{z}-g-\frac{F_{Magnus}}{m}">     
<img src="http://latex.codecogs.com/gif.latex?F_{Magnus}=S_{0}\omega\,\times\,v">      
运用Euler法
#### 4 图像与分析
* 参数：
* 1.S0/m=4.1e-4
* 2.B2/m=0039+0.0058(1+exp((v-35)/5)))      
* 3.omega=4000*pi/60       
* vx=30m/s,vy=10m/s,vz=20m/s          
![]()
* 棒球旋转后，会产生一个“回旋力”，对球的轨迹造成很大的影响，甚至有回旋回来的趋势。
* 上旋球会“抬高”棒球的轨迹，使球飞的更远。下旋球正相反，会使球更快降落。      
！[]()      
* 显然顺风会打的更远

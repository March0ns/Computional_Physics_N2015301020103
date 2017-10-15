## The trajectory of a cannon shell    (exerxise2.9)
* 姓名：王硕
* 学号：2015301020103
* 班级：物基二
### 1.摘要：
*  1.不同射击角度的轨迹
* 2.密度修正
* 3.射击范围最大的角度
### 2.题目    
Calculate the trajectory of your cannon shell including both air drag and the 
Reduced air density at high altitudes so that you can reproduce the results in 
Figure2.5.Perform your calculation for different firing angles and determine the 
Value of the angle that gives the maximum range
### 3.基本原理 
炮弹运动轨迹为抛物线
<div align=center>
<img src="http://latex.codecogs.com/gif.latex?x_{i+1}=x_{i}+v_{x,i}\Delta\,t">    

<img src="http://latex.codecogs.com/gif.latex?v_{x,i+1}=v_{x,i}-\frac{F_{X}}{M}\Delta\,t">    


<img src="http://latex.codecogs.com/gif.latex?Y_{i+1}=y_{i}+v_{Y,i}\Delta\,t">    

<img src="http://latex.codecogs.com/gif.latex?v_{y,i+1}=v_{y,i}-g\Delta\,t-\frac{F_{y}}{M}\Delta,t">   
</div>
F为炮弹运动中受到的空气阻力,与速度和空气密度有关
<img src="http://latex.codecogs.com/gif.latex?F=-B_{2}v^{2}\frac{\rho\,}{\rho\,_{0}}"> 
<img src="http://latex.codecogs.com/gif.latex?\rho\,=\rho\,_{0}(1-\frac{ay}{T_{0}})"> 
### 4.参数选择与图像绘制
* 参数选择：
* B2/M=4*10^(-5)/m    
* a=6.5*10^(-3) K/m   
* T0=293.16K
* 有无密度修正的轨迹：
* 不同射击角度的轨迹：
* 角度与射程的关系：
### 5.结果分析
* 空气阻力受空气密度的影响，在计算炮弹轨道时要加入密度修正
* 由于空气密度随海拔高度上升而降低，空气密度对空气阻力的影响也会降低
* 考虑空气阻力时，最大射击角度并不是45°

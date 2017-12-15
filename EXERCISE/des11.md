
## Exercise6.6
* 姓名 ：王硕
* 学号：2015301020103

#### 1.摘要    

模拟两列在弦上相遇的波，以此验证波的叠加原理。

#### 2.正文
* 波的叠加性原理： 
如果有两列以上的同类波在空间相遇，在共存的空间内，总的波是各个分波的矢量和（即相加时不仅考虑振幅，还考虑相位），而各个分波相互并不影响，分开后仍然保持各自的性质不变。叠加性的依据是，（线性）波的方程的几个解之和仍然是这个方程的解；这个原理称叠加原理。    
* 解决方法：
波动方程:    
<div align=center>
<img src="http://latex.codecogs.com/gif.latex?\frac{\partial\,y^2}{\partial\,t^2}=c^{2}\frac{\partial\,y^2}{\partial\,x^2}"> 
</div>    
研究弦上的波动问题，可将弦的运动写为：    
<div align=center>
<img src="http://latex.codecogs.com/gif.latex?\mu\,\Delta\,x\frac{\mathrm{d}^{2}y_{i}}{\mathrm{d}\,x^{2}}=Tsin\theta\,_{i+1}-Tsin\theta_{i}">
  </div>    
  利用近似：    
  <div align=center>
<img src="http://latex.codecogs.com/gif.latex?sin\theta_{i}\approx\frac{y_{i}-y_{i-1}}{\Delta\,x}">
  </div>    
  可得：    
  <div align=center>
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}^{2}\,y_{i}}{\mathrm{d}\,t^{2}}\approx\,(\frac{T}{\mu})\frac{y_{i+1}-2y_{i}+y_{i-1}}{(\Delta\,x)^{2}}">
  </div>    
  做数值计算时，将横坐标划分为若干个点，做数值计算。    
  <div align=center>
<img src="http://latex.codecogs.com/gif.latex?x=i\Delta\,x">
  </div><div align=center>
  <img src="http://latex.codecogs.com/gif.latex?t=n\Delta\,t">
   </div><div align=center>
  <img src="http://latex.codecogs.com/gif.latex?y\equiv\,y">
  </div>        
  y由此有如下关系式：    
  <div align=center>
<img src="http://latex.codecogs.com/gif.latex?\frac{y(i,n+1)+y(i,n-1)-2y(i,n)}{(\Delta\,t)^{2}}=c^{2}[\frac{y(i,n+1)+y(i,n-1)-2y(i,n)}{(\Delta\,x)^{2}}]">
  </div>    
  因为Delta t已知，且为定值，上式可化为：
<div align=center>
<img src="http://latex.codecogs.com/gif.latex?y(i,n+1)=2[1-r^2]y(i,n)-y(i,n-1)+r^2[y(i+1,n)+y(i-1,n)]"> 
  </div>    
  两端<div align=center>    
  <img src="http://latex.codecogs.com/gif.latex?(y(0,n)=0,y(M,n)=0)">
  </div>    
  "Gaussian pluck"    
  <div align=center>    
  <img src="http://latex.codecogs.com/gif.latex?y_{0}(x)=e^{-k(x-x_{0})}">
  </div>    
  
  #### 3.图像    
  

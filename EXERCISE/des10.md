## Exercise 5.1
* 姓名：王硕
* 学号：2015301020103

#### 1.摘要
运用Jacobi方法模拟给定边界条件下的电势和电场
#### 2.正文
<img src="http://latex.codecogs.com/gif.latex?V(i,j)=\frac{1}{4}[V(i+1,j,k)+V(i-1,j,k)+V(i,j+1,k)+V(i,j-1,k)]">    
<img src="http://latex.codecogs.com/gif.latex?E_{x}=-\frac{\partial\,V}{\partial\,x}">  
<img src="http://latex.codecogs.com/gif.latex?E_{x}(i,j)\approx\,-\frac{V(i+1,j)-V(i-1,j)}{2\Delta\,x}">    

#### 3.图像    


边界条件1    

V=(0,x=±1或y=±1    
   1,-0.3<=x<=0.3且-0.3<=y<=0.3    
   0,other)
![]()    
![]()
![]()    
边界条件2    
![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
![]()
![]()
![]()    
边界条件3
![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)    
![]()
![]()
![]()    
边界条件4
![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)



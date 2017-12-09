## Exercise 5.1
* 姓名：王硕
* 学号：2015301020103

#### 1.摘要
运用Jacobi方法模拟给定边界条件下的电势和电场
#### 2.正文
<img src="http://latex.codecogs.com/gif.latex?V(i,j)=\frac{1}{4}[V(i+1,j,k)+V(i-1,j,k)+V(i,j+1,k)+V(i,j-1,k)]">    
<img src="http://latex.codecogs.com/gif.latex?E_{x}=-\frac{\partial\,V}{\partial\,x}">  
<img src="http://latex.codecogs.com/gif.latex?E_{x}(i,j)\approx\,-\frac{V(i+1,j)-V(i-1,j)}{2\Delta\,x}">      
[代码](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/temp10.py)    


#### 3.图像    


边界条件1    
      
-0.3<=x<=0.3且-0.3<=y<=0.3,V=1                
其他, V=0     
   
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v11.png)    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v12.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v13.png)    

边界条件2     
     
-0.3<=x<=0.3且y=0.3,V=1        
-0.3<=x<=0.3且y=-0.3,V=-1       
其他，V=0    

![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v21.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v22.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v23.png)    

边界条件3    
x=0,y=0,V=-1    
其他，V=0     
   
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v31.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v32.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v33.png)    

边界条件4        
x=-0.3且y=0,V=1     
x=0.3且y=0,V=-1        
其他，V=0     
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v41.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v42.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/v43.png)
#### 致谢
参考了Chen yebo学长的代码，在此表示感谢



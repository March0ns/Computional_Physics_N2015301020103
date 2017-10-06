
## CHAPTER 1 *exercise 1.3
* 姓名：王硕  
* 学号： 2015301020103

### 一 内容提要：    

* 编程模拟跳伞时的速度    
* 使用Euler法求解速度的微分方程    

### 二 题目：
   It is often the case that the frictional force on an object will increase as the object moves faster. A fortunate example of this is a parachutist; the role of the parachute is to produce a frictional force due to air drag , which is larger than would normally be the case without the parachute. The physics of air drag will be discussed in more detail in the next chapter. Here we consider a very simple example in which thE frictional force depends on the velocity. Assume that the velocity of an object obeys an equation of the form where a and b are 	constants. You could think of a as coming from an applied force such as gravity, while arises from friction.   Note that the frictional force is negative（we assume that b > 0 ), so that it opposes the motion, and that it increases in magnitude as the velocity increases. Use the Euler method to solve the equation for v as a function of time.       
   
<img src="http://latex.codecogs.com/gif.latex?cht=tx&chl=\frac{\mathrm{d} v}{\mathrm{d} t}=a-bv">
    

### 三 使用Euler法推导公式：   

<img src="http://latex.codecogs.com/gif.latex? v(\Delta t)\ = v(0) + \frac{\mathrm{d} v}{\mathrm{d} t}\Delta t+\frac{1}{2}\frac{\mathrm{d} v^2}{\mathrm{d}^2 x}(\Delta t)^2+...">     
   
只保留一阶项：

<img src="http://latex.codecogs.com/gif.latex? v(\Delta t)\ \approx  v(0) + \frac{\mathrm{d} v}{\mathrm{d} t}\Delta t">
    
由导数定义：

<img src="http://latex.codecogs.com/gif.latex? \frac{\mathrm{d} v}{\mathrm{d} t}\equiv \lim_{\Delta t\rightarrow 0}\frac{v(t+\Delta t)-v(t)}{\Delta t}\approx \frac{v(t+\Delta t)-v(t)}{\Delta t}">  
   
整理得：

<img src="http://latex.codecogs.com/gif.latex? v(t+\Delta t)\approx v(t)+\frac{\mathrm{d} v}{\mathrm{d} t}\Delta t">



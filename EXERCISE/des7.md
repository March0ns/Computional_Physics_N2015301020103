## EXERCISE 3.26
* 姓名：王硕
* 学号：2015301020103
* 班级：物基二班    
#### 1. 背景：混沌图像---洛伦兹的蝴蝶
      Lorenz系统作为第一个混沌模型，是混沌学发展史上的一个重要的里程碑，具有举足轻重的地位。我看过很多本关于混沌方面的书,每一本都会有洛伦兹吸引子，并且几乎每一本的封面上都会画上洛伦兹的蝴蝶曲线。虽然我看了这么多书，却始终没明白，这洛伦兹的方程式怎么就跟天气发生了关系。气象学家洛伦兹在1963年论文中提出的它的公式以表示天气模型。天气系统如此复杂，用数百万个变量来描述都不为过，但洛仑兹将其压缩到了三个变量：x，y和z，所以这只是一个玩具模型。这个玩具模型对于他的论点来说，也许恰到好处。之前的天气模型大多是线性的，没有过多考虑各种因素之间的复杂关系，洛伦兹早认为这样的模型无法描述多变的天气。而他的模型，尽管只有三个随着时间变化的变量，但变量之间却有着非线性的联系，能够很好地诠释了因素之间的相互影响。        
    就在这样简单的Lorenz模型之下，出现了混沌现象。而且这种现象似乎是普遍的，因为在三个变量取值的大部分可能性下，系统演变的轨迹都会渐渐趋近于同一个产生混沌的区域，就像磁铁吸引着图钉，混沌的行为成为了必然。这就是人们发现的第一个混沌吸引子：洛伦兹吸引子。它的形状，就像一只蝴蝶；这大概也是洛伦兹将这种混沌的现象称为“蝴蝶效应”的原因。一只南美洲蝴蝶的扑翼，在蝴蝶效应的放大下，也许引起德克萨斯州的一场飓风。天气不可能准确预测，因为天气是混沌的，微小的扰动在长远看来是不可忽略的，而我们又无力去追踪无数的扰动，只能一边预计，一边修正。[*](http://www.cnblogs.com/WhyEngine/p/4308445.html)    
  
#### 2.正文
洛伦兹模型的方程：    
[代码](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/temp7.py)

<div align=center>     
<img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,x}{\mathrm{d}\,t}=\sigma\,(y-x)">        
</div>    
<div align=center>

 <img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,y}{\mathrm{d}\,t}=-xz+rx-y">         
 </div>    
 <div align=center>

 <img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\,z}{\mathrm{d}\,x}=xy-bz">         
</div>    

#### 3.图像：    

* 1.r不同时速度z随时间变化的图像：    
    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_20.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_25.png)    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_30.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_150.png)    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_160.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_a_170.png) 

* 2.速度z与温度x和密度y的图像    
    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_c_25.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_c_25x.png) 
     
* 3.当x=0时，z与y和y=0时，z与x的图像    
    
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_b_25x.png)
![](https://github.com/March0ns/Computional_Physics_N2015301020103/blob/master/EXERCISE/F_b_25y.png) 

#### 4.分析    
 1. 当r较小时，流体经过一个暂态过程后逐渐变得稳定。r增加到25时，开始出现混沌现象。    
 
 2. 当r 增加到160左右时，变得具有周期性，继续增加r，又开始出现混沌现象。

#### 5.致谢
（*）处引用了[叶飞鱼的博客](http://www.cnblogs.com/WhyEngine/p/4308445.html)     

参考了夏海峰学长的代码，在此表示感谢。

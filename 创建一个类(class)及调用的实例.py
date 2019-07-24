#ex20.py 创建一个类(class)及调用的实例 

class CUBE(): #创建一个名为CUBE的类
    def __init__(self,l,w,h=1):#magic method,括弧内最后一个是可选参量，第一个是创建类时必须的参量
        self.len=l #类内定义好要用到的变量，
        self.width=w
        self.high=h 
#        self.color=0#python是动态变量，所以这里可以赋予0
#        self.merterial=0
#        self.oth=0

    def cuboid(self): #计算方体体积的metod，跟函数功能相似，但在类内就叫方法(method)，注意调用时也与函数不同。 
        return self.len*self.width*self.high #返回数字，注意用的都是内部定义的变量
			
    def cylinder(self):#计算圆柱体体积的mehod，
        import math   #因为后面要使用pi值，所以需先导入math模块
        return (math.pi*(self.width*self.width/4))*self.high
			
    def other(self,c,m):#另需参量的一个mehod，
        self.color=c #在本mehod用到的参量可在这指定
        self.merterial=m
#        self.oth=0
        self.oth=self.color+self.merterial  #注意，这里是赋值，下面是返回，注意二者的区别，
        return self.color+' '+self.merterial
			
ob=CUBE(3,4)#首先将类赋予一个对象，且必须给出参数值，不能空
ob.len=3.5    #可以在赋予对象后重新赋值
print(ob.len,ob.width,ob.high,ob.cuboid())#注意调用不同形式的方法时与下面的区别

ob.other('yellow','iron')#可以重新赋值
print(ob.color,ob.merterial,ob.oth,ob.other('red','copper'))#调用另需参数的方法时必须要给出参量值


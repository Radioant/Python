class Orange():
    def __init__(self,w,c):
        self.weight=w
        self.color=c



    def rot(self,days,temp):
        self.days=days
        self.temp=temp
        return days*temp


orange=Orange(2,'red')
orange.rot(4,12)
print(orange.weight,orange.color,orange.days,orange.temp,orange.rot(5,12))
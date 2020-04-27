class Robot:
    def __init__(self,Name,color,weight):
        self.Name=Name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print("My name is "+ self.Name)
r1=Robot("Tom","Blue",30)
r2=Robot("Jerry","Red",40)
'''r1.introduce_self()
r2.introduce_self()'''

class Person:
    def __init__(self,n,p,i):
        self.name=n
        self.personality=p
        self.isSitting=i
    def sitDown(self):
        self.isSitting=True
    def standUp(self):
        self.isSitting=False
p1=Person("Alice","Vile",False)
p2=Person("Jenny","Aggressive",True)
p1.robot_owened=r2
p2.robot_owened=r1
p1.robot_owened.introduce_self()
p2.robot_owened.introduce_self()

class person:
    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a
    
    def talk(self):
        print("hi ! my name is ",self.name)
        print("gender: ",self.age)
    
    def vote(self):
        if self.age> 18 :
            print("i am eligible to vote")
        else:
            print("i am not eligible to vote")

ob1=person("sam","male",36)
ob2=person("sushant","male",20)

ob1.talk()
ob1.vote()
ob2.talk()
ob2.vote()
print(ob1.__dict__)
print(ob2.__dict__)


        
        





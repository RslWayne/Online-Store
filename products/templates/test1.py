class Human: # name,age
 def __init__(self,name,age):
    self.name = name
    self.age = age


 def description(self):
    print(f"{self.name} {self.age}")

 def__

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.education = True
        self.__wallet = 0

    def description(self):
        print(f"{self.name} {self.age}")

# class Female(Human):
#    def __init__(self,name,age):
#        super().__init__(name, age)



male1 = Male('Erzhan',22)
male1.description()
# male2 = Female('Dariya',20)
print(male1)

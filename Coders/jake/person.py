class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def iAm(self):
        print("hello, my name is {}".format(self.name))
        if (self.age < 18 and self.gender == "male"):
            print("i am a boy")
        elif (self.age >= 18 and self.gender =="male") :
            print("i am a man")
        elif (self.age < 18 and self.gender =="female"):
            print(" i am a girl")
        else:
            print(" i am a lady")
            
        
    def my_age(self):
        print("i am {} years old".format(self.age))
        
    def my_gender(self):
        print("i am {}".format(self.gender))
        
    
     
    

    
        

me = Person("jake jones",9, "male")

print(me.iAm())
print(me.my_age())
print(me.my_gender())

me = Person("jack",21, "male")

print(me.iAm())
print(me.my_age())
print(me.my_gender())

me = Person("jane smith",19, "female")
print(me.iAm())
print(me.my_age())
print(me.my_gender())

me = Person("jane davies",5, "female")
print(me.iAm())
print(me.my_age())
print(me.my_gender())
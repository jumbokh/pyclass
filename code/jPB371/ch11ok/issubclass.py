class Parents:        
    def hello(self):
        print("I am in Parents")
 
class Child(Parents):
    def hello(self):
        print("I am in Child")

print(issubclass(Child, object))
print(issubclass(Child, Parents))

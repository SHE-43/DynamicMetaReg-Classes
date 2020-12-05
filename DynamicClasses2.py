class Parent:
    def childMethod(self):
        print("This is a child method xx1")



def child__init(self, age, grade):
    self.age = age
    self.grade = grade


# How to add property decorators?
# Need to perfect this.    


Child = type("Child", (Parent,), {"name":"Child Class", "__init__":child__init})


obj = Child(43, "A")
obj.childMethod()
print(obj.age, obj.grade)





print("\n\n\nHow init and new work.")

class checkOrder:
    def __init__(self,a):
        self.a = a
        print("init")
    
    def __new__(self, className, bases, attrs):
        return type(className, bases, attrs)

obj2 = checkOrder(2)



# A bit about decorators.
# Let's make a property one.

def dec(func):
    def wrapper(*args, **kwargs) -> "args are passed in as (1,2), kwargs are passed in as c = 3, d = 4 (dictionary)" : 
        print("Beginning")
        func(*args, **kwargs) # the same args are opened up from (1,2) to 1 and 2. kwargs are passed in as c, d == 3, 4
        # try yielding as well.
        print("Ending")
    return wrapper

print("\n\nUsing decorators.\n")


@dec
def myFunction(a,b, c, d):
    print(a*b*b*a)
    
    # try with return and yield as well.

t = (3,8)
d = {'c': 3, 'd':7}
myFunction(*t, **d)



# If you make a class that creates child classes dynamically, then you are done with this.
p = lambda x : print(x)

# When an obj.anything() is done, the object passes itself as the first instance.


# Normal Method with some cool features.


############
class Test1:
    @classmethod
    def method1(cls):
        print("Hey there.")

    # Yet another way. using ->
    def conjugator(self) -> complex:
        print("Get Nothing.")

    # A way to add better documentation - from the Fathers of Python.
    def helperMethod(self, n  : "Just n", h: "just h") -> "Nothing":
        print(n)
############

p(type(Test1()))
obj = Test1()
Test1.method1()
obj.method1() # because the object is that class's object - they are of the "same class"
print(obj.conjugator())
print(obj.helperMethod("Print THIS", "2"))


# Dynamic Method


############
Test2 = type("Test2", (), {}) 
# type(NameOfClassCreated, ParentClass(es), Attributes)
############
p(type(Test2()))



p("\n\n\nReal Example")


# Defining our init method.

def user_init(self, userName, userAge, userSubjects):
    self.userName = userName
    self.userAge = userAge
    self.userSubjects = userSubjects



# Real example coming up.
# Property methods can be used to change the methods.
# theVariable name is the class name
User = type("User", (), {"total":0, 
                        "name" : "User Class", 
                        "method1" : lambda: print("Hello"), 
                        "__init__" : user_init, # because methods can be assigned as objects.
                        "sayHi" : lambda self: f"Hi, I a {self.userName} and I am {self.userAge} with subjects {self.userSubjects}."
                        }
                        )


object_for_User = User("Rob Foreman", "Underage", ["Math", "English", "Physics"])
print(object_for_User.sayHi())
p(object_for_User.__dict__)

# Adding class methods, static methods, and instance methods.
print("\nAdding methods manually.")
print(User.sayHi(object_for_User))


# Add a new class method to your dynamic class.
def extend_my_class(cls):
    return lambda f : (setattr(cls, f.__name__, f) or f)

p(help(setattr))

@extend_my_class(User)
def regular_class_method():
    print("Regular class method")

User.regular_class_method()

# Differences between the types, once again.

class A:
    
    def normal(self):
        print("normal")
    
    @classmethod
    def classMethod(cls):
        print("classMethod")
    
    @staticmethod
    def staticMethod():
        print("staticMethod")


obj_A = A()
A.classMethod()
obj_A.classMethod()
A.staticMethod()
obj_A.staticMethod()
obj_A.normal()

def nothing():
    pass

print(nothing.__name__)





p("\n\nInspect Only")

import inspect

print(inspect.getmembers(User, lambda a: not(inspect.isroutine(a))))
globals()["FandF"] = "FandF9000"
print(FandF)






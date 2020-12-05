
print("Class 1")
# this returns the class and that class's object
def classCreator():
    class Class1:
        total = 0
        def __init__(self):
            total += 1
        # This creates a child class dedicated to that object.
        def classMaker(self):
            dictOfAttrs = self.__dict__ # this has all the attributes.
    # Use glovals() to create it.


    return Class1, Class1()



call_for_Class1 = classCreator()[0]
obj_for_Class1 = classCreator()[1]
print(call_for_Class1)
print(obj_for_Class1)
obj_for_Class1.name = "My Name"
obj_for_Class1.age = "There you go"
print(obj_for_Class1.__class__.__name__)
print(obj_for_Class1.__dict__)

class Class1_Child(obj_for_Class1.__class__):
    pass
    # def

print("\n\nClass 2")

class Class2:
    pass

obj_for_Class2 = Class2()
print(Class2)
print(obj_for_Class2)

# Class defines rules, attibutes, parameters, method, things that are allowed, operations that can be performed.
# A metaclass automatically creates a new user class


# Inspect.
class JustForInspection:
    a = "User"
    b = 3433
    c = [x for x in range(1,3+1)]

    def method():
        pass

import inspect

attributes = (inspect.getmembers(JustForInspection, lambda a: not(inspect.isroutine(a))))
for x in attributes:
    if x[0].startswith("__") and x[0].endswith("__"):
        pass
    else:
        print(x)





# Continue revised.
for x in range(4):
    if x == 2:
        continue
    print(x)

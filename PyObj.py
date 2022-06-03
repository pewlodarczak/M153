class Person():

    arr = [1,2,3]
    def __init__(myStupidObject, name, salary):
        myStupidObject.name, myStupidObject.salary = name, salary

    def __repr__(myStupidObject):
        return myStupidObject.name


perObj1 = Person('Jo', 70000)
print(perObj1.name)
print(perObj1.salary)
print(perObj1.arr)
print(perObj1)

perObj2 = Person('Jane', 70000)
print(perObj2.name)
print(perObj2.salary)

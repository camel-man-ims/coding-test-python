# 22.07.07

# https://www.geeksforgeeks.org/difference-between-__eq__-vs-is-vs-in-python/
# https://stackoverflow.com/questions/10254594/what-makes-a-user-defined-class-unhashable

# id 함수 -> hash 처럼 unique 한 값을 반환
# https://www.w3schools.com/python/ref_func_id.asp

class Car:
    def __init__(self,color,height):
        self.color = color
        self.height = height

    def __eq__(self,other):
        if isinstance(other, Car):
            if self.color == other.color and self.height == other.height:
                return True
        return False

    def __hash__(self):
        return id(self.color)

    def __str__(self):
        return self.color + " " + str(self.height)

car1 = Car("red",180)
car2 = Car("red",180)

print(car1 == car2)

hashSet = set()

hashSet.add(car1)
hashSet.add(car2)

for s in hashSet:
    print(s)
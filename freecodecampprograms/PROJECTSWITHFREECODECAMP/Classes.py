#Create a class of persons and obtaine objects of it
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
Bruno=Person("Bruno",23)
print(Bruno.name)
print(Bruno.age)    
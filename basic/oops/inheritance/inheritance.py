class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname, self.age)

#Use the Person class to create an object, and then execute the printname method:


x = Person("Ajit", "Kumar", 36)
x.printname()
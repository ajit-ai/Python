class employee:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, DOB: {self.dob}")
        
    # get the employye name and age
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_dob(self):
        return self.dob


if __name__ == "__main__":
    emp1 = employee("Ajit", 50, "1971-11-14")
    emp1.display()
    
    emp2 = employee("Vidhi", 11, "2013-03-19")
    emp2.display()
    
    print(f"Employee 1 Name: {emp1.get_name()}, Age: {emp1.get_age()}")
    print(f"Employee 2 Name: {emp2.get_name()}, Age: {emp2.get_age()}")
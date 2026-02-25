class Student:

    score = 0
    
    def __init__(self, name_, age_, height_, gender_):
        self.name = name_
        self.age = age_
        self.height = height_
        self.gender = gender_
    

    def learn(self, test):
        self.score+= test

    def __str__(self):
        return (f"Hello my name is: {self.name}, {self.age}, {self.height}, {self.gender}, {self.score}")



lajos = Student("Lajos", 13, 178, "fiu")
anna = Student("Anna", 15, 170, "lany")
print(lajos.height)

print(lajos.height)
print(lajos.name)
print(lajos.score)
print(lajos.learn(10))
print(lajos)
print(anna.score)
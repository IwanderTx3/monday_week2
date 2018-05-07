
class Person:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.other_person = ''
        self.friends = []
        self.count_friends = 0
        self.greet_count = 0
        self.unique_greet = []
        self.num_unique = len(self.unique_greet)
                
    def greet(self,other_person):
        self.other_person = other_person
        self.greet_count += 1
        print(f"Hello {self.other_person}, I am {self.name}")
        #print(self.greet_count)
        self.check_greet(other_person)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self,friend):
        self.friends.append(friend)
        self.num_friends()

    def num_friends(self):
        self.count_friends = len(sonny.friends)

    def __repr__(self):
        return f"{self.name},{self.email},{self.phone}"

    def check_greet(self,other_person):
        if other_person not in self.unique_greet:
            self.unique_greet.append(other_person)
            self.num_unique = len(self.unique_greet)

                  
    def num_unique_greet(self):
        print(f"{self.name} has greeted {self.num_unique} people.")







sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

sonny.greet(jordan.name)
jordan.greet(sonny.name)

print(f"{sonny.name}'s email adreess is {sonny.email} and thier phone number is {sonny.phone}")
print(f"{jordan.name}'s email adreess is {jordan.email} and thier phone number is {jordan.phone}")

sonny.print_contact_info()

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.year} {self.make} {self.model} " )
    

car = Vehicle('Nissan','Leaf','2015')


print(sonny.friends)
print("No one")
sonny.friends.append(jordan.name)
sonny.num_friends()
print(sonny.friends)
print(f"{sonny.name}, has {sonny.count_friends} friend")

sonny.add_friend(input("Who do you want to add as a friend? "))
print(f"{sonny.name}, has {sonny.count_friends} friends. {sonny.friends[0]} and  {sonny.friends[1]}")

print(sonny)  

sonny.greet('jordan')
sonny.num_unique_greet()
sonny.greet('Kim')
sonny.num_unique_greet()
sonny.greet('Kim')
sonny.num_unique_greet()
sonny.greet('Bill')
sonny.num_unique_greet()

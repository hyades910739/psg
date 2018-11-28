# class Person:
#     def __init__(self, name, job=None, pay=0):
#         self.name = name
#         self.job = job
#         self.pay = pay

# bob = Person('Bob Smith')
# sue = Person('Sue Jones', job = 'dev', pay=100000)
# print(bob.name, bob.pay)
# print(sue.name, sue.pay)

# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job = 'dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)






from lesson3_classtools import AttrDisplay
    
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)
        
        
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)

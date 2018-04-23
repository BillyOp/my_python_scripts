from collections import namedtuple

Car = namedtuple('Car', 'mileage color model capacity')

cayene = Car('1234.22','green','porsche','4000')
print(cayene.mileage)
print(cayene.color)
print(cayene.model)
print(cayene.capacity)

# Namedtuple like all tuples are immutable i.e. cannot be changed
cayene.color = 'blue'
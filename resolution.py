from pyprover import *
from utils import to_cnf

if __name__ == '__main__':
    KB = ['∃x Dog(x) & Owns(J, x)',
        '∀x [∃y Dog(y) & Owns(x, y)]>AnimalLover(x)',
        '∀x AnimalLover(x)>∀y Animal(y)>~Kills(x, y)',
        'Kills(J, T)|Kills(C, T)',
        'Cat(T)',
        '∀x Cat(x)>Animal(x)']

    for i in to_cnf(KB):
        print(i)


# OUTPUT:
# xDog(a)&Owns(J,a)
# ~Dog(b)|Owns(b,b)|AnimalLover(b)
# ~AnimalLover(c)|~Animal(c)|~Kills(c,c)
# ~AnimalLover(c)|~Animal(c)|~Kills(c,c)
# Cat(T)
# ~Cat(f)|Animal(f)
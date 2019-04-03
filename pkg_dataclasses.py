from dataclasses import dataclass, field
from inspect import signature

def get_kind():
    return 'Dog'


@dataclass
class Animal:
    '''__init__, __repr__, __eq__ are auto-generated'''
    legs: int  # no default value
    name: str = field(default='Nameless Animal') # default value
    kind: str = field(default_factory=get_kind()) # zero parameter function

    # kind: first default_factory function is applied, then __post_init__
    def __post_init__(self):
        self.kind = self.kind.upper()


@dataclass(frozen=True)
class FrozenAnimal:
    legs: int
    name: str
    kind: str



dog = Animal(name = 'Jackfruit', kind= 'Dog', legs = 4)
dog2 = Animal(4, 'Jackfruit', 'Dog')


print(dog)
print(signature(dog.__init__))
print(dog == dog2)


dogFrozen = FrozenAnimal(legs=3, name='Walter', kind='Dog')
dogFrozen2 = FrozenAnimal(legs=4, name='White', kind='Dog')

# instances of frozen dataclasses are hashable,
# can be keys in dicts or values in tuples
dogs_dict = {dogFrozen: 1, dogFrozen2: 3}
dogs_tuple = {dogFrozen, dogFrozen2}

print(dogs_dict)
print(dogs_tuple)
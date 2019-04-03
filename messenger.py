''' Messenger/ Data Transfer Object
Useful to return data accessible via dot notation
'''

class Messenger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


m = Messenger(info="Some Information", a_list=['a', 'list'])

m.more = 11

print(m.info)
print(m.a_list)
print(m.more)

def bla():
    return m


print("------")

print(bla().more)



from numpy import byte


class person():
    def __init__(self):
        self.fname = 'Victor'
        self.lname = 'Martinez'
        self.age = 40

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self) -> str:
        return f'<Person Class - {self.fname}, {self.lname}, {self.age}'
    
    # TODO: called when str(object), print(object)
    def __str__(self) -> str:
        return f' {self.fname} {self.lname} is {self.age} years old'

    # TODO: use __repr__ to create a string useful for debugging
    def __bytes__(self) -> bytes:
        val = f'Person:{self.fname}:{self.lname}:{self.age}'
        return bytes(val.encode('utf-8'))

def main():
    cls1 = person()

    # use different python functinos to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print(cls1)
    print(bytes(cls1))

if __name__ == '__main__':
    main()
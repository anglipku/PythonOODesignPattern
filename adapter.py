# The adapter pattern provides a different interface for a class. It is useful to integrate
# classes that couldn't be integrated due to their incompatible interfaces.

class Dog(object):
    def __init__(self):
        self.name = 'dog'

    def bark(self):
        return "woof!"

class Cat(object):
    def __init__(self):
        self.name = 'cat'

    def meow(self):
        return "meow!"

class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "hello"

class Car(object):
    def __init__(self):
        self.name = 'Car'

    def make_noise(self, decibel):
        return "vroom{0}".format("!" * decibel)


class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        '''we set the adapted methods in the object's dict'''
        self.obj = obj # composition
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        '''all non-adapted calls are passed to the object'''
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == '__main__':
    objects = []

    dog   = Dog()
    cat   = Cat()
    human = Human()
    car   = Car()

    objects.append(Adapter(dog,   make_noise = dog.bark))
    objects.append(Adapter(cat,   make_noise = cat.meow))
    objects.append(Adapter(human, make_noise = human.speak))
    objects.append(Adapter(car,   make_noise = lambda : car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))

### Output ###
'''
A dog goes woof!
A cat goes meow!
A Human goes hello
A Car goes vroom!!!
'''

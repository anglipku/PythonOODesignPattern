# Create new object instances by cloning prototype

class Prototype(object):
    value = 'proto'

    def clone(self, **attrs):
        '''clone a prototype and update inner attributes dictionary'''
        obj = self.__class__()      # clone!
        obj.__dict__.update(attrs)  # clone!
        return obj

class PrototypeDispatcher(object):

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


if __name__ == '__main__':
    dispatcher = PrototypeDispatcher()
    prototype  = Prototype()

    # a, b, c are the clones of prototype (b, c are mutated)
    a = prototype.clone()
    b = prototype.clone(value = 'b-value', category = 'b')
    c = prototype.clone(value = 'c-value', is_checked = True)

    dispatcher.register_object('objectB', b)
    dispatcher.register_object('objectC', c)
    dispatcher.register_object('proto', a)

    print([{n: p.value} for n, p in dispatcher.get_objects().items()])

### Output ###
'''
[{'objectB': 'b-value'}, {'objectC': 'c-value'}, {'proto': 'proto'}]
'''
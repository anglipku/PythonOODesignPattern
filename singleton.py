# In Singleton pattern, we can have only one instance of a class, or multiple instances that share the same state.
# Useful for multithreading (to keep a uniform setting)

# In Python, instance attributes are stored in an attribute dictionary __dict__. Usually, each
# instance has its own dictionary, but in singleton pattern, it is modified so that all instances
# have the same dictionary

class Borg(object):
    '''Class attribute works like class method
    only ClassName.ClassAttribute = XXX can change it.
    All instances share the same value'''
    _shared = {} # name of this variable doesn't matter here

    def __init__(self):
        '''all further revisions on attributes are shared'''
        self.__dict__ = self._shared
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg(Borg):
    '''A Null Statement.  It does nothing, but is needed.'''
    pass

if __name__ == "__main__":
    obj_1 = Borg()
    obj_2 = Borg()

    obj_1.state = 'Idle'
    obj_2.state = 'Busy'

    print ('obj_1: {0}'.format(obj_1))
    print ('obj_2: {0}'.format(obj_2))

    obj_2.state = 'Super Busy'

    print ('obj_1: {0}'.format(obj_1))
    print ('obj_2: {0}'.format(obj_2))

    obj_3 = YourBorg()

    print ('obj_1: {0}'.format(obj_1))
    print ('obj_2: {0}'.format(obj_2))
    print ('obj_3: {0}'.format(obj_3))


### Output ###
'''
obj_1: Busy
obj_2: Busy
obj_1: Super Busy
obj_2: Super Busy
obj_1: Init
obj_2: Init
obj_3: Init
'''
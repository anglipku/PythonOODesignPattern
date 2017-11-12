# Builder decouples the creation of a complex object and its representation, so that the same
# process can be reused to build objects from the same family.

# This is useful when we need to separate the specification of an object from its actual representation
# (for abstraction purpose)

# In this example, Director "hires" a builder, who "configures" and "creates" a building

# Director
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building

# Abstract Builder
class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

# Concrete Builders
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'

class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'

# Building
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        '''S.t. we can use print buildingObject to see what it has'''
        return 'Floor: {0.floor}| Size: {0.size}'.format(self)


if __name__ == '__main__':
    # Let's hire a BuilderHouse, and build a house
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print building

    # Let's hire a BuilderFlat, and build a flat
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print building


### Output ###
'''
Floor: One| Size: Big
Floor: More than One| Size: Small
'''
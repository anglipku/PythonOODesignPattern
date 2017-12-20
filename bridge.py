# Decouples an abstraction from its implementation

# Implementor 1
class DrawingAPI_1(object):
    def draw_circle(self, x, y, radius):
        print('API_1.circle at {0}:{1} radius {2}'.format(x, y, radius))

# Implementor 2
class DrawingAPI_2(object):
    def draw_circle(self, x, y, radius):
        print('API_2.circle at {0}:{1} radius {2}'.format(x, y, radius))

# Abstraction
class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        self._radius *= pct


if __name__ == '__main__':
    shapes = (
        CircleShape(1, 1, 1, DrawingAPI_1()),
        CircleShape(5, 6, 10, DrawingAPI_2())
    )

    for shape in shapes:
        shape.scale(2)
        shape.draw()

# Output
'''
API_1.circle at 1:1 radius 2
API_2.circle at 5:6 radius 20
'''
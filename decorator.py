# Adds behavior to object without affecting its class
class TextTag(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

class BoldWrapper(TextTag):
    '''Wraps a tag in <b>'''
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())

class ItalicWrapper(TextTag):
    '''Wraps a tag in <i>'''
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello  = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    print("before decorating:", simple_hello.render())
    print("after decorating:", special_hello.render())

# Output
'''
('before decorating:', 'hello, world!')
('after decorating:', '<i><b>hello, world!</b></i>')
'''
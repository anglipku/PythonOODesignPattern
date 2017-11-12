# The Factory pattern is used to create an interface for a method, leaving the implementation
# to the class that gets instantiated.

# In the example below, get_localizer() determines which the object to create, based on input

class ChineseGetter(object):
    '''A simple localizer gettext'''
    def __init__(self):
        self.trans = {'dog': 'gou', 'cat': 'mao'}

    def get(self, msg):
        return self.trans.get(msg, msg)

class EnglishGetter(object):
    def get(self, msg):
        return msg

def get_localizer(language):
    '''The factory method: depending on the input,
    factory decides which class object to create
    '''
    languages = {'English': EnglishGetter, 'Chinese': ChineseGetter}
    return languages[language]()


if __name__ == '__main__':
    # Create localizers
    e = get_localizer(language = 'English')
    c = get_localizer(language = 'Chinese')

    for msg in "dog tiger cat dumplings".split():
        print e.get(msg), c.get(msg)
        print '\n'

### Output ###
'''
dog gou
tiger tiger
cat mao
dumplings dumplings
'''
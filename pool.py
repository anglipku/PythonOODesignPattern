# The pattern is used when creating an object is costly, but only a few are used at a time.
# With a Pool, we can manage those instances we have by caching them. Now it's possible to skip
# the costly creation of an object if one is available in the pool.

# A pool allows to 'check out' an inactive object and then to return it. If none are available the pool
# creates one to provide without wait.

# "It returns things every times it uses"

class ObjectPool(object):
    def __init__(self, queue, auto_get = False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

def main():
    try:
        import queue
    except ImportError: # python 2.x compatibility
        import Queue as queue

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print('Inside func: {}'.format(pool.item))

    sample_queue = queue.Queue()
    sample_queue.put('Ang')

    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('Li')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

### Output ###
'''
Inside with: Ang
Outside with: Ang
Inside func: Li
Outside func: Li
'''
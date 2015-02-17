class Composite:

    def getValue(self):
        return self._value
    def setValue(self, value):
        self._value = value
    def delValue(self):
        del self._value
    value = property(getValue, setValue, delValue)

    def __init__(self, position, size, resolution, value=None):
        self._position = position
        self._size = size
        self._resolution = resolution

        self._value = value

        self._composites = [None] * self._resolution[0] * self._resolution[1] * self._resolution[2]

    def _map(self, n, a, b):
        try:
            return b[0] + ((n - a[0]) / (a[1] - a[0])) * (b[1] - b[0])
        except ZeroDivisionError:
            return b[0]

    def add(self, composite):
        i, j, k = self.index(composite)
        self[i, j, k] = composite

    def remove(self, composite):
        i, j, k = self.index(composite)
        del self[i, j, k]

    def index(self, composite):
        if composite._position > self._size:
            raise Exception

        i = int(self._map(composite._position[0], [0, self._size[0]], [0, self._resolution[0]]))
        j = int(self._map(composite._position[1], [0, self._size[1]], [0, self._resolution[1]]))
        k = int(self._map(composite._position[2], [0, self._size[2]], [0, self._resolution[2]]))

        return i, j, k

    def __len__(self):
        return self._composites.__len__()

    def __length_hint__(self):
        return self._composites.__length_hint__()

    def __getitem__(self, key):
        key = key[0] + (key[1] * self._resolution[1]) + (key[2] * self._resolution[1] * self._resolution[2])
        return self._composites.__getitem__(key)

    def __setitem__(self, key, value):
        key = key[0] + (key[1] * self._resolution[1]) + (key[2] * self._resolution[1] * self._resolution[2])
        self._composites.__setitem__(key, value)
        return None

    def __delitem__(self, key):
        key = key[0] + (key[1] * self._resolution[1]) + (key[2] * self._resolution[1] * self._resolution[2])
        self._composites.__delitem__(key)
        return None

    def __iter__(self):
        return self._composites.__iter__()

    def __reversed__(self):
        return self._composites.__reversed__()

    def __contains__(self, value):
        return self._composites.__contains__(value)



if __name__ == "__main__":

    container = Composite((0,0,0), (10,10,10), (20,20,20))
    container.add(Composite((5,5,5), (10,10,10), (10,10,10), 9))

    print(container[0,0,0]._position)

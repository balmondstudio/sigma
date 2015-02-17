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

        # XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
        self._composites = [[]] * self._resolution[0] * self._resolution[1] * self._resolution[2]
        # XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX

    def map(self, n, a, b):
        try:
            return b[0] + ((n - a[0]) / (a[1] - a[0])) * (b[1] - b[0])
        except ZeroDivisionError:
            return b[0]

    def append(self, composite):
        i, j, k = self.index(composite)
        self[i, j, k].append(composite)

    def remove(self, composite):
        i, j, k = self.index(composite)
        self[i, j, k].remove(composite)

    def index(self, composite):
        if composite._position > self._size:
            raise Exception

        i = int(self.map(composite._position[0], [0, self._size[0]], [0, self._resolution[0]]))
        j = int(self.map(composite._position[1], [0, self._size[1]], [0, self._resolution[1]]))
        k = int(self.map(composite._position[2], [0, self._size[2]], [0, self._resolution[2]]))
        l = self[i][j][k].index(composite)

        return i, j, k, l

    # TODO
    def __len__(self):
        return self._composites.__len__()

    # TODO
    def __length_hint__(self):
        return self._composites.__length_hint__()

    def __getitem__(self, key):
        return self._composites[key[0]][key[1]][key[2]][key[3]]

    def __setitem__(self, key, value):
        self._composites[key[0]][key[1]][key[2]][key[3]] = value
        return None

    def __delitem__(self, key):
        del self._composites[key[0]][key[1]][key[2]][key[3]]
        return None

    # TODO
    def __iter__(self):
        return self._composites.__iter__()

    # TODO
    def __reversed__(self):
        return self._composites.__reversed__()

    # TODO
    def __contains__(self, value):
        return self._composites.__contains__(value)



if __name__ == "__main__":

    container = Composite(
            position=(0,0,0),
            size=(20,20,20),
            resolution=(10,10,10)
            )

    composite = Composite(
            position=(5,5,5),
            size=(10,10,10),
            resolution=(10,10,10),
            value=9
            )

    container.add(composite)

    print(container.index(composite))

import sigma.data_transfer_object
import sigma.operator

class Component(sigma.data_transfer_object.IDataTransferObject):
    pass


class Primitive(Component):

    @property
    def relative_key(self):
        return self._relative_key

    @relative_key.setter
    def relative_key(self, value):
        self._relative_key = value

    @property
    def absolute_key(self):
        return self._absolute_key

    @absolute_key.setter
    def absolute_key(self, value):
        self._absolute_key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __init__(self, relative_key, absolute_key, value):
        self._relative_key = relative_key
        self._absolute_key = absolute_key
        self._value = value


class Composite(Component, sigma.operator.IRepresentable,
        sigma.operator.IComparable, sigma.operator.IBitwise,
        sigma.operator.IContainer, sigma.operator.ISequence):

    @property
    def primitives(self):
        return self._primitives

    @primitives.setter
    def primitives(self, value):
        self.components = value

    def __init__(self, primitives):
        self._primitives = primitives

    def __repr__(self):
        return "Composite({0})".format(self._primitives)

    def __str__(self):
        return "{0}".format(self._primitives)

    def __bytes__(self):
        return bytes(self._primitives)

    def __format__(self, format_spec=""):
        return "{0}".format(self._primitives)

    def __lt__(self, other):
        return self._primitives.__lt__(other._primitives)

    def __le__(self, other):
        return self._primitives.__le__(other._primitives)

    def __eq__(self, other):
        return self._primitives.__eq__(other._primitives)

    def __ne__(self, other):
        return self._primitives.__ne__(other._primitives)

    def __gt__(self, other):
        return self._primitives.__gt__(other._primitives)

    def __ge__(self, other):
        return self._primitives.__ge__(other._primitives)

    def __bool__(self):
        return  self._primitives.__bool__()

    def __len__(self):
        return self._primitives.__len__()

    def __length_hint__(self):
        return self._primitives.__length_hint__()

    def __getitem__(self, key):
        return self._primitives.__getitem__(key)

    def __setitem__(self, key, value):
        self._primitives.__setiterm__(key, value)
        return None

    def __delitem__(self, key):
        self._primitives.__delitem__(key)
        return None

    def __iter__(self):
        return self._primitives.__iter__()

    def __reversed__(self):
        return self._primitives.__reversed__()

    def __contains__(self, value):
        return self._primitives.__contains__(value)

    def append(self, value):
        self._primitives.append(value)
        return None

    def extend(self, other):
        self._primitives.extend(other._primitives)
        return None

    def insert(self, key, value):
        self._primitives.insert(key, value)
        return None

    def remove(self, value):
        self._primitives.remove(value)
        return None

    def pop(self, key):
        return self._primitives.pop(key)

    def clear(self):
        self._primitives.clear()
        return None

    def index(self, value):
        return self._primitives.index(value)

    def count(self, value):
        return self._primitives.count(value)

    def sort(self):
        self._primitives.sort()
        return None

    def reverse(self):
        self._primitives.reverse()
        return None

    def copy(self):
        return self._primitives.copy()

    def __add__(self, other):
        return self._primitives.__add__(other._primitives)

    def __radd__(self, other):
        return self._primitives.__radd__(other._primitives)

    def __iadd__(self, other):
        return self._primitives.__iadd__(other._primitives)

    def __mul__(self, other):
        return self._primitives.__mull__(other._primitives)

    def __rmul__(self, other):
        return self._primitives.__rmul__(other._primitives)

    def __imul__(self, other):
        return self._primitives.__imul__(other._primitives)

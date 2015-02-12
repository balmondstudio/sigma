class Composite(sigma.interface.IRepresentable, sigma.interface.IComparable,
		  sigma.interface.IContainer, sigma.interface.ISequence):

    @property
    def composites(self):
        return self._composites

    @composites.setter
    def composites(self, value):
        self._composites = value

    def __init__(self, composites=None):
        self._composites = [] if composite is None else composites

    def __repr__(self):
        return "Composite({0})".format(self._composites)

    def __str__(self):
        return "{0}".format(self._composites)

    def __bytes__(self):
        return bytes("{0}".format(self._composites), "utf-8")

    def __format__(self, format_spec=""):
        return "{0}".format(self._composites)

    def __lt__(self, other):
        return self._composites.__lt__(other._composites)

    def __le__(self, other):
        return self._composites.__le__(other._composites)

    def __eq__(self, other):
        return self._composites.__eq__(other._composites)

    def __ne__(self, other):
        return self._composites.__ne__(other._composites)

    def __gt__(self, other):
        return self._composites.__gt__(other._composites)

    def __ge__(self, other):
        return self._composites.__ge__(other._composites)

    def __bool__(self):
        return  self._composites.__bool__()

    def __len__(self):
        return self._composites.__len__()

    def __length_hint__(self):
        return self._composites.__length_hint__()

    def __getitem__(self, key):
        return self._composites.__getitem__(key)

    def __setitem__(self, key, value):
        self._composites.__setiterm__(key, value)
        return None

    def __delitem__(self, key):
        self._composites.__delitem__(key)
        return None

    def __iter__(self):
        return self._composites.__iter__()

    def __reversed__(self):
        return self._composites.__reversed__()

    def __contains__(self, value):
        return self._composites.__contains__(value)

    def append(self, value):
        self._composites.append(value)
        return None

    def extend(self, other):
        self._composites.extend(other._composites)
        return None

    def insert(self, key, value):
        self._composites.insert(key, value)
        return None

    def remove(self, value):
        self._composites.remove(value)
        return None

    def pop(self, key):
        return self._composites.pop(key)

    def clear(self):
        self._composites.clear()
        return None

    def index(self, value):
        return self._composites.index(value)

    def count(self, value):
        return self._composites.count(value)

    def sort(self):
        self._composites.sort()
        return None

    def reverse(self):
        self._composites.reverse()
        return None

    def copy(self):
        return self._composites.copy()

    def __add__(self, other):
        return self._composites.__add__(other._composites)

    def __radd__(self, other):
        return self._composites.__radd__(other._composites)

    def __iadd__(self, other):
        return self._composites.__iadd__(other._composites)

    def __mul__(self, value):
        return self._composites.__mull__(value)

    def __rmul__(self, value):
        return self._composites.__rmul__(value)

    def __imul__(self, value):
        return self._composites.__imul__(value)

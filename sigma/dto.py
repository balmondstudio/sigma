import sigma.interface
import sigma.vo


class IDTO:
    pass


class Primitive(IDTO, sigma.interface.IRepresentable):

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
        self._relative_key = sigma.vo.RelativeKey(relative_key)
        self._absolute_key = sigma.vo.AbsoluteKey(absolute_key)
        self._value = sigma.vo.Value(value)

    def __repr__(self):
        return "Primitive({0}, {1}, {2})".format(self._relative_key,
                self._absolute_key, self._value)

    def __str__(self):
        return "{{relative_key: {0}, absolute_key: {1}, value: {2}}}".format(self._relative_key, self._absolute_key, self._value)

    def __bytes__(self):
        return bytes("{{relative_key: {0}, absolute_key: {1}, value: {2}}}".format(
            self._relative_key, self._absolute_key, self._value), "utf-8")

    def __format__(self, format_spec=""):
        return "{{relative_key: {0}, absolute_key: {1}, value: {2}}}".format(self._relative_key, self._absolute_key, self._value)


class Composite(IDTO, sigma.interface.IRepresentable,
        sigma.interface.IComparable, sigma.interface.IBitwise,
        sigma.interface.IContainer, sigma.interface.ISequence):

    @property
    def primitives(self):
        return self._primitives

    @primitives.setter
    def primitives(self, value):
        self._primitives = value

    def __init__(self, primitives=None):
        self._primitives = [] if primitives is None else primitives

    def __repr__(self):
        return "Composite({0})".format(self._primitives)

    def __str__(self):
        return "{0}".format(self._primitives)

    def __bytes__(self):
        return bytes("{0}".format(self._primitives), "utf-8")

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

    def __mul__(self, value):
        return self._primitives.__mull__(value)

    def __rmul__(self, value):
        return self._primitives.__rmul__(value)

    def __imul__(self, value):
        return self._primitives.__imul__(value)


class IDTOConverter:

    def assemble(self, data):
        raise NotImplementedError

    def disassemble(self, dto):
        raise NotImplementedError


class DTOConverter(IDTOConverter):

    def assemble(self, data):
        composite = Composite()
        for value in data:
            primitive = Primitive(value["relative_key"], value["absolute_key"], value["value"])
            composite.append(primitive)
        return composite

    def disassemble(self, composite):
        data = []
        for primitive in composite:
            data.append({
                "relative_key": primitive.relative_key.data,
                "absolute_key": primitive.absolute_key.data,
                "value": primitive.value.data
                })
        return data

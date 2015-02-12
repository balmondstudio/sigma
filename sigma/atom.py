class Atom(sigma.interface.IRepresentable, sigma.interface.IComparable):

    @property
    def relative(self):
        return self._relative

    @relative.setter
    def relative(self, value):
        self._relative = value

    @property
    def absolute(self):
        return self._absolute

    @absolute.setter
    def absolutek(self, value):
        self._absolute = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __init__(self, relative, absolute, value):
        self._relative = sigma.vo.Relative(relative)
        self._absolute = sigma.vo.Absolute(absolute)
        self._value = sigma.vo.Value(value)

    def __repr__(self):
        return "Atom({0}, {1}, {2})".format(self._relative, self._absolute, self._value)

    def __str__(self):
        return "{{relative: {0}, absolute: {1}, value: {2}}}".format(self._relative, self._absolute, self._value)

    def __bytes__(self):
        return bytes("{{relative: {0}, absolute: {1}, value: {2}}}".format(self._relative, self._absolute, self._value), "utf-8")

    def __format__(self, format_spec=""):
        return "{{relative: {0}, absolute: {1}, value: {2}}}".format(self._relative, self._absolute, self._value)

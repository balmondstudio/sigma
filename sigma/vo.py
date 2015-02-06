"""Interface and concrete classes emulating Value Objects.

The Value Object module defines interfaces and concrete classes which
encapsulate a set of operations that emulate equality behaviours based on field
values within the class and not on their id."""


import sigma.interface


class IVO(sigma.interface.IRepresentable, sigma.interface.IComparable, 
        sigma.interface.IBitwise, sigma.interface.INumeric):
    """Value Object interface.

    Interface to be implemented by classes that require their baseis for
    equality to be based on field values within the class and not on their id.

    Attributes:
        data: A list of the data to be used as the basis for equality
        operations.
    """

    @property
    def data(self):
        """Data accessor data."""
        return self._data

    @data.setter
    def data(self, value):
        """Data mutator data."""
        self._data = value

    def __init__(self, data):
        """Data to be used as the basis for equality operations."""
        self._data = data

    def __repr__(self):
        """Overload repr operator."""
        return "IVO({0})".format(self._data)

    def __str__(self):
        """Overload str operator."""
        return "{0}".format(self._data)

    def __bytes__(self):
        """Overload bytes operator."""
        return bytes("{0}".format(self._data), "utf-8")

    def __format__(self, format_spec=""):
        """Overload fromat operator."""
        return "{0}".format(self._data)

    def __lt__(self, other):
        """Overload binary < operator."""
        return self._data < other._data

    def __gt__(self, other):
        """Overload binary > operator."""
        return self._data > other._data

    def __le__(self, other):
        """Overload binary <= operator."""
        return self._data <= other._data

    def __ge__(self, other):
        """Overload binary >= operator."""
        return self._data >= other._data

    def __eq__(self, other):
        """Overload binary == operator."""
        return self._data == other._data

    def __ne__(self, other):
        """Overload binary != operator."""
        return self._data < other._data

    __hash__ = None # IVO is mutable hence non-hashable

    def __bool__(self):
        """Overload binary nonzero operator."""
        return bool(self._data)

    def __add__(self, other):
        """Overload binary + operator."""
        data = [a + b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __radd__(self, other):
        """Overload reverse binary + operator."""
        data = [a + b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __iadd__(self, other):
        """Overload augmented + operator."""
        self._data = [a + b for a, b in zip(self._data, other._data)]
        return self

    def __sub__(self, other):
        """Overload binary - operator."""
        data = [a - b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rsub__(self, other):
        """Overload reverse binary - operator."""
        data = [b - a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __isub__(self, other):
        """Overload augmented - operator."""
        self._data = [a - b for a, b in zip(self._data, other._data)]
        return self

    def __mul__(self, other):
        """Overload binary * operator."""
        data = [a * b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rmul__(self, other):
        """Overload reverse binary * operator."""
        data = [a * b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __imul__(self, other):
        """Overload augmented * operator."""
        self._data = [a * b for a, b in zip(self._data, other._data)]
        return self

    def __div__(self, other):
        """Overload binary / operator."""
        data = [a / b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rdiv__(self, other):
        """Overload reverse binary / operator."""
        data = [b / a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __idiv__(self, other):
        """Overload augmented / operator."""
        self._data = [a / b for a, b in zip(self._data, other._data)]
        return self

    def __truediv__(self, other):
        """Overload binary true / operator."""
        data = [float(a) / float(b) for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rtruediv__(self, other):
        """Overload reverse binary true / operator."""
        data = [float(b) / float(a) for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __itruediv__(self, other):
        """Overload augmented true / operator."""
        self._data = [float(a) / float(b) for a, b in zip(self._data,
            other._data)]
        return self

    def __floordiv__(self, other):
        """Overload binary // operator."""
        data = [int(a) / int(b) for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rfloordiv__(self, other):
        """Overload reverse binary // operator."""
        data = [int(b) / int(a) for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ifloordiv__(self, other):
        """Overload augmented // operator."""
        self._data = [int(a) / int(b) for a, b in zip(self._data, other._data)]
        return self

    def __mod__(self, other):
        """Overload binary % operator."""
        data = [a % b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rmod__(self, other):
        """Overload reverse binary % operator."""
        data = [b % a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __imod__(self, other):
        """Overload augmented % operator."""
        self._data = [a % b for a, b in zip(self._data, other._data)]
        return self

    def __divmod__(self, other):
        """Overload binary divmod operator."""
        quotient = [a / b for a, b in zip(self._data, other._data)]
        remainder = [a % b for a, b in zip(self._data, other._data)]
        return type(self)(quotient), type(self)(remainder)

    def __rdivmod__(self, other):
        """Overload reverse binary divmod operator."""
        quotient = [b / a for a, b in zip(self._data, other._data)]
        remainder = [b % a for a, b in zip(self._data, other._data)]
        return type(self)(quotient), type(self)(remainder)

    def __pow__(self, other):
        """Overload binary ** operator."""
        data = [a ** b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rpow__(self, other):
        """Overload reverse binary ** operator."""
        data = [b ** a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ipow__(self, other):
        """Overload augmented ** operator."""
        self._data = [a ** b for a, b in zip(self._data, other._data)]
        return self

    def __lshift__(self, other):
        """Overload binary >> operator."""
        data = [a >> b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rlshift__(self, other):
        """Overload reverse binary >> operator."""
        data = [b >> a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ilshift__(self, other):
        """Overload augmented >> operator."""
        self._data = [a >> b for a, b in zip(self._data, other._data)]
        return self

    def __rshift__(self, other):
        """Overload binary << operator."""
        data = [a << b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rrshift__(self, other):
        """Overload reverse binary << operator."""
        data = [b << a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __irshift__(self, other):
        """Overload augmented << operator."""
        self._data = [a << b for a, b in zip(self._data, other._data)]
        return self

    def __and__(self, other):
        """Overload binary & operator."""
        data = [a & b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rand__(self, other):
        """Overload reverse binary & operator."""
        data = [b & a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __iand__(self, other):
        """Overload augmented & operator."""
        self._data = [a & b for a, b in zip(self._data, other._data)]
        return self

    def __xor__(self, other):
        """Overload binary ^ operator."""
        data = [a ^ b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __rxor__(self, other):
        """Overload reverse binary ^ operator."""
        data = [b ^ a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ixor__(self, other):
        """Overload augmented ^ operator."""
        self._data = [a ^ b for a, b in zip(self._data, other._data)]
        return self

    def __or__(self, other):
        """Overload binary | operator."""
        data = [a | b for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ror__(self, other):
        """Overload reverse binary | operator."""
        data = [b | a for a, b in zip(self._data, other._data)]
        return type(self)(data)

    def __ior__(self, other):
        """Overload augmented | operator."""
        self._data = [a | b for a, b in zip(self._data, other._data)]
        return self

    def __neg__(self):
        """Overload binary - operator."""
        data = [-a for a in self._data]
        return type(self)(data)

    def __pos__(self):
        """Overload binary + operator."""
        data = [+a for a in self._data]
        return type(self)(data)

    def __abs__(self):
        """Overload binary abs operator."""
        data = [abs(a) for a in self._data]
        return type(self)(data)

    def __invert__(self):
        """Overload binary ~ operator."""
        data = [~a for a in self._data]
        return type(self)(data)

    # FIXME: return complex not list
    def __complex__(self):
        """Overload binary complex operator."""
        data = [complex(a) for a in self._data]
        return type(self)(data)

    # FIXME: return int not list
    def __int__(self):
        """Overload binary int operator."""
        data = [int(a) for a in self._data]
        return type(self)(data)

    # FIXME: return float not list
    def __float__(self):
        """Overload binary float operator."""
        data = [float(a) for a in self._data]
        return type(self)(data)

    def __round__(self, n=2):
        """Overload binary round operator."""
        data = [round(a, n) for a in self._data]
        return type(self)(data)

    # FIXME: return int not list (called by bin(), hex(), oct(), slicing)
    def __index__(self):
        """Overload binary index operator."""
        data = [int(a) for a in self._data]
        return type(self)(data)


class RelativeKey(IVO):
    """3D relative cartesian coordinates.

    Class representing 3D relative cartesian coordinates, relative to objects.

    Attributes:
        null
    """

    @property
    def i(self):
        """Data accessor i."""
        return self._data[0]

    @i.setter
    def i(self, value):
        """Data mutator i."""
        self._data[0] = int(value)

    @property
    def j(self):
        """Data accessor j."""
        return self._data[1]

    @j.setter
    def j(self, value):
        """Data mutator j."""
        self._data[1] = int(value)

    @property
    def k(self):
        """Data accessor k."""
        return self._data[2]

    @k.setter
    def k(self, value):
        """Data mutator k."""
        self._data[2] = int(value)

    def __init__(self, data):
        """X, Y, Z absolute coordinates data."""
        super().__init__(data)


class AbsoluteKey(IVO):
    """3D absolute cartesian coordinates.

    Class representing 3D absolute cartesian coordinates, relative to world.

    Attributes:
        null
    """

    @property
    def x(self):
        """Data accessor x."""
        return self._data[0]

    @x.setter
    def x(self, value):
        """Data mutator x."""
        self._data[0] = value

    @property
    def y(self):
        """Data accessor y."""
        return self._data[1]

    @y.setter
    def y(self, value):
        """Data mutator y."""
        self._data[1] = value

    @property
    def z(self):
        """Data accessor z."""
        return self._data[2]

    @z.setter
    def z(self, value):
        """Data mutator z."""
        self._data[2] = value

    def __init__(self, data):
        """X, Y, Z absolute coordinates data."""
        super().__init__(data)


class Value(IVO):
    """Value representation.

    Class representing a generic value.

    Attributes:
        null
    """

    @property
    def n(self):
        """Data accessor value."""
        print(self._data)
        return self._data[0]

    @n.setter
    def n(self, value):
        """Data mutator value."""
        self._data = [value]

    def __init__(self, data):
        """Value data."""
        super().__init__(data)

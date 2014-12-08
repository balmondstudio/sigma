class IRepresentable(object):

    def __repr__(self): raise NotImplementedError

    def __str__(self): raise NotImplementedError

    def __bytes__(self): raise NotImplementedError

    def __format__(self, format_spec=""): raise NotImplementedError


class IComparable(object):

    def __lt__(self, other): raise NotImplementedError

    def __le__(self, other): raise NotImplementedError

    def __eq__(self, other): raise NotImplementedError

    def __ne__(self, other): raise NotImplementedError

    def __gt__(self, other): raise NotImplementedError

    def __ge__(self, other): raise NotImplementedError

    def __bool__(self): raise NotImplementedError


class IHashable(object):

    def __hash__(self): raise NotImplementedError


class IBitwise(object):

    def __lshift__(self, other): raise NotImplementedError

    def __rlshift__(self, other): raise NotImplementedError

    def __ilshift__(self, other): raise NotImplementedError

    def __rshift__(self, other): raise NotImplementedError

    def __rrshift__(self, other): raise NotImplementedError

    def __irshift__(self, other): raise NotImplementedError

    def __and__(self, other): raise NotImplementedError

    def __rand__(self, other): raise NotImplementedError

    def __iand__(self, other): raise NotImplementedError

    def __xor__(self, other): raise NotImplementedError

    def __rxor__(self, other): raise NotImplementedError

    def __ixor__(self, other): raise NotImplementedError

    def __or__(self, other): raise NotImplementedError

    def __ror__(self, other): raise NotImplementedError

    def __ior__(self, other): raise NotImplementedError

    def __invert__(self): raise NotImplementedError


class IContainer(object):

    def __len__(self): raise NotImplementedError

    def __length_hint__(self): raise NotImplementedError

    def __getitem__(self, key): raise NotImplementedError

    def __setitem__(self, key, value): raise NotImplementedError

    def __delitem__(self, key): raise NotImplementedError

    def __iter__(self): raise NotImplementedError

    def __reversed__(self): raise NotImplementedError

    def __contains__(self, value): raise NotImplementedError


class IMapping(object): pass


class ISequence(object):

    def append(self, value): raise NotImplementedError

    def extend(self, other): raise NotImplementedError

    def insert(self, key, value): raise NotImplementedError

    def remove(self, value): raise NotImplementedError

    def pop(self, key): raise NotImplementedError

    def clear(self): raise NotImplementedError

    def index(self, value): raise NotImplementedError

    def count(self, value): raise NotImplementedError

    def sort(self): raise NotImplementedError

    def reverse(self): raise NotImplementedError

    def copy(self): raise NotImplementedError

    def __add__(self, other): raise NotImplementedError

    def __radd__(self, other): raise NotImplementedError

    def __iadd__(self, other): raise NotImplementedError

    def __mul__(self, other): raise NotImplementedError

    def __rmul__(self, other): raise NotImplementedError

    def __imul__(self, other): raise NotImplementedError


class INumeric(object):

    def __add__(self, other): raise NotImplementedError

    def __radd__(self, other): raise NotImplementedError

    def __iadd__(self, other): raise NotImplementedError

    def __sub__(self, other): raise NotImplementedError

    def __rsub__(self, other): raise NotImplementedError

    def __isub__(self, other): raise NotImplementedError

    def __mul__(self, other): raise NotImplementedError

    def __rmul__(self, other): raise NotImplementedError

    def __imul__(self, other): raise NotImplementedError

    def __truediv__(self, other): raise NotImplementedError

    def __rtruediv__(self, other): raise NotImplementedError

    def __itruediv__(self, other): raise NotImplementedError

    def __floordiv__(self, other): raise NotImplementedError

    def __rfloordiv__(self, other): raise NotImplementedError

    def __ifloordiv__ (self, other): raise NotImplementedError

    def __mod__(self, other): raise NotImplementedError

    def __rmod__(self, other): raise NotImplementedError

    def __imod__ (self, other): raise NotImplementedError

    def __divmod__(self, other): raise NotImplementedError

    def __rdivmod__(self, other): raise NotImplementedError

    def __pow__(self, other): raise NotImplementedError

    def __rpow__(self, other): raise NotImplementedError

    def __ipow__(self, other): raise NotImplementedError

    def __neg__(self): raise NotImplementedError

    def __pos__(self): raise NotImplementedError

    def __abs__(self): raise NotImplementedError

    def __complex__(self): raise NotImplementedError

    def __int__(self): raise NotImplementedError

    def __float__ (self): raise NotImplementedError

    def __round__(self, n=2): raise NotImplementedError

    def __index__(self): raise NotImplementedError

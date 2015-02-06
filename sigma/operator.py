import math


class Operator:

    def __init__(self):
        pass

    def operate(self, dto):
        raise NotImplementedError


# Modifier---------------------------------------------------------------------

class Modifier(Operator):

    def __init__(self):
        super().__init__()


class SigmaModifier(Modifier):

    def __init__(self):
        super().__init__()

    def _digital_root(self, n):
        return n - 9 * math.floor((n - 1) / 9)

    def operate(self, dto):
        for primitive in dto:
            primitive.value.data = self._digital_root(primitive.value.n)

        return dto


# Filter-----------------------------------------------------------------------

class Filter(Operator):

    def __init__(self):
        super().__init__()


# Creator----------------------------------------------------------------------

class Creator(Operator):

    def __init__(self):
        super().__init__()

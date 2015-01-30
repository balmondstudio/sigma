class Operator:

    def __init__(self):
        pass

    def operate(data_transfer_object):
        raise NotImplementedError


class Filter(Operator):

    def __init__(self):
        pass


class Modifier(Operator):

    def __init__(self):
        pass


class Creator(Operator):

    def __init__(self):
        pass


class SigmaFilter(Filter):

    def __init__(self):
        pass

    def operate(data_transfer_object):
        print("sigmafilter is operating...")

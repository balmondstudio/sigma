class IInputPort:

    def setup(self, **kwargs):
        raise NotImplementedError

    def execute(self, dto):
        raise NotImplementedError


class IOutputPort:

    def setup(self, **kwargs):
        raise NotImplementedError

    def execute(self, dto):
        raise NotImplementedError

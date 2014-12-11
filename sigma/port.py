class IInputPort:

    def execute(self, data_transfer_object):
        raise NotImplementedError


class IOutputPort:

    def execute(self, data_transfer_object):
        raise NotImplementedError

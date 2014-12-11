class IInputPort(object):

    def execute(self, data_transfer_object):
        raise NotImplementedError


class IOutputPort(object):

    def execute(self, data_transfer_object):
        raise NotImplementedError

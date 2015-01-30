import sigma.adapter
import sigma.operator


class ICore(sigma.port.IInputPort):

    def __init__(self, output_adapter_name, operator_stack_name):
        self._output_adapter = self._create_output_adapter(output_adapter_name)
        self._operator_stack = [self._create_operator(operator_name) for operator_name in operator_stack_name]

    def _create_operator(self, operator_name):
        return eval("sigma.operator.{0}".format(operator_name))

    def _create_output_adapter(self, output_adapter_name):
        return eval("sigma.adapter.{0}".format(operator_name))

    def execute(self, data_transfer_object):
        raise NotImplementedError


class Core(ICore):

    def __init__(self, output_adapter_name, operator_stack_name):
        super().__init__(output_adapter_name, operator_stack_name)

    def execute(self, data_transfer_object):
        self._data_transfer_object = data_transfer_object

        # TODO: Main algorithm

        self._service.execute(data_transfer_object)

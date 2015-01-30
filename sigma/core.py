import sigma.adapter
import sigma.operator
import sigma.port


class Core(sigma.port.IInputPort):

    def __init__(self):
        output_adapter_name = "{0}OutputAdapter".format(sigma.config.OUTPUT_SERVICE)
        self._output_adapter = self._create_output_adapter(output_adapter_name)

    def _create_operator(self, operator_name):
        return eval("sigma.operator.{0}".format(operator_name))

    def _create_output_adapter(self, output_adapter_name):
        return eval("sigma.adapter.{0}".format(output_adapter_name))

    def execute(self, data_transfer_object):
        operator_stack = [self._create_operator(operator_name) for operator_name in self._operator_stack_name]
        for operator in operator_stack:
            data_transfer_object = operator.operate(data_transfer_object)

        print(self._output_adapter)
        self._output_adapter.execute(data_transfer_object)

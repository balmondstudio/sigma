import sigma.adapter
import sigma.operator
import sigma.port


class Core(sigma.port.IInputPort):

    def __init__(self):
        output_adapter_name = "{0}OutputAdapter".format(sigma.config.OUTPUT_SERVICE)
        self._output_adapter = self._create_output_adapter(output_adapter_name)

        self._operator_stack = None

    def _create_operator(self, operator_name):
        return eval("sigma.operator.{0}".format(operator_name))()

    def _create_output_adapter(self, output_adapter_name):
        return eval("sigma.adapter.{0}".format(output_adapter_name))()

    def setup(self, **kwargs):
        self._operators = [self._create_operator(operator_name) for operator_name in kwargs["operator"]]

    def execute(self, dto):
        for operator in self._operators:
            dto = operator.operate(dto)

        self._output_adapter.execute(dto)

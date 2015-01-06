import json

import sigma.core
import sigma.data_transfer_object
import sigma.port
import sigma.service


class IInputAdapter:

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_adaptee_converter(self):
        raise NotImplementedError


class IOutputAdapter(sigma.port.IOutputPort):

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_adaptee_converter(self):
        raise NotImplementedError

    def execute(self, target_data):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.TerminalService):

    def __init__(self):
        super().__init__()
        self.input()

    def _command(self, args):
        self._args = args

        target_data = self._args.data.read()
        generic_data = json.loads(target_data)
        adaptee_data = self._create_adaptee_converter().assemble(generic_data)

        self._create_adaptee().execute(adaptee_data)

    def _create_adaptee(self):
         return sigma.core.Core(
                 self._args.creator,
                 self._args.filter,
                 self._args.modifier,
                 self._args.service
                 )

    def _create_adaptee_converter(self):
        return sigma.data_transfer_object.DataTransferObjectConverter()


class TerminalOutputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()

    def execute(self, target_data):
        generic_data = self._create_adaptee_converter().disassemble(target_data)
        adaptee_data = json.dumps(generic_data)

        self._create_adaptee().output(adaptee_data)

    def _create_adaptee(self):
        return sigma.service.TerminalService()

    def _create_adaptee_data_converter(self):
        return sigma.data_transfer_object.DataTransferObjectConverter()

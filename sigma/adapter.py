import json

import sigma.core
import sigma.dto
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

    def setup(self, **kwargs):
        raise NotImplementedError

    def execute(self, target_data):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.TerminalService):

    def __init__(self):
        super().__init__()

        self.input()

    def _command(self, args):
        # Adaptee data
        target_data = args.data.read()
        generic_data = json.loads(target_data)
        adaptee_data = self._create_adaptee_converter().assemble(generic_data)

        # Adaptee
        adaptee = self._create_adaptee()
        adaptee.setup(stack=args.stack)
        adaptee.execute(adaptee_data)

    def _create_adaptee(self):
        return sigma.core.Core()

    def _create_adaptee_converter(self):
        return sigma.dto.DTOConverter()


class TerminalOutputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()

    def setup(self, **kwargs):
        pass

    def execute(self, target_data):
        # Adaptee data
        generic_data = self._create_adaptee_converter().disassemble(target_data)
        #adaptee_data = json.dumps(generic_data)
        adaptee_data = json.dumps(generic_data, indent=4, sort_keys=True)

        # Adaptee
        self._create_adaptee().output(adaptee_data)

    def _create_adaptee(self):
        return sigma.service.TerminalService()

    def _create_adaptee_converter(self):
        return sigma.dto.DTOConverter()

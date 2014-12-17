import sigma.core
import sigma.data_transfer_object
import sigma.port
import sigma.service


class IInputAdapter:

    def _execute(self, target_data):
        adaptee_data = self._convert_data(target_data)
        self._create_adaptee().execute(adaptee_data)

    def _convert_data(self, adaptee_data):
        raise NotImplementedError

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_data_converter(self):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.TerminalService):

    def __init__(self):
        super().__init__()
        self.input()

    def _convert(self, target_data):
        data = json.dumps(target_data)
        adaptee_data = self._create_assembler.assemble(data)
        return data_tranfer_object

    def _create_adaptee(self):
        return sigma.core.Core(
                self._args.creator,
                self._args.filter,
                self._args.modifier,
                self._args.outservice
                )

    def _create_assembler(self):
        return sigma.data_transfer_object.DataTransferObjectAssembler()

    def _command(self, args):
        self._args = args
        self._execute(self._args.infile.read())


class IOutputAdapter(sigma.port.IOutputPort):

    def execute(self, target_data):
        adaptee_data = self._convert_data(target_data)
        self._create_adaptee().output(adaptee_data)

    def _convert_data(self, data):
        raise NotImplementedError

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_disassembler(self):
        raise NotImplementedError


class TerminalOutputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()

    def _convert(self, data_transfer_object):
        data = disassembler.disassemble(data_transfer_object)
        raw_data = self._convert(data)
        return json.loads(data)

    def _create_adaptee(self):
        return sigma.service.TerminalService()

    def _create_disassembler(self):
        return sigma.data_transfer_object.DataTransferObjectDisassembler()


class IAdapter:

    def _adapt(self, target_data):
        adaptee_data = self._convert_data(target_data)
        self._create_adaptee()._execute_adaptee(adaptee_data)

    def _convert_data(self, target_data):
        raise NotImplementedError

    def _execute_adaptee(self, adaptee_data):
        raise NotImplementedError

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_adaptee_data_converter(self):
        raise NotImplementedError

    def _create_target_data_converter(self):
        raise NotImplementedError

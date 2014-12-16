import sigma.core
import sigma.data_transfer_object
import sigma.port
import sigma.service


class IInputAdapter:

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_assembler(self):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.TerminalService):

    def __init__(self):
        super().__init__()
        self.input()

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

        adaptee = self._create_adaptee()
        assembler = self._create_assembler()

        data_transfer_object = assembler.assemble(args.infile.read())
        adaptee.execute(data_transfer_object)


class IOutputAdapter(sigma.port.IOutputPort):

    def __init__(self):
        super().__init__()

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_disassembler(self):
        raise NotImplementedError

    def execute(self, data_transfer_object):
        raise NotImplementedError


class TerminalOutputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()

    def _create_adaptee(self):
        return sigma.service.TerminalService()

    def _create_disassembler(self):
        return sigma.data_transfer_object.DataTransferObjectDisassembler()

    def execute(self, data_transfer_object):
        adaptee = self._create_adaptee()
        disassembler = self._create_disassembler()

        raw_data = disassembler.disassemble(data_transfer_object)
        adaptee.output(raw_data)

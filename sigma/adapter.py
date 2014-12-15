import sigma.core
import sigma.data_transfer_object
import sigma.port
import sigma.service


class IInputAdapter:

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_assembler(self):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.ITerminal):

    def __init__(self):
        super().__init__()
        args = self._input()
        self._command(args)

    def _create_adaptee(self, *args, **kwargs):
        return sigma.core.Core(
                self._args.outservice,
                self._args.modifiers,
                self._args.filters,
                self._args.creator
                )

    def _create_assembler(self, *args, **kwargs):
        return sigma.data_tranfer_object.DataTransferObjectAssembler()

    def _command(self, args):
        adaptee = self._create_adaptee()
        disassembler = self._create_disassembler()

        raw_data = self._args.infile.read()
        data_transfer_object = assembler.assemble(raw_data)
        adaptee.execute(data_tranfer_object)


class IOutputAdapter(sigma.port.IOutputPort):

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_disassembler(self):
        raise NotImplementedError

    def execute(self, data_transfer_object):
        raise NotImplementedError


class TerminalInputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()
        self._adaptee = self._create_adaptee()
        self._disassembler = self._create_disassembler()

    def _create_adaptee(self):
        return sigma.service.ITerminal()

    def _create_disassembler(self):
        return sigma.data_tranfer_object.DataTransferObjectDisassembler()

    def execute(self, data_transfer_object):
        raw_data = self._disassembler.disassembler(data_transfer_object)
        self._adaptee.output(raw_data)

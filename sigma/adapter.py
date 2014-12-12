import sigma.core
import sigma.data_transfer_object
import sigma.port
import sigma.service


class IInputAdapter:

    def __init__(self):
        self._adaptee = self._create_adaptee()
        self._assembler = self._create_assembler()

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_assembler(self):
        raise NotImplementedError


class TerminalInputAdapter(IInputAdapter, sigma.service.ITerminal):

    def __init__(self):
        super().__init__()

    def _create_adaptee(self):
        return sigma.core.Core()

    def _create_assembler(self):
        return sigma.data_tranfer_object.DataTransferObjectAssembler()

    def execute(self):
        self._adaptee.execute(
                self._assembler.assemble(raw_data),
                self._args.modifiers,
                self._args.filters,
                self._args.creator
                )


class IOutputAdapter(sigma.port.IOutputPort):

    def __init__(self):
        super().__init__()
        self._adaptee = self._create_adaptee()
        self._disassembler = self._create_disassembler()

    def _create_adaptee(self):
        raise NotImplementedError

    def _create_disassembler(self):
        raise NotImplementedError

    def execute(self, data_transfer_object):
        raise NotImplementedError


class TerminalInputAdapter(IOutputAdapter):

    def __init__(self):
        super().__init__()

    def _create_adaptee(self):
        return sigma.service.ITerminal

    def _create_disassembler(self):
        return sigma.data_tranfer_object.DataTransferObjectDisassembler()

    def execute(self, data_transfer_object):
        pass

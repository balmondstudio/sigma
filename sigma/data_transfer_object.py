class IDataTransferObject:
    pass


class IDataTransferObjectAssembler:

    def assemble(self, data):
        raise NotImplementedError


class DataTransferObjectAssembler(IDataTransferObjectAssembler):

    def assemble(self, data):
        return data_tranfer_object


class IDataTransferObjectDisassembler:

    def disassemble(self, data_transfer_object):
        raise NotImplementedError


class DataTransferObjectDisassembler(IDataTransferObjectDisassembler):

    def disassemble(self, data_transfer_object):
        return data

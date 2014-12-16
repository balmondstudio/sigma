class IDataTransferObject:
    pass


class IDataTransferObjectAssembler:

    def assemble(self, raw_data):
        return raw_data # FIXME

    def createDataTransferObject(self):
        raise NotImplementedError


class DataTransferObjectAssembler(IDataTransferObjectAssembler):

    def createDataTransferObject(self):
        pass


class IDataTransferObjectDisassembler:

    def disassemble(self, data_transfer_object):
        return data_transfer_object # FIXME

    def createRawData(self):
        raise NotImplementedError


class DataTransferObjectDisassembler(IDataTransferObjectDisassembler):

    def createRawData(self):
        pass

class IDataTransferObject:
    pass


class IDataTransferObjectAssembler:

    def assemble(self):
        data_transfer_object = self.createDataTransferObject()
        #TODO: Append Primitive to Composite
        return data_transfer_object

    def createDataTransferObject(self):
        raise NotImplementedError


class IDataTransferObjectDisassembler:

    def disassemble(self, data_transfer_object):
        pass

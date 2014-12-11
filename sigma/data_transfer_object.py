class IDataTransferObject(object):
    pass


class IDataTransferObjectAssembler(object):

    def assemble(self):
        data_transfer_object = self.createDataTransferObject()
        #TODO: Append Primitive to Composite
        return data_transfer_object

    def createDataTransferObject(self):
        raise NotImplementedError


class IDataTransferObjectDisassembler(object):

    def disassemble(self, data_transfer_object):
        pass

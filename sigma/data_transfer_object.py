import sigma.value_object


class IDataTransferObject:
    pass


class DataTransferObject(IDataTransferObject):
    pass


class IDataTransferObjectConverter:

    def assemble(self, data):
        raise NotImplementedError

    def disassemble(self, data_transfer_object):
        raise NotImplementedError


class DataTransferObjectConverter(IDataTransferObjectConverter):

    def assemble(self, data):
        data_tranfer_object = DataTransferObject()
        for i, table in enumerate(data):
            for j, row in enumerate(table):
                for k, columnt in enumerate(row):
                    relative_key = sigma.relative_key.RelativeKey([i, j, k])
                    absolute_key = sigma.value_object.AbsoluteKey([i, j, k])
                    value = sigma.value_object.Value(column)
                    data_transfer_object.append(ralative_key, absolute_key, value)
        return data_tranfer_object

    def disassemble(self, data_transfer_object):
        data = []
        for value_object in data_transfer_object:
            pass
        return data

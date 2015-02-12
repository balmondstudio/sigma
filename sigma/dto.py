

class IDTO:
    pass


class IDTOConverter:

    def assemble(self, data):
        raise NotImplementedError

    def disassemble(self, dto):
        raise NotImplementedError


class DTOConverter(IDTOConverter):

    def assemble(self, data):
        composite = Composite()
        for value in data:
            primitive = Primitive(value["relative_key"], value["absolute_key"], value["value"])
            composite.append(primitive)
        return composite

    def disassemble(self, composite):
        data = []
        for primitive in composite:
            data.append({
                "relative_key": primitive.relative_key.data,
                "absolute_key": primitive.absolute_key.data,
                "value": primitive.value.data
                })
        return data

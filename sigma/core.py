import sigma.adapter
import sigma.creator
import sigma.filter
import sigma.modifier
import sigma.port


class ICore(sigma.port.IInputPort):

    def __init__(self, creator, filter, modifier, outservice):
        self._creator = self._create_creator(creator)
        self._filter = self._create_filter(filter)
        self._modifier = self._create_modifier(modifier)
        self._output_service = self._create_output_service(outservice)

    def _create_creator(self, name):
        raise NotImplementedError

    def _create_filter(self, name):
        raise NotImplementedError

    def _create_modifier(self, name):
        raise NotImplementedError

    def _create_output_service(self, name):
        raise NotImplementedError


class Core(ICore):

    def __init__(self, modifier, filter, creator, outservice):
        super().__init__(modifier, filter, creator, outservice)

    def _create_creator(self, name):
        print(name)
        #command = "sigma.creator.{0}Creator()".format(name)
        #return eval(command)

    def _create_filter(self, name):
        print(name)
        #command = "sigma.filter.{0}Filter()".format(name)
        #return eval(command)

    def _create_modifier(self, name):
        print(name)
        #command = "sigma.modifier.{0}Modifier()".format(name)
        #return eval(command)

    def _create_output_service(self, name):
        command = "sigma.adapter.{0}OutputAdapter()".format(name)
        return eval(command)

    def execute(self, data_transfer_object):
        self._output_service.execute(data_transfer_object)

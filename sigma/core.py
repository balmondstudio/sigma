import sigma.adapter
import sigma.creator
import sigma.filter
import sigma.modifier
import sigma.port


class ICore(sigma.port.IInputPort):

    def __init__(self):
        self._output_port = self._create_output_port()
        self._modifier = self._create_modifier()
        self._creator = self._create_creator()
        self._filter = self._create_filter()

    def _create_output_port(self):
        raise NotImplementedError

    def _create_modifier(self):
        raise NotImplementedError

    def _create_creator(self):
        raise NotImplementedError

    def _create_filter(self):
        raise NotImplementedError


class Core(ICore):

    def _create_output_port(self):
        pass

    def _create_modifier(self):
        pass

    def _create_creator(self):
        pass

    def _create_filter(self):
        pass

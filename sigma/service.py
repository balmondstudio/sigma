import sigma.config


class IService:

    def __init__(self):
        super().__init__()

    def input(self):
        raise NotImplementedError

    def output(self):
        raise NotImplementedError


class TerminalService(IService):

    def __init__(self):
        super().__init__()

    def _command(self, args):
        raise NotImplementedError

    def input(self):
        argparse = __import__("argparse")

        parser = argparse.ArgumentParser(description="Sigma")

        parser.add_argument("-m", "--modifier",
          nargs="+",
          type=str,
          choices=sigma.config.MODIFIERS,
          help="modifier name stack")

        parser.add_argument("-f", "--filter",
          nargs="+",
          type=str,
          choices=sigma.config.FILTERS,
          help="filter name stack")

        parser.add_argument("-c", "--creator",
          nargs=1,
          type=str,
          choices=sigma.config.CREATORS,
          help="creator name")

        parser.add_argument("-i", "--infile",
          nargs="?",
          default=sigma.config.DATA_FILENAME,
          type=argparse.FileType("r"),
          help="input raw-data filename")

        parser.add_argument("-o", "--outservice",
          nargs="?",
          default=sigma.config.OUTPUT_SERVICE,
          type=str,
          choices=sigma.config.SERVICES,
          help="output service name")

        args = parser.parse_args()

        self._command(args)

    def output(self, data):
        print(data)


class GUIService(IService):
    pass


class MatplotlibService(IService):
    pass


class RhinoService(IService):
    pass


class BlenderService(IService):
    pass


class DatabaseService(IService):
    pass


class FilesystemService(IService):
    pass

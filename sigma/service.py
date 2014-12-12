import sigma.config


class ITerminal:

    def __init__(self):
        self._args = self._parse_args()
        self._execute()

    def _parse_args(self):
        argparse = __import__("argparse")

        parser = argparse.ArgumentParser(description="Sigma")

        parser.add_argument("-m", "--modifier",
          nargs="+",
          type=str,
          choices=sigma.config.MODIFIERS,
          help="data modifier stack")

        parser.add_argument("-f", "--filter",
          nargs="+",
          type=str,
          choices=sigma.config.FILTERS,
          help="data filter stack")

        parser.add_argument("-c", "--creator",
          nargs=1,
          type=str,
          choices=sigma.config.CREATORS,
          help="creator on data")

        parser.add_argument("-i", "--infile",
          nargs="?",
          default=sigma.config.DATA_FILENAME,
          type=argparse.FileType("r"),
          help="raw data file")

        args = parser.parse_args()

        return args

    def _execute(self):
        raise NotImplementedError


class IGUI:
    pass


class IMatplotlib:
    pass


class IRhino:
    pass


class IBlender:
    pass


class IDatabase:
    pass


class IFilesystem:
    pass

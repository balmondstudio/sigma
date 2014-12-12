import config


class ITerminal:

    def __init__(self):
        self._args = self.parse_args()
        self.execute()

    def parse_args(self):
        argparse = __import__("argparse")

        parser = argparse.ArgumentParser(description="Sigma")

        parser.add_argument("-m", "--modifier",
          nargs="+",
          type=str,
          choices=config.modifiers,
          help="data modifier stack")

        parser.add_argument("-f", "--filter",
          nargs="+",
          type=str,
          choices=config.filters,
          help="data filter stack")

        parser.add_argument("-c", "--creator",
          nargs=1,
          type=str,
          choices=config.creators,
          help="creator on data")

        parser.add_argument("-i", "--infile",
          nargs="?",
          default=config.data_filename,
          type=argparse.FileType("r"),
          help="raw data file")

        args = parser.parse_args()

        return args

    def execute(self):
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

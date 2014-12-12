import config


class ITerminal:

    def __init__(self):
        self._argparse = __import__("argparse")

        self._parser = self._argparse.ArgumentParser(description="Sigma")

        self._parser.add_argument("-m", "--modifier",
                nargs="+",
                type=str,
                choices=config.modifiers,
                help="data modifier stack")

        self._parser.add_argument("-f", "--filter",
                nargs="+",
                type=str,
                choices=config.filters,
                help="data filter stack")

        self._parser.add_argument("-c", "--creator",
                nargs=1,
                type=str,
                choices=config.creators,
                help="creator on data")

        self._parser.add_argument("-i", "--infile",
                nargs="?",
                default=config.data_filename,
                type=argparse.FileType("r"),
                help="raw data file")

        self._args = self._parser.parse_args()

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

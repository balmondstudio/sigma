import sigma.config


class ITerminal:

    def input(self):
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

    def output(self, data):
        print(data)


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

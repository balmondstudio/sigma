import argparse
import sigma.config


class StackAction(argparse.Action):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, parser, namespace, values, option_string):
        values = "{0}{1}".format(values, self.option_strings[1][2:].capitalize())

        try:
            getattr(namespace, self.dest).append(values)
        except AttributeError:
            setattr(namespace, self.dest, [values])

parser = argparse.ArgumentParser(description="Sigma")

parser.add_argument("-s", "--stack",
        nargs="+",
        type=str,
        choices=sigma.config.CREATORS + sigma.config.FILTERS + sigma.config.MODIFIERS,
        help="dataflow stack")

parser.add_argument("-d", "--data",
        nargs="?",
        default=sigma.config.DATA_FILENAME,
        type=argparse.FileType("r"),
        help="data filename")

args = parser.parse_args()

print(args)

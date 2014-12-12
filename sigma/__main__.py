import sigma.service


class Terminal(sigma.service.ITerminal):

    def execute(self):
        print(self._args.infile.read())


def main():
    terminal = Terminal()


if __name__ == "__main__":
    main()

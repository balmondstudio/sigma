import sigma.adapter


def main():
    input_adapter = sigma.adapter.TerminalInputAdapter()
    output_adapter = sigma.adapter.TemrinalOutputAdapter()

    input_adapter.execute(output_adapter)


if __name__ == "__main__":
    main()

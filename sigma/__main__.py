import sigma.config
import sigma.adapter


def main():
    command = "sigma.adapter.{0}InputAdapter()".format(sigma.config.INPUT_SERVICE)
    exec(command)


if __name__ == "__main__":
    main()

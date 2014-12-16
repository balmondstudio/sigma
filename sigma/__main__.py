import sigma.config
import sigma.adapter


def main():
    command = "sigma.adapter.{0}InputAdapter()".format(sigma.config.INPUT_SERVICE)
    exec(command)

    #exec("sigma.adapter.Test()")


if __name__ == "__main__":
    main()

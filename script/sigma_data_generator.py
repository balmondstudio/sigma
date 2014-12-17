import json

import sigma.config


def generate_data():
        x_range = range(1, 10)
        y_range = range(1, 10)
        z_range = range(1, 10)

        depth = []
        for z in z_range:
            height = []
            for y in y_range:
                width = []
                for x in x_range:
                    width.append(x * y * z)
                height.append(width)
            depth.append(height)
        return depth


def main():
    with open(sigma.config.DATA_FILENAME, "w") as outfile:
        data = generate_data()
        json.dump(data, outfile)


if __name__ == "__main__":
    main()

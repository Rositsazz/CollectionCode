from pandas import Panda
from social import PandaSocialNetwork


def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")

    for panda in [ivo, rado, tony]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)

    network.connection_level(ivo, rado) == 1  # True
    network.connection_level(ivo, tony) == 2  # True

    network.how_many_gender_in_network(1, rado, "female") == 1  # True
    # print(network)
    # network.save("json.txt")
    network.load("json.txt")


if __name__ == '__main__':
    main()

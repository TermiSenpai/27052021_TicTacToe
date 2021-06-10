#!/usr/bin/python3

# import class Game from Game.py
from Game import Game


def main():
    answer = ["Y"]

    while True:
        Game()

        user = input("\n\tDesea volver a jugar? [Y]es or [N]o ")

        user = user.upper()

        if user not in answer:
            return False


main()

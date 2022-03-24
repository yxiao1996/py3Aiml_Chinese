import Kernel


def main():
    one_piece = Kernel.Kernel()
    one_piece.learn("one-piece.aiml")
    one_piece.learn("one-piece-food.aiml")

    while True:
        print(one_piece.respond(input('>>')))


if __name__ == "__main__":
    main()
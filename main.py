from rock import Result


def Play():
    print("\n")
    first_player = int(input("1)rock\n2)paper\n3)scissors\nFirst PLayer choose:"))
    print("\n")
    second_player = int(input("1)rock\n2)paper\n3)scissors\nSecond PLayer choose:"))
    print("\n")
    print(Result(first_player, second_player))
    answer = input("Write e to exit : ")
    if answer == "e" or answer == "E" :
        exit()
    else:
        Play()

Play()



def Result(first_player , second_player):
    if first_player == 1:
        if second_player == 2:
            return "Second player wins"
        elif second_player == 3:
            return "First player wins"
        else :
            return "TIE"
    elif first_player == 2:
        if second_player == 1:
            return "First player wins"
        elif second_player == 3:
            return "Second player wins"
        else :
            return "TIE"
    else :
        if second_player == 1:
            return "Second player wins"
        elif second_player == 2:
            return "First player wins"
        else :
            return "TIE"
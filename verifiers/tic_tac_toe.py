def verify_win(board):
    if (board['7'] == board['8'] ==
            board['9']) and (board['7'] != " "):
        return True

    elif (board['4'] == board['5'] ==
          board['6']) and (board['4'] != " "):
        return True

    elif (board['1'] == board['2'] ==
          board['3']) and (board['1'] != " "):
        return True

    elif (board['7'] == board['4'] ==
          board['1']) and (board['7'] != " "):
        return True

    elif (board['8'] == board['5'] ==
          board['2']) and (board['8'] != " "):
        return True

    elif (board['9'] == board['6'] ==
          board['3']) and (board['9'] != " "):
        return True

    elif (board['1'] == board['5'] ==
          board['9']) and (board['1'] != " "):
        return True

    elif (board['7'] == board['5'] ==
          board['3']) and (board['7'] != " "):
        return True

    return False

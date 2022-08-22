from show.tic_tac_toe import printBoard
from verifiers.tic_tac_toe import verify_win

from random import choice


board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

choiceds = []

def random_choice(excluded_choices):
    choices = [k for k in board.keys() if k not in excluded_choices]
    return choice(choices)


def run():
    choices = 0
    turn = 'X'
    while choices < 9:

        print(f"A vez é do {turn}")
        printBoard(board)
        
        if turn == 'X':
            choice = input("Informe qual casa você quer marcar: ")

            if not (choice in board.keys()):
                print('Escolha uma opção válida')
                continue

            if board[choice] != " ":
                print('Escolha uma opção válida')
                continue
        
        else:
            choice = random_choice(choiceds)
        
        board[choice] = turn
        choiceds.append(choice)
            

        if verify_win(board):
            printBoard(board)
            print(f'O jogador {turn} ganhou')
            break

        choices += 1

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        printBoard(board)
        print("Deu velha")


if __name__ == "__main__":
    run()

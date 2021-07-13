from show.tic_tac_toe import printBoard
from verifiers.tic_tac_toe import verify_win
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def run():
    choices = 0
    turn = 'X'
    while choices < 9:

        print(f"A vez é do {turn}")
        printBoard(board)

        choice = input("Informe qual casa você quer marcar: ")

        if not (choice in board.keys()):
            print('Escolha uma opção válida')
            continue

        if board[choice] != " ":
            print('Escolha uma opção válida')
            continue

        board[choice] = turn

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

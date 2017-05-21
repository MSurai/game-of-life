import os
import random


def main():
    board = initialize_board(5, 5)


def initialize_board(width, height):
    board = [[False for i in range(width)] for j in range(height)]
    return board


def fill_board_randomly(board):
    width = len(board[0])
    height = len(board)

    for y in range(height):
        for x in range(width):
            board[y][x] = bool(random.randint(0, 1))


def count_neighbors(x, y, board):
    width = len(board[0])
    height = len(board)
    counter = 0

    for yDelta in [-1, 0, 1]:
        for xDelta in [-1, 0, 1]:
            if not yDelta == xDelta == 0 and 0 <= y + yDelta < height and 0 <= x + xDelta < width:
                counter += int(board[y + yDelta][x + xDelta])

    return counter


def print_board(board):
    for row in board:
        for item in row:
            print('o ' if item == True else '. ', end='')
        print()


def clear_screen():
    os.system('clear')

if __name__ == '__main__':
    main()

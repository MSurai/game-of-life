def main():
    board = initialize_board(5, 5)


def initialize_board(width, height):
    board = [[False for i in range(width)] for j in range(height)]
    return board


def count_neighbors(x, y, board):
    width = len(board[0])
    height = len(board)
    counter = 0

    for yDelta in [-1, 0, 1]:
        for xDelta in [-1, 0, 1]:
            if not yDelta == xDelta == 0 and 0 <= y + yDelta < height and 0 <= x + xDelta < width:
                counter += int(board[y + yDelta][x + xDelta])

    return counter


if __name__ == '__main__':
    main()

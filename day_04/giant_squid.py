"""
Day 4: Giant Squid
https://adventofcode.com/2021/day/4
"""

def load_input(filepath):
    with open(filepath) as f:
        lines = [line for line in f.readlines()]
    
        drawn = [int(word) for word in lines[0].split(',')]

        boards = []
        for line in lines[1:]:
            if (line == '\n') or (line == ' '):
                board = []
            else:
                board.extend(int(word) for word in line.split(' ') if word != '')
                if len(board) == 25:
                    boards.append([{'value': item, 'marked': False} for item in board])
    return drawn, boards


def mark_cells(number, board):
    for cell in board:
        if cell['value'] == number:
            cell['marked'] = True


def winning_row(board):
    for i in range(5):
        row = board[i:i+5]
        if all(cell['marked'] for cell in row):
            return True
    return False


def winning_column(board):
    for i in range(5):
        indices = [j+i for j in range(0,25,5)]
        col = [board[i] for i in indices]
        if all(cell['marked'] for cell in col):
            return True
    return False


def sum_unmarked_numbers(board):
    return sum(cell['value'] for cell in board if cell['marked'] is False)


def play(drawn, boards):
    # One drawn number at a time
    for number in drawn:
        # Mark cells with drawn value
        for board in boards:
            mark_cells(number, board)
        # Check if there is a winning row or column
        for board in boards: 
            if winning_row(board) or winning_column(board):
                sum_unmarked = sum_unmarked_numbers(board)
                print(f'Sum, number: {sum_unmarked}, {number}')
                return sum_unmarked * number


if __name__ == '__main__':
    # 1
    drawn, boards = load_input('day_04/input.txt')
    score = play(drawn, boards)
    print(f'The winning score is {score}')


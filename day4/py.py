import numpy as np

class BingoBoard:
    def __init__(self):
        self.board = np.zeros((5,5))
        self.marked = np.zeros((5,5), dtype=bool)
    
    def fill_row(self, idx, list_row):
        self.board[idx, :] = list_row

    def check_bingo(self):
        for i in range(5):
            if self.marked[:, i].sum() == 5 or self.marked[i, :].sum() == 5:
                return True
        
        return False

boards = []
with open('input.txt') as f:
    draws = [int(i) for i in f.readline().strip().split(",")]
    ctr = 0
    for line in f:
        if line != "\n":
            line = [int(i) for i in line.strip().split(" ") if i.isnumeric()]
            if (ctr % 5 == 0):
                boards.append(BingoBoard())
            
            boards[-1].fill_row(ctr % 5, line)
            ctr += 1

for draw in draws:
    winning_boards = []
    for b in boards:
        coordinate = np.where(b.board == draw)

        if coordinate[0].size > 0:
            b.marked[coordinate[0], coordinate[1]] = 1

        # Check for win
        if b.check_bingo():
            winning_boards.append(b)

    # Check all winning boards
    if len(winning_boards) > 0:
        sums = []
        for wb in winning_boards:
            sum = wb.board[np.invert(wb.marked)].sum()
            sums.append(sum)

            # Remove from boards
            boards.remove(wb)
            
        if not boards:
            print(min(sums) * draw)

        # print(max(sums) * draw)
        # break


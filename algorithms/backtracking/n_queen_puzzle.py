def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 1:
                return False
        return True
    
    def solve(row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0
        return False
    
    if solve(0):
        for row in board:
            print(["Q" if cell == 1 else "." for cell in row])
    else:
        print("No solution exists")

if __name__ == "__main__":
    n = 4
    print(f"Solving {n}-Queens:")
    solve_n_queens(n)
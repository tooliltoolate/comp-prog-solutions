reserved: list[tuple[int, int]] = list()
for row in range(8):
    line = input()
    for column in range(8):
        if line[column] == '*': reserved.append((row, column))

def solve() -> int:
    counter = 0
    free_columns = [True] * 8
    free_add_diags = [True] * 16
    free_minus_diags = [True] * 16
    def backtrack(row: int):
        nonlocal counter
        if row == 8:
            counter += 1
            return
        for column in range(8):
            if free_columns[column] and free_add_diags[row + column] and free_minus_diags[row - column + 7] and ((row, column) not in reserved):
                free_columns[column] = False
                free_add_diags[row + column] = False
                free_minus_diags[row - column + 7] = False
                backtrack(row + 1)
                free_columns[column] = True
                free_add_diags[row + column] = True
                free_minus_diags[row - column + 7] = True

    backtrack(0)
    return counter
print(solve())

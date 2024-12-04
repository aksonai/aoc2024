# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a
# device and pushes the only button on it. After a brief flash, you recognize
# the interior of the Ceres monitoring station!

# As the search for the Chief continues, a small Elf who lives on the station
# tugs on your shirt; she'd like to know if you could help her with her word
# search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, written
# backwards, or even overlapping other words. It's a little unusual, though,
# as you don't merely need to find one instance of XMAS - you need to find all
# of them. Here are a few ways XMAS might appear, where irrelevant characters
# have been replaced with .:

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word
# search again, but where letters not involved in any XMAS have been replaced
# with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?


def check_horizontal(row: int, col: int, matrix: list[str]) -> int:
    count = 0
    left_to_right = matrix[row][col : col + 4]
    if left_to_right == "XMAS":
        count += 1
    right_to_left = matrix[row][col - 3 : col + 1]
    if right_to_left == "SAMX":
        count += 1
    return count


def check_vertical(row: int, col: int, matrix: list[str]) -> int:
    count = 0
    if row < len(matrix) - 3:
        top_to_bottom = (
            matrix[row][col]
            + matrix[row + 1][col]
            + matrix[row + 2][col]
            + matrix[row + 3][col]
        )
        if top_to_bottom == "XMAS":
            count += 1
    if row > 2:
        bottom_to_top = (
            matrix[row][col]
            + matrix[row - 1][col]
            + matrix[row - 2][col]
            + matrix[row - 3][col]
        )
        if bottom_to_top == "XMAS":
            count += 1
    return count


def check_diagonal(row: int, col: int, matrix: list[str]) -> int:
    count = 0
    if row < len(matrix) - 3 and col < len(matrix[row]) - 3:
        top_left_to_bottom_right = (
            matrix[row][col]
            + matrix[row + 1][col + 1]
            + matrix[row + 2][col + 2]
            + matrix[row + 3][col + 3]
        )
        if top_left_to_bottom_right == "XMAS":
            count += 1
    if row > 2 and col > 2:
        bottom_right_to_top_left = (
            matrix[row][col]
            + matrix[row - 1][col - 1]
            + matrix[row - 2][col - 2]
            + matrix[row - 3][col - 3]
        )
        if bottom_right_to_top_left == "XMAS":
            count += 1

    if row < len(matrix) - 3 and col > 2:
        top_right_to_bottom_left = (
            matrix[row][col]
            + matrix[row + 1][col - 1]
            + matrix[row + 2][col - 2]
            + matrix[row + 3][col - 3]
        )
        if top_right_to_bottom_left == "XMAS":
            count += 1
    if row > 2 and col < len(matrix[row]) - 3:
        bottom_left_to_top_right = (
            matrix[row][col]
            + matrix[row - 1][col + 1]
            + matrix[row - 2][col + 2]
            + matrix[row - 3][col + 3]
        )
        if bottom_left_to_top_right == "XMAS":
            count += 1
    return count


matrix = []
f = open("input.txt", "r")
for line in f:
    matrix.append(line.strip())
f.close()

total = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "X":
            total += check_horizontal(row, col, matrix)
            total += check_vertical(row, col, matrix)
            total += check_diagonal(row, col, matrix)

print(total)

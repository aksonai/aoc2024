# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that this
# isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed
# to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram.
# Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have
# been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.

# Flip the word search from the instructions back over to the word search side
# and try again. How many times does an X-MAS appear?


def check_diagonal(row: int, col: int, matrix: list[str]) -> int:
    count = 0
    top_left_to_bottom_right = (
        matrix[row - 1][col - 1] + matrix[row][col] + matrix[row + 1][col + 1]
    )
    top_right_to_bottom_left = (
        matrix[row - 1][col + 1] + matrix[row][col] + matrix[row + 1][col - 1]
    )
    if (top_left_to_bottom_right == "MAS" or top_left_to_bottom_right == "SAM") and (
        top_right_to_bottom_left == "MAS" or top_right_to_bottom_left == "SAM"
    ):
        count += 1
    return count


matrix = []
f = open("input.txt", "r")
for line in f:
    l = line.strip()
    matrix.append("." + l + ".")
f.close()
matrix.insert(0, "." * len(matrix[0]))
matrix.append("." * len(matrix[0]))

total = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            total += check_diagonal(row, col, matrix)

print(total)

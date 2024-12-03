# --- Part Two ---
# The engineers are surprised by the low number of safe reports until they
# realize they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor
# safety systems tolerate a single bad level in what would otherwise be a
# safe report. It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level
# from an unsafe report would make it safe, the report instead counts as
# safe.

# More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener
# can remove a single level from unsafe reports. How many reports are now
# safe?


def check_sign(num: int) -> int:
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def is_safe(report: list[int]) -> int:
    first_diff = check_sign(report[1] - report[0])
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) > 3 or diff == 0 or check_sign(diff) != first_diff:
            return 0
    return 1


def is_safe_with_dampener(report: list[int]) -> int:
    if is_safe(report):
        return 1
    for i in range(len(report)):
        report_copy = report.copy()
        report_copy.pop(i)
        if is_safe(report_copy):
            return 1
    return 0


count = 0
f = open("input.txt", "r")
for line in f:
    report = [int(x) for x in line.strip().split()]
    count += is_safe_with_dampener(report)
f.close()
print(count)

# --- Part Two ---

# While the Elves get to work printing the correctly-ordered updates, you have a
# little time to fix the rest of them.

# For each of the incorrectly-ordered updates, use the page ordering rules to put
# the page numbers in the right order. For the above example, here are the three
# incorrectly-ordered updates and their correct orderings:

#     75,97,47,61,53 becomes 97,75,47,61,53.
#     61,13,29 becomes 61,29,13.
#     97,13,75,29,47 becomes 97,75,47,29,13.

# After taking only the incorrectly-ordered updates and ordering them correctly,
# their middle page numbers are 47, 29, and 47. Adding these together produces 123.

# Find the updates which are not in the correct order. What do you get if you add
# up the middle page numbers after correctly ordering just those updates?


def check_ordering(pages: list[int], rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[0]) > pages.index(rule[1]):
                return False
    return True


rules: list[tuple[int, int]] = []
pages_list: list[list[int]] = []
f = open("test.txt", "r")
for line in f:
    stripped = line.strip()
    if "|" in stripped:
        rules.append(tuple([int(p) for p in line.strip().split("|")]))
    if "," in stripped:
        pages_list.append([int(p) for p in line.strip().split(",")])
f.close()

total = 0
for pages in pages_list:
    if not check_ordering(pages, rules):
        print(pages)

print(total)

# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

# For right alignment of words while printing letters
colWidth = [0] * len(tableData)

# Calculating max width for each list
for i in range(len(tableData)):
    colWidth[i] = len(max(tableData[i], key=len))

# Printing table
for j in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][j].rjust(colWidth[i]) + " ", end="")
    print()

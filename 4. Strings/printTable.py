tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidth = [0] * len(data)

    # To calculate the column width
    for i in range(len(data)):
        for datom in data[i]:
            length = len(datom)
            if length > colWidth[i]:
                colWidth[i] = length
    
    # To print table 
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(colWidth[j]), end=" ")
        print()

printTable(tableData)
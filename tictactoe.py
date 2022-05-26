#noughts and crosses

#0 is nothing, 1 is x, 2 is o
gameboard=[
    [1,1,2],
    [0,0,2],
    [0,0,2]
    ]

def checkwin(board):
    #rows
    for k in range(0,2):
        row=[board[k][i] for i in range(0,2)]
        if len(set(row))==1:
            if row[0]==1:
                return(1)
            elif row[0]==2:
                return(2)
    
    
    #columns
    for k in range(0,2):
        column=[board[i][k] for i in range(0,2)]
        if len(set(column))==1:
            if column[0]==1:
                return(1)
            elif column[0]==2:
                return(2)
    
print(checkwin(gameboard))

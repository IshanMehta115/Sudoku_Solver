grid = [[3,0,0,0,0,9,0,1,0],
        [0,6,0,0,0,0,2,0,4],
        [0,0,4,0,5,0,0,0,0],
        [0,0,0,1,0,0,7,8,0],
        [0,0,0,2,8,3,0,0,0],
        [0,1,8,0,0,5,0,0,0],
        [0,0,0,0,2,0,9,0,0],
        [2,0,1,0,0,0,0,5,0],
        [0,4,0,6,0,0,0,0,8]]


def print_grid():
    print("Sudoku grid")
    global grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()

def possible(i,j,n):
    for z in range(9):
        if(grid[i][z]==n):
            return False
    for z in range(9):
        if(grid[z][j]==n):
            return False
    for ti in range(9):
        for tj in range(9):
            if(ti//3==i//3 and tj//3== j//3 and grid[ti][tj]==n):
                return False
    return True

def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if(grid[i][j]==0):
                for n in range(1,10):
                    if(possible(i,j,n)):
                        grid[i][j]=n
                        solve()
                        grid[i][j]=0
                return
    print_grid()

solve()
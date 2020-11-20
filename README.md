# Sudoku_Solver
A python3 program that solves a sudoku using backtracking

grid[][]
        It is list of lists of dimensions 9x9 that stores the initial values of the unsolved sudoku grid.
        Empty spaces are filled with a 0.
        
print_grid()
        This function prints the sudoku grid in a 9x9 matrix form.
        It does not return anything.
        
possible(i,j,n):
        It checks and return True if it is possible to put the number n at the position i,j (i.e.  if grid[i][j]=n is possible)  ,  False otherwise.
        First it checks for same number n in the row and columns.
        Then it checks for the same number n in the same 3x3 sub block in which i,j exists. 
       
void solve()
        This is a recursive backtracking function that finds an empty slot , then finds a possible entry for that slot then fills the slot with this possible value and calls               itself to solve the rest of the grid.If it doesnt find a solution then it tries again by filling a different possible entry to the empty slot.
        If it doesnt find any solution for any possible entry to a slot then the answer doesnt exist or the initial sudoku grid is incorrect.
        It does not return anything.

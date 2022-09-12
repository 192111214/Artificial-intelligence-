import time
n = 8
current_solution = [0 for x in range (n)]
solution = []

def isSafe(testrow,testcolumn):
    if testrow== 0:
        return True

    for row in range(0,testrow):
        if(testcolumn == current_solution[row]):
            return False

        if( abs(testrow - row ) == abs(testcolumn - current_solution[row])):
            return False
    return True

def placeQueen(row):
    global current_solution,solution,n

    for col in range(n):
        if not isSafe(row,col):
            continue
        else:
            current_solution[row] = col
            if row == (n-1):
                solution.append(current_solution.copy())
                print("solution number ", len(solution), current_solution )
            else:
                placeQueen(row+1)

print("solving for "+ str(n) + " Queens")

time.sleep(2)
placeQueen(0)

print(len(solution), " solution found")
for solutions in solution:
    print(solutions)

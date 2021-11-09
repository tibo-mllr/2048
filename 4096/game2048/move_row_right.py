from move_row_left import move_row_left_vBilal

def move_row_right_vBilal(l):
    leftl = move_row_left_vBilal(l)
    newl = []
    for i in range(len(l)):
        x=len(l)-1
        if leftl[x-i] != 0:
            newl = [leftl[x-i]] + newl
    finallist = []
    for i in range(len(l)-len(newl)):
        finallist = finallist + [0]
    finallist = finallist + newl
    return finallist
    

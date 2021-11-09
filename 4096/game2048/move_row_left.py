


def move_row_left_vBilal(l):
    newl = []
    for i in range(len(l)):
        if l[i] != 0 :
            newl = newl + [l[i]]
    comp_newl = []
    for i in range(len(l)-len(newl)):
        comp_newl = comp_newl + [0]
    for i in range(len(newl)-1):
        if newl[i] == newl[i+1]:
            newl[i] = 2*newl[i]
            newl[i+1] =  0
    newl = newl + comp_newl
    newl2 =[]
    for i in range(len(newl)):
        if newl[i] != 0 :
            newl2 = newl2 + [newl[i]]
    comp_newl2 = []
    for i in range(len(newl)-len(newl2)):
        comp_newl2 = comp_newl2 + [0]
    return newl2 + comp_newl2



    if a in positions and check_small(m,position,a)==True:
        print()
        neighbours+=[m[position[0]-1][position[1]-1]]

    if b in positions and check_small(m,position,b)==True:
        neighbours+=[m[position[0]-1][position[1]]]

    if c in positions and check_small(m,position,c)==True:
        neighbours+=[m[position[0]-1][position[1]+1]]

    if d in positions and check_small(m,position,d)==True:
        neighbours+=[m[position[0]][position[1]-1]]

    if e in positions and check_small(m,position,e)==True:
        #print("blaa")
        neighbours+=[m[position[0]][position[1]+1]]

    if f in positions and check_small(m,position,f)==True:
        neighbours+=[m[position[0]+1][position[1]-1]]

    if g in positions and check_small(m,position,g)==True:
        neighbours+=[m[position[0]+1][position[1]]]

    if h in positions and check_small(m,position,h)==True:
        neighbours+=[m[position[0]+1][position[1]+1]]

    return neighbours

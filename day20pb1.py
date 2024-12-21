import sys
sys.setrecursionlimit(10000)

INFINITY = 1e100

class Grid :
    def __init__(self,g,s,e) :
        self.g = g
        self.s = s
        self.e = e

def read_file() :
    g = []
    with open("input.txt","r") as input :
        for j,line in enumerate(input) :
            l = []
            for i,c in enumerate(line) :
                if c in "#." :
                    l.append(c)
                elif c == "S" :
                    start = (i,j)
                    l.append(".")
                elif c == "E" :
                    l.append(".")
                    end = (i,j)
            g.append(l)
    return Grid(g,start,end)

def parcours(grid) :
    n = len(grid.g)
    m = len(grid.g[0])
    cost = {}
    preds = {}
    preds[grid.s] = grid.s
    for i in range(m) :
        for j in range(n) :
            cost[(i,j)] = INFINITY
    cost[grid.s] = 0
    todo = [grid.s]
    found = False
    while todo != [] and not found :
        imin = 0
        for i,s in enumerate(todo) :
            if cost[s] < cost[todo[imin]] :
                imin = i
        i,j = todo.pop(i)
        if grid.g[j+1][i] == '.' and cost[(i,j+1)] > cost[(i,j)] + 1 :
            todo.append((i,j+1))
            preds[(i,j+1)] = (i,j)
            cost[(i,j+1)] = cost[(i,j)] + 1
        if grid.g[j-1][i] == '.' and cost[(i,j-1)] > cost[(i,j)] + 1 :
            todo.append((i,j-1))
            preds[(i,j-1)] = (i,j)
            cost[(i,j-1)] = cost[(i,j)] + 1
        if grid.g[j][i+1] == '.' and cost[(i+1,j)] > cost[(i,j)] + 1 :
            todo.append((i+1,j))
            preds[(i+1,j)] = (i,j)
            cost[(i+1,j)] = cost[(i,j)] + 1
        if grid.g[j][i-1] == '.' and cost[(i-1,j)] > cost[(i,j)] + 1 :
            todo.append((i-1,j))
            preds[(i-1,j)] = (i,j)
            cost[(i-1,j)] = cost[(i,j)] + 1
    def predsl(s,set) :
        if preds[s] == s :
            return {s} | set
        return predsl(preds[s],set | {s})
    print(f"c : {cost[grid.e]}")
    return cost[grid.e],predsl(grid.e,set()),cost



if __name__=="__main__" :
    grid = read_file()
    n = len(grid.g)
    m = len(grid.g[0])
    ref,predsl,cost = parcours(grid)
    cpt = {}
    for i,j in predsl :
        if i >= 2 and grid.g[j][i-2] == "." and cost[(i-2,j)] - cost[(i,j)] > 2 :
            k = cost[(i-2,j)] - cost[(i,j)] - 2
            if k in cpt :
                cpt[k] += 1
            else :
                cpt[k] = 1
        if i < m-2 and grid.g[j][i+2] == '.' and cost[(i+2,j)] - cost[(i,j)] > 2:
            k = cost[(i+2,j)] - cost[(i,j)] - 2
            if k in cpt :
                cpt[k] += 1
            else :
                cpt[k] = 1
        if j >= 2 and grid.g[j-2][i] == "." and cost[(i,j-2)] - cost[(i,j)] > 2 :
            k = cost[(i,j-2)] - cost[(i,j)] - 2
            if k in cpt :
                cpt[k] += 1
            else :
                cpt[k] = 1
        if j < n-2 and grid.g[j+2][i] == "." and cost[(i,j+2)] - cost[(i,j)] > 2 :
            k = cost[(i,j+2)] - cost[(i,j)] - 2
            if k in cpt :
                cpt[k] += 1
            else :
                cpt[k] = 1



    # cpt = {}
    # for i in range(ref) :
    #     if i%100 == 0 :
    #         print(f"{round(i*100/ref,1)}%")
    #     k = cheat_parcours(grid,i)
    #     if k < ref :
    #         shrtct = ref-k
    #         if shrtct in cpt :
    #             cpt[shrtct] += 1
    #         else :
                # cpt[shrtct] = 1
    tot = 0
    print()
    for x in sorted(list(cpt.keys())) :
        if x >= 100 :
            tot += cpt[x]
        print(f"{x} : {cpt[x]}")
    print()


    print(f"tot : {tot}")

# 9268
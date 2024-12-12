def read_file() :
    r = []
    with open("input.txt","r") as input :
        for line in input :
            l = []
            for c in line :
                if c != "\n":
                    l.append(int(c))
            r.append(l)
    return r

def n_path_from(i : int,j : int,prev : int, r : list) -> int :
    n = len(r)
    m = len(r[0])
    if i<0 or j<0 or i>=n or j >=m :
        return 0
    act = r[i][j]
    if act != prev + 1 :
        return 0
    if act == 9 :
        return 1
    
    return n_path_from(i - 1, j, act, r) + n_path_from(i + 1, j, act, r) + n_path_from(i, j - 1, act, r) + n_path_from(i, j + 1, act, r)

def n_path_from_0(i : int,j : int,r : list) -> int :
    return n_path_from(i-1,j,0,r) + n_path_from(i+1,j,0,r) + n_path_from(i,j-1,0,r) + n_path_from(i,j+1,0,r)




def main() :
    r = read_file()
    c = 0
    for i,line in enumerate(r) :
        for j,n in enumerate(line) :
            if n == 0 :
                c += n_9_from_0(i,j,r)
    print(c)


if __name__ == "__main__" :
    main()

def readfile() :
    grid = []
    chars = []
    with open("input.txt","r") as input :
        for line in input :
            for c in line[:-1] :
                if not c in chars and c!= '.' :
                    chars.append(c)
            grid.append(line[:-1])
    return grid,chars

def print_grid(grid) :
    for l in grid :
        print(l)

def empty(ref) :
    e = []
    for i in range(len(ref)):
        e.append(["."] * len(ref[0]))
    return e


def antinodes(c : str, antennas, nodes) :
    antennes_c = []
    for y,l in enumerate(antennas) :
        for x,ltr in enumerate(l) :
            if ltr == c :
                antennes_c.append((x,y))
    
    paires = [(a,b) for a in antennes_c for b in antennes_c if a != b]

    for paire in paires :
        (xa,ya),(xb,yb) = paire
        xv,yv = (xb - xa),(yb-ya)
        nx1,ny1 = (xb+xv),(yb+yv)
        nx2,ny2 = (xa-xv),(ya-yv)
        if 0 <= nx1 < len(antennas[0]) and 0 <= ny1 < len(antennas) :
            nodes[ny1][nx1] = 'X'
        if 0 <= nx2 < len(antennas[0]) and 0 <= ny2 < len(antennas) :
            nodes[ny2][nx2] = 'X'
        
    
    return nodes


def nb_nodes(nodes) :
    cpt = 0
    for l in nodes :
        for c in l :
            if c == 'X' :
                cpt +=1
    return cpt








def main() :
    antennas_grid,chars = readfile()
    antinodes_grid = empty(antennas_grid)

    for char in chars :
        antinodes_grid = antinodes(char,antennas_grid,antinodes_grid)
    
    # for l in antinodes_grid :
    #     for c in l :
    #         print(c,end="")
    #     print()

    print(nb_nodes(antinodes_grid))
    


if __name__ == "__main__" :
    main()
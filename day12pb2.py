class Region :
    def __init__(self,c : str,i : int, j : int) :
        self.c = c
        self.s = [(i,j)]
        
    def __str__(self) :
        return f"{self.c}, {self.s}"

    def aire(self) :
        return len(self.s)
    
    def perim(self) :
        global map
        p = 0
        n = len(map)
        m = len(map[0])
        for case in self.s :
            i,j = case
            if i == 0 or map[i-1][j] != self.c :
                p += 1
            if j == 0 or map[i][j-1] != self.c :
                p += 1
            if i == n-1 or map[i+1][j] != self.c :
                p+=1
            if j == m-1 or map[i][j+1] != self.c:
                p+=1
        return p

    def n_sides(self) :
        global map
        n_coins = 0
        n = len(map)
        m = len(map)
        for i,j in self.s :
            # haut gauche intérieur
            if (i-1,j-1) not in self.s and (i-1,j) in self.s and (i,j-1) in self.s :
                n_coins += 1
            # haut gauche extérieur : 
            elif (i-1,j) not in self.s  and (i,j-1) not in self.s :
                n_coins +=1
            
            
            # haut droit intérieur
            if (i-1,j+1) not in self.s and (i-1,j) in self.s and (i,j+1) in self.s :
                n_coins += 1
            # haut droit extérieur
            elif (i-1,j) not in self.s and (i,j+1) not in self.s :
                n_coins += 1
            
            # bas gauche intérieur
            if (i+1,j-1) not in self.s and (i+1,j) in self.s and (i,j-1) in self.s :
                n_coins += 1
            # bas gauche extérieur : 
            elif self.s and (i+1,j) not in self.s and (i,j-1) not in self.s :
                n_coins +=1
            
            # bas droit intérieur
            if (i+1,j+1) not in self.s and (i+1,j) in self.s and (i,j+1) in self.s :
                n_coins += 1
            # bas droit extérieur : 
            elif (i+1,j) not in self.s and (i,j+1) not in self.s :
                n_coins +=1
            
        return n_coins

    def price(self) :
        a = self.aire()
        
        if a != 0 :
            p = self.n_sides()
            # print(f"{self.c} : a = {a} | sides = {p}          t = {a*p}")
            return a * p
        return 0

def read_file() :
    r = []
    with open("input.txt","r") as input :
        for line in input :
            l = []
            for c in line :
                if c != "\n" :
                    l.append(c)
            r.append(l)
    # print(r)
    return r

def exp_reg(c : str,i : int, j : int, map : list) -> list :
    global seen
    if (i,j) in seen :
        return []
    seen.add((i,j))
    l = [(i,j)]
    # print(f"Actual {c}:({i},{j})")
    n = len(map)
    m = len(map[0])
    if i > 0 and (i-1,j) not in seen and map[i-1][j] == c :
        # print("in1")
        l += exp_reg(c,i-1,j,map)
    if j > 0 and (i,j-1) not in seen and map[i][j-1] == c :
        # print("in2")
        l += exp_reg(c,i,j-1,map)
    if i < n-1 and (i+1,j) not in seen and map[i+1][j] == c :
        # print("in3")
        l += exp_reg(c,i+1,j,map)
    if j < m - 1 and (i,j+1) not in seen and map[i][j+1] == c :
        # print("in4")
        l += exp_reg(c,i,j+1,map)
    # print(l)
    return l



def map_regions(map : list) -> dict :
    # regions = [region1,region2...]
    regions = []
    d_i = {}
    global seen
    seen = set()
    for i,l in enumerate(map) :
        for j,c in enumerate(l) :
            if not (i,j) in seen :
                # print(c)
                region = Region(c,i,j)
                l  = exp_reg(c,i,j,map)
                region.s = l
                regions.append(region)
            
    print(f"n regions : {len(regions)}")
    return regions


            
def main() :
    global map
    map = read_file()
    regions = map_regions(map)

    tot = 0
    for region in regions :
        if region.c != "0" :
            tot += region.price()
    print(tot)
    

if __name__ == "__main__" :
    main()
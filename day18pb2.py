import pyxel as px
import re
motif = r"(\d+)\,(\d+)"
N = 71
INFINITY = 1e100

def read_file() :
    l = []
    with open("input.txt","r") as input :
        for line in input :
            x,y = re.findall(motif,line)[0]
            x,y = int(x),int(y)
            l.append((x,y))
    return l

class Grid :
    def __init__(self,l,n = N) :
        self.n = n
        self.g = [['.' for _ in range(n)] for _ in range(n)]
        self.l = l
        self.start = (0,0)
        self.exit = (n-1,n-1)
    
    def step(self) :
        if self.l != [] :
            x,y = self.l.pop(0)
            self.g[y][x] = "#"
            return(x,y)
    
    def draw(self) :
        for l in self.g :
            print("".join(l))

def parcours(grid) :
    x_s,y_s = grid.start
    n = grid.n
    x_e,y_e = grid.exit
    todo = [(x_s,y_s)]
    cost = [[INFINITY for _ in range(n)] for _ in range(n)]
    cost[y_s][x_s] = 0
    while todo != [] :
        # grid.fall()
        x,y = todo.pop(0)
        if x > 0 and grid.g[y][x-1] == '.' and cost[y][x-1] > cost[y][x] + 1 :
            todo.append((x-1,y))
            cost[y][x-1] = cost[y][x] + 1
        if y > 0 and grid.g[y-1][x] == '.' and cost[y-1][x] > cost[y][x] + 1 :
            todo.append((x,y-1))
            cost[y-1][x] = cost[y][x] + 1
        if x < n-1 and grid.g[y][x+1] == '.' and cost[y][x+1] > cost[y][x] + 1 :
            todo.append((x+1,y))
            cost[y][x+1] = cost[y][x] + 1
        if y < n-1 and grid.g[y+1][x] == '.' and cost[y+1][x] > cost[y][x] + 1 :
            todo.append((x,y+1))
            cost[y+1][x] = cost[y][x] + 1
    return cost[y_e][x_e]

CASE = 5
WIDTH = N

class Parcours :
    def __init__(self,grid) :
        n = grid.n
        self.grid = grid
        self.start = grid.start
        self.exit = grid.exit
        self.frame_refresh = 1
        self.n = self.grid.n
        x_s,y_s = grid.start
        self.todo = [(x_s,y_s)]
        self.cost = [[INFINITY for _ in range(n)] for _ in range(n)]
        self.cost[y_s][x_s] = 0
        self.seen = [grid.start]
        self.current = grid.start
        self.b = False
        px.init(N*CASE,N*CASE)
        px.run(self.update,self.draw)
    def update(self) :
        if px.frame_count % self.frame_refresh == 0 :
            if self.todo != [] :
                self.grid.step()
                x,y = self.todo.pop(0)
                self.current = (x,y)
                self.seen.append((x,y))
                if x > 0 and self.grid.g[y][x-1] == '.' and self.cost[y][x-1] > self.cost[y][x] + 1 :
                    self.todo.append((x-1,y))
                    self.cost[y][x-1] = self.cost[y][x] + 1
                if y > 0 and self.grid.g[y-1][x] == '.' and self.cost[y-1][x] > self.cost[y][x] + 1 :
                    self.todo.append((x,y-1))
                    self.cost[y-1][x] = self.cost[y][x] + 1
                if x < self.n-1 and self.grid.g[y][x+1] == '.' and self.cost[y][x+1] > self.cost[y][x] + 1 :
                    self.todo.append((x+1,y))
                    self.cost[y][x+1] = self.cost[y][x] + 1
                if y < self.n-1 and self.grid.g[y+1][x] == '.' and self.cost[y+1][x] > self.cost[y][x] + 1 :
                    self.todo.append((x,y+1))
                    self.cost[y+1][x] = self.cost[y][x] + 1
            else :
                if not self.b :
                    x_e,y_e = self.exit
                    print(self.cost[y_e][x_e])
                    self.b = True
    def draw(self) :
        px.cls(7)
        for j,l in enumerate(self.grid.g) :
            for i,c in enumerate(l) :
                if c == "#" :
                    px.rect(i*CASE,j*CASE,CASE,CASE,0)
        for i,j in self.seen :
            px.rect(i * CASE,j * CASE,CASE,CASE,3)
        for i,j in self.todo :
            px.rect(i * CASE,j * CASE,CASE,CASE,10)
        i,j = self.current
        px.rect(i * CASE,j * CASE,CASE,CASE,8)
        i,j = self.exit
        px.rect(i * CASE,j * CASE,CASE,CASE,1)
            




            

if __name__ == "__main__" :
    affichage = True
    grid = Grid(read_file())
    for _ in range(1024) :
        x,y = grid.step()
    if affichage :
        grid.draw()
        Parcours(grid)
    else :
        while parcours(grid) < INFINITY :
            x,y = grid.step()
        print(x,y)

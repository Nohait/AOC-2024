import pyxel as px
INFINITY = 1e1000


def read_file() :
    r = []
    with open('input.txt','r') as input :
        for j,line in enumerate(input) :
            l = []
            for i,c in enumerate(line) :
                if c == 'S' :
                    start = (i,j,'E')
                    l.append('.')
                elif c == 'E' :
                    exit = (i,j)
                    l.append('.')
                elif c == '#' :
                    l.append('#')
                elif c == '.' :
                    l.append('.')
            r.append(l)
    return r,start,exit

def parcours(r : list, start : tuple, exit : tuple) -> int :
    n = len(r)
    m = len(r[0])
    cost = [[INFINITY for _ in range(m)] for _ in range(n)]
    i,j,_ = start
    cost[j][i] = 0
    td = [start]
    
    def gon(i,j,d) :
        if d == "N" :
            rot = 0
        elif d in "EW" :
            rot = 1000
        else :
            return
        if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1 + rot:
                td.append((i,j-1,'N'))
                cost[j-1][i] = cost[j][i] + 1 + rot
    def gos(i,j,d) :
        if d == "S" :
            rot = 0
        elif d in "EW" :
            rot = 1000
        else :
            return
        if r[j+1][i] == '.' and cost[j+1][i] > cost[j][i] + 1 + rot:
                td.append((i,j+1,'S'))
                cost[j+1][i] = cost[j][i] + 1 + rot
    def goe(i,j,d) :
        if d == "E" :
            rot = 0
        elif d in "NS" :
            rot = 1000
        else :
            return
        if r[j][i+1] == '.' and cost[j][i+1] > cost[j][i] + 1 + rot :
            td.append((i+1,j,"E"))
            cost[j][i+1] = cost[j][i] + 1 + rot
    def gow(i,j,d) :
        if d == "W" :
            rot = 0
        elif d in "NS" :
            rot = 1000
        else :
            return
        if r[j][i-1] == '.' and cost[j][i-1] > cost[j][i] + 1 + rot :
            td.append((i-1,j,"W"))
            cost[j][i-1] = cost[j][i] + 1 + rot

    while td != [] :
        i,j,d = td.pop()
        if d == 'E' :
            goe(i,j,'E')
            gon(i,j,'E')
            gos(i,j,'E')
        elif d == 'W' :
            gow(i,j,'W')
            gon(i,j,'W')
            gos(i,j,'W')
        elif d == 'N' :
            gon(i,j,'N')            
            goe(i,j,'N')            
            gow(i,j,'N')            
        elif d == 'S' :
            gos(i,j,'S')
            goe(i,j,'S')
            gow(i,j,'S')
    ie,je = exit
    return cost[je][ie]

def main():
    r,start,exit = read_file()
    print(parcours(r,start,exit))

WIDTH = 141
HEIGHT = 141
CASE = 5

class Parcours :
    def __init__(self,r,start,end) :
        self.r = r
        self.start = start
        self.exit = end
        self.frame_refresh = 1
        self.td = [start]
        n = len(r)
        m = len(r[0])
        self.cost = [[INFINITY for _ in range(m)] for _ in range(n)]
        i,j,_ = start
        self.cost[j][i] = 0
        self.seen = [(i,j)]
        self.b = False
        self.current = (i,j)
        px.init(WIDTH * CASE, HEIGHT*CASE)
        px.run(self.update,self.draw)
    def update(self) :
        
        if self.td != [] and px.frame_count % self.frame_refresh == 0 :
            i,j,d = self.td.pop(0)
            if not d in "EWNS" :
                print(i,j,"erreur")
            self.current = (i,j)
            self.seen.append((i,j))
            if d == 'E' :
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1001
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1001
            elif d == 'W' :
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1001
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1001
            elif d == 'N' :
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1001
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1001
            elif d == 'S' :
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1001
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1001
        elif self.td == [] and not self.b :
            self.b = True
            ie,je = self.exit
            print(self.cost[je][ie])
    def draw(self) :
        px.cls(7)
        for j,l in enumerate(self.r) :
            for i,c in enumerate(l) :
                if c == '#' :
                    px.rect(i * CASE,j * CASE,CASE,CASE,0)
        for i,j in self.seen :
            px.rect(i * CASE,j * CASE,CASE,CASE,3)
        for i,j,_ in self.td :
            px.rect(i * CASE,j * CASE,CASE,CASE,10)
        i,j = self.current
        px.rect(i * CASE,j * CASE,CASE,CASE,8)
        i,j = self.exit
        px.rect(i * CASE,j * CASE,CASE,CASE,1)






if __name__ == '__main__' :
    affichage = True
    if affichage :
        r,start,end = read_file()
        Parcours(r,start,end)
    else :
        main()
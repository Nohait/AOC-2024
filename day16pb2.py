import pyxel as px
from time import sleep
INFINITY = 1e100


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

WIDTH = 15
HEIGHT = WIDTH
CASE = 5

def draw(r,seen,td,current,exit):
    px.cls(7)
    for j,l in enumerate(r):
        for i,c in enumerate(l) :
            if c == "#" :
                px.rect(i*CASE,j*CASE,CASE,CASE,0)
    for i,j in seen :
        px.rect(i*CASE,j*CASE,CASE,CASE,3)
    for i,j,_ in td :
        px.rect(i*CASE,j*CASE,CASE,CASE,10)
    i,j = current
    px.rect(i*CASE,j*CASE,CASE,CASE,8)
    i,j = exit
    px.rect(i*CASE,j*CASE,CASE,CASE,1)

def draw2(r,seen,td,current,exit) :
    map = [[" " for _ in r] for _ in r[0]]
    for j,l in enumerate(r) :
        for i,c in enumerate(l) :
            if c == "#" :
                map[j][i] = "#"
    for i,j in seen :
        map[j][i] = "."
    for i,j,_ in td :
        map[j][i] = "x"
    i,j = exit
    map[j][i] = "O"
    i,j = current
    map[j][i] = "@"
    for l in map :
        print("".join(l))
    print()



def parcours(r : list, start : tuple, exit : tuple) -> int :
    n = len(r)
    m = len(r[0])
    cost = [[INFINITY for _ in range(m)] for _ in range(n)]
    i_s,j_s,_ = start
    td = [start]
    cost[j_s][i_s] = 0
    preds = [[[] for _ in range(m)] for _ in range(n)]
    seen = [(i_s,j_s)]
    def gon(i,j,d) :
        if d == "N" :
            rot = 0
        elif d in "EW" :
            rot = 1000
        else :
            return
        if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1 + rot:
            td.append((i,j-1,'N'))
            preds[j-1][i] = [(i,j,"N")]
            cost[j-1][i] = cost[j][i] + 1 + rot
        elif r[j-1][i] == '.' and cost[j-1][i] < 1e10:
            if (j-1,i) == (j_s,i_s) :
                return
            _,_,d = preds[j-1][i][0]
            if d == 'N' and cost[j-1][i] == cost[j][i] + 1 :
                preds[j-1][i] += (i,j,'N')
            elif d in 'EW' and cost[j-1][i] == cost[j][i] + 1001 :
                preds[j-1][i] =+ (i,j,'N')
    def gos(i,j,d) :
        if d == "S" :
            rot = 0
        elif d in "EW" :
            rot = 1000
        else :
            return
        if r[j+1][i] == '.' and cost[j+1][i] > cost[j][i] + 1 + rot:
                td.append((i,j+1,'S'))
                preds[j+1][i] = [(i,j,'S')]
                cost[j+1][i] = cost[j][i] + 1 + rot
        elif r[j-1][i] == '.' and cost[j+1][i] < 1e10 :
            if (j+1,i) == (j_s,i_s) :
                return
            _,_,d = preds[j+1][i][0]
            if d == 'S' and cost[j+1][i] == cost[j][i] + 1 :
                preds[j+1][i] += (i,j,'N')
            elif d in 'EW' and cost[j+1][i] == cost[j][i] + 1001 :
                preds[j+1][i] =+ (i,j,'N')
    def goe(i,j,d) :
        if d == "E" :
            rot = 0
        elif d in "NS" :
            rot = 1000
        else :
            return
        if r[j][i+1] == '.' and cost[j][i+1] > cost[j][i] + 1 + rot :
            td.append((i+1,j,"E"))
            preds[j][i+1] = [(i,j,'E')]
            cost[j][i+1] = cost[j][i] + 1 + rot
        elif r[j][i+1] == '.' and cost[j][i+1] < 1e10:
            if (j,i+1) == (j_s,i_s) :
                return
            _,_,d = preds[j][i+1][0]
            if d == 'E' and cost[j][i+1] == cost[j][i] + 1 :
                preds[j][i+1] += (i,j,'N')
            elif d in 'NS' and cost[j][i+1] == cost[j][i] + 1001 :
                preds[j][i+1] =+ (i,j,'N')
    def gow(i,j,d) :
        if d == "W" :
            rot = 0
        elif d in "NS" :
            rot = 1000
        else :
            return
        if r[j][i-1] == '.' and cost[j][i-1] > cost[j][i] + 1 + rot :
            td.append((i-1,j,"W"))
            preds[j][i-1] = [(i,j,'W')]
            cost[j][i-1] = cost[j][i] + 1 + rot
        elif r[j][i-1] == '.' and cost[j][i-1] < 1e10:
            if (j,i-1) == (j_s,i_s) :
                return
            _,_,d = preds[j][i-1][0]
            if d == 'W' and cost[j][i-1] == cost[j][i] + 1 :
                preds[j][i-1] += (i,j,'N')
            elif d in 'NS' and cost[j][i+1] == cost[j][i] + 1001 :
                preds[j][i-1] =+ (i,j,'N')

    while td != [] :
        i,j,d = td.pop()
        seen.append((i,j))
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
        # draw2(r,seen,td,(i,j),exit)
        # sleep(0.05)
    
    ie,je = exit
    print(cost[je][ie])
    seen = {(ie,je)}
    def n_seats(i,j) :
        c = 1
        for ip,jp,_ in preds[j][i] :
            if not (ip,jp) in seen :
                c += n_seats(ip,jp)
                seen.add((ip,jp))
        return c
    rp = r.copy()
    for i,j in seen :
        rp[j][i] = "O"
    return n_seats(ie,je)


def main():
    r,start,exit = read_file()
    print(parcours(r,start,exit))




class Parcours :
    def __init__(self,r,start,end) :
        self.r = r
        self.start = start
        self.exit = end
        self.frame_refresh = 3
        self.td = [start]
        n = len(r)
        m = len(r[0])
        self.cost = [[(INFINITY,None) for _ in range(m)] for _ in range(n)]
        self.preds = [[[] for _ in range(m)] for _ in range(n)]
        i,j,_ = start
        self.cost[j][i] = (0,"E")
        self.seen = [(i,j)]
        self.b = False
        self.current = (i,j)
        px.init(WIDTH * CASE, HEIGHT*CASE)
        px.run(self.update,self.draw)
    

    def update(self) :
        if self.td != [] and px.frame_count % self.frame_refresh == 0 :
            i,j,d = self.td.pop()
            if not d in "EWNS" :
                print(i,j,"erreur")
            self.current = (i,j)
            self.seen.append((i,j))
            if d == 'E' :
                if self.r[j][i+1] == '.' and self.cost[j][i+1][0] > self.cost[j][i][0] + 1 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = (self.cost[j][i][0] + 1,"E")
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' :
                    if self.cost[j][i+1][1] == 'E' and self.cost[j][i+1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i+1] += [(i,j)]
                    elif self.cost[j][i+1][1] in "NS" and self.cost[j][i+1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i+1] += [(i,j)]
                if self.r[j+1][i] == '.' and self.cost[j+1][i][0] > self.cost[j][i][0] + 1001 : 
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = (self.cost[j][i][0] + 1001,'S')
                    self.preds[j+1][i] = [(i,j)]
                elif self.r[j+1][i] == '.' :
                    if self.cost[j+1][i][1] == 'S' and self.cost[j+1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j+1][i] += [(i,j)]
                    elif self.cost[j+1][i][1] in "EW" and self.cost[j+1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j+1][i] += [(i,j)]

                if self.r[j-1][i] == '.' and self.cost[j-1][i][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = (self.cost[j][i][0] + 1001,'N')
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' :
                    if self.cost[j-1][i][1] == 'N' and self.cost[j-1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j-1][i] += [(i,j)]
                    elif self.cost[j-1][i][1] in "EW" and self.cost[j-1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j-1][i] += [(i,j)]

            elif d == 'W' :
                if self.r[j][i-1] == '.' and self.cost[j][i-1][0] > self.cost[j][i][0] + 1 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = (self.cost[j][i][0] + 1,'W')
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' :
                    if self.cost[j][i+1][1] == 'W' and self.cost[j][i-1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i-1] += [(i,j)]
                    elif self.cost[j][i-1][1] in "NS" and self.cost[j][i-1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i-1] += [(i,j)]
                if self.r[j+1][i] == '.' and self.cost[j+1][i][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = (self.cost[j][i][0] + 1001,'S')
                    self.preds[j+1][i] = [(i,j)]
                elif self.r[j+1][i] == '.' :
                    if self.cost[j+1][i][1] == 'S' and self.cost[j+1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j+1][i] += [(i,j)]
                    elif self.cost[j+1][i][1] in "EW" and self.cost[j+1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j+1][i] += [(i,j)]
                if self.r[j-1][i] == '.' and self.cost[j-1][i][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = (self.cost[j][i][0] + 1001,'N')
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' :
                    if self.cost[j-1][i][1] == 'N' and self.cost[j-1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j-1][i] += [(i,j)]
                    elif self.cost[j-1][i][1] in "EW" and self.cost[j-1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j-1][i] += [(i,j)]


            elif d == 'N' :
                if self.r[j-1][i] == '.' and self.cost[j-1][i][0] > self.cost[j][i][0] + 1 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = (self.cost[j][i][0] + 1,'N')
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' :
                    if self.cost[j-1][i][1] == 'N' and self.cost[j-1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j-1][i] += [(i,j)]
                    elif self.cost[j-1][i][1] in "EW" and self.cost[j-1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j-1][i] += [(i,j)]

                if self.r[j][i+1] == '.' and self.cost[j][i+1][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = (self.cost[j][i][0] + 1001,'E')
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' :
                    if self.cost[j][i+1][1] == 'E' and self.cost[j][i+1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i+1] += [(i,j)]
                    elif self.cost[j][i+1][1] in "NS" and self.cost[j][i+1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i+1] += [(i,j)]
                if self.r[j][i-1] == '.' and self.cost[j][i-1][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = (self.cost[j][i][0] + 1001,'W')
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' :
                    if self.cost[j][i+1][1] == 'W' and self.cost[j][i-1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i-1] += [(i,j)]
                    elif self.cost[j][i-1][1] in "NS" and self.cost[j][i-1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i-1] += [(i,j)]
                

            elif d == 'S' :
                if self.r[j+1][i] == '.' and self.cost[j+1][i][0] > self.cost[j][i][0] + 1 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = (self.cost[j][i][0] + 1,'S')
                    self.preds[j+1][i] = [(i,j)]
                elif self.r[j+1][i] == '.' :
                    if self.cost[j+1][i][1] == 'S' and self.cost[j+1][i][0] == self.cost[j][i][0] + 1 :
                        self.preds[j+1][i] += [(i,j)]
                    elif self.cost[j+1][i][1] in "EW" and self.cost[j+1][i][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j+1][i] += [(i,j)]
                if self.r[j][i+1] == '.' and self.cost[j][i+1][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = (self.cost[j][i][0] + 1001,'E')
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' :
                    if self.cost[j][i+1][1] == 'E' and self.cost[j][i+1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i+1] += [(i,j)]
                    elif self.cost[j][i+1][1] in "NS" and self.cost[j][i+1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i+1] += [(i,j)]
                if self.r[j][i-1] == '.' and self.cost[j][i-1][0] > self.cost[j][i][0] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = (self.cost[j][i][0] + 1001,'W')
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' :
                    if self.cost[j][i+1][1] == 'W' and self.cost[j][i-1][0] == self.cost[j][i][0] + 1 :
                        self.preds[j][i-1] += [(i,j)]
                    elif self.cost[j][i-1][1] in "NS" and self.cost[j][i-1][0] == self.cost[j][i][0] + 1001 :
                        self.preds[j][i-1] += [(i,j)]

        elif self.td == [] and not self.b :
            self.b = True
            ie,je = self.exit
            print(self.cost[je][ie])
            seen = set()
            seen.add((ie,je))
            #print(self.preds[7][5])
            def n_seats(i,j) :
                c = 1
                # print(self.preds[j][i])
                for ip,jp in self.preds[j][i] :
                    if not (ip,jp) in seen :
                        seen.add((ip,jp))
                        c += n_seats(ip,jp)
                return c
            print(n_seats(ie,je))
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
        def draw_seats(i,j) :
            for ip,jp in self.preds[j][i] :
                px.rect(ip*CASE,jp*CASE,CASE,CASE,2)
                draw_seats(ip,jp)
        ie,je = self.exit
        draw_seats(ie,je)

        px.rect(ie * CASE,je * CASE,CASE,CASE,1)
        i,j = self.current
        px.rect(i * CASE,j * CASE,CASE,CASE,8)
        


if __name__ == '__main__' :
    affichage = False
    if affichage :
        r,start,end = read_file()
        Parcours(r,start,end)
    else :
        main()
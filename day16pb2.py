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
    preds = [[[] for _ in range(m)] for _ in range(n)]

    while td != [] :
        i,j,d = td.pop() 
        if d == 'E' :
            if r[j][i+1] == '.' and cost[j][i+1] > cost[j][i] + 1 :
                td.append((i+1,j,'E'))
                cost[j][i+1] = cost[j][i] + 1
                preds[j][i+1] = [(i,j)]
            elif r[j][i+1] == '.' and cost[j][i+1] == cost[j][i] + 1 :
                preds[j][i+1] += [(i,j)]
            if r[j+1][i] == '.' and cost[j+1][i] > cost[j][i] + 1001 :
                td.append((i,j+1,'S'))
                cost[j+1][i] = cost[j][i] + 1001
                preds[j+1][i] = [(i,j)]
            elif r[j+1][i] == '.' and cost[j+1][i] == cost[j][i] + 1001 :
                preds[j+1][i] += [(i,j)]
            if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1001 :
                td.append((i,j-1,'N'))
                cost[j-1][i] = cost[j][i] + 1001
                preds[j-1][i] = [(i,j)]
            elif r[j-1][i] == '.' and cost[j-1][i] == cost[j][i] + 1001 :
                preds[j-1][i] += [(i,j)]
        elif d == 'W' :
            if r[j][i-1] == '.' and cost[j][i-1] > cost[j][i] + 1 :
                td.append((i-1,j,'W'))
                cost[j][i-1] = cost[j][i] + 1
                preds[j][i-1] = [(i,j)]
            elif r[j][i-1] == '.' and cost[j][i-1] == cost[j][i] + 1 :
                preds[j][i-1] += [(i,j)]
            if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1001 :
                td.append((i,j-1,'N'))
                cost[j-1][i] = cost[j][i] + 1001
                preds[j-1][i] = [(i,j)]
            elif r[j-1][i] == '.' and cost[j-1][i] == cost[j][i] + 1001 :
                preds[j-1][i] += [(i,j)]
            if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1001 :
                td.append((i,j-1,'N'))
                cost[j-1][i] = cost[j][i] + 1001
                preds[j-1][i] = [(i,j)]
            elif r[j-1][i] == '.' and cost[j-1][i] == cost[j][i] + 1001 :
                preds[j-1][i] += [(i,j)]
        elif d == 'N' :
            if r[j-1][i] == '.' and cost[j-1][i] > cost[j][i] + 1 :
                td.append((i,j-1,'N'))
                cost[j-1][i] = cost[j][i] + 1
                preds[j-1][i] = [(i,j)]
            elif r[j-1][i] == '.' and cost[j-1][i] == cost[j][i] + 1 :
                preds[j-1][i] += [(i,j)]
            if r[j][i+1] == '.' and cost[j][i+1] > cost[j][i] + 1001 :
                td.append((i+1,j,'E'))
                cost[j][i+1] = cost[j][i] + 1001
                preds[j][i+1] = [(i,j)]
            elif r[j][i+1] == '.' and cost[j][i+1] == cost[j][i] + 1001 :
                preds[j][i+1] += [(i,j)]
            if r[j][i-1] == '.' and cost[j][i-1] > cost[j][i] + 1001 :
                td.append((i-1,j,'W'))
                cost[j][i-1] = cost[j][i] + 1001
                preds[j][i-1] = [(i,j)]
            elif r[j][i-1] == '.' and cost[j][i-1] == cost[j][i] + 1001 :
                preds[j][i-1] += [(i,j)]
        elif d == 'S' :
            if r[j+1][i] == '.' and cost[j+1][i] > cost[j][i] + 1 :
                td.append((i,j+1,'S'))
                cost[j+1][i] = cost[j][i] + 1
                preds[j+1][i] = [(i,j)]
            elif r[j+1][i] == '.' and cost[j+1][i] == cost[j][i] + 1 :
                preds[j+1][i] += [(i,j)]
            if r[j][i+1] == '.' and cost[j][i+1] > cost[j][i] + 1001 :
                td.append((i+1,j,'E'))
                cost[j][i+1] = cost[j][i] + 1001
                preds[j][i+1] = [(i,j)]
            elif r[j][i+1] == '.' and cost[j][i+1] == cost[j][i] + 1001 :
                
                preds[j][i+1] += [(i,j)]
            if r[j][i-1] == '.' and cost[j][i-1] > cost[j][i] + 1001 :
                td.append((i-1,j,'W'))
                cost[j][i-1] = cost[j][i] + 1001
                preds[j][i-1] = [(i,j)]
            elif r[j][i-1] == '.' and cost[j][i-1] == cost[j][i] + 1001 :
                preds[j][i-1] += [(i,j)]
    ie,je = exit
    seen = {(ie,je)}
    def n_seats(i,j) :
        c = 1
        for ip,jp in preds[j][i] :
            if not (ip,jp) in seen :
                c += n_seats(ip,jp)
                seen.add((ip,jp))
        return c
    return n_seats(ie,je)



def main():
    r,start,exit = read_file()
    print(parcours(r,start,exit))


WIDTH = 20
HEIGHT = WIDTH
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
        self.preds = [[[] for _ in range(m)] for _ in range(n)]
        i,j,_ = start
        self.cost[j][i] = 0
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
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' and self.cost[j][i+1] == self.cost[j][i] + 1 :
                    self.preds[j][i+1] += [(i,j)]
                    #print("ui")
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1001
                    self.preds[j+1][i] = [(i,j)]
                    
                elif self.r[j+1][i] == '.' and self.cost[j+1][i] == self.cost[j][i] + 1001 :
                    self.preds[j+1][i] += [(i,j)]
                    #print("ui")
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1001
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' and self.cost[j-1][i] == self.cost[j][i] + 1001 :
                    self.preds[j-1][i] += [(i,j)]
                    #print("ui")
            elif d == 'W' :
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' and self.cost[j][i-1] == self.cost[j][i] + 1 :
                    self.preds[j][i-1] += [(i,j)]
                    #print("ui")
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1001
                    self.preds[j+1][i] = [(i,j)]
                elif self.r[j+1][i] == '.' and self.cost[j+1][i] == self.cost[j][i] + 1001 :
                    self.preds[j+1][i] += [(i,j)]
                    #print("ui")
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1001 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1001
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' and self.cost[j-1][i] == self.cost[j][i] + 1001 :
                    self.preds[j-1][i] += [(i,j)]
                    #print("ui")
            elif d == 'N' :
                if self.r[j-1][i] == '.' and self.cost[j-1][i] > self.cost[j][i] + 1 :
                    self.td.append((i,j-1,'N'))
                    self.cost[j-1][i] = self.cost[j][i] + 1
                    self.preds[j-1][i] = [(i,j)]
                elif self.r[j-1][i] == '.' and self.cost[j-1][i] == self.cost[j][i] + 1 :
                    self.preds[j-1][i] += [(i,j)]
                    #print("ui")
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1001
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' and self.cost[j][i+1] == self.cost[j][i] + 1001 :
                    self.preds[j][i+1] += [(i,j)]
                    #print("ui")
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1001
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' and self.cost[j][i-1] == self.cost[j][i] + 1001 :
                    self.preds[j][i-1] += [(i,j)]
            elif d == 'S' :
                if self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1 :
                    self.td.append((i,j+1,'S'))
                    self.cost[j+1][i] = self.cost[j][i] + 1
                    self.preds[j+1][i] = [(i,j)]
                elif self.r[j+1][i] == '.' and self.cost[j+1][i] > self.cost[j][i] + 1 :
                    self.preds[j+1][i] += [(i,j)]
                    #print("ui")
                if self.r[j][i+1] == '.' and self.cost[j][i+1] > self.cost[j][i] + 1001 :
                    self.td.append((i+1,j,'E'))
                    self.cost[j][i+1] = self.cost[j][i] + 1001
                    self.preds[j][i+1] = [(i,j)]
                elif self.r[j][i+1] == '.' and self.cost[j][i+1] == self.cost[j][i] + 1001 :
                    self.preds[j][i+1] += [(i,j)]
                    #print("ui")
                if self.r[j][i-1] == '.' and self.cost[j][i-1] > self.cost[j][i] + 1001 :
                    self.td.append((i-1,j,'W'))
                    self.cost[j][i-1] = self.cost[j][i] + 1001
                    self.preds[j][i-1] = [(i,j)]
                elif self.r[j][i-1] == '.' and self.cost[j][i-1] == self.cost[j][i] + 1001 :
                    self.preds[j][i-1] += [(i,j)]
                    #print("ui")
        elif self.td == [] and not self.b :
            self.b = True
            ie,je = self.exit
            seen = set()
            seen.add((ie,je))
            print(self.preds[7][15])
            def n_seats(i,j) :
                c = 1
                print(self.preds[j][i])
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
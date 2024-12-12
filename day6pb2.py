def read_file() :
    grid = []
    with open("input.txt","r") as input :
        for line in input :
            l = []
            for c in line :
                if c == '#' :
                    l.append(1)
                elif c == '.' :
                    l.append(0)
                elif c == '^' :
                    l.append('h')
                    x,y = len(l)-1,len(grid)
            grid.append(l)
    return grid, x, y

directions = {"h" : 0, "d" : 1, "b" : 2, "g" : 3}

class Guard :
    def __init__(self,o = None) :
        grid,x,y = read_file()
        self.x = x
        self.y = y
        self.grid = grid
        self.h = len(grid)
        self.l = len(grid[0])
        self.dir = 0
        self.out = False
        self.steps = 1
        self.looped = False

        if o != None :
            xo,yo = o
            self.grid[yo][xo] = 1
    
    def is_out(self) :
        if not (0<= self.x <= self.l-1 and 0<= self.y <= self.h - 1) :
            self.out = True
        return self.out

    def move(self) :
        if self.dir == 0 :            
            if self.y == 0 :
                self.y -= 1
                self.out = True
            else :
                if self.grid[self.y-1][self.x] != 1 :
                    self.y -= 1
                    if self.grid[self.y][self.x] == 0 :
                        self.grid[self.y][self.x] = 'h'
                        self.steps += 1
                    elif self.grid[self.y][self.x] == 'h' :
                        self.looped = True
                else :
                    self.dir = (self.dir + 1) % 4
        elif self.dir == 1 :
            if self.x == self.l - 1 :
                self.x == self.l
                self.out = True
            else :
                if self.grid[self.y][self.x + 1] != 1 :
                    self.x += 1
                    if self.grid[self.y][self.x] == 0:
                        self.grid[self.y][self.x] = 'd'
                        self.steps += 1
                    elif self.grid[self.y][self.x] == 'd' :
                        self.looped = True
                else :
                    self.dir = (self.dir + 1) % 4
        elif self.dir == 2 :
            if self.y == self.h-1 :
                self.y += 1
                self.out = True
            else :
                if self.y >=self.h - 1 :
                    print(self.y)
                if self.x >= self.l :
                    print(self.x)
                if self.grid[self.y+1][self.x] != 1 :
                    self.y += 1
                    if self.grid[self.y][self.x] == 0 :
                        self.grid[self.y][self.x] = 'b'
                        self.steps += 1
                    elif self.grid[self.y][self.x] == 'b' :
                        self.looped = True
                else :
                    self.dir = (self.dir + 1) % 4
        elif self.dir == 3 :
            if self.x == 0 :
                self.x -= 1
                self.out = True
            else :
                if self.grid[self.y][self.x - 1] != 1 :
                    self.x -= 1
                    if self.grid[self.y][self.x] == 0:
                        self.grid[self.y][self.x] = 'g'
                        self.steps += 1
                    elif self.grid[self.y][self.x] == 'g' :
                        self.looped = True
                else :
                    self.dir = (self.dir + 1) % 4
    def path(self):
        while not self.out :
            self.move()
        return self.steps
    
    def is_looped(self) :
        while not (self.out or self.looped) :
            self.move()
        return self.looped

def main() :
    c = 0
    grid,x,y = read_file()
    h = len(grid)
    l = len(grid[0])
    for i in range(h):
        if i%10 == 0:
            print(f"{round(i*100/h,0)}%")
        for j in range(l):
            g = Guard((i,j))
            if g.is_looped() :
                c += 1
    print(c)

if __name__ == "__main__" :
    main()



                


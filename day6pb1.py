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
                    l.append(2)
                    x,y = len(l)-1,len(grid)
            grid.append(l)
    print(x,y)
    return grid, x, y

directions = {"h" : 0, "d" : 1, "b" : 2, "g" : 3}

class Guard :
    def __init__(self) :
        grid,x,y = read_file()
        self.x = x
        self.y = y
        self.grid = grid
        self.n = len(grid)
        self.dir = 0
        self.out = False
        self.steps = 1
    
    def is_out(self) :
        if not (0<= self.x <= self.n-1 and 0<= self.y <= self.n - 1) :
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
                        self.grid[self.y][self.x] = 2
                        self.steps += 1
                else :
                    self.dir = (self.dir + 1) % 4
        elif self.dir == 1 :
            if self.x == self.n - 1 :
                self.x == self.n
                self.out = True
            else :
                if self.grid[self.y][self.x + 1] != 1 :
                    self.x += 1
                    if self.grid[self.y][self.x] == 0:
                        self.grid[self.y][self.x] = 2
                        self.steps += 1
                else :
                    self.dir = (self.dir + 1) % 4
        elif self.dir == 2 :
            if self.y == self.n-1 :
                self.y += 1
                self.out = True
            else :
                if self.grid[self.y+1][self.x] != 1 :
                    self.y += 1
                    if self.grid[self.y][self.x] == 0 :
                        self.grid[self.y][self.x] = 2
                        self.steps += 1
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
                        self.grid[self.y][self.x] = 2
                        self.steps += 1
                else :
                    self.dir = (self.dir + 1) % 4
    def path(self):
        while not self.out :
            self.move()
        return self.steps

def main() :
    g = Guard()
    g.path()
    print(g.steps)

if __name__ == "__main__" :
    main()



                


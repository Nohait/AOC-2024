import pyxel as px

class Box :
    def __init__(self,x,y) :
        self.x = x
        self.y = y


class Robot :
    def __init__(self,x : int,y : int, moves : list) :
        self.x = x
        self.y = y
        self.moves = moves    

class Warehouse :
    def __init__(self,n : int,m : int,walls : list, boxes : list, bot : Robot) :
        self.n = n
        self.m = m
        self.walls = walls
        self.boxes = boxes
        
        self.bot = bot
    
    def map(self) :
        map = [['.' for _ in range(self.m)] for _ in range(self.n)]
        for x,y in self.walls :
            map[y][x] = "#"
        for box in self.boxes :
            map[box.y][box.x] = "["
            map[box.y][box.x + 1] = "]"
        map[self.bot.y][self.bot.x] = "@"
        return map
    
    def can_be_moved_updown(self,box : Box,dir : str) -> bool :
        if dir == "^" :
            for x,y in self.walls :
                if box.y - 1 == y :
                    if box.x == x or box.x+1 == x :
                        return False
            bpos = []
            for boxb in self.boxes :
                # boite a gauche
                if boxb.y == box.y - 1 :
                    if box.x == boxb.x :
                        return self.can_be_moved_updown(boxb,dir)
                        
                    if  box.x == boxb.x - 1 :
                        bpos.append(boxb)
                    elif box.x == boxb.x + 1 :
                        bpos.append(boxb)
            for bb in bpos :
                if not self.can_be_moved_updown(bb,dir) :
                    return False
            return True
        
        elif dir == "v" :
            for x,y in self.walls :
                if (box.x,box.y + 1) == (x,y) or (box.x+1,box.y + 1) == (x,y):
                    return False
            bpos = []
            for boxb in self.boxes :
                # boite a gauche
                if boxb.y == box.y + 1 :
                    if box.x == boxb.x :
                        if self.can_be_moved_updown(boxb,dir):
                            return True
                        return False
                    if  box.x == boxb.x - 1 :
                        bpos.append(boxb)
                    elif box.x == boxb.x + 1 :
                        bpos.append(boxb)
            for bb in bpos :
                if not self.can_be_moved_updown(bb,dir) :
                    return False
            return True
        

    def move_box(self,box : Box,dir : str,b : bool = True) :
        if dir == "^" :
            for boxb in self.boxes :
                if boxb.y == box.y - 1 :
                    if boxb.x == box.x - 1 or boxb.x == box.x or boxb.x == box.x + 1 :
                        self.move_box(boxb,dir)
            box.y -= 1
        elif dir == "v" :
            for boxb in self.boxes :
                if boxb.y == box.y + 1 :
                    if  box.x in [boxb.x - 1, boxb.x, boxb.x + 1] :
                        self.move_box(boxb,dir)
            box.y += 1
        elif dir == ">" :
            for x,y in self.walls :
                if (box.x+2,box.y) == (x,y) :
                    return False
            for boxb in self.boxes :
                if (boxb.x,boxb.y) == (box.x+2,box.y) :
                    if self.move_box(boxb,dir) :
                        box.x += 1
                        return True
                    else :
                        return False
            box.x += 1
            return True
        else :
            for x,y in self.walls :
                if (box.x-1,box.y) == (x,y) :
                    return False
            for boxb in self.boxes :
                if (boxb.x + 1,boxb.y) == (box.x-1,box.y) :
                    if self.move_box(boxb,dir) :
                        box.x -= 1
                        return True
                    else :
                        return False
            box.x -= 1
            return True
            
    def move_bot(self) :
        move = self.bot.moves.pop(0)
        if move == "^" :
            for x,y in self.walls :
                if (self.bot.x,self.bot.y - 1) == (x,y) :
                    return
            for box in self.boxes :
                if (box.y == self.bot.y-1) and (box.x == self.bot.x or box.x == self.bot.x - 1) :
                    if self.can_be_moved_updown(box,move) :
                        self.move_box(box,move)
                        self.bot.y -= 1
                        return
                    else :
                        return
            self.bot.y -= 1
            return
        elif move == "v" :
            for x,y in self.walls :
                if (self.bot.x,self.bot.y + 1) == (x,y) :
                    return
            for box in self.boxes :
                if (box.y == self.bot.y + 1) and (self.bot.x in [box.x,box.x+1]) :
                    if self.can_be_moved_updown(box,move) :
                        self.move_box(box,move)
                        self.bot.y += 1
                        return
                    else :
                        return
            self.bot.y += 1
            return
        elif move == ">" :
            for x,y in self.walls :
                if (self.bot.x + 1,self.bot.y) == (x,y) :
                    return
            for box in self.boxes :
                if (box.x,box.y) == (self.bot.x + 1, self.bot.y) :
                    if self.move_box(box,move) :
                        self.bot.x += 1
                        return
                    else :
                        return
            self.bot.x += 1
            return
        else :
            for x,y in self.walls :
                if (self.bot.x - 1,self.bot.y) == (x,y) :
                    return
            for box in self.boxes :
                if (box.x + 1,box.y) == (self.bot.x - 1, self.bot.y) :
                    if self.move_box(box,move) :
                        self.bot.x -= 1
                        return
                    else :
                        return
            self.bot.x -= 1
            return
    
    def tot(self) -> int :
        c = 0
        for box in self.boxes :
            c += box.x + box.y*100

        return c




HEIGHT = 50
WIDTH = 2*HEIGHT
CASE = 10

def read_file() :
    with open("input.txt", "r") as input :
        boxes = []
        walls = []
        for j,line in enumerate(input) :
            if line[0] == "#" :
                for i,c in enumerate(line) :
                    if c == "#" :
                        walls += [(2 * i, j), (2 * i + 1, j)]
                    elif c == "O" :
                        boxes.append(Box(2*i,j))
                    elif c == "@" :
                        bot = Robot(2*i,j,[])
            else :
                for c in line :
                    if c in "<>v^" :
                        bot.moves.append(c)
    warehouse = Warehouse(HEIGHT,WIDTH,walls,boxes,bot)
    return warehouse

class Main :
    def __init__(self,warehouse) :
        self.frame_refresh = 1
        self.warehouse = warehouse
        self.b = False
        px.init(WIDTH*CASE,HEIGHT*CASE)
        px.run(self.update,self.draw)
    
    def update(self) :
        if len(self.warehouse.bot.moves) > 0 and px.frame_count % self.frame_refresh == 0 :
            self.warehouse.move_bot()
    
    def draw(self) :
        if len(self.warehouse.bot.moves) > 0 :
            px.cls(7)
            for x,y in self.warehouse.walls :
                px.rect(x*CASE,y*CASE,CASE,CASE,0)
            for box in self.warehouse.boxes :
                x,y = box.x,box.y
                px.rect(x*CASE,y*CASE,CASE,CASE,4)
                px.rect((x+1)*CASE, y*CASE,CASE,CASE,9)
            x,y = self.warehouse.bot.x,self.warehouse.bot.y
            px.rect(x*CASE,y*CASE,CASE,CASE,12)
            px.text(4,4,f"remaining : {len(self.warehouse.bot.moves)}",7)
        else :
            px.cls(7)
            for x,y in self.warehouse.walls :
                px.rect(x*CASE,y*CASE,CASE,CASE,0)
            for box in self.warehouse.boxes :
                x,y = box.x,box.y
                px.rect(x*CASE,y*CASE,CASE,CASE,4)
                px.rect((x+1)*CASE, y*CASE,CASE,CASE,9)
            x,y = self.warehouse.bot.x,self.warehouse.bot.y
            px.rect(x*CASE,y*CASE,CASE,CASE,12)
            
            res = self.warehouse.tot()
            if not self.b :
                print(res)
                self.b = True
            # px.cls(0)
            px.text(40,40,f"GPS : {res}",0)
            


if __name__ == "__main__" :
    affichage = True
    if affichage :
        m = Main(read_file())
    else:
        w = read_file()
        while len(w.bot.moves) > 0 :
            w.move_bot()
        print(w.tot())






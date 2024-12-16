import re

N = 103
M = 101

class Robot :
    def __init__(self,x,y,vx,vy) :
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self) :
        self.x = (self.x + self.vx + M) % M
        self.y = (self.y + self.vy + N) % N
    


def read_file() :
    robots = []
    with open("input.txt","r") as input :
        for line in input :
            x,y,vx,vy = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",line)[0]
            x,y,vx,vy = int(x), int(y), int(vx), int(vy)
            r = Robot(x,y,vx,vy)
            robots.append(r)
        return robots

def print_bots(robots) :
    r = [['.' for i in range(M)] for i in range(N)]
    for bot in robots :
        x,y = bot.x,bot.y
        if r[y][x] == "." :
            r[y][x] = "1"
        else :
            r[y][x] = str(int(r[y][x]) + 1)
    xm,ym = M//2,N//2

    for i in range(M) :
        r[ym][i] = " "
    for j in range(N) :
        r[j][xm] = " "
    for line in r :
        print("".join(line))
    print()

def main() :
    robots = read_file()
    for _ in range(100) :
        for robot in robots :
            robot.move()
    print_bots(robots)
    
    n_quad_hg = 0
    n_quad_hd = 0
    n_quad_bg = 0
    n_quad_bd = 0

    xm = M//2
    ym = N//2
    # print(xm,ym)
    for robot in robots :
        x,y = robot.x, robot.y
        if x < xm and y < ym :
            n_quad_hg += 1
        elif x < xm and y > ym :
            n_quad_bg += 1
        elif x > xm and y < ym :
            n_quad_hd += 1
            
        elif x > xm and y > ym :
            n_quad_bd += 1
    res = n_quad_bd * n_quad_bg * n_quad_hd * n_quad_hg
    # print(n_quad_hg,n_quad_hd,n_quad_bg,n_quad_bd)
    print(res)


if __name__ == "__main__" :
    main()
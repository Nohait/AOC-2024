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

    return r

def len_chaine(r) :
    def chaine(i,j,vus,t) :
        if j >= N or i >= M or (i,j) in vus or  r[j][i] == '.' :
            return t
        if t >= 30 :
            return 31
        vus2 = vus + [(i,j)]
        m1 = chaine(i+1,j+1,vus2,t+1)
        m2 = chaine(i+1,j-1,vus2,t+1)
        m3 = chaine(i-1,j+1,vus2,t+1)
        m4 = chaine(i-1,j-1,vus2,t+1)
        
        return max([m1,m2,m3,m4])
    maxs = []
    for i in range(M) :
        for j in range(N) :
            m = chaine(i,j,[],0)
            if m >= 30 :
                return m
            maxs.append(m)
    return max(maxs)




def main() :
    seuil_r = 0
    robots = read_file()
    K = 10000
    for i in range(6645) :
        if i%1000 == 0 :
            print(f"{i*100/K}%")
        for robot in robots :
            robot.move()
        r = print_bots(robots)
        if i == 6643 :
            print(i)
            for l in r :
                print("".join(l))

    
    # print(n_quad_hg,n_quad_hd,n_quad_bg,n_quad_bd)


if __name__ == "__main__" :
    main()
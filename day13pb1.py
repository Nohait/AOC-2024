import re
from sympy import symbols, Eq, solve
class Machine :
    def __init__(self,ax,ay,bx,by,px,py) :
        self.ax = ax
        self.ay = ay
        
        self.bx = bx
        self.by = by

        self.px = px
        self.py = py 
        

    def cost(self) -> int :
        ax,ay = self.ax,self.ay
        bx,by = self.bx,self.by

        px,py = self.px,self.py

        x,y = symbols("x y")

        eq1 = Eq(ax * x + bx * y,px)
        eq2 = Eq(ay * x + by * y,py)

        sol = solve((eq1,eq2),(x,y))

        sx,sy = sol[x],sol[y]
        if int(sx) == sx and int(sy) == sy :
            return 3 * sx + sy
        return 0

    def __str__(self) :
        return f"Button A : X+{self.ax}, Y+{self.ay}\nButton B : X+{self.bx}, Y+{self.by}\nPrize : X={self.px}, Y={self.py}\n"
    

def read_file() :
    motif = r"X\+(\d+), Y\+(\d+)"
    l_machines = []
    with open("input.txt","r") as input :
        for line in input :
            if line[:9] == "Button A:" :
                x, y = re.findall(motif,line)[0]
                ax, ay = int(x),int(y)
            elif line[:9] == "Button B:" :
                x,y = re.findall(motif,line)[0]
                bx,by = int(x),int(y)
            elif line[:3] == "Prize"[:3] :
                x,y = re.findall(r"X\=(\d+), Y\=(\d+)",line)[0]
                px,py = int(x),int(y)
            else :
                m = Machine(ax,ay,bx,by,px,py)
                l_machines.append(m)
    return l_machines
                

if __name__ == "__main__" :
    l_machines = read_file()
    tot_cost = 0
    for m in l_machines :
        tot_cost += m.cost()
    print(tot_cost)
    
    



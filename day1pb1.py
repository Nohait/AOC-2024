
def read_file() -> tuple[list,list] :
    with open("input.txt","r") as input :

        l1 = []
        l2 = []

        for line in input :
            valeurs = line.split()
            l1.append(int(valeurs[0]))
            l2.append(int(valeurs[1]))
    return l1,l2


def fusion(l1 : list,l2 : list) -> list:
    l = []
    while (l1,l2) != ([],[]):
        if l1 == [] :
            l.append(l2.pop(0))
        elif l2 == [] :
            l.append(l1.pop(0))
        else :
            if l1[0] <= l2[0] :
                l.append(l1.pop(0))
            else :
                l.append(l2.pop(0))
    return l

def merge_sort(l : list) -> list :
    if len(l) <= 1 :
        return l
    else :
        n = int(len(l) / 2)
        l1 = l[:n]
        l2 = l[n:]
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        return fusion(l1,l2)
        
def abs(a):
    if a>=0 :
        return a
    else :
        return -a

def dist(l1 : list,l2 : list) -> int :
    assert(len(l1) == len(l2))
    d = 0
    for i in range(len(l1)):
        x1,x2 = l1.pop(0),l2.pop(0)
        d += abs(x1-x2)
    return d


def main() -> int:
    l1,l2 = read_file()
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    return dist(l1,l2)

if __name__ == "__main__":
    print(main())
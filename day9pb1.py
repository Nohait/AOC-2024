def read_file() :
    s = []
    id = 0
    file = True
    with open("input.txt","r") as input :
        for line in input :
            for c in line :
                if file :
                    s += [str(id)] * int(c)
                    file = False
                    id += 1
                else :
                    s += ['.'] * int(c)
                    file = True
    return s

def pp(s) :
    for i,c in enumerate(s) :
        if c == '.' :
            return i
    return None

def lc(s) :
    n = len(s)
    for i in range(len(s)) :
        if s[n-1-i] != '.' :
            return n-1-i
    return None

def compact(s) :

    ppoint = pp(s)
    lchiffre = lc(s)
    while ppoint <= lchiffre :
        s[ppoint],s[lchiffre] = s[lchiffre],s[ppoint]
        ppoint = pp(s)
        lchiffre = lc(s)
    return s

def checksum(s) :
    # print(s)
    i = 0
    sum = 0
    while s[i] != '.' :
        sum += i * int(s[i])
        i += 1
    return sum



def main() :
    si = read_file()
    s = compact(si)
    print("COMPACTED")
    print(checksum(s))
    
    
    


if __name__ == "__main__" :
    main()
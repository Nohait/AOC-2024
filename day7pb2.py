
def read_file():
    d = {}
    with open("input.txt","r") as input :
        for line in input :
            v = line.split(':')
            d[int(v[0])] = [int(x) for x in v[1].split()]
    return d

def anticoncat(obj,sub) :
    o = str(obj)
    s = str(sub)
    if len(s) > len(o) :
        return None
    for i in range(len(s)) :
        if s[-(i+1)] != o[-(i+1)] :
            return None
    if len(o) == len(s) :
        return 0
    return int(o[:-len(s)])

def atteignable(obj, rmn):
    if obj == 0 :
        return rmn == []
    if rmn == [] :
        return False
    if len(rmn) == 1 :
        return rmn[0] == obj

    lp = rmn[:]
    n = lp.pop()

    if atteignable( obj - n, lp ) :
        return True
    if obj % n == 0 and atteignable( obj // n, lp ) :
        return True
    if anticoncat(obj,n) != None and atteignable(anticoncat(obj,n),lp) :
        return True
    return False


    
    

def main() :
    d = read_file()
    c = 0
    n = len(d)
    i = 0
    for v in d :
        i+=1
        if atteignable(v,d[v]):
            c += v

    print(c)



if __name__== "__main__" :
    main()

from day9pb1 import read_file

def available_space(s,i_s) :
    i = i_s
    while s[i] == '.' :
        i += 1
    return i - i_s




# bloc juste avant ip
def bloc(s,ip) :
    n = len(s)
    i = ip
    while s[i] == '.' :
        i -= 1
    il = i
    id = s[i]
    while s[i] == id :
        i -= 1

    isrt = i + 1
    size = il - isrt + 1
    return isrt,size,id
    
def space(s,size,m) :
    crt = 0
    for i in range(0,m) :
        if s[i] == '.' :
            crt += 1
            if crt == size :
                return i + 1 - crt
        else :
            crt = 0
        i += 1
    return None

def mv(s,istrt,size,idest) :
    i = 0

    while i < size :
        s[idest + i] = s[istrt + i]
        s[istrt + i] = '.'
        i+=1
    return s

def compact(s) :
    n = len(s)
    i = n - 1
    while i >= 0 :
        isrt,size,_ = bloc(s,i)
        j = space(s,size,i)
        if j != None :
            s = mv(s,isrt,size,j)
        i = isrt - 1
        # print("".join(s))
    return s
        
        
        
    

def checksum(s) :
    # print(s)    
    sum = 0
    for i,c in enumerate(s) :
        if c != '.' :
            sum += int(c) * i
    return sum


def main() :
    si = read_file()
    s = compact(si)
    print("COMPACTED")
    print(checksum(s))
    
    
    


if __name__ == "__main__" :
    main()
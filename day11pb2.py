L = ["6","11","33023","4134","564","0","8922422","688775"]
L2 = ["125","17"]


def n_stones(s, blinks) :
    global d 
    if blinks == 0:
        # print(s)
        return 1
    if (s,blinks) in d :
        return d[(s,blinks)]
    if s == "0" :
        r = n_stones("1",blinks - 1)
    elif len(s)%2 == 0 :
        x,y = s[:len(s)//2], s[len(s)//2:]
        r = n_stones(x,blinks - 1) + n_stones(str(int(y)), blinks - 1)
    else :
        r = n_stones(str(int(s) * 2024), blinks - 1)
    d[(s,blinks)] = r
    return r


def main() :
    l = L
    c = 0
    i = 0
    global d
    d = {}
    for stone in l :
        i+=1
        c += n_stones(stone,75)

    print(c)

if __name__ == "__main__" :
    main()

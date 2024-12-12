from day1pb1 import read_file

def occ(l : list) -> dict :
    d = {}
    for x in l :
        if x in d :
            d[x] += 1
        else :
            d[x] = 1
    return d

def simiscore(lg : list,ld : list) -> int :
    occd = occ(ld)
    score = 0
    for x in lg :
        if x in occd :
            score += x * occd[x]
    return score


def main() :
    lg,ld = read_file()
    print(simiscore(lg,ld))

if __name__ == "__main__" :
    main()
L = ["6","11","33023","4134","564","0","8922422","688775"]
L2 = ["125","17"]

def iter(l : list) -> list :
    lf = []
    for n in l :
        if int(n) == 0 :
            lf.append("1")
        elif len(n) % 2 == 0 :
            p = len(n)
            lf += [n[:p//2],str(int(n[p//2:]))]
        else : 
            lf.append(str(2024 * int(n)))
    return lf

def main() :
    l = L
    for i in range(25) :
        l = iter(l)
    print(len(l))

if __name__ == "__main__" :
    main()

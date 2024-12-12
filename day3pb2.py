import re

def main() :
    do = True
    C = 0
    l = []
    motif = r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    with open("input.txt","r") as f :
        for line in f :
            fd = re.findall(motif,line)
            print(len(fd))
            l += re.findall(motif,line)
        print(l)
        for match in l :
            if match[2] == "do()" :
                do = True
            elif match[3] == "don't()" :
                do = False
            elif do :
                C += int(match[0]) * int(match[1])
    print(C)
            
if __name__ == "__main__" :
    main()
import re

def main() :
    with open("input.txt","r") as f :
        C = 0
        motif = r"mul\(\d{1,3},\d{1,3}\)"
        for line in f :
            matches = re.findall(motif,line)
            print(matches)
            for match in matches :
                tpl = match[4:-1]
                v = tpl.split(',')
                C+= int(v[0]) * int(v[1])
    return C

if __name__ == "__main__" :
    print(main())
    
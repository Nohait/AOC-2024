def read_file() :
    regles = []
    updates = []
    with open("input.txt","r") as input :
        for line in input :
            if line == "\n" :
                pass
            elif line[2] == '|' :
                v = line.split('|')
                regles.append((int(v[0]),int(v[1])))
            elif line[2] == ',' :
                v = line.split(',')
                updates.append([int(x) for x in v])
    return regles, updates


def fix(update,regles) -> int :
    b = False
    for i in range(len(update)):
        for j in range(i+1,len(update)):
            if (update[j],update[i]) in regles :
                update[j],update[i] = update[i],update[j]
                b = True
    if b :
        return update[len(update) // 2]
    else :
        return 0

def main():
    regles,updates = read_file()
    c = 0
    for update in updates :
        c += fix(update,regles)

    print(c)


if __name__ == "__main__" :
    main()



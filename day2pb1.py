def abs(a) :
    if a >= 0 :
        return a
    return -a


def read_file() -> list :
    reports = []
    with open("input.txt","r") as f :
        for line in f :
            reports.append([int(x) for x in line.split()])
    return reports

def is_safe(report : list) -> bool :
    croissant = report[1] > report[0]
    for i in range(len(report) - 1) :
        if croissant :
            pas = report[i+1] - report[i]
        else :
            pas = report[i] - report[i+1]
        if not (1<=pas<=3) :
                return False
    return True




def main():
    reports = read_file()
    cpt_safe = 0
    for report in reports :
        if is_safe(report) :
            cpt_safe += 1
    print(cpt_safe)
        



if __name__ == "__main__" :
    main()

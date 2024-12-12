from day2pb1 import is_safe,read_file

def is_safe_2(report : list) -> bool :
    for i in range(len(report) + 1) :
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False

def main() : 
    reports = read_file()
    cpt_safe = 0
    for report in reports :
        if is_safe_2(report) :
            cpt_safe += 1
    print(cpt_safe)


if __name__ == "__main__" :
    main()
from day4pb1 import read_file

def main() :
    f = read_file()
    n = len(f)
    cpt = 0
    for i in range(1,n-1) :
        for j in range(1,n-1) :
            if f[i][j] == 'A' :
                k = False
                if (f[i+1][j+1],f[i-1][j-1]) in [('M','S'),('S','M')] :
                    k = True
                if k and (f[i+1][j-1],f[i-1][j+1]) in [('M','S'),('S','M')]  :
                    cpt += 1
    print(cpt)

if __name__ == "__main__" :
    main()
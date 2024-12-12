import re

def read_file() -> list :
    r = []
    with open("input.txt","r") as f :
        for line in f :
            r.append(line)
    return r


def main() :
    f = read_file()
    n = len(f)
    cpt = 0
    for i in range(n) :
        for j in range(n) :
            if f[i][j] == 'X' :
                k = 0
                #colonnes
                if i+3 < n and f[i+1][j] + f[i+2][j] + f[i+3][j] == "MAS" :
                    cpt += 1
                    k += 1
                if i-3 >= 0 and f[i-1][j] + f[i-2][j] + f[i-3][j] == "MAS" :
                    k += 1
                    cpt += 1
                #lignes
                if j+3 < n and f[i][j+1] + f[i][j+2] + f[i][j+3] == "MAS" :
                    k += 1
                    cpt += 1
                if j-3 >= 0 and f[i][j-1] + f[i][j-2] + f[i][j-3] == "MAS":
                    cpt +=1
                    k += 1
                #diagonales
                if i+3 < n and j+3 < n and f[i+1][j+1] + f[i+2][j+2] + f[i+3][j+3] == "MAS" :
                    k += 1
                    cpt += 1
                if i-3>=0 and j+3 < n and f[i-1][j+1] + f[i-2][j+2] + f[i-3][j+3] == "MAS" :
                    k += 1
                    cpt += 1
                if i-3 >=0 and j-3 >=0 and  f[i-1][j-1] + f[i-2][j-2] + f[i-3][j-3] == "MAS" :
                    k += 1
                    cpt += 1 
                if i+3 < n and j-3 >=0 and f[i+1][j-1] + f[i+2][j-2] + f[i+3][j-3] == "MAS" :
                    k += 1
                    cpt += 1
                
    
    print(cpt)


if __name__ == "__main__" :
    main()
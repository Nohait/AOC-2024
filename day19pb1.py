def read_file() :
    available = []
    motifs = []
    fl = True
    with open("input.txt","r") as input :
        for line in input :
            if fl :
                available = [x.strip(" ").strip("\n") for x in line.split(",")]
                fl = False
            elif line != "\n" :
                motifs.append(line.strip("\n"))
    return available,motifs

def faisable(motif : str,available : list) -> bool :
    if motif == "" :
        return True
    for twl in available :
        n = len(twl)
        if motif[:n] == twl and faisable(motif[n:],available) :
            return True
    return False
            



if __name__ == "__main__" :
    available,motifs = read_file()
    compte = 0
    for motif in motifs :
        if faisable(motif,available) :
            compte += 1
    print(compte)
            


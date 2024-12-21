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



def n_ways(motif : str,available : list) -> int :
    global mnemo
    if motif in mnemo :
        return mnemo[motif]
    c = 0
    for twl in available :
        n = len(twl)
        if motif[:n] == twl :
            nw = n_ways(motif[n:],available)
            mnemo[motif[n:]] = nw
            c += nw
    return c




if __name__ == "__main__" :
    available,motifs = read_file()
    global mnemo
    mnemo = {"" : 1}
    
    compte = 0
    n = len(motifs)
    for i,motif in enumerate(motifs) :
        # if i%1 == 0 :
        #     print(f"{i*100/n}%")
        compte += n_ways(motif,available)
    print(compte)
            


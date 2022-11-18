# CSCI 1550, hw13pr4
# Filename: hw13pr4.py
# Name: Peter Morales
# Problem description: bioinformatics skills will make me rich!
#

def shortToLong(seq1, seq2):
    LoL = [[len(seq1), seq1], [len(seq2), seq2]]
    maxElem = max(LoL)
    minElem = min(LoL)
    return (maxElem[1], minElem[1])

def edit_distance(seq1, seq2):
    (seq1, seq2) = shortToLong(seq1, seq2)
    if seq1 == "":
        return len(seq2)
    elif seq2 == "":
        return len(seq2)
    elif seq1[0] == seq2[0]:
        return edit_distance(seq1[1:], seq2[1:])
    else:
        subst_use_it = edit_distance(seq2[0] + seq1[1:], seq2)
        del_use_it = edit_distance(seq1[1:], seq2)
        insert_use_it = 1 + edit_distance(seq1[0] + seq2[1:], seq1)
        eDist = max(subst_use_it, del_use_it, insert_use_it)
        return eDist
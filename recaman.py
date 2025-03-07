X = int(input("Length of sequence: ")) # this should be your only input

def recamanSequence(X):
    RecamanSeq = []
    CurrentNum = 0
    NoDuplicates = set()

    for y in range(X):
        RecamanSeq.append(CurrentNum)
        NoDuplicates.add(CurrentNum)
        NextRecValue = CurrentNum - y - 1

        if NextRecValue > 0 and NextRecValue  not in NoDuplicates:
            CurrentNum = NextRecValue
        else:
            CurrentNum += y + 1
    return RecamanSeq

print((recamanSequence(X)))
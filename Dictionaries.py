for letter in s:
    aCount = 0
    cCount = 0
    gCount = 0
    tCount = 0
    for s in letter:
        if s == 'A':
            aCount = aCount + 1
        elif s == 'C':
            cCount = cCount + 1
        elif s == 'G':
            gCount = gCount + 1
        elif s == 'T':
            tCount = tCount + 1
print str(aCount) + ' ' + str(cCount) + ' ' + str(gCount) + ' ' + str(tCount)


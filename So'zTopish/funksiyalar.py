def get_info(xname, yname):
    ans = input('bElgi kiriting: ')
    yname = list(yname)
    i=0
    for x in xname:
        if x == ans:
            yname[i] = ans
        i+=1
    yname = ''.join([x for x in yname])

    return yname


def search_arow():
    f = open('INPUT.TXT', 'r')
    s = f.read()
    s.strip()
    f.close()

    n = 0
    k = -4
    while k != -1:
        k = s.find('<--<<', k+4, len(s) - 1)
        if k != -1:
            n += 1


    k = -4
    while k != -1:
        k = s.find('>>-->', k+4, len(s) - 1)
        if k != -1:
            n += 1


    f = open('OUTPUT.TXT', 'w')
    f.write(str(n))
    f.close()










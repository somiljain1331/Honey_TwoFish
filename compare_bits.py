#p_t = '\x10\xe7\xb8\xbb\xb9j\xbd\xf1\xad\xcc\x87T\x88U\t\x06'
#p_t2 ='\xbaAkj\xb9\xdc\xf9_\x19Rk>\x81\xea|L'
def comp_count(p1,p2):

    #print(p1)
    #print(type(p1))
    s1=''.join(format(ord(i), '02b') for i in p1)
    s2=''.join(format(ord(i), '02b') for i in p2)
    #print(len(s1))
    c=0
    if len(s1)>len(s2):
        diff=len(s1)-len(s2)
        s='0'*diff
        s2=s+s2
    else:
        diff=len(s2)-len(s1)
        s='0'*diff
        s1=s+s1
    #print(s1)
    #print(s2)
    for i in range (0,len(s1)):
        if s1[i]!=s2[i]:
            c=c+1
    #print(c)
    print("Avalance Effect is \n")
    print((c/len(s1))*100)
#comp_count(p_t,p_t2)
for test in range(0,int(input())):
    s=input()
    i=0
    while i<=1000:
        s=str(s)
        if s==s[::-1]:
            print(i,s)
            break
        else:
            s=int(s)+int(s[::-1])
            i+=1



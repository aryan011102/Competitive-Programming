for test in range(0,int(input())):
    track=input()
    c1=track.count('M')
    c2=track.count('F')
    if len(track)<4: #this is the corner case maybe which you didn't think of.
        print('NO LOOP')
    elif c1!=c2:
        print('NO LOOP')
    else:
        print('LOOP')

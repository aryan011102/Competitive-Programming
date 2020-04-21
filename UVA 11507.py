while True:
    length=int(input())
    if length==0:
        break
    else:
        commands=[x for x in input().split()]
        d={0:'+x',1:'-x',2:'+y',3:'-y',4:'+z',5:'-z'}
        dir=0 #initial direction set to 0
        #for reference: 0 -> +x | 1 -> -x | 2 -> +y | 3 -> -y | 4 -> +z | 5 -> -z |
        for i in commands:
            if i=='No':
                continue
            if i=='+z':
                if dir==0: dir=4
                elif dir==1: dir=5
                elif dir==4: dir=1
                elif dir==5: dir=0
            if i=='-z':
                if dir==0: dir=5
                elif dir==1: dir=4
                elif dir==4: dir=0
                elif dir==5: dir=1
            if i=='+y':
                if dir==0: dir=2
                elif dir==1: dir=3
                elif dir==2: dir=1
                elif dir==3: dir=0
            if i=='-y':
                if dir==0: dir=3
                elif dir==1: dir=2
                elif dir==2: dir=0
                elif dir==3: dir=1
        print(d[dir])
